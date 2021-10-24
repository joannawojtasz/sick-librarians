from django.contrib import admin 
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'type', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'type')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['publish_draft']

    def publish_draft(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['disapprove_comments']

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)