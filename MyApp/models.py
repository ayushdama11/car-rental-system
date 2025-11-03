from email.policy import default
from django.db import models

class Car(models.Model):
    VEHICLE_TYPES = (
        ('car', 'Car'),
        ('van', 'Van'),
        ('bike', 'Bike'),
    )
    car_id = models.IntegerField(default=0)
    car_name = models.CharField(max_length=30,default="")
    car_desc = models.CharField(max_length=300,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="car/images",default="")
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPES, default='car')

    def __str__(self):
        return self.car_name

class Order(models.Model) :
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
    )
    
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    cars = models.CharField(max_length=50,default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50,default="")
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    issue_reported = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    phone_number = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def __str__(self) :
        return self.name
