from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from requests import Request
from django.http import HttpResponse
import json
from django.contrib.auth import authenticate, login


# Create your views here.
def show_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        context = {"username": username}
        return render(request=request, template_name="user.html", context=context)
    else:
        return redirect("login")


def login_user(request):
    if request.method == "POST":
        byte_data = request.body
        data = json.loads(byte_data.decode("utf-8"))
        username = data["username"]
        password = data["password"]
        auth_user = authenticate(request=request, username=username, password=password)
        if auth_user is not None:
            login(request=request, user=auth_user)
            return redirect("user")
        else:
            return HttpResponse(status=401, reason="Wrong username or password")

    elif request.method == "GET":
        return render(request=request, template_name="user_login.html")


def register_user(request: Request):
    if request.method == "POST":
        byte_data = request.body
        data = json.loads(byte_data.decode("utf-8"))
        username = data["username"]
        email = data["email"]
        password = data["password"]
        user = User.objects.filter(username=username, email=email)
        if not user.exists():
            new_user = User.objects.create_user(
                username=username, email=email, password=password
            )
            new_user.save()
            auth_user = authenticate(
                request=request, username=username, password=password
            )
            if auth_user is not None:
                # запоминание юзера через сессию
                login(request=request, user=auth_user)
                # return redirect('products')
                return HttpResponse(status=200, reason="Success")
            else:
                return HttpResponse(status=500, reason="Server found error, sorry :(")

        else:
            return HttpResponse(status=404, reason="This user already exists")

    elif request.method == "GET":
        return render(request=request, template_name="user_register.html")
