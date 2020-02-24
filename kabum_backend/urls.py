# This file stores every url path used in the application
from django.urls import path
from . import views

# This paths call the method from views, which generate the page parameters
urlpatterns = [
    # It is composed by the path in the url,
    # a method to be called and a path name to be referenced on htmls
    path('', views.home, name = 'home'),
    path('cart/', views.cart, name = 'cart'),
    path('multiplier/', views.multiplier, name = 'multiplier'),
    path('price/', views.price, name = 'price'),
]
