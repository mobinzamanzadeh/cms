from django.contrib import admin
from django.urls import path, include
from blog.views import UserListView, UserDetailView, PostListView, PostDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<str:username>/', UserDetailView.as_view(), name='user-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
]
