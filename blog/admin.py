from django.contrib import admin
from .models import BlogModel, BlogCategoryModel, CryptoBlogModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


# Register your models here.
class BlogModelAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = BlogModel  # Replace with your actual model name
        fields = ['thumb', 'slug', 'title', 'author', 'description','crypto', 'category', 'content', 'status']

        # widgets = {
        #     'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        # }


@admin.register(BlogModel)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'author', 'status', 'crypto', 'category', 'created_at', 'updated_at')
    list_filter = ('status', 'category',)
    search_fields = ('title',)

    form = BlogModelAdminForm


@admin.register(CryptoBlogModel)
class CryptoBlog(admin.ModelAdmin):
    list_display = ('name', 'symbol','status', 'created_at', 'updated_at')
    list_filter = ('name', 'symbol',)
    search_fields = ('name', 'symbol',)




@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('name',)

    # form = BlogModelAdminForm
