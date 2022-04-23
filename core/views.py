from django.shortcuts import render
from product.models import Product

# Create your views here.


def frontpage(request):
    products = Product.objects.all()[0:8] #only first 8
    context = {'products':products}
    return render(request,'core/frontpage.html',context)
