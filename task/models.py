from django.db import models
from user import models as user_model

class TaskModel(models.Model):
    status_choices = ((1 , "completed") , (0 , "underprocess") , (2 , "not assigned"))
    name = models.CharField(max_length= 1000 )
    user = models.ForeignKey(user_model.UserModel , on_delete= models.CASCADE)
    description = models.CharField(max_length= 1000)
    status = models.IntegerField(choices = status_choices, default = 2 )
    assignees = models.ManyToManyField(user_model.UserModel, through='Assignment', related_name='tasks_assigned')

class Assignment(models.Model):
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)
    assignee = models.ForeignKey(user_model.UserModel, on_delete=models.CASCADE)



