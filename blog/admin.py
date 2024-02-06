from django.contrib import admin
from .models import Post, Comment 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for blog """
    list_display = ('title', 'status', 'created_on') 
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on') 
    prepopulated_fields = {'slug': ('title',)} 


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('body', 'post', 'created_on') 
    search_fields = ('email', 'body') 
    list_filter = ['created_on']    
