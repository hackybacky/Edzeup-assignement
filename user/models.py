from django.db import models

# Create your models here.

class UserModel(models.Model):
    role_choices = ((0 , "Manager") , (1 , "Employee"))
    name = models.CharField( max_length= 1000)
    username = models.CharField( max_length= 1000)
    role = models.IntegerField(choices = role_choices , default = 0)
