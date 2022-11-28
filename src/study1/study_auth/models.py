from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxLengthValidator
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    subscriptions = models.ManyToManyField('self', related_name='subscriptions', blank=True, null=True)
    slug = models.SlugField(unique=True, db_index=True)


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True)
    title = models.CharField(max_length=127)
    content = models.CharField(max_length=1023)
    created_at = models.DateTimeField(editable=True, auto_now_add=True)
    updated_at = models.DateTimeField(editable=True, auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
