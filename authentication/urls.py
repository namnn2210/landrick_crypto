from django.urls import path
from .views import login, signup, reset

urlpatterns = [
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('reset', reset, name='reset'),

]
