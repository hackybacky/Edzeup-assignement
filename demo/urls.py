
from django.contrib import admin
from django.urls import path
from django.urls import path
from task import  views as task_views

urlpatterns = [
    path('create-task/', task_views.TaskCreateView.as_view(), name='create-task'),
    path('get-task-created/', task_views.TaskListCreatedByUser.as_view(), name='tasks-by-user-id'),
    path('task-assigned/', task_views.TaskAssigned.as_view(), name='tasks-assigned'),
    path('update-task/<int:pk>/', task_views.TaskUpdateStatusView.as_view(), name='update-task-status'),
    path('admin/', admin.site.urls),
]


