from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.db.models import Count

from .forms import CustomUserCreationForm, PostForm
from .models import CustomUser, Post


class SignUpService:
    def __init__(self, request, form: CustomUserCreationForm):
        self._form = form
        self._request = request

    def sign_up(self):
        if self._form.is_valid():
            user = self._form.save(commit=False)
            user.slug = user.username
            user.save()
            default_group = Group.objects.get(name='default')
            default_group.user_set.add(user)
            login(self._request, user)
        return self._form.is_valid()


class PostService:
    def __init__(self, request, form: PostForm = None):
        self._form = form
        self._request = request

    def get_all(self):
        return Post.objects.select_related('author')\
            .filter(author__groups__name__in=['default'])

    def create_post(self):
        if self._form.is_valid():
            post = self._form.save(commit=False)
            post.author = self._request.user
            post.slug = 'post-'+post.title
            post.save()
        return self._form.is_valid()

    def get_user_posts(self, user: CustomUser):
        return Post.objects.filter(author=user)

    def get_post_by_slug(self, post_slug):
        post = Post.objects.filter(slug=post_slug)
        if post.exists():
            return post.first()

    def delete_post(self):
        post = Post.objects.filter(id=self._request.POST.get('post_id')).first()
        if post and post.author == self._request.user:
            post.delete()


class UserService:
    def __init__(self, request, user_slug=None):
        self._request = request
        self.user_slug = user_slug

    def get_user(self):
        user = CustomUser.objects.filter(slug=self.user_slug)
        if user.exists():
            return user.first()

    def ban_user(self):
        if self._request.user.is_staff:
            processed_user = CustomUser.objects.get(id=self._request.POST.get('user_id'))
            mod_group = Group.objects.get(name='mod')
            default_group = Group.objects.get(name='default')
            mod_group.user_set.add(processed_user)
            default_group.user_set.remove(processed_user)

    def subscribe(self, followed_user_id):
        try:
            following_user = self._request.user
            followed_user = CustomUser.objects.filter(id=followed_user_id).first()
            if followed_user != following_user:
                following_user.subscriptions.add(followed_user)
        except:
            return

    def check_if_fllowed(self, user: CustomUser):
        return self._request.user.subscriptions.contains(user)

    def get_followers_count(self, followed_user: CustomUser):
        try:
            return followed_user.subscriptions.count()
        except:
            pass


class IndexService:

    def __init__(self, request):
        self._request = request
        self._action_code = self._request.POST.get('action_code', 'no_code')

        self.sub_services = {
            'delete post': PostService(request).delete_post,
            'ban user': UserService(request).ban_user,
        }

    def process(self):
        try:
            self.sub_services[self._action_code]()
        except KeyError:
            return