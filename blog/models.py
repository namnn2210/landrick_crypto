from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

# Create your models here.
UserModel = get_user_model()


class BlogCategoryModel(models.Model):
    name = models.TextField(null=False)
    slug = models.TextField(default='slug')
    description = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_categories'

    def __str__(self):
        return self.name


class CryptoBlogModel(models.Model):
    name = models.TextField(null=False)
    symbol = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.symbol


class BlogModel(models.Model):
    thumb = models.ImageField(null=True, default=None, upload_to='')
    title = models.TextField(null=False)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    slug = models.TextField(default='slug')
    description = models.TextField(null=False)
    crypto = models.ForeignKey(CryptoBlogModel, null=True, on_delete=models.CASCADE)
    content = RichTextField(null=False)
    category = models.ForeignKey(BlogCategoryModel, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'

    def save(self, *args, **kwargs):
        if not self.author and hasattr(self, 'request') and hasattr(self.request, 'user'):
            user = self.request.user
            if user.first_name and user.last_name:
                author_name = f"{user.first_name} {user.last_name}"
                self.author = author_name
        super().save(*args, **kwargs)
