from django.urls import path
from .views import blog, blog_detail


urlpatterns = [
    path('', blog, name='blog'),
    path('detail/<str:slug>/', blog_detail, name='blog_detail'),
]

