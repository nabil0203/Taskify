from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    CATEGORY = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()

    status = models.CharField(max_length=100, choices = STATUS, default='pending')                  # choices = STATUS -> kon STATUS choice hobe? Pending/Completed [by default pending]
    category = models.CharField(max_length=100, choices = CATEGORY)                           # choices = CATEGORY -> kon CATEGORY choice hobe? Work/Personal/Other

    is_completed = models.BooleanField(default=False)                                # initially every task will be pending, so not completed

    user = models.ForeignKey(User, on_delete=models.CASCADE)                         # 1 to many relationship


    def __str__(self):
        return self.title







