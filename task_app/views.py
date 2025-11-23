from django.shortcuts import render, redirect, get_object_or_404

from .models import Task

from .forms import TaskForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, logout, login

from django.contrib.auth.decorators import login_required

from .forms import UserRegForm, UserUpdateForm

from django.contrib import messages

from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth import update_session_auth_hash





# Create your views here.



# 1. Task List
@login_required
def task_list(request):

    # filter based on status
    status_filter = request.GET.get('status','all')                         # by default all the task's status will be seen
    
    # filter based on category
    category_filter = request.GET.get('category','all')                     # by default all the task's category will be seen

    tasks = Task.objects.filter(user = request.user)                          # the specific user will see only his tasks; not all the tasks



    # if the status filter in not 'all' then check if it is completed or not
    # means, if all the tasks are not shown, then show the tasks based on if it is completed or not
    if status_filter != 'all':
        tasks = tasks.filter(is_completed = (status_filter == 'completed'))


    # if the category exists then filter based on it
    if category_filter != 'all':
        tasks = tasks.filter(category = category_filter)


    # For the UI
    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)



    return render(request,'task_list.html',{
        'completed_tasks' : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status_filter' : status_filter,
        'category_filter' : category_filter
    })





 
# 2. task create
# same as student_create
@login_required
def task_create(request):
    
    if request.method == 'POST':
        form  = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)            # 'commit = False' -> form won't be saved in DB but the model is ready to be saved in DB
            form.user = request.user
            form.save()                                 # save in DB
            return redirect('task_list')
        

    else:
        form = TaskForm()
    
    return render(request, 'task_form.html', {'form' : form})







# 3. Task details page
# see all task details
@login_required
def task_details(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)               # filtering; getting the exact object details that the user wants by matching the id and user

    return render(request, 'task_details.html', {'task' : task})
    





# 4. task delete
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)
    task.delete()

    return redirect('task_list')







# 5. Mark task as completed
# click a button and it will show as completed
@login_required
def task_mark_completed(request, task_id):
    task = get_object_or_404(Task, id = task_id, user = request.user)

    task.is_completed = True
    task.save()
    return redirect('task_list')






# 6. user register
# minimal register method
# def register(request):

#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()                                                      # Save user to the database
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
            
#             user = authenticate(username = username, password = password)                            
            
#             login(request, user)                                                        # Log the user in immediately

#             return redirect('task_list')

#     else:
#         form = UserCreationForm()

#     return render(request, 'register.html', {'form' : form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()                                           # Save user to the database
            
            login(request, user)                                        # Log the user in immediately
            
            return redirect('task_list')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})






#7. User profile
@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})



# 8.  update user 
@login_required
def update_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")  # go back to task list after update
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "update_profile.html", {"form": form})



# 9. pass change
@login_required
def pass_change(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed!')
            return redirect('task_list')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})

