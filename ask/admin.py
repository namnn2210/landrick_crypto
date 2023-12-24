from django.contrib import admin
from .models import AskModel


# Register your models here.
@admin.register(AskModel)
class AskAdmin(admin.ModelAdmin):
    list_display = ('user', 'ask', 'answer', 'status', 'created_at', 'updated_at')
    list_filter = ('user', 'status', 'created_at',)
    search_fields = ('ask', 'answer',)
