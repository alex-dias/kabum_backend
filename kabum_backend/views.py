from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from . import businessRules

multipliers = {}

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
    prof = []

    if 'priceValidator' not in parameters:
        for id, name, price, multiplier in productForm.productsCollection:
            if id in parameters:
                multipliers[id] = (request.GET[id])
                products.append([id, name, price, 100, request.GET[id]])
        print(multipliers)
        return render(request, 'price.html', {'productsInfo': productForm.productsCollection, 'products': products, 'username': username, 'question': ', quanto você quer pagar por cada produto?'})
    else:
        for id, name, price, multiplier in productForm.productsCollection:
            if id in parameters:
                prof.append([id] + businessRules.profitability(price, request.GET[id]))
        if 0 in [item[1] for item in prof]:
            for id, name, price, multiplier in productForm.productsCollection:
                if id in parameters:
                    products.append([id, name, request.GET[id], "%.2f" % round(businessRules.profitability(price, request.GET[id])[1]*100, 2), multipliers.get(id)])

            return render(request, 'price.html', {'productsInfo': productForm.productsCollection, 'products': products, 'username': username, 'question': ', um ou mais itens não alcançaram a rentabilidade mínima de 90%, por favor sugira outro preço.'})

        else:
            for id, name, price, multiplier in productForm.productsCollection:
                if id in parameters:
                    products.append([id, name, request.GET[id], "%.2f" % round(businessRules.profitability(price, request.GET[id])[1]*100, 2), multipliers.get(id)])
            return render(request, 'resume.html', {'productsInfo': productForm.productsCollection, 'products': products, 'username': username, 'question': ', seu pedido foi aceito. Obrigado por comprar conosco.'})
