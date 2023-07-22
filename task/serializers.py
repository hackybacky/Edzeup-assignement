from rest_framework import serializers
from task import models as task_models
from user import serializers as user_serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task_models.TaskModel
        fields = '__all__'
class AssigneeSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    assignee = user_serializers.UserSerializer()
    class Meta:
        model = task_models.Assignment
        fields = ['id' , 'task' , 'assignee']

