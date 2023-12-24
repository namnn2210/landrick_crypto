from django.urls import path
from .views import ask, add_ask

urlpatterns = [
    path('', ask, name='ask'),
    path('add', add_ask, name='add_ask')
]
