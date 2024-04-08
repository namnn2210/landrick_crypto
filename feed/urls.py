from django.urls import path
from .views import feed,feed_detail, add_comment

urlpatterns = [
    path('list', feed, name='feed'),
    path('<str:slug>',feed_detail, name='feed_detail'),
    path('comment/<str:slug>',add_comment,name='add_comment')
]

