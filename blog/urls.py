from django.contrib import admin
from django.urls import path, include
from blog.views import UserListView, UserDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user list'),
    path('users/<str:username>/', UserDetailView.as_view(), name='user-detail'),
]