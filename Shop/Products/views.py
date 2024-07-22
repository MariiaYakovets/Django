from django.shortcuts import render
from .models import Product

# Create your views here.
def start(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request= request, template_name= 'index.html', context= context)
    