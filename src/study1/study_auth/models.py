from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    slug = models.SlugField(unique=True, db_index=True)


class Subscription(models.Model):
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='followed')
    objects = models.Manager()


class Post(models.Model):

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True)
    title = models.CharField(max_length=127, name='title')
    content = models.CharField(max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    #custom validation example
    """def clean(self):
        if self.title.startswith('a'):
            raise ValidationError({'title': 'unreal value'})"""

    def __str__(self):
        return self.title
