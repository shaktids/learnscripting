---
title: "The HTML DOCTYPE"
description: "The DOCTYPE in HTML is an instruction that tells the web browser which version of HTML the document is written in. It is the first line of an HTML…"
lang: other
categories: ["HTML"]
author: "LearnScripting"
pubDate: 2022-12-27T12:39:37Z
updatedDate: 2022-12-28T15:01:27Z
legacy: true
wpId: 2945
---

The `DOCTYPE` in HTML is an instruction that tells the web browser which version of HTML the document is written in. It is the first line of an HTML document, and is usually placed at the very top of the file, before the `<html>` element.

The `DOCTYPE` is not an HTML element, and does not have a closing tag. It is used to tell the web browser which version of HTML to use when rendering the document.

There are several different versions of HTML, each with its own `DOCTYPE` declaration. The most common `DOCTYPE` declarations are:

- `<!DOCTYPE html>`: This `DOCTYPE` is used for HTML5 documents.
- `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">`: This `DOCTYPE` is used for HTML 4.01 Strict documents.
- `<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">`: This `DOCTYPE` is used for HTML 4.01 Transitional documents.

Here is an example of an HTML document with a `DOCTYPE` declaration:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Welcome to My Page</h1>
    <p>Here is some information about me:</p>
    <ul>
      <li>Name: John</li>
      <li>Age: 30</li>
      <li>Location: New York</li>
    </ul>
  </body>
</html>
```

In this example, the `DOCTYPE` declaration is `<!DOCTYPE html>`, which tells the web browser that the document is written in HTML5.

It's important to include a `DOCTYPE` declaration in your HTML documents, as this will help the web browser correctly interpret and render the document.

That's it! You now know what the HTML `DOCTYPE` is and how to use it in your HTML documents.
