from django.shortcuts import render
from .models import Product

def result(request):
    all_product = Product.available.all()
    return render(request, "products/result.html",{'all_product': all_product})