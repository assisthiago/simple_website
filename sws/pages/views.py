from django.shortcuts import render

from products.models import Product


def index(request):
    last_arrivals = Product.last_arrivals()
    context = {'last_arrivals' : last_arrivals}
    return render(request, 'pages/index.html', context=context)

def listings(request):
    return render(request, 'pages/listings.html')

def details(request):
    return render(request, 'pages/details.html')
