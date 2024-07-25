from django.shortcuts import render
from django.contrib.auth.models import User
from requests import Request
from django.http import HttpResponse

# Create your views here.
def show_user(request):
    pass


def login_user(request):
    pass


def register_user(request: Request):
    if request.method == 'POST':
        print(request.body)
        return HttpResponse(200)
    elif request.method == 'GET':
        return render( request= request, template_name= 'user_register.html')
        
