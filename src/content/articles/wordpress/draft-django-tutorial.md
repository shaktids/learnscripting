---
title: "Django Tutorial"
description: "1.1 Home: Django is high level web framework,written in Python. A web framework is a set of components that helps you to develop websites faster and…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-05-30T11:24:05
legacy: true
wpId: 2373
draft: true
---

## 1.1 Home:

Django is high-level web framework,written in Python. A web framework is a set of components that helps you to develop websites faster and easier.

           When we're building a website, we always need a similar set of components: a way to handle user authentication (signing up, signing in, signing out), a management panel for our website, forms, a way to upload files, etc.

Luckily for us, other people long ago noticed that web developers face similar problems when building a new site, so they teamed up and created frameworks (Django being one of them) that give us ready-made components to use.

                    Frameworks exist to save our from having to reinvent the wheel and to help reduce some of the overhead when we’re building a new site.

## 1.2 Basic:

Django is free, open source web development framework written in python programming language. A “web development framework” is software that abstracts away many of the common challenges related to building a website, such as connecting to a database, handling security, user accounts, and so on. It is based on MVT (Model View Template) design pattern. It does not take more time to build a application after collecting  client information. These days most developers rely on web frameworks rather than trying to build a website truly from scratch.

## 1.3 Overview:

Django was initially developed between 2003 and 2005 by a web team who were responsible for creating and maintaining newspaper websites. After creating a number of sites, the team began to factor out and reuse lots of common code and design patterns. This common code evolved into a generic web development framework, which was open-sourced as the "Django" project in July 2005.

Django has continued to grow and improve, from its first milestone release (1.0) in September 2008 through to the recently-released version 3.1 (2020). Each release has added new functionality and bug fixes, ranging from support for new types of databases, template engines, and caching, through to the addition of "generic" view functions and classes (which reduce the amount of code that developers have to write for a number of programming tasks).

## 1.4 Django Version History:

|  |  |  |
| --- | --- | --- |
| **Version** | **Date** | **Description** |
| 0.90 | 16 Nov 2005 |  |
| 0.91 | 11 Jan 2006 | magic removal |
| 0.96 | 23 Mar 2007 | newforms, testing tools |
| 1.0 | 3 Sep 2008 | API stability, decoupled admin, Unicode |
| 1.1 | 29 Jul 2009 | Aggregates, transaction based tests |
| 1.2 | 17 May 2010 | Multiple db connections, CSRF, model validation |
| 1.3 | 23 Mar 2011 | Timezones, in browser testing, app templates. |
| 1.5 | 26 Feb 2013 | Python 3 Support, configurable user model |
| 1.6 | 6 Nov 2013 | Dedicated to Malcolm Tredinnick, db transaction management, connection pooling. |
| 1.7 | 2 Sep 2014 | Migrations, application loading and configuration. |
| 1.8 LTS | 2 Sep 2014 | Migrations, application loading and configuration. |
| 1.8 LTS | 1 Apr 2015 | Native support for multiple template engines.*Supported until at least April 2018* |
| 1.9 | 1 Dec 2015 | Automatic password validation. New styling for admin interface. |
| 1.10 | 1 Aug 2016 | Full text search for PostgreSQL. New-style middleware. |
| 1.11 LTS | 1.11 LTS | Last version to support Python 2.7.*Supported until at least April 2020* |
| 2.0 | Dec 2017 | First Python 3-only release, Simplified URL routing syntax, Mobile friendly admin. |

## 2.  django  installization step by step :

2.1 Before you can start learning Django, you must install some software on your computer. Fortunately, this is a simple three-step process:

I) Install Python

II)Install a Python Virtual Environment

III)nstall Django

For Windows users, your computer can be running any recent version of Windows (7, 8.1 or 10). This chapter also assumes you’re installing Django on a desktop or laptop computer and will use the development server and SQLite to run all the code in this book. This is by far the easiest and best way to set up Django when you are first starting.

A lot of Windows applications use Python, so it may be already installed on your system. You can check this out by opening a command prompt, or running PowerShell, and typing python at the prompt.

If Python isn’t installed you’ll get a message saying that Windows can’t find Python. If Python is installed, the python command will open the Python interactive interpreter:

2.2 Installing Django:

Installing Django is very easy, but the steps required for its installation depends on your operating system. Since Python is a platform-independent language, Django has one package that works everywhere regardless of your operating system.

You can download the latest version of Django from the link <http://www.djangoproject.com/download>

The complete installation process is described below. Before installing make sure pip is installed in local system.

Here, we are installing Django using pip, the installation command is given below.

## 3.1 Creating a Python project﻿

To get started with PyCharm, let’s write a Python script.

Let’s start our project: if you’re on the [Welcome screen](https://www.jetbrains.com/help/pycharm/welcome-screen.html), click **New Project**. If you’ve already got a project open, choose **File | New Project**.

Another way to create a django project is at first we create a folder and then press shift and right click to open command prompt in this folder.

Then go to the pycharm and open the myfirstwebsite project by new open and the project folder name.

Then click on the terminal and go the project folder where manage.py exist.In my project manage.py exist in the projectname folder .you can go to the projectname folder by the command cd projectname.

Then type the command Python manage.py runserver and see a server  http://127.0.0.1:8000/ and click here

And finally run our first django project.
