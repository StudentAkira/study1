from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, PostForm
from .models import CustomUser, Post


class SignUpService:
    def __init__(self, request, form: CustomUserCreationForm):
        self._form = form
        self._request = request

    def sign_up(self):
        if self._form.is_valid():
            user = self._form.save()
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
            post.save()
        return self._form.is_valid()


class PostDeletionService:
    def __init__(self, request):
        self._request = request

    def process(self):
        post = Post.objects.filter(id=self._request.POST.get('post_id')).first()
        if post and post.author == self._request.user:
            post.delete()


class BanUserService:
    def __init__(self, request):
        self._request = request

    def process(self):
        if self._request.user.is_staff:
            processed_user = CustomUser.objects.get(id=self._request.POST.get('user_id'))
            mod_group = Group.objects.get(name='mod')
            default_group = Group.objects.get(name='default')
            mod_group.user_set.add(processed_user)
            default_group.user_set.remove(processed_user)


class IndexService:

    sub_services = {
        'delete post': PostDeletionService,
        'ban user': BanUserService,
    }

    def __init__(self, request):
        self._request = request

    def process(self):
        try:
            self.sub_services[self._request.POST.get('action_code')](self._request).process()
        except KeyError:
            return

