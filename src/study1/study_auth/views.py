from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'study_auth/home.html')


def sign_up(request):

    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'registration/sign-up.html', {'form': form})

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'study_auth/home.html')
        return render(
            request,
            'registration/sign-up.html',
            {'form': form}
        )
