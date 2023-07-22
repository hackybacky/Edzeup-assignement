from rest_framework import permissions
from user import models as user_models
from task import models as task_models
from rest_framework.exceptions import PermissionDenied
class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        try :
            user = user_models.UserModel.objects.get(id = request.data["created_by"])
            if(user.role != 0):
                raise PermissionDenied(detail="You do not have permission to access this resource.")
            request.data['user'] = user.id
            return True
        except user_models.UserModel.DoesNotExist:
            return False

class IsManagerOrAssignee(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user = user_models.UserModel.objects.get(id=request.data.get("id"))
            task = task_models.TaskModel.objects.get(id=view.kwargs.get("pk"))
            assignment = task_models.Assignment.objects.get(task=task, assignee=user)
            return True
        except task_models.Assignment.DoesNotExist:
            return False
        except user_models.UserModel.DoesNotExist:
            return False
        except task_models.TaskModel.DoesNotExist:
            return False
