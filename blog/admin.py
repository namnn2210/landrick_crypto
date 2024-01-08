from django.contrib import admin
from .models import BlogModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# Register your models here.
class BlogModelAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = BlogModel  # Replace with your actual model name
        fields = ['thumb', 'slug', 'title', 'description', 'content', 'status']

        # widgets = {
        #     'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        # }


@admin.register(BlogModel)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('title',)

    form = BlogModelAdminForm
