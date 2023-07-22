from rest_framework import serializers
from user import models as user_models
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.UserModel
        fields = '__all__'