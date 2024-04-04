from django.urls import path
from .views import blog, blog_detail,blog_by_category

urlpatterns = [
    path('list', blog, name='blog'),
    path('category/<str:slug>', blog_by_category, name='blog_by_category'),
    path('<str:slug>', blog_detail, name='blog_detail'),
]

