from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def listings(request):
    return render(request, 'pages/listings.html')
