from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class AskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.TextField(default='slug')
    ask = models.TextField()
    answer = models.TextField(null=True, default=None)
    content = RichTextField(null=True, default=None)
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
