from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PostForm
from .services import SignUpService, PostService, IndexService, UserService


@login_required(login_url='/login')
@permission_required('study_auth.view_post', login_url='logout')
def index(request):
    posts = PostService(request).get_all()
    if request.method == 'GET':
        return render(
            request,
            'study_auth/home.html',
            {
                'posts': posts,
                'subscriptoions': request.user.subscriptions.all(),
            }
        )
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


@login_required(login_url='sign-up')
def user_page_view(request, user_slug):

    if request.method == 'GET':
        service = UserService(request, user_slug)
        user = service.get_user()
        followers_count = service.get_followers_count(user)
        if user:
            posts = PostService(request).get_user_posts(user)
            followed = service.check_if_fllowed(user)
            return render(
                request,
                'study_auth/user_page.html',
                {
                    'user': user,
                    'posts': posts,
                    'followed': followed,
                    'followers_count': followers_count,
                }
            )
    if request.method == 'POST':
        service = PostService(request)
        service.delete_post()
    return redirect('/')


@login_required(login_url='sign-up')
def post_view(request, post_slug):
    if request.method == 'GET':
        service = PostService(request)
        post = service.get_post_by_slug(post_slug)
        if post:
            return render(
                request,
                'study_auth/post_page.html',
                {'post': post}
            )
    if request.method == 'POST':
        service = PostService(request)
        service.delete_post()
    return redirect('/')


@login_required(login_url='sign-up')
def subscribe(request, followed_user_id):
    if request.method == 'POST':
        service = UserService(request)
        service.subscribe(followed_user_id)
        return redirect('/')


@login_required(login_url='sign-up')
def subscriptions(request):
    if request.method == 'GET':
        service = UserService(request)
        subscriptions = service.get_subscriptions()
        print(subscriptions)
        return render(
            request,
            'study_auth/subscriptions.html',
            {
                'subscriptions': subscriptions,
            }
        )


@login_required(login_url='sign-up')
def subscribers(request):
    if request.method == 'GET':
        service = UserService(request)
        subscribers = service.get_subscribers()
        return render(
            request,
            'study_auth/subscribers.html',
            {
                'subscribers': subscribers,
            }
        )
