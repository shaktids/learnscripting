---
title: "Django Interview Questions and Answers"
description: "1. What is Django? Ans: Django is a high level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2021-01-18T11:38:28Z
legacy: true
wpId: 2150
draft: true
---

#### 1. What is Django?
**Ans:** **Django** is a high-level **Python** Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open-source..

---

#### 2. What does Django mean?
**Ans:** Django is named after Django Reinhardt, a gypsy jazz guitarist from the 1930s to early 1950s who is known as one of the best guitarists of all time.

---

#### 3. Which architectural pattern does Django Follow?
**Ans:** Django follows **Model-View Template** (MVT) architectural pattern.

---

#### 4. Explain the architecture of Django?
**Ans:** Django is based on **MVT** architecture. It contains the following layers:

Models: It describes the database schema and data structure.

Views: The view layer is a user interface. It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data, and pass it to the template.

Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page.

Controller: Controller is the heart of the system. It handles requests and responses, setting up database connections and loading add-ons. It specifies the Django framework and URL parsing.

---

#### 5. Which foundation manages Django web framework?
Ans: Django web framework is managed and maintained by an independent and non-profit organization named Django Software Foundation (DSF).

---

#### 6. Is Django stable?
**Ans:** Yes, Django is quite stable. Many companies like Disqus, Instagram, Pinterest, and Mozilla have been using Django for many years.

---

#### 7. What are the features available in Django web framework?
**Ans:** Features available in Django web framework are:

Admin Interface (CRUD)
Templating
Form handling
Internationalization
Session, user management, role-based permissions
Object-relational mapping (ORM)
Testing Framework
Fantastic Documentation

---

#### 8. What are the advantages of using Django for web development?
**Ans:** It facilitates you to divide code modules into logical groups to make it flexible to change.
It provides auto-generated web admin to make website administration easy.
It provides pre-packaged API for common user tasks.
It provides template system to define HTML template for your web page to avoid code duplication.
It enables you to define what URL is for a given function.
It enables you to separate business logic from the HTML.

---

#### 9. How to create a project in Django?
**Ans:** To start a project in Django, use the command $django-admin.py and then use the following command:

Project

\_init\_.py

manage.py

settings.py

urls.py

---

#### 10. What are the inheritance styles in Django?
**Ans:** There are three possible inheritance styles in Django:

**1. Abstract base classes:** This style is used when you only want parent?s class to hold information that you don’t want to type out for each child model.

**2. Multi-table Inheritance:** This style is used if you are sub-classing an existing model and need each model to have its own database table.

**3. Proxy models:** This style is used, if you only want to modify the Python level behavior of the model, without changing the model’s fields.

---

#### 11. How can you set up the database in Djanago?
**Ans:** To set up a database in Django, you can use the command edit mysite/setting.py , it is a normal python module with module level representing Django settings.

By default, Django uses SQLite database. It is easy for Django users because it doesn’t require any other type of installation. In the case of other database you have to the following keys in the DATABASE ‘default’ item to match your database connection settings.

Engines: you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql\_psycopg2’, ‘django.db.backends.oracle’ and so on

Name: The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.

Note: You have to add setting likes setting like Password, Host, User, etc. in your database, if you are not choosing SQLite as your database.

---

#### 12. What does the Django templates contain?
**Ans:** A template is a simple text file. It can create any text-based format like XML, CSV, HTML, etc. A template contains variables that get replaced with values when the template is evaluated and tags (%tag%) that controls the logic of the template.

---

#### 13. Is Django a content management system (CMS)?
**Ans:** No, Django is not a CMS. Instead, it is a Web framework and a programming tool that makes you able to build websites.

---

#### 14. What is the use of session framework in Django?
**Ans:** The session framework facilitates you to store and retrieve arbitrary data on a per-site visitor basis. It stores data on the server side and abstracts the receiving and sending of cookies. Session can be implemented through a piece of middleware.

---

#### 15. How can you set up static files in Django?
**Ans:** There are three main things required to set up static files in Django:

1. Set STATIC\_ROOT in settings.py

2. run manage.py collectsatic

3. set up a Static Files entry on the PythonAnywhere web tab

---

#### 16. How to use file based sessions?
**Ans:** You have to set the SESSION\_ENGINE settings to “django.contrib.sessions.backends.file” to use file based session.

---

#### 17. What is some typical usage of middlewares in Django?
**Ans:** Some usage of middlewares in Django is:

Session management,
Use authentication
Cross-site request forgery protection
Content Gzipping, etc.

---

#### 18. What does of Django field class types do?
**Ans:** The Django field class types specify:

