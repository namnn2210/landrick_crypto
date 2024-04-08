from django.urls import path
from .views import feed,feed_detail

urlpatterns = [
    path('list', feed, name='feed'),
    path('<str:slug>',feed_detail, name='feed_detail')
]

