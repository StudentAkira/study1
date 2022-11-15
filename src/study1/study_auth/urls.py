from django.urls import path
from .views import index, sign_up

urlpatterns = [
    path('', index, name='home'),
    path('sign-up', sign_up, name='sign_up')
]
