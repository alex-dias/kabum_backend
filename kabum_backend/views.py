from django.http import HttpResponse
from django.shortcuts import render
from . import forms

def home(request):
    userForm = forms.usersClass()
    return render(request, 'home.html', {'users': userForm.userNames})

def cart(request):
    productForm = forms.productClass()
    username = request.GET['username']
    return render(request, 'cart.html', {'products': productForm.productsCollection, 'username': username})

def multiplier(request):
    productForm = forms.productClass()
    parameters = request.GET
    products = []
    username = request.GET['username']

    for id, name, price, multiplier in productForm.productsCollection:
        if id in parameters:
            products.append([id, name, multiplier, request.GET[id]])
    return render(request, 'multiplier.html', {'productsInfo': productForm.productsCollection, 'products': products, 'username': username})

def price(request):
    productForm = forms.productClass()
    parameters = request.GET
    products = []
    username = request.GET['username']

    for id, name, price, multiplier in productForm.productsCollection:
        if id in parameters:
            products.append([id, name, price, request.GET[id]])
    return render(request, 'price.html', {'productsInfo': productForm.productsCollection, 'products': products, 'username': username})
