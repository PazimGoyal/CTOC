from django.contrib.auth.models import User
from django.db import models
from supplier.models import Supplier


class Category(models.Model):
    title=models.CharField(max_length=255)
    catUID=models.CharField(unique=True,max_length=20)
    description=models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    productSKU = models.CharField(unique=True,max_length=20)
    price = models.FloatField()
    short_description = models.CharField(max_length=600)
    description = models.TextField()
    thumbnail = models.ImageField()
    quantity=models.IntegerField()
    live=models.BooleanField()
    ship_picup=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    image1 = models.ImageField(null=False)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(null=True)
    image5 = models.ImageField(null=True)



