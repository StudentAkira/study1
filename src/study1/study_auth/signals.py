from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def my_callback(sender, instance, *args, **kwargs):
    default_group = Group.objects.get(name='default')
    default_group.user_set.add(instance)
