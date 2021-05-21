from django.shortcuts import render

# Create your views here.
from .models import Product
def all_products(request):
    products=Product.object.all()
    return products

