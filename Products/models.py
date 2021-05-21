from django.db import models

from supplier.models import Supplier


class Category(models.Model):
    title = models.CharField(max_length=255)
    catUID = models.CharField(unique=True, max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    productSKU = models.CharField(unique=True, max_length=20)
    price = models.FloatField()
    short_description = models.CharField(max_length=600)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField()
    live = models.BooleanField()
    ship_picup = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image1 = models.ImageField(null=False)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
