# user_roles/urls.py
from django.urls import path
from rest_framework import routers
from . import views

# Define routers for viewsets
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'user_roles', views.UserRoleViewSet)

urlpatterns = [
    # Add other paths if needed
]

# Add router URLs to urlpatterns
urlpatterns += router.urls
