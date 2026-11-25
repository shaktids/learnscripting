---
title: "Python Flask Interview Questions"
description: "Q1. What is Flask WTF? Flask WTF is an inbuilt module of flask framework that provides an extensive way of designing HTML forms in flask web applications…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-01-19T09:55:41
legacy: true
wpId: 2182
draft: true
---

**Q1. What is Flask-WTF?**

Flask-WTF is an inbuilt module of flask framework that provides an extensive way of designing HTML forms in flask web applications.

**Q2. For what python flask is used?**

Python flask is a web development framework. It can be used for

1) Creating web services.
2) Creating websites
3) Building complex web applications
4) Creating CRM or shopping websites.
5) Creating Twitter/Facebook bot

**Q3. How to install python flask on linux?**

pip install flask

**Q4. How to deploy python flask app on Heroku?**

**Q5. How to structure python flask project?**

**Q6. How to check request is json type in flask?**

**request.content\_type** is used to check the request type in Flask. To check request is of json type use if request.content\_type == 'application/json':

**Q7. What is Jsonify in flask?**

**jsonify()** function is used to return flask.Response() object with content-type header 'application/json'.

**Q8. How to change Flask server host/port using config file?**

In the config file, you can set the **server host** and **port** values using the following line`app.run(host=’host_value’, port=’port_value’)`Here, you can set and change your host and port value of your server.

**Q9. How to log request body in python flask?**

You can take advantage of Flask.before\_request hook to log the request body in python flask. Here is an example:

```
@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())
```

**Q10. How to divide flask app into multiple py files?**

**Q11. Is python flask multithreaded?**

Yes, Flask is multithreaded.

**Q12. How to create an array with checkboxes in Flask?**

To create an array with checkboxes in Flask you have to create your checkbox input names with the same name.

Below is an example which demonstrates how to create an array with checkboxes in Flask

**In your view**

```
<input type="checkbox" value="X" class="danger" name='my_checkbox'>
<input type="checkbox" value="Y" class="danger" name='my_checkbox'>
<input type="checkbox" value="Z" class="danger" name='my_checkbox'>
```

**In Flask code you can get selected checkbox values as**

```
print(request.form.getlist('my_checkbox'))
```

Above code outputs value of all selected checkboxes

**Q13. How to get visitor ip address in Flask?**

**request.remote\_addr** is used to get visitor IP address in Flask. Here is an example:

```
from flask import request
from flask import jsonify

@app.route("/get_user_ip", methods=["GET"])
def get_user_ip():
    return jsonify({'ip': request.remote_addr}), 200
```

**Q14. What is g in python flask?**

Occasionally you might find a situation in which using a global variable is a perfectly reasonable solution to a problem. However, in a Flask app, your code is likely to end up running in an environment with multiple requests being handled at the same time. If you used a normal global variable, one request might modify the global variable and interfere with another request that happens to be executing simultaneously. To avoid that, Flask provides this g object to which you can attach such variables. Each request gets a different g object, so simultaneous requests can't interfere with each other, but you still have the same convenience as a global variable.

**Further Reading:** [Read More Flask g](https://www.reddit.com/r/learnpython/comments/45zaav/can_someone_explain_the_g_object_in_flask_ive/)

**Q15. What is Flask Sijax?**

**Flask Sijax** is Python/jQuery library to perform  Ajax function in Flask.

You can install Flask-Sijax by using below command

```
easy_install flask-sijax
```

```
pip install flask-sijax
```

**Q16. For what url\_for() function is used in Flask?**

**url\_for()** function in flask is used for generating dynamic URL for a specific function.url\_for() accept the name of a function as the first parameter and one or more arguments for the variable part of URL.

**Q17. What is WSGI?**

**WSGI** stands for **Web Server Gateway Interface**. It a convention or standard that describes how web servers communicate to web applications or Python frameworks.

**Q18. How to get http headers in flask?**

You can use **request.headers.get** method to get http headers in the flask. **request.headers** method in flask framework behaves like a dictionary so the value of headers are available in array format too something like `request.headers['your-header-name']`

**Example**

```
from flask import request
rrequest.headers.get('Authorization')
```

**Q19. How to serve static files in Flask?**

**Static files** should be added to the **flasks/static directory** and then the files are referenced in the HTML to serve the static files. Static files such as **CSS** and **JavaScript** acts as a template and adds more functions to your web application. All the static files are added to the flask/static directory and referenced by the following line to **serve it**.

```
//referencing static files in the flask
url_for(‘static’, filename=’static_file_name’)
```

**Q20. How to get a query string in Flask?**

**The query string** is a key/value pair that is sent by the client to the server in the web URL. These values are actually a part of the URL as a string of parameters and values. To get and work with the query string, we need to use the import request method from the flask.

```
//example of getting a query string in the Flask
from flask import request   //request method is used to work with the query string values
@app.route("/query")
def query():
args = request.args     //here, we get the query string object in a variable called ‘args’ using
print(args)
```

**Q21. How to import function into main file in flask?**

You can use the import statement to **import functions** from other files into the main file in the Flask. You can also use the **'from'** statement with the **'import**' statement to import a specific function from other files into your main flask file.

```
//example of importing functions
from otherFile import function  //importing function method from the file otherFile.py
@app.route("/")
@app.route("/index")
def index():
    baz = function()     //the function imported from your file otherFile.py
if __name__ == '__main__':
    app.run(debug=True)
```

**Q22. How to disable csrf for a view with flask-wft for a restapi?**

When you create the form, you can disable the **CSRF** for a view with **flask-wtf** for a **restapi** by using the following statement.

```
form = myForm(request.form, csrf_enabled=False)
```

**Q23. How to share the global app object in flask?**

You can create an overall package and add an **\_\_init\_\_.py file** under the package folder where you declare all the global variables that you need to share between the classes. Then, you should add the code **"app = Flask(\_\_name\_\_)"** in the \_\_init\_\_.py file. Now you can share and use the app variables anywhere if you just import the package name.

**Q24. What is the purpose of Flask's context stacks?**

Flask in Python language helps to handle multiple apps in the process. Contexts allow separating application environments from one another.

**Q25. How to get logged user id in flask?**

current\_user.get\_id() is used to get logged in user id in flask.

**Here is an example:**

```
from flask import g
if current_user.is_authenticated():
        g.user = current_user.get_id()
```
