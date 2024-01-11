from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class BlogCategoryModel(models.Model):
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_categories'


class BlogModel(models.Model):
    thumb = models.ImageField(null=True, default=None, upload_to='')
    title = models.TextField(null=False)
    slug = models.TextField(default='slug')
    description = models.TextField(null=False)
    content = RichTextField(null=False)
    category = models.ForeignKey(BlogCategoryModel, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'