The database column type.
The default HTML widget to avail while rendering a form field.
The minimal validation requirements used in Django admin.
Automatic generated forms.

---

#### 19. What is the command to start Django’s built-in development server?
A. manage.py runserver
B. manage.py –start
C. manage.py run
D. manage.py startserver –dev
E. manage.py –run
Ans: A

---

#### 20. Given a model named ‘User’ that contains a DateTime field named ‘last\_login’, how do you query for users that have never logged in?
A. User.objects.filter( last\_login=Null )
B. User.objects.filter( last\_login\_\_null=True )
C. User.objects.filter( last\_login\_\_isnull=False )
D. User.objects.filter( last\_login\_\_isnull=True )
E. User.objects.filter( last\_login=Never )
Ans: D

---

#### 21. What does the Django command `manage.py shell` do?
A. Starts a command line in whatever $SHELL your environment uses.
B. Starts a Django command prompt with your Python environment pre-loaded.
C. Starts a Python command prompt with your Django environment pre-loaded.
D. Loads a special Pythonic version of the Bash shell.
E. Loads a Python command prompt you can use to sync your database schema remotely.
Ans: C

---

#### 22. Assuming you’ve imported the proper Django model file, how do you add a ‘User’ model to the Django admin?
A. admin.register( Users )
B. admin.site( self, User )
C. user.site.register( Admin )
D. users.site.register( Admin )
E. admin.site.register( User )
Ans: E

---

#### 23. What is the Django command to start a new app named ‘users’ in an existing project?
A. manage.py –newapp users
B. manage.py newapp users
C. manage.py –startapp users
D. manage.py startapp users
E. manage.py start users
Ans: D

---

#### 24. What does a urls.py file do in Django?
A. This file contains site deployment data such as server names and ports.
B. It contains a site map of Django-approved URLs.
C. It contains URL matching patterns and their corresponding view methods.
D. You run this file when you get obscure 404 Not Found errors in your server logs.
E. This file provides an up to date list of how-to URLs for learning Django more easily.
Ans: C

---

#### 25. What is the command to run Django’s development server on port 8080 on IP address 12.34.56.78?
A. manage.py –run 12.34.56.78 8080
B. manage.py –dev 12.34.56.78:8080
C. manage.py runserver 12.34.56.78:8000
D. manage.py run 12.34.56.78:8080
E. manage.py runserver 12.34.56.78:8080
Ans: E

---

#### 26. Django is written using what programming language?
A. PHP
B. Ruby
C. Javascript
D. Java
E. Python
Ans: E

---

#### 27. After you make a new ‘app’ in your existing Django project, how do you get Django to notice it?
A. No additional action is required, Django notices new apps automatically.
B. Run the `manage.py validate` command, and then start a new shell.
C. Run the `manage.py syncdb` command.
D. In settings.py, add the app to the PROJECT\_APPS variable.
E. In settings.py, add the new app to the INSTALLED\_APPS variable.
Ans: E

#### 28. What is the purpose of settings.py?
A. To configure settings for the Django project
B. To configure settings for an app
C. To set the date and time on the server
D. To sync the database schema
Ans: A

---

#### 29. How do you define a ‘name’ field in a Django model with a maximum length of 255 characters?
A. name = models.CharField(max\_len=255)
B. model.CharField(max\_length=255)
C. name = models.CharField(max\_length=255)
D. model = CharField(max\_length=255)
E. name = model.StringField(max\_length=auto)
Ans: C

---

#### 30. What is the definition of a good Django app?
A. A good Django app provides a small, specific piece of functionality that can be used in any number of Django projects.
B. A good Django app is a fully functioning website that has 100% test coverage.
C. A good Django app is highly customized and cannot be used in multiple projects.
Ans: A

---

#### 31. What is the most easiest, fastest, and most stable deployment choice in most cases with Django?
A. FastCGI
B. mod\_wsgi
C. SCGI
D. AJP
Ans: B

---

#### 32. How do you exclude a specific field from a ModelForm?
A. Create a new Form, don’t use a ModelForm
B. Use the exclude parameter in the Meta class in your form
C. Set the field to hidden
D. You can not do this
Ans: B

---

#### 33. Assuming you have a Django model named ‘User’, how do you define a foreign key field for this model in another model?
A. model = new ForeignKey(User)
B. user = models.IntegerKey(User)
C. user = models.ForeignKey(User)
D. models.ForeignKey( self, User )
Ans: C

---

