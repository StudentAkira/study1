from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class CustomUser(AbstractUser):
    slug = models.SlugField(unique=True, db_index=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.username
        super().save(force_insert, force_update, using, update_fields)
        default_group = Group.objects.get(name='default')
        default_group.user_set.add(self)


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
