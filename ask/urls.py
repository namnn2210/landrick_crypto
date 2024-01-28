from django.urls import path
from .views import ask, add_ask, ask_detail, ask_category

urlpatterns = [
    path('', ask, name='ask'),
    path('add', add_ask, name='add_ask'),
    path('detail/<str:slug>', ask_detail, name='ask_detail'),
    path('category/<str:slug>', ask_category, name='ask_category')
]
