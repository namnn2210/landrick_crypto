from django.urls import path
from .views import user_login, signup, reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', user_login, name='login'),
    path('signup', signup, name='signup'),
    path('reset', reset, name='reset'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
