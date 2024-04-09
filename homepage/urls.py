from django.urls import path
from .views import index, about, market, token, services, faqs, whitepapers, no_responsibility

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('market', market, name='market'),
    path('token', token, name='token'),
    path('services', services, name='services'),
    path('faqs', faqs, name='faqs'),
    path('whitepapers', whitepapers, name='whitepapers'),
    path('no_responsibility', no_responsibility, name='no_responsibility'),


]
