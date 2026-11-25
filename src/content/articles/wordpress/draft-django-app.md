---
title: "Django App"
description: "Django application consists of project and app, it also generates an automatic base directory for the app, so we can focus on writing code (business…"
lang: other
categories: []
author: "LearnScripting"
pubDate: 2021-07-26T04:08:28
legacy: true
wpId: 2879
draft: true
---

Django application consists of project and app, it also generates an automatic base directory for the app, so we can focus on writing code (business logic) rather than creating app directories.

The difference between a project and app is, a project is a collection of configuration files and apps whereas the app is a web application which is written to perform business logic.

## Creating an app:

To create an app, we can use the following command.

```
 python3 manage.py startapp appname
```

## Django app Example:

```
python manage.py startapp firstapp
```

Project folder :

These files are:

- The outer `website/` root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](https://docs.djangoproject.com/en/3.2/ref/django-admin/).
- The inner `website/` directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `website.urls`).
- `website/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
- `website/settings.py`: Settings/configuration for this Django project. [Django settings](https://docs.djangoproject.com/en/3.2/topics/settings/) will tell you all about how settings work.
- `website/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/3.2/topics/http/urls/).
- `website/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/) for more details.
- `mwebsite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/) for more details.

To consider the app in your project you need to specify your project name in INSTALLED\_APPS list as follows in settings.py:
