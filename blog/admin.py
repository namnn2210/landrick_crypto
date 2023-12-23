from django.contrib import admin
from .models import BlogModel


# Register your models here.
@admin.register(BlogModel)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title',)
