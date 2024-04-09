from django.contrib import admin
from .models import FeedModel, FeedCommentModel, FeedCategoryModel


# Register your models here.
@admin.register(FeedModel)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'thumb', 'description', 'category', 'hashtags', 'slug', 'status', 'created_at', 'updated_at')
    list_filter = ('author', 'status',)
    search_fields = ('author', 'slug')


@admin.register(FeedCommentModel)
class FeedCommentAdmin(admin.ModelAdmin):
    list_display = ('feed', 'user', 'comment', 'status', 'created_at', 'updated_at')
    list_filter = ('user', 'status',)
    # search_fields = ('','slug')


@admin.register(FeedCategoryModel)
class FeedCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name',)