#### 34. What preferred method do you add to a Django model to get a better string representation of the model in the Django admin?
A. \_\_unicode\_\_
B. to\_s( self )
C. \_\_translate\_\_
D. \_\_utf\_8\_\_
Ans: A

---

#### 36. What is Model Form used for?
A. To model an input form for a template
B. To specify rules for correct form when writing Django code
C. To define a form based on an existing model
Ans: C

---

#### 37. What happens if MyObject.objects.get() is called with parameters that do not match an existing item in the database?
A. The Http404 exception is raised.
B. The DatabaseError exception is raised.
C. The MyObject.DoesNotExist exception is raised.
D. The object is created and returned.
Ans: C

---

#### 38. A set of helpful applications to use within your Django projects is included in the official distribution. This module is called what?
A. django.extras
B. django.helpers
C. django.utilities
D. django.ponies
E. django.contrib
Ans: E

---

#### 39. What is the correct syntax for including a class based view in a URLconf?
A. (r’^pattern/$’, YourView.as\_view()),
B. (r’^pattern/$’, YourView.init()),
C. (r’^pattern/$’, YourView),
D. (r’^pattern/$’, YourView()),
Ans: A

---

#### 40. What is the command to start a new Django project called ‘myproject’?
A. django-admin.py startproject myproject
B. django-admin.py –start myproject
C. django.py startproject myproject
D. django.py –new myproject
E. django.py new myproject
Ans: A

---

#### 41. How to make django timezone-aware?
A. In settings.py: USE\_L10N=True
B. in views.py, import timezone
C. in views.py, import tz
D. in urls.py, import timezone
E. In settings.py: USE\_TZ=True
Ans: E

---

#### 42. In Django how would you retrieve all the ‘User’ records from a given database?
A. User.objects.all()
B. Users.objects.all()
C. User.all\_records()
D. User.object.all()
E. User.objects
Ans: A

---

#### 43. How can you define additional behavior and characteristics of a Django class?
A. def setUp():
B. class Meta:
C. class \_\_init\_\_:
D. def Meta():
E. def \_\_init\_\_():
Ans: B

---

#### 44. What is the Django shortcut method to more easily render an html response?
A. render\_to\_html
B. render\_to\_response
C. response\_render
D. render
Ans: B

---

#### 45. What does the Django command `manage.py validate` do?
A. Checks for errors in your views.
B. Checks for errors in your templates.
C. Checks for errors in your controllers.
D. Checks for errors in your models.
E. Checks for errors in your settings.py file.
Ans: D

---

#### 46. What is the correct way to include django’s admin urls? from django.contrib import admin’) from django.conf.urls import patterns, include, url urlpatterns = patterns(”, \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ )
A. url(r’^admin/’, admin.as\_view(), name=’admin ),
B. url(r’^admin/’, include(admin) ),
C. url(r’^admin/’, include(admin.site.urls) ),
D. url(r’^admin/’, admin.urls ),
E. admin.autodiscover()
Ans: C

---

#### 47. Where is pre\_save signal in Django
A. from django.db.models import pre\_save
B. from django.db.models.signals import pre\_save
C. There is no pre\_save signal
D. from django.db.models.signal import pre\_save
Ans: B

---

#### 48. Given the Python data: mydata = [ [ 0, ‘Fred’ ], [ 1, ‘Wilma’ ] ] How do you access the data in a Django template?
A. {% for d in mydata %}

{% d.1 %}

{% endfor %}
B. {% for d in mydata -%}

{{ d.1 }}

{% end -%}
C. {% for d in mydata %}

{{ d.1 }}

{% endfor %}
D. {{ for d in mydata }}

{{ d[1] }}

{{ endfor }}
E. {% mydata.each |d| %}

{{ d.2 }}

{% end %}
Ans: C

---

#### 49. What is the purpose of the STATIC\_ROOT setting?
A. Defines the URL prefix where static files will be served from .
B. Defines the location where all static files will be copied by the ‘collectstatic’ management command, to be served by the production webserver.
C. A project’s static assets should be stored here to be served by the development server.
D. Defines the location for serving user uploaded files.
Ans: B

---

#### 50. How to create a DateTimeField named created and filled in only on the creation with the current time?
A. created = models.CreationTimeField()
B. created = models.DateTimeField(default=datetime.datetime.now())
C. created = models.DateTimeField(auto\_now\_add=True, auto\_now=True)
D. created = models.DateTimeField(auto\_now=True)
E. created = models.DateTimeField(auto\_now\_add=True)
Ans: E

### 51. What is the difference between a project and an app in Django?
**Ans:** In Django, a project is the entire application and an app is a module inside the project that deals with one specific requirement. E.g., if the entire project is an ecommerce site, then inside the project we will have several apps, such as the retail site app, the buyer site app, the shipment site app, etc.

