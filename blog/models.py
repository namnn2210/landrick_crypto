from django.db import models


# Create your models here.
class BlogModel(models.Model):
    thumb = models.ImageField(null=True, default=None, upload_to='')
    title = models.TextField(null=False)
    slug = models.TextField(default='slug')
    description = models.TextField(null=False)
    content = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'
