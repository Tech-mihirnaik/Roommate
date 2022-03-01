from django.db import models
import datetime
from django.db.models.aggregates import Max
from django.db.models.fields import CharField

# Create your models here.

class bookedCab(models.Model):
    email=models.CharField(max_length=50,default='')
    PassName=models.CharField(max_length=40)
    PassPhone=models.CharField(max_length=40)
    PassPickup=models.CharField(max_length=40)
    PassDrop=models.CharField(max_length=40)
    Car=models.CharField(max_length=40)
    PassDate=models.CharField(max_length=40)
    PassTime=models.CharField(max_length=40)

    booking_id=models.CharField(max_length=40,default=0)
    cab_id = models.CharField(max_length=30, default=0)
    date = models.DateTimeField(default=datetime.datetime.now())

    payment = models.BooleanField(default=False)  # should be updated after complete is marked
    total = models.IntegerField(default=0)
    advpay_price=models.IntegerField(default=0)
    advpay_link=models.CharField(max_length=100,default=0)
    duepay_price=models.IntegerField(default=0)

    transaction_id = models.CharField(max_length=50, default=0)
    transaction_date = models.CharField(max_length=50, default=0)
    bank_transaction_id_200=models.CharField(max_length=50,default=0)
    bank_name_200=models.CharField(max_length=50,default=0)

    confirmation = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)  # if confirmed(true) from dashboard then pending should be true
    completed = models.BooleanField(default=False)  # when pending will be marked completed then pending eill be again false and completed will be true payment  should be set to true


    def __str__(self):
        return self.PassName+'_'+self.booking_id

class driver(models.Model):

    driver_name=models.CharField(max_length=30)
    cab_registration_no=models.CharField(max_length=10)
    contact_no=models.IntegerField()
    car_type=models.CharField(max_length=10)
    price=models.IntegerField(default=0)#value will be same as amount due
    booking_id=models.CharField(max_length=40,default='')

    def __str__(self):
        return self.driver_name

class addcab(models.Model):
    cab_id=models.CharField(max_length=30,default="")
    cab_name=models.CharField(max_length=100,default="")
    category=models.CharField(max_length=30)
    PassPickup=models.CharField(max_length=40)
    PassDrop=models.CharField(max_length=40)
    discount=models.CharField(max_length=30)
    description=models.CharField(max_length=3000,default="Best in class cab service with AC facilities .Enjoy your journey with your loved ones.")
    email=models.CharField(max_length=50)
    date=models.CharField(max_length=15,default="")
    price=models.CharField(max_length=30)
    image1=models.FileField(upload_to='media/')
    verified=models.BooleanField(default=False)
    def __str__(self):
        return self.cab_name+'_'+self.cab_id+'_'+self.category

class cabowner(models.Model):
    Email=models.CharField(max_length=40,default=False)
    CabOwnerName=models.CharField(max_length=40)
    CabOwnerContact=models.CharField(max_length=20,null=True)
    CabOwnerPhoto=models.FileField(upload_to='media/', null=True)
    CabOwnerAdhar=models.FileField(upload_to='media/', null=True)
    CabOwnerPan=models.FileField(upload_to='media/', null=True)
    vechileType=models.CharField(max_length=15)
    CabName=models.CharField(max_length=50)
    CabContactNo=models.CharField(max_length=15)
    CabNumberPlate=models.CharField(max_length=30)
    CabPhoto=models.FileField(upload_to='media/', null=True)
    CabNumberPhoto=models.FileField(upload_to='media/', null=True)
    Cabregistration=models.FileField(upload_to='media/', null=True)
    CabAllData=models.FileField(upload_to='media/', null=True)
    isverified=models.BooleanField(default=False)

    def __str__(self):
        return self.CabOwnerName

