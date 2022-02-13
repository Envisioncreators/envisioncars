from pickle import TRUE
from django.db import models

# Create your models here.
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s",(timeNow, old_filename)
    return os.path.join('uploads/',filename)


class Seller(models.Model):
    name = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 15)
    phone_wa = models.CharField(max_length= 15)
    email =  models.EmailField()
    identity = models.CharField(max_length= 50)
    identity_no = models.CharField(max_length=20)
    identity_img = models.ImageField(upload_to='images', null=TRUE, blank = True)
    address_temp = models.TextField()
    address = models.TextField()
    seller_type = models.CharField(max_length= 20)
    remarks = models.TextField() 

class Buyer(models.Model):
    name = models.CharField(max_length= 100)
    phone = models.CharField(max_length= 15)
    phone_wa = models.CharField(max_length= 15)
    email =  models.EmailField()
    identity = models.CharField(max_length= 50)
    identity_no = models.CharField(max_length=20)
    identity_img = models.ImageField(upload_to='images', null=TRUE, blank = True)
    address_temp = models.TextField()
    address = models.TextField()
    buyer_type = models.CharField(max_length= 20)
    remarks = models.TextField() 



    

