from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    time = models.DateTimeField()
    body = models.TextField()


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time')
    list_instances = True
    search_fields = ['title']


admin.site.register(BlogPost, BlogPostAdmin)
