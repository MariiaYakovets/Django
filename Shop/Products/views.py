from django.shortcuts import render, redirect
from .models import Product
import json
from django.http import HttpResponse


# Create your views here.
def show_products(request):
    # if request.user.is_authenticated:
    user = request.user
    products = Product.objects.all()
    context = {'products': products, 'user': user}
    return render(request = request, template_name= 'products.html', context = context)

    # else:
    #     return redirect('login')
def create_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            byte_data = request.body
            data = json.loads(byte_data.decode("utf-8"))
            name = data['name']
            price = data['price']
            description = data['description']
            image = data['image']
            product = Product.objects.create(name= name, price= price, description= description, image= image)
            product.save()
            return HttpResponse(status=200, reason="Product has been successfully created")
            
        elif request.method == 'GET':
            return render(request= request, template_name= 'create_product.html')
    else:
        return redirect('login')
