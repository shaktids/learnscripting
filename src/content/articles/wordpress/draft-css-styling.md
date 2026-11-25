---
title: "CSS Styling"
description: "Cascading Style Sheet(CSS) is used to set the style in web pages that contain HTML elements. It sets the background color, font size, font family, color…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-11T18:17:38Z
legacy: true
wpId: 2673
draft: true
---

Cascading Style Sheet(CSS) is used to set the style in web pages that contain HTML elements. It sets the background color, font-size, font-family, color, … etc property of elements on a web page.
There are three types of CSS which are given below:

- Inline CSS
- Internal or Embedded CSS
- External CSS

**Inline** styles are placed right where you need them, next to the text or graphic you wish to decorate. You can insert inline styles anywhere in the middle of your HTML code, giving you real freedom to specify each web page element. On the other hand, this can make maintaining web pages a real chore!

**Internal** styles are placed at the top of each web page document, before any of the content is listed. This is the next best thing to external, because they're easy to find, yet allow you to 'override' an external style sheet -- for that special page that wants to be a nonconformist!

**External** style sheets are separate files full of CSS instructions (with the file extension .css). When any web page includes an external stylesheet, its look and feel will be controlled by this CSS file (unless you decide to override a style using one of these next two types). This is how you change a whole website at once. And that's perfect if you want to keep up with the latest fashion in web pages without rewriting every page!

## Example of Inline CSS:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

    <body style="background-color:white;">
        <h1 style="color:rgb(0, 255, 21);padding:20px;">www.learnscripting.com</h1>
        <p style="color:rgb(255, 145, 0);">This is a good website</p>
    </body>

</html>
```

## Output:

## Example of Internal CSS:

```css
<!DOCTYPE html>
<html>

<head>
    <style>
        body {
            background-color: rgb(43, 7, 126);
        }

        h1 {
            color: red;
            padding: 50px;
        }
    </style>
</head>

<body>
    <h1>www.learnscripting.com</h1>
    <p>This is a good website</p>
</body>

</html>
```

## Output:

Example of External CSS:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Css Stylesheet</title>
    <link rel="stylesheet" href="mystyle.css">
</head>
</head>

<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
</body>

</html>
```

## mystyle.css

```css
body {
    background-color: lightblue;
  }

  h1 {
    color: navy;
    margin-left: 20px;
  }
```

## Output:
