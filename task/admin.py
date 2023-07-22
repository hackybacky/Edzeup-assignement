from django.contrib import admin
from task import models as task_models
# Register your models here.

admin.site.register(task_models.TaskModel)
admin.site.register(task_models.Assignment)