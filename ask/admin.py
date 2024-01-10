from django.contrib import admin
from .models import AskModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from tinymce.widgets import TinyMCE


class AskModelAdminForm(forms.ModelForm):
    class Meta:
        model = AskModel  # Replace with your actual model name
        fields = ['user', 'slug', 'ask', 'answer', 'content', 'status']

        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }


# Register your models here.
@admin.register(AskModel)
class AskAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'ask', 'answer', 'status', 'created_at', 'updated_at')
    list_filter = ('user', 'status', 'created_at',)
    search_fields = ('ask', 'answer',)

    form = AskModelAdminForm
