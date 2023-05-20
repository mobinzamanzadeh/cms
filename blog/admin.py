from django.contrib import admin
from blog.models import Tag, Category, Post, Comment
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
