from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'author']
    search_fields = ['title', 'author']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'post', 'author']
    list_filter = ['post']
    search_fields = ('text', 'post__title', 'author')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'author']
    list_filter = ['post']
    search_fields = ('post__title', 'author')