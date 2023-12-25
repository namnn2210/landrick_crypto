from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ask = models.TextField()
    answer = models.TextField(null=True, default=None)
    content = models.TextField(null=True, default=None)
    status = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
