from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('myfridge/', FridgeListView.as_view(), name='myfridge_list'),
    path('create/', FridgeCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
]