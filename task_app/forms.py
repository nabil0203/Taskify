from django import forms

from .models import Task

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']              # we need all fields of Task Model excluding User field
        # fields = []


        widgets = {                                                                                     
            'due_date': forms.DateInput(attrs={'type':'date'}),                             # to show time and date as 2 fields in form
            'due_time': forms.TimeInput(attrs={'type':'time'}),
        }






class UserRegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        

        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]