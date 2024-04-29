from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home-page'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('password-change/', UserChangePasswordView.as_view(), name='password-change'),
]
