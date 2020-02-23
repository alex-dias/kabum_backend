from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cart/', views.cart, name = 'cart'),
    path('multiplier/', views.multiplier, name = 'multiplier'),
    path('price/', views.price, name = 'price'),
]
