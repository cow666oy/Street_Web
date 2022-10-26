from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def glav(request):
    return render(request, 'main/Главная.html')

def about(request):
    return render(request, 'main/about.html')

def Store(request):
    return render(request, 'main/Store.html')

def YUMMS(request):
    return render(request, 'main/YUMMS.html')

    
