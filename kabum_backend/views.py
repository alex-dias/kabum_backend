# The methods on this file are used to build the pages and its parameters
# Each method is used to build one particular page
# The argument for the methods is always request, which stores parameters from the previous page
# render function receive the request, the target html template and a dictionary of parameters
from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from . import businessRules
# An global dictionary used to store the multipliers for each product item
multipliers = {}
# Method to build home page
def home(request):
    # It gets all users from user class
    userForm = forms.usersClass()
    # Build the page using the following parameters
    # userNames is a collection of names and its IDs
    return render(request, 'home.html', {'users': userForm.userNames})

def cart(request):
    # It gets all products from product class
    productForm = forms.productClass()
    # It gets the username trough the url parameter sent through the previous page
    username = request.GET['username']
    # Build the page using the following parameters
    # productsCollection is a collection of prodcut names, price, multiplier and its IDs
    return render(request, 'cart.html', {'products': productForm.productsCollection, 'username': username})

def multiplier(request):
    # It gets all products from product class
    productForm = forms.productClass()
    # It gets all parameters from the url
    parameters = request.GET
    # Described at line 44
    selectedProducts = []
    # It gets the value from the specific parameter 'username'
    username = request.GET['username']

    # Iterates through productsCollection looking for only products given from urls
    for id, name, price, multiplier in productForm.productsCollection:
        if id in parameters:
            # After fiding an ID from a specific product, its information is append to products list
            selectedProducts.append([id, name, multiplier, request.GET[id]])
    # Build the page using the following parameters
    # selectedProducts is a collection of products information (id, name and multiplier) chosen by the user on the previous page, based on url parameters
    return render(request, 'multiplier.html', {'productsInfo': productForm.productsCollection, 'products': selectedProducts, 'username': username})

def price(request):
    # It gets all products from product class
    productForm = forms.productClass()
    # It gets all parameters from the url
    parameters = request.GET
    selectedProducts = []
    # It gets the value from the specific parameter 'username'
    username = request.GET['username']
    # Described at line 75
    profit = []

    # priceValidator is a flag which determines if the user already suggested a price before
    # That means if it is the first time the user access this page
    if 'priceValidator' not in parameters:
        # Iterates through productsCollection looking for only products given from urls
        for id, name, price, multiplier in productForm.productsCollection:
            if id in parameters:
                # It saves the multipliers given at the previous page
                multipliers[id] = (request.GET[id])
                # Now selectedProducts has profitability (4th parameter), which is 100% because the price is still the original price
                selectedProducts.append([id, name, price, 100, request.GET[id]])
        # question parameter is given to shape the page based on priceValidator flag
        return render(request, 'price.html', {'productsInfo': productForm.productsCollection, 'products': selectedProducts, 'username': username, 'question': ', quanto você quer pagar por cada produto?'})
    # Now the user already suggested prices, priceValidator indicates that
    else:
        # Iterates through productsCollection looking for only products given from urls
        for id, name, price, multiplier in productForm.productsCollection:
            if id in parameters:
                # profit stores lists of product ID, profitability flag and profitability percentage
                profit.append([id] + businessRules.profitability(price, request.GET[id]))
        #  Check on the second column from profit matrix if there is any bad profitability (0)
        if 0 in [item[1] for item in profit]:
            # Iterates through productsCollection looking for only products given from urls
            for id, name, price, multiplier in productForm.productsCollection:
                if id in parameters:
                    # Now selectedProducts stores suggested price (3rd parameter), profitability (4th parameter), and multipliers (5th parameter)
                    # profitability (4th parameter) is converted to percentage and rounded to two decimal places
                    selectedProducts.append([id, name, request.GET[id], "%.2f" % round(businessRules.profitability(price, request.GET[id])[1]*100, 2), multipliers.get(id)])
            # Notice that question parameter now has another value
            return render(request, 'price.html', {'productsInfo': productForm.productsCollection, 'products': selectedProducts, 'username': username, 'question': ', um ou mais itens não alcançaram a rentabilidade mínima de 90%, por favor sugira outro preço.'})
        # If none of the suggested prices has bad profitabilities the user is directed to the resume page, which shows the order resume
        else:
            # Iterates through productsCollection looking for only products given from urls
            for id, name, price, multiplier in productForm.productsCollection:
                if id in parameters:
                    # selectedProducts is the same from the line 84
                    selectedProducts.append([id, name, request.GET[id], "%.2f" % round(businessRules.profitability(price, request.GET[id])[1]*100, 2), multipliers.get(id)])
            # Notice that the html is different, due the profitability calculation on the price page
            # is easier to use a new template if the profitability were accepeted instead to create another page.
            return render(request, 'resume.html', {'productsInfo': productForm.productsCollection, 'products': selectedProducts, 'username': username, 'question': ', seu pedido foi aceito. Obrigado por comprar conosco.'})