---

### 52. What is Django Admin Interface?
**Ans:** Django comes with a fully customizable in-built admin interface, which lets us see and make changes to all the data in the database of registered apps and models. To use a database table with the admin interface, we need to register the model in the admin.py file.

---

### 53. Explain Django’s Request/Response Cycle.
**Ans:** In the Request/Response Cycle, first, a request is received by the Django server. Then, the server looks for a matching URL in the urlpatterns defined for the project. If no matching URL is found, then a response with 404 status code is returned. If a URL matches, then the corresponding code in the view file associated with the URL is executed to build and send a response.

---

### 54. What is a model in Django?
**Ans:** A model is a Python class in Django that is derived from the django.db.models.Model class. A model is used in Django to represent a table in a database. It is used to interact with and get results from the database tables of our application.

---

### 55. What are migrations in Django?
**Ans:** A migration in Django is a Python file that contains changes we make to our models so that they can be converted into a database schema in our DBMS. So, instead of manually making changes to our database schema by writing queries in our DBMS shell, we can just make changes to our models. Then, we can use Django to generate migrations from those model changes and run those migrations to make changes to our database schema.

---

### 56. What are views in Django?
**Ans:** A view in Django is a class and/or a function that receives a request and returns a response. A view is usually associated with urlpatterns, and the logic encapsulated in a view is run when a request to the URL associated with it is run. A view, among other things, gets data from the database using models, passes that data to the templates, and sends back the rendered template to the user as an HttpResponse.

---

### 57. What is the use of the include function in the urls.py file in Django?
**Ans:** As in Django there can be many apps, each app may have some URLs that it responds to. Rather than registering all URLs for all apps in a single urls.py file, each app maintains its own urls.py file, and in the project’s urls.py file we use each individual urls.py file of each app by using the include function.

---

### 58. Why is Django called a loosely coupled framework?
**Ans:** Django is called a loosely coupled framework because of its MVT architecture, which is a variant of the MVC architecture. It helps in separating the server code from the client-related code. Django’s models and views take care of the code that needs to be run on the server like getting records from database, etc., and the templates are mostly HTML and CSS that just need data from models passed in by the views to render them. Since these components are independent of each other, Django is called a loosely coupled framework.

---

#### 59.Mention the architecture of [Django](https://www.kausalvikash.in/python-training-in-pune/) architecture?
**Ans:** Django architecture consists of

- **Models:** It describes your database schema and your data structure
- **Views:** It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template
- **Templates:** It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page
- **Controller:** The Django framework and URL parsing

---

#### 60. Why [Django](https://www.kausalvikash.in/python-training-in-pune/) should be used for web-development?
**Ans:**

- It allows you to divide code modules into logical groups to make it flexible to change
- To ease the website administration, it provides auto-generated web admin
- It provides pre-packaged API for common user tasks
- It gives you template system to define HTML template for your web page to avoid code duplication
- It enables you to define what URL be for a given function
- It enables you to separate business logic from the HTML
- Everything is in python

---

#### 61. Explain how you can create a project in [Django](https://www.kausalvikash.in/python-training-in-pune/)?
**Ans:**To start a project in Django, you use command $ django-admin.py and then use the command
**Project**
**\_init\_.py**
**manage.py**
**settings.py**
**urls.py**

---

#### 62. Explain how you can set up the Database in Django?
**Ans:**You can use the command edit **mysite/setting.py**, it is a normal python module with module level representing Django settings.
Django uses SQLite by default; it is easy for Django users as such it won’t require any other type of installation. In the case your database choice is different that you have to the following keys in the **DATABASE ‘default’**item to match your database connection settings

- **Engines:** you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql\_psycopg2’, ‘django.db.backends.oracle’ and so on
- **Name:**The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.

If you are not choosing SQLite as your database then setting like Password, Host, User, etc. must be added.

---

#### 63. Give an example how you can write a VIEW in [Django](https://www.kausalvikash.in/python-training-in-pune/)?
**Ans:**Views are Django functions that take a request and return a response.  To write a view in Django we take a simple example of “Guru99\_home” which uses the template Guru99\_home.html and uses the date-time module to tell us what the time is whenever the page is refreshed.  The file we required to edit is called view.py, and it will be inside mysite/myapp/

