from django.shortcuts import render
from .models import Product

# Create your views here.
def show_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request = request, template_name= 'products.html', context = context)