from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AskCategoryModel(models.Model):
    name = models.TextField()
    slug = models.TextField(default='slug')
    description = models.TextField()
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(AskCategoryModel, on_delete=models.CASCADE, null=True)
    slug = models.TextField(default='slug')
    ask = models.TextField()
    answer = models.TextField(null=True, default=None)
    content = models.TextField(null=True, default=None)
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


