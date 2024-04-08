from django.contrib import admin
from .models import FeedModel

# Register your models here.
@admin.register(FeedModel)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('author','thumb', 'description', 'slug', 'status', 'created_at', 'updated_at')
    list_filter = ('author','status',)
    search_fields = ('author','slug')
    
