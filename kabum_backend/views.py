from django.http import HttpResponse
from django.shortcuts import render
from . import forms

def home(request):
    userForm = forms.usersClass()
    return render(request, 'home.html', {'users': userForm.userNames})

def cart(request):
    productForm = forms.productClass()
    username = request.GET['user']
    return render(request, 'cart.html', {'products': productForm.productsCollection, 'username': username})

def multiplier(request):
    productForm = forms.productClass()
    products = []

    for id, name, price, multiplier in productForm.productsCollection:
        getValue = [id, name, multiplier, request.GET[id]]
        if getValue[3] != 'No':
            products.append(getValue)
    return render(request, 'multiplier.html', {'productsInfo': productForm.productsCollection, 'products': products})
