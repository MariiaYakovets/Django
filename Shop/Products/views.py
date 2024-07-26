from django.shortcuts import render, redirect
from .models import Product


# Create your views here.
def show_products(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        context = {'products': products}
        return render(request = request, template_name= 'products.html', context = context)
    else:
        return redirect('login')

