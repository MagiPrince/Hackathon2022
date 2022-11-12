from django.shortcuts import render

def charging_page(request):
    return render(request, 'charging_page.html')

def index(request):
    return render(request, 'index.html')

def social(request):
    return render(request, 'social.html')

def defis(request):
    return render(request, 'defis.html')