Copy the below code into it and save the file
**from datatime import datetime**
**from django.shortcuts import render**
**def home (request):**
**return render(request, ‘Guru99\_home.html’, {‘right\_now’: datetime.utcnow()})**
Once you have determined the VIEW, you can uncomment this line in urls.py
**# url ( r ‘^$’ , ‘mysite.myapp.views.home’ , name ‘Guru99’),**
The last step will reload your web app so that the changes are noticed by the web server.

---

#### 64. Explain how you can setup static files in Django?
**Ans:**There are three main things required to set up static files in Django

- Set STATIC\_ROOT in settings.py
- run manage.py collectsatic
- set up a Static Files entry on the **PythonAnywhere** web tab

---

#### 65. Mention what does the Django templates consists of?
**Ans:**The template is a simple text file.  It can create any text-based format like XML, CSV, HTML, etc.  A template contains variables that get replaced with values when the template is evaluated and tags (% tag %) that controls the logic of the template.

---

#### 66. Explain the use of session framework in Django?
**Ans:** In Django, the session framework enables you to store and retrieve arbitrary data on a per-site-visitor basis.  It stores data on the server side and abstracts the receiving and sending of cookies.  Session can be implemented through a piece of middleware.

---

#### 67. Explain how you can use file based sessions?
**Ans:**To use file based session you have to set the **SESSION\_ENGINE**settings to “django.contrib.sessions.backends.file”

---

#### 68. Explain the migration in Django and how you can do in SQL?
**Ans:**Migration in Django is to make changes to your models like deleting a model, adding a field, etc. into your database schema.  There are several commands you use to interact with migrations.

- Migrate
- Makemigrations
- Sqlmigrate

To do the migration in SQL, you have to print the SQL statement for resetting sequences for a given app name.
**django-admin.py sqlsequencreset**
Use this command to generate SQL that will fix cases where a sequence is out sync with its automatically incremented field data.

---

#### 69. Mention what command line can be used to load data into Django?
**Ans:**To load data into Django you have to use the command line**Django-admin.py loaddata.**The command line will searches the data and loads the contents of the named fixtures into the database.

---

#### 70. Explain what does django-admin.py makemessages command is used for?
**Ans:**This command line executes over the entire source tree of the current directory and abstracts all the strings marked for translation.  It makes a message file in the locale directory.

---

#### 71. List out the inheritance styles in Django?
**Ans:**In Django, there is three possible inheritance styles

- **Abstract base classes:** This style is used when you only wants parent’s class to hold information that you don’t want to type out for each child model
- **Multi-table Inheritance:** This style is used If you are sub-classing an existing model and need each model to have its own database table
- **Proxy models:** You can use this model, If you only want to modify the Python level behavior of the model, without changing the model’s fields

---

#### 72. Mention what does the Django field class types?
**Ans:**Field class types determines

- The database column type
- The default HTML widget to avail while rendering a form field
- The minimal validation requirements used in Django admin and in automatically generated forms

---

#### 73. What constitutes Django templates ?
**Ans**: Template can create formats like XML,HTML and CSV(which are text based formats). In general terms template is a simple text file. It is made up of variables that will later be replaced by values after the template is evaluated and has tags which will control template’s logic.

---

#### 74. List some typical usage of middlewares in Django.
**Ans:**Some of the typical usage of middlewares in Django are: Session management, user authentication, cross-site request forgery protection, content Gzipping, etc.

---

#### 75. How do you use views in Django?
**Ans:**Views will take request to return response.  Let’s write a view in Django :  “example” using template example.html , using  the date-time module to tell us exact time of reloading the page.  Let’s edit a file called view.py, and it will be inside randomsite/randomapp/
**To do this save and copy following into a file:**
Default

from datatime import datetime

from django.shortcuts import render

def home (request):

return render(request, ‘Guru99\_home.html’, {‘right\_now’: datetime.utcnow()})
Default

You have to determine the  VIEW first, and then uncomment this line located in file *urls.py*

**# url ( r ‘^$’ , ‘randomsite.randomapp.views.home’ , name ‘example’),**

---

#### 76. How do you make a Django app that is test driven and will display Fibonacci’s sequence?
This will reload the site making changes obvious.

**Ans:**Keep in mind that it should take an index number and output the sequence. Additionally, there should be a page that shows the most recent generated sequences.

Following is one of the solution for generating fibonacci series:
Default

def fib(n):

“Complexity: O(log(n))”

if n &lt;= 0:

return 0

i = n – 1

(a, b) = (1, 0)

(c, d) = (0, 1)

while i > 0:

if i % 2:

(a, b) = (d \* b + c \* a,  d \* (b + a) + c \* b)

(c, d) = (c \* c + d \* d, d \* (2 \* c + d))

