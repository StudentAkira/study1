from django.urls import path
from .views import \
    index, sign_up,\
    create_post, user_page_view,\
    post_view, subscribe,\
    subscriptions, subscribers, \
    unsubscribe

urlpatterns = [
    path('', index, name='home'),
    path('sign-up', sign_up, name='sign_up'),
    path('create-post', create_post, name='create_post'),
    path('user/<slug:user_slug>', user_page_view, name='user_page'),
    path('post/<slug:post_slug>', post_view, name='post_page'),
    path('follow-user/<int:followed_user_id>', subscribe, name='subscribe'),
    path('unfollow-user/<int:unfollowed_user_id>', unsubscribe, name='unsubscribe'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('subscribers/', subscribers, name='subscribers'),

]
