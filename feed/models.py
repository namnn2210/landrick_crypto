from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

UserModel = get_user_model()


# Create your models here.
class FeedModel(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    title = models.TextField(null=False)
    thumb = models.ImageField(null=True, default=None, upload_to='')
    slug = models.TextField(default='slug')
    description = models.TextField(null=False)
    content = RichTextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feeds'

    def __str__(self):
        return self.title


class FeedCommentModel(models.Model):
    feed = models.ForeignKey(FeedModel, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feed_comments'
