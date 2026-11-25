---
title: "Django Architecture"
description: "There are 3 main elements or code compartments for most websites on the internet Input Logic , Business Logic , and UI Logic . These partitions of code…"
lang: python
categories: ["Django"]
author: "LearnScripting"
pubDate: 2022-02-08T18:44:39Z
updatedDate: 2022-03-31T15:49:06Z
legacy: true
wpId: 2899
---

There are 3 main elements or code compartments for most websites on the internet **Input Logic**, **Business Logic**, **and UI Logic**.

These partitions of code have specific tasks to achieve, the input logic is the dataset and how the data gets organized in the database. It just takes that input and sends it to the database in the desired format. The Business logic is the main controller which handles the output from the server in the HTML or desired format. The UI Logic as the name suggests is the HTML, CSS, and JavaScript pages.

When the traditional approach was used for programming all this code was written in a single file, i.e., every piece of code increases the webpage size, which is downloaded and rendered by the browser. This was not a big problem back in the time, the webpages were largely static, and websites didn’t contain much multimedia and large coding. Also, this architecture poses difficulty for developers while testing and maintaining the project as everything is inside one file.

Now, time is changing and the websites are getting bigger and bigger while providing applications and online artificial intelligence training, online development environments, and whatnot, these projects are all implemented using MVC architecture.

## MVC Architecture:

MVC is abbreviated as Model View Controller is a design pattern created for developing applications specifically web applications. As the name suggests, it has three major parts. The traditional software design pattern works in an "Input - Process - Output" pattern whereas MVC works as a "Controller -Model - View" approach.

1. **Model**: The Model encloses the clean application-related data. But the model does not deal with any logic about how to present the data.
2. View: The View element is used for presenting the data of the model to the user. This element deals with how to link up with the model's data but doesn't provide any logic regarding what this data is all about or how users can use these data.
3. Controller: The Controller is in between the model and the view element. It listens to all the incidents and actions triggered in the view and performs an appropriate response back to the events.

## MVT Architecture:

- **Model:** This is an abstraction layer for structuring and manipulating the data of the Web Application. It acts as an interface for maintaining data. This is a logical data structure behind the entire application and helps to handle the database.
- **View:**This layer encapsulates the logic responsible for processing a user’s request and returns a response. It is a user interface to execute the logic and interact with the models. It is responsible for displaying all or a portion of data to the user.
- **Template:** The template layer provides a designer-friendly syntax for rendering the information to be presented to the user. It contains the static parts of the desired HTML output along with some special syntax, also known as Django Template Language (DTL), describing how dynamic content will be inserted.

Here, a user requests a resource to the Django, Django works as a controller and checks the available resource in the URL.

If URL maps, a view is called that interacts with the model and template, it renders a template.

Django responds back to the user and sends a template as a response.
