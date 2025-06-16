from django.shortcuts import render
from ..models import Product


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})
