
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import User, Role, UserRole

@receiver(m2m_changed, sender=User.roles.through)
def update_user_roles(sender, instance, action, **kwargs):
    if action == 'post_add':
        for role in instance.roles.all():
            UserRole.Objects.create(user=instance, role=role)
    elif action == 'post_remove':
        UserRole.Objects.filter(user=instance).delete()
