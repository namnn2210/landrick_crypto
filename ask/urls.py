from django.urls import path
from .views import ask, add_ask, ask_detail

urlpatterns = [
    path('', ask, name='ask'),
    path('add', add_ask, name='add_ask'),
    path('detail/<int:ask_id>', ask_detail, name='ask_detail')
]
