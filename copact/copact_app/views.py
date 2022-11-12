from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

def charging_page(request):
    return render(request, 'charging_page.html')

def index(request):
    return render(request, 'index.html')

def social(request):
    return render(request, 'social.html')

def conseil(request):
    return render(request, 'conseil.html')