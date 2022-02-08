from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def home(request):
    return render(request, "index.html")

def seller(request):
    return render(request, "seller.html")

def buyer(request):
    return render(request, "buyer.html")
