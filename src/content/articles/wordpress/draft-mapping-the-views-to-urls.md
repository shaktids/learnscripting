---
title: "Mapping the views to URLs"
description: "A request in Django first comes to urls.p y and then goes to the matching function in views.py. Python functions in views.py take the web request from…"
lang: other
categories: []
author: "LearnScripting"
pubDate: 2021-08-05T09:18:46
legacy: true
wpId: 2919
draft: true
---

A request in Django first comes to urls.p*y* and then goes to the matching function in views.py. Python functions in views.py take the web request from urls.py and give the web response to templates. It may go to the data access layer in models.py as per the queryset.

Django has a urls.py file under the project by default. It also has a prep-defined path for the *admin* app. However, Django recommends mapping all resources via another urls.py newly created under the app.

## website urls.py folder:

```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls'))
]
```

## myapp urls.py folder:

```
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
]
```

## myapp views.py folder:

```
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello Leanscripting")
def login(request):
    return HttpResponse("welcome to login page")
def register(request):
    return HttpResponse("This is register page")
```

## Running our First app:
