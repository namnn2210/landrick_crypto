from django.contrib import admin
from .models import FeedModel, FeedCommentModel


# Register your models here.
@admin.register(FeedModel)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'thumb', 'description', 'slug', 'status', 'created_at', 'updated_at')
    list_filter = ('author', 'status',)
    search_fields = ('author', 'slug')


@admin.register(FeedCommentModel)
class FeedCommentAdmin(admin.ModelAdmin):
    list_display = ('feed', 'user', 'comment', 'status', 'created_at', 'updated_at')
    list_filter = ('user', 'status',)
    # search_fields = ('','slug')
