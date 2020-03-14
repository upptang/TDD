"""first_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from lists import views
from lists import urls as list_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home_page,name='home_page'),
    url(r'^lists/',include(list_urls))#include使用一个正则表达式作为URL的前缀，这个前缀会添加到引用的URL前面
]
