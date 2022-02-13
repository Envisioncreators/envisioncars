from email import message
from django.shortcuts import redirect, render
from django.http import HttpRequest,HttpResponse
from .models import Seller,Buyer
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "index.html")

def seller(request):
    if request.method=='POST':
        """ name phone phone_wa email identity identity_no identity_img address_temp address seller_type remarks """  
        obj = Seller()
        obj.name = request.POST.get('name')
        print(request.POST.get('name'))
        obj.phone = request.POST.get('phone')
        obj.phone_wa = request.POST.get('phone_wa')
        obj.email= request.POST.get('email')
        obj.identity= request.POST.get('identity')
        obj.identity_no= request.POST.get('identity_no')

        if len(request.FILES) !=0:
            obj.identity_img= request.FILES['identity_img']
            
        obj.address_temp= request.POST.get('address_temp')
        obj.address= request.POST.get('address')
        obj.seller_type = request.POST.get('seller_type')
        obj.remarks = request.POST.get('remarks')

        obj.save()
        messages.success(request, "Seller Added Successfully!")
        return redirect('/')

    return render(request, "seller.html")

def buyer(request):
    if request.method=='POST':
        """ name phone phone_wa email identity identity_no identity_img address_temp address seller_type remarks """ 
        obj = Buyer()
        obj.name = request.POST.get('name')
        obj.phone = request.POST.get('phone')
        obj.phone_wa = request.POST.get('phone_wa')
        obj.email= request.POST.get('email')
        obj.identity= request.POST.get('identity')
        obj.identity_no= request.POST.get('identity_no')

        if len(request.FILES) !=0:
            obj.identity_img= request.FILES['identity_img']
            
        obj.address_temp= request.POST.get('address_temp')
        obj.address= request.POST.get('address')
        obj.buyer_type = request.POST.get('buyer_type')
        obj.remarks = request.POST.get('remarks')
        obj.save()
        messages.success(request, "Buyer Added Successfully!")
        return redirect('/')

    return render(request, "buyer.html")

