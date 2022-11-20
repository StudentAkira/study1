from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Post


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(strip=True,)
    password1 = forms.CharField(strip=True, widget=forms.PasswordInput())
    password2 = forms.CharField(strip=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
