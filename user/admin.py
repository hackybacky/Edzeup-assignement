from django.contrib import admin
from user.models import  UserModel
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'role')

admin.site.register(UserModel , UserModelAdmin)