i = i / 2

return a + b
Default

Below is a model that would keep track of latest numbers:

from django.db import models

class Fibonacci(models.Model):

parameter = models.IntegerField(primary\_key=True)

result = models.CharField(max\_length=200)

time = models.DateTimeField()
DefaultFor view, you can simply use the following code:

from models import Fibonacci

def index(request):

result = None

if request.method==”POST”:

try:

n=int(request.POST.get(‘n’))

except:

return Http404

try:

result = Fibonacci.objects.get(pk=n)

result.time = datetime.now()

except DoesNotExist:

result = str(fib(n))

result = Fibonacci(n, result, datetime.now())

result.save()

return direct\_to\_template(request, ‘base.html’, {‘result’:result.result})
You could use models to get last ‘n’ entities.

---

#### 77.What makes up Django architecture?
**Ans:**Django runs on MVC architecture. Following are the components that make up django architecture:

- **Models:** Models elaborate back-end stuffs like database schema.(relationships)
- **Views:**Views control what is to be shown to end-user.
- **Templates:** Templates deal with formatting of view.
- **Controller:** Takes entire control of Models.A MVC framework can be compared to a Cable TV with remote. A Television set is View(that interacts with end user), cable provider is model(that works in back-end) and Controller is remote that controls which channel to select and display it through view.

---

#### 78. What does session framework do in django framework ?
**Ans:** Session framework in django will store data on server side and interact with end-users. Session is generally used with a middle-ware. It also helps in receiving and sending cookies for authentication of a user.

---

#### 79.Can you create singleton object in python?If yes, how do you do it?
**Ans:**Yes, you can create singleton object. Here’s how you do it :

Default

|  |  |
| --- | --- |
| 12345 | class Singleton(object):def \_\_new\_\_(cls,\*args,\*\*kwargs):if not hasattr(cls,’\_inst’):cls.\_inst = super(Singleton,cls).\_\_new\_\_(cls,\*args,\*\*kwargs)return cls.\_inst |

---

#### 80. Mention caching strategies that you know in Django!
**Ans:** Few caching strategies that are available in Django are as follows:

- File system caching
- In-memory caching
- Using Memcached
- Database caching

#### 81. What are inheritance type in Django?
**Ans:**There are 3 inheritance types in Django

- Abstract base classes
- Multi-table Inheritance
- Proxy models

---

#### 82. What do you think are limitation of [Django](https://www.kausalvikash.in/python-training-in-pune/) Object relation mapping(ORM) ?
**Ans:**If the data is complex and consists of multiple joins using the SQL  will be clearer.

If Performance is a concern for your, ORM aren’t your choice. Genrally. Object-relation-mapping are considered good option to construct an optimized query, SQL has an upper hand when compared to ORM.

---

#### 83. How to Start Django project with ‘Hello World!’? Just say hello world in django project.
**Ans:** **There are 7 steps ahead to start Django project.**

**Step 1:** Create project in terminal/shell

f2finterview:~$ django-admin.py startproject sampleproject

**Step 2:** Create application

f2finterview:~$ cd sampleproject/

f2finterview:~/sampleproject$ python manage.py startapp sampleapp

**Step 3:** Make template directory and index.html file

f2finterview:~/sampleproject$ mkdir templates

f2finterview:~/sampleproject$ cd templates/

f2finterview:~/sampleproject/templates$ touch index.html

**Step 4:** Configure initial configuration in settings.py

Add PROJECT\_PATH and PROJECT\_NAME

import os

PROJECT\_PATH = os.path.dirname(os.path.abspath(\_\_file\_\_))

PROJECT\_NAME = ‘sampleproject’

Add Template directories path

TEMPLATE\_DIRS = (

os.path.join(PROJECT\_PATH, ‘templates’),

)

Add Your app to INSTALLED\_APPS

INSTALLED\_APPS = (

‘sampleapp’,

)

**Step 5:** Urls configuration in urls.py

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns(”,

url(r’^$’, ‘sampleproject.sampleapp.views.index’, name=’index’),

)

**Step 6:** Add index method in views.py

from django.shortcuts import render\_to\_response, get\_object\_or\_404

from django.template import RequestContext

def index(request):

welcome\_msg = ‘Hello World’

return render\_to\_response(‘index.html’,locals(),context\_instance=RequestContext(request))

**Step7:** Add welcome\_msg in index.html

&lt;!DOCTYPE html>

&lt;html>

&lt;body>

&lt;h1>My First Heading For Say…&lt;/h1>

&lt;p>{{welcome\_msg}}&lt;/p>

&lt;/body>

