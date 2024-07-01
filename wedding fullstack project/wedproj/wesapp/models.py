from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
class Wedding(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-defaul,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    

class Traditional(models.Model):
    category=models.ForeignKey(Wedding,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    hall_image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    old_price=models.IntegerField(null=True,blank=True)
    dis_price=models.IntegerField(null=False,blank=False)
    adress=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-defaul,1-Hidden")
    handpicked=models.BooleanField(default=False,help_text="0-defaul,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Traditional,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    
class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Traditional,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gname= models.CharField(max_length=150,null=False,blank=False)
    bname= models.CharField(max_length=150,null=False,blank=False)
    email= models.EmailField(max_length=150,null=True,blank=True)
    occ_date = models.DateField(null=False,blank=False)
    total_price = models.FloatField(null=False,blank=False)
    payment_mode = models.CharField(max_length=150,null=False,blank=False)
    payment_id = models.CharField(max_length=250,null=True,blank=True)
    orderstatuses =(
        ('Pending','Pending'),
        ('Everything getting ready','Everything getting ready'),
        ('Completed','Completed'),
    )
    status = models.CharField( max_length=150,choices=orderstatuses,default='Pending')
    message = models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return '{} - {}'.format(self.id)


class OdrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Traditional, on_delete=models.CASCADE)
    price =  models.FloatField(null=False,blank=False)
    
    def __str__(self) -> str:
        return '{} {}'.format(self.order.id)
    
