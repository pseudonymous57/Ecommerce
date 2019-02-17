from django.shortcuts import render, HttpResponse, redirect
from shop101.models import Product

# Create your views here.
def test(request):
    return HttpResponse('Hello World')

def product_list(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'products_list.html', context={'product_list':products})

def product_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product_view.html', context={'product': product})