&lt;/html>

---

#### 84. How to login with email instead of username in Django?
**Ans:**Use bellow sample method to login with email or username.

from django.conf import settings
from django.contrib.auth import authenticate, login, REDIRECT\_FIELD\_NAME
from django.shortcuts import render\_to\_response
from django.contrib.sites.models import Site
from django.template import Context, RequestContext
from django.views.decorators.cache import never\_cache
from django.views.decorators.csrf import csrf\_protect
@csrf\_protect
@never\_cache
def signin(request,redirect\_field\_name=REDIRECT\_FIELD\_NAME,authentication\_form=LoginForm):
redirect\_to = request.REQUEST.get(redirect\_field\_name, settings.LOGIN\_REDIRECT\_URL)
form = authentication\_form()
current\_site = Site.objects.get\_current()
if request.method == “POST”:
pDict =request.POST.copy()
form = authentication\_form(data=request.POST)
if form.is\_valid():
username = form.cleaned\_data[‘username’]
password = form.cleaned\_data[‘password’]
try:
user = User.objects.get(email=username)
username = user.username
except User.DoesNotExist:
username = username
user = authenticate(username=username, password=password)
# Log the user in.
login(request, user)
return HttpResponseRedirect(redirect\_to)
else:
form = authentication\_form()
request.session.set\_test\_cookie()
if Site.\_meta.installed:
current\_site = Site.objects.get\_current()
else:
current\_site = RequestSite(request)
return render\_to\_response(‘login.html’,locals(), context\_instance=RequestContext(request))

---

#### 85. How Django processes a request?
**Ans:** When a user requests a page from your Django-powered site, this is the algorithm the system follows to determine which Python code to execute:
Django determines the root URLconf module to use. Ordinarily, this is the value of the ROOT\_URLCONF setting, but if the incoming HttpRequest object has an attribute called urlconf (set by middleware request processing), its value will be used in place of the ROOT\_URLCONF setting.
Django loads that Python module and looks for the variable urlpatterns. This should be a Python list, in the format returned by the function django.conf.urls.patterns()
Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL.

Once one of the regexes matches, Django imports and calls the given view, which is a simple Python function (or a class based view). The view gets passed an HttpRequest as its first argument and any values captured in the regex as remaining arguments.

If no regex matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view.

---

#### 86. How to filter latest record by date in Django?
**Ans: Messages(models.Model):**
    message\_from = models.ForeignKey(User,related\_name=”%(class)s\_from”)
message\_to = models.ForeignKey(User,related\_name=”%(class)s\_to”)
message=models.CharField(max\_length=140,help\_text=”Your message”)
created\_on = models.DateTimeField(auto\_now\_add=True)
class Meta:
db\_table = ‘messages’

**Query**:messages = Messages.objects.filter(message\_to = user).order\_by(‘-created\_on’)[0]

**Output:**

message\_from | message\_to  | message                 | created\_on

——————|—————–|——————–|——————–

Stephen        | Anto              | Hi, How are you? | 2012-10-09 14:27:48

---

#### 87.How to filter data from Django models using python datetime?
**Ans:** Assume Bellow model for storing messages with timelines
class Message(models.Model):
from = models.ForeignKey(User,related\_name = “%(class)s\_from”)
to = models.ForeignKey(User, related\_name = “%(class)s\_to”)
msg = models.CharField(max\_length=255)
rating = models.IntegerField(blank=’True’,default=0)
created\_on = models.DateTimeField(auto\_now\_add=True)
updated\_on = models.DateTimeField(auto\_now=True)
Filter messages with specified Date and Time
today = date.today().strftime(‘%Y-%m-%d’)

yesterday = date.today() – timedelta(days=1)
yesterday = yesterday.strftime(‘%Y-%m-%d’)

this\_month = date.today().strftime(‘%m’)
last\_month = date.today() – timedelta(days=32)
last\_month = last\_month.strftime(‘%m’)
this\_year = date.today().strftime(‘%Y’)

last\_year = date.today() – timedelta(days=367)
last\_year = last\_year.strftime(‘%Y’)

today\_msgs = Message.objects.filter(created\_on\_\_gte=today).count()
yesterday\_msgs = Message.objects.filter(created\_on\_\_gte=yesterday).count()
this\_month\_msgs = Message.objects.filter(created\_on\_\_month=this\_month,created\_on\_\_year=this\_year).count()
last\_month\_msgs = Message.objects.filter(created\_on\_\_month=last\_month,created\_on\_\_year=this\_year).count()
this\_year\_msgs = Message.objects.filter(created\_on\_\_year=this\_year).count()
last\_year\_msgs = Message.objects.filter(created\_on\_\_year=last\_year).count()

