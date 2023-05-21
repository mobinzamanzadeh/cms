from dj_rest_auth.views import PasswordResetConfirmView
from django.contrib import admin
from django.urls import path, include
from blog.views import UserListView, UserDetailView, PostListView, PostDetailView, CommentListView, CommentDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<str:username>/', UserDetailView.as_view(), name='user-detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<str:slug>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/<str:slug>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('rest-auth/password/reset/confirm/<uid64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
]
