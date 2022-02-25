from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "basetemp/index.html")


def test(request):
    return HttpResponse("Hello this is test_1")


def buyer(request):
    return render(request, "basetemp/buyer.html")


def seller(request):
    return render(request, "basetemp/seller.html")
