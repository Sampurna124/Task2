from rest_framework import serializers

from .models import User,UserRole,AbstractUser




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRole
        fields='__all__'
class AbstractUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AbstractUser
        fields='__all__'