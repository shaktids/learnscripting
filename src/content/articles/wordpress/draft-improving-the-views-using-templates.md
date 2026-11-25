---
title: "Improving the views using templates"
description: "What is templates Templates are the third and most important part of Django MVT Structure. A template in Django is basically written in HTML, CSS and…"
lang: other
categories: []
author: "LearnScripting"
pubDate: 2021-08-05T23:22:29
legacy: true
wpId: 2925
draft: true
---

## What is templates

Templates are the third and most important part of Django MVT Structure. A template in Django is basically written in HTML, CSS and Javascript in an .html file. Django framework efficiently handles and generates dynamically HTML web pages that are visible to end-user.

To configure the template system, we have to provide some entries in **settings.py** file and mentioned the templates directory name as 'templates'

## Template creation:Right click on th project name and then click directory

Right click on the directory and then click html template

## Set urls.py folder:

```
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index,name='index'),

]
```

## set views.py folder

```
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
```

Then goto the terminal and type

```
python manage.py runserver
```

## Variable passing through templates:

Django template uses its own syntax to deal with variable, tags, expressions etc. To deal with the variable we have to change the views.py folder and index.html folder..

## views.py

```
from django.shortcuts import render,HttpResponse

# Create your views here.
context={"name":"Learnscripting"}
def index(request):
    return render(request,'index.html',context)
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Templates</title>
</head>
<body>
<h>The website name is {{name}}</h>
</body>
</html>
```

Then go to terminal and type the syntax ...python manage.py runserver

## Template inheritance

Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

Django allows us to avoid that by creating a ‘base’ template which contains the common components and inheriting that template in all our other templates.

## base.html

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Template Inheritence</title>
</head>
<body>
<h2>Basic File Inheritence</h2>
{% block content %}
    <p> PlaceHolder to be Replaced</p>
{% endblock %}
</body>
</html>
```

## login.html

```
{% extends 'base.html' %}
{% block content %}
        <h3>Welcome to the App</h3><br>
{% endblock %}
```

## output