---

#### 88. What does Django mean?
**Ans:** Django is named after Django Reinhardt, a gypsy jazz guitarist from the 1930s to early 1950s who is known as one of the best guitarists of all time.

---

#### 89. Which architectural pattern does Django Follow?
**Ans:** Django follows Model-View Controller (MVC) architectural pattern.

---

#### 90. Is Django a high level web framework or low level framework?
**Ans:** Django is a high level Python’s web framework which was designed for rapid development and clean realistic design.

---

#### 91. How would you pronounce Django?
**Ans:** Django is pronounced JANG-oh. Here D is silent.

---

#### 92. How does Django work?
**Ans:** Django can be broken into many components:

**Models.py file:** This file defines your data model by extending your single line of code into full database tables and add a pre-built administration section to manage content.

**Urls.py file:** It uses regular expression to capture URL patterns for processing.

**Views.py file:** It is the main part of Django. The actual processing happens in view.
When a visitor lands on Django page, first Django checks the URLs pattern you have created and uses information to retrieve the view. After that view processes the request, querying your database if necessary, and passes the requested information to template.
After that the template renders the data in a layout you have created and displays the page.

---

#### 93. Which foundation manages Django web framework?
**Ans:** Django web framework is managed and maintained by an independent and non-profit organization named Django Software Foundation (DSF).

---

#### 94. Is Django stable?
**Ans:** Yes, Django is quite stable. Many companies like Disqus, Instagram, Pinterest, and Mozilla have been using Django for many years.

---

#### 95. What are the features available in Django web framework?
**Ans:** Features available in [Django](https://www.kausalvikash.in/python-training-in-pune/)web framework are:

- Admin Interface (CRUD)
- Templating
- Form handling
- Internationalization
- Session, user management, role-based permissions
- Object-relational mapping (ORM)
- Testing Framework
- Fantastic Documentation

---

#### 96. What are the advantages of using Django for web development?
**Ans:**

- It facilitates you to divide code modules into logical groups to make it flexible to change.
- It provides auto-generated web admin to make website administration easy.
- It provides pre-packaged API for common user tasks.
- It provides template system to define HTML template for your web page to avoid code duplication.
- It enables you to define what URL is for a given function.
- It enables you to separate business logic from the HTML.

---

#### 97. How to create a project in Django?
**Ans:** To start a project in Django, use the command **$django-admin.py** and then use the following command:
**Project**
**\_init\_.py**
**manage.py**
**settings.py**
**urls.py**

---

#### 98. What are the inheritance styles in Django?
**Ans: There are three possible inheritance styles in Django:**

**1) Abstract base classes:** This style is used when you only want parent’s class to hold information that you don’t want to type out for each child model.

**2) Multi-table Inheritance:** This style is used if you are sub-classing an existing model and need each model to have its own database table.

**3) Proxy models:** This style is used, if you only want to modify the Python level behavior of the model, without changing the model’s fields.

---

#### **99. How can you set up the database in Djanago**?

**Ans: A:** To set up a database in Django, you can use the command edit mysite/setting.py , it is a normal python module with module level representing Django settings.
By default, Django uses SQLite database. It is easy for Django users because it doesn’t require any other type of installation. In the case of other database you have to the following keys in the DATABASE ‘default’ item to match your database connection settings.

**Engines:** you can change database by using ‘django.db.backends.sqlite3’ , ‘django.db.backeneds.mysql’, ‘django.db.backends.postgresql\_psycopg2’, ‘django.db.backends.oracle’ and so on

**Name:** The name of your database. In the case if you are using SQLite as your database, in that case database will be a file on your computer, Name should be a full absolute path, including file name of that file.
**Note:** You have to add setting likes setting like Password, Host, User, etc. in your database, if you are not choosing SQLite as your database.

---

#### 100. What does the Django templates contain?
**Ans:** A template is a simple text file. It can create any text-based format like XML, CSV, HTML, etc. A template contains variables that get replaced with values when the template is evaluated and tags (%tag%) that controls the logic of the template.

---

#### 101. Is Django a content management system (CMS)?
**Ans:** No, Django is not a CMS. Instead, it is a Web framework and a programming tool that makes you able to build websites.

---

#### 102.What is the use of session framework in Django?
**Ans**: The session framework facilitates you to store and retrieve arbitrary data on a per-site visitor basis. It stores data on the server side and abstracts the receiving and sending of cookies. Session can be implemented through a piece of middleware.

---
