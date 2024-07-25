"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Products.views import show_products
from Users.views import show_user, login_user, register_user
from django.conf.urls.static import static
from .settings import STATIC_URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', show_products),
    path('user/', show_user, name= 'user'),
    path('user/login', login_user, name= 'login'),
    path('user/registration', register_user, name= 'registration')
]+ static(STATIC_URL)
