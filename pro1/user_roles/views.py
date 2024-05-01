
from rest_framework import viewsets
from .models import User,AbstractUser, UserRole
from .serializers import UserSerializer, AbstractUserSerializer, UserRoleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = AbstractUser.objects.all()
    serializer_class = AbstractUserSerializer
class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
