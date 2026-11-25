---
title: "Django apps"
description: "Create an application: In our main \"website\" folder, the same folder then manage.py − Figure:App folder init .py − Just to make sure python handles this…"
lang: other
categories: []
author: "LearnScripting"
pubDate: 2021-08-04T07:20:57
legacy: true
wpId: 2911
draft: true
---

## Create an application:

 In our main "website" folder, the same folder then manage.py −

```
python manage.py startapp appname
```

Figure:App folder

- **\_\_init\_\_.py** − Just to make sure python handles this folder as a package.
- **admin.py** − This file helps you make the app modifiable in the admin interface.
- **models.py** − This is where all the application models are stored.
- **tests.py** − This is where your unit tests are.
- **views.py** − This is where your application views are.

Now we need to register it with our Django project "website". To do so, update INSTALLED\_APPS tuple in the settings.py file of our project (add your app name) −

Now we have create a urls.py file in the app folder and change both project folder and app folder urls.py file and app folder views.py file

## urls.py file in the website folder

```
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index,name='index')
]
```

## urls.py file in the app folder

```
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index,name='index')
]
```

## views.py file in the website folder

```
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello Leanscripting")
```

## Output:

 Now, let's run the it by using the following command. This command will start the server at port 8000.
