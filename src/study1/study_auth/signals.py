from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post


@receiver(post_save, sender=Post)
def my_callback(sender, *args, **kwargs):
    print("post saved", args, kwargs)