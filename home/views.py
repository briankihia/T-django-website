from django.shortcuts import render
from django.http import  HttpResponse
from .models import product


# Create your views here.

def home(request):
    return render (request,'home.html')

def products(request):
    prods = product.objects.all()
    return render (request,'products.html',{'prods':prods})
