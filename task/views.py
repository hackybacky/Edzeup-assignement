from rest_framework import generics, permissions
from rest_framework.response import Response

from task import models as task_models
from task import serializers as task_serializers
from task import permissions as task_permissions
from user import models as user_models

class TaskCreateView(generics.CreateAPIView):
    queryset = task_models.TaskModel.objects.all()
    serializer_class = task_serializers.TaskSerializer
    permission_classes = [task_permissions.IsManager]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid()
            new_task = serializer.save()
            [task_models.Assignment.objects.create(task = new_task , assignee = user_models.UserModel.objects.get(id = assignee)) for assignee in request.data["assignee"]]
            return Response(serializer.data , status = 201)
        except user_models.UserModel.DoesNotExist:
            return Response("User Does not Exist in Assignee" , status = 500)

class TaskListCreatedByUser(generics.ListAPIView):
    serializer_class = task_serializers.TaskSerializer

    def get_queryset(self):
        user_id = self.request.data["id"]
        return task_models.TaskModel.objects.filter(user_id=user_id)

class TaskAssigned(generics.ListAPIView):
    serializer_class = task_serializers.AssigneeSerializer
    def get_queryset(self):
        user_id = self.request.data["id"]
        return task_models.Assignment.objects.filter(assignee=user_models.UserModel.objects.get(id = user_id))

class TaskUpdateStatusView(generics.UpdateAPIView):
    queryset = task_models.TaskModel.objects.all()
    serializer_class = task_serializers.TaskSerializer
    permission_classes = [task_permissions.IsManagerOrAssignee]



