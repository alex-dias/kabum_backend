from django.http import HttpResponse
from django.shortcuts import render
from . import forms

def home(request):
    userForm = forms.usersClass()
    productForm = forms.productClass()
    return render(request, 'home.html', {'users': userForm.userNames, 'products': productForm.productsCollection})
