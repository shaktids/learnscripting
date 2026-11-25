---
title: "Starting a project"
description: "To create the first Django project, we need to install the Django and related packages (for additional functionality). We should also have Python…"
lang: other
categories: []
author: "LearnScripting"
pubDate: 2021-08-03T10:22:55
legacy: true
wpId: 2905
draft: true
---

To create the first Django project, we need to install the Django and related packages (for additional functionality). We should also have Python installed. The best toolkit for Python and the working environment is Pycharm(recommended for installation). Django is available on pip. Run it with your terminal:

```
> pip install Django
```

To start our project at first we create a folder and then open the folder and press control plus right click and then choose the option open with cmd promt and type

```
django-admin startproject projectname
```

```
django-admin startproject website
```

In the website folder you can see the following structure:

A Django project contains the following packages and files. The outer directory is just a container for the application. We can rename it further.

- **manage.py:** It is a command-line utility which allows us to interact with the project in various ways and also used to manage an application that we will see later on in this tutorial.
- **\_\_init\_\_.py:** It is an empty file that tells to the Python that this directory should be considered as a Python package.
- **settings.py:** This file is used to configure application settings such as database connection, static files linking etc.
- **urls.py:** This file contains the listed URLs of the application. In this file, we can mention the URLs and corresponding actions to perform the task and display the view.
- **wsgi.py:** It is an entry-point for WSGI-compatible web servers to serve Django project.

## Running the project

Django project has a built-in development server which is used to run application instantly without any external web server. It means we don't need of Apache or another web server to run the application in development mode.

command for run the website

```
python manage.py runserver
```

click on the url 127.0.0.1:8000 and see our first django project
