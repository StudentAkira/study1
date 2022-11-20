from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PostForm
from .services import SignUpService, PostService, IndexService


@login_required(login_url='/login')
@permission_required('study_auth.view_post', login_url='logout')
def index(request):
    posts = PostService(request).get_all()
    if request.method == 'GET':
        return render(request, 'study_auth/home.html', {'posts': posts})
    if request.method == 'POST':
        service = IndexService(request)
        service.process()
    return render(request, 'study_auth/home.html', {'posts': posts})


def sign_up(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        form = CustomUserCreationForm()
        return render(request, 'registration/sign-up.html', {'form': form})
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        service = SignUpService(request, form)
        if service.sign_up():
            return redirect('/')
        return render(request, 'registration/sign-up.html', {'form': form})


@login_required(login_url='/login')
@permission_required('study_auth.add_post', login_url='logout')
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'study_auth/create_post.html', {'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST)
        service = PostService(request, form)
        if service.create_post():
            return redirect('/')
        return render(request, 'study_auth/create_post.html', {'form': form})
