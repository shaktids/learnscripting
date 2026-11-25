---
title: "HTML Scripts"
description: "The HTML < script tag is used to define a client side script (JavaScript). The < script element either contains script statements, or it points to an…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-09T22:46:25
legacy: true
wpId: 2602
draft: true
---

The **HTML** &lt;**script**> tag is used to define a client-side **script** (JavaScript). The &lt;**script**> element either contains **script** statements, or it points to an external **script** file through the src attribute. Common uses for JavaScript are image manipulation, form validation, and dynamic changes of content.

## Syntax of HTML &lt;script> Tag:

```
<script>
document.getElementById("demo").innerHTML = "Hello JavaScript";
</script>
```

## Example of HTML Script:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript</title>
</head>

<body>
    <h1>My First JavaScript</h1>

    <p id="demo">JavaScript is the Programming Language for the Web. JavaScript can update and change both HTML and CSS.
    </p>

    <script>
        function myFunction() {
            document.getElementById("demo").style.fontSize = "55px";
            document.getElementById("demo").style.color = "blue";
            document.getElementById("demo").style.backgroundColor = "yellow";
        }
    </script>

    <button type="button" onclick="myFunction()">try it</button>

</body>

</html>
```

Output:
