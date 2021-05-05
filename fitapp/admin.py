"""
*  REFERENCES
*
*  Title: Creating Comments System With Django
*  Author: Django Central
*  URL: https://djangocentral.com/creating-comments-system-with-django/
"""
from django.contrib import admin
from .models import Profile, Logs, Comment

admin.site.register(Profile)
admin.site.register(Logs)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)