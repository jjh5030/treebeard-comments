from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
