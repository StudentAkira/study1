from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PostForm
from .models import Post


@login_required(login_url='/login')
def index(request):
    posts = Post.objects.select_related('author').all()
    if request.method == 'GET':
        return render(request, 'study_auth/home.html', {'posts': posts})
    if request.method == 'POST':
        post = Post.objects.filter(id=request.POST.get('post_id')).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'study_auth/home.html', {'posts': posts})



def sign_up(request):

    if request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, 'registration/sign-up.html', {'form': form})

    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        return render(
            request,
            'registration/sign-up.html',
            {'form': form}
        )


@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
        return render(request, 'study_auth/create_post.html', {'form': form})
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'study_auth/create_post.html', {'form': form})
