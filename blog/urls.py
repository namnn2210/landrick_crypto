from django.urls import path
from .views import blog, blog_detail


urlpatterns = [
    path('list', blog, name='blog'),
    path('<str:slug>', blog_detail, name='blog_detail'),
]

