---
title: "HTML Frames"
description: "HTML Frames are used to divide the web browser window into multiple sections where each section can be loaded separately. A <frameset tag is the…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-08T11:23:30
legacy: true
wpId: 2561
draft: true
---

HTML Frames are used to divide the web browser window into multiple sections where each section can be loaded separately. A &lt;frameset> tag is the collection of frames in the browser window.

## Syntax of HTML frame Tag:

```
< frame src = "URL" >
```

## HTML Vertical Frame Example:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vertical Frame Tag</title>
</head>
<frameset cols="25%,50%,25%">
    <frame src="frame1.html">
        <frame src="frame2.html">
            <frame src="frame3.html">
</frameset>

<body>

</body>

</html>
```

## Frame1:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            background-color: #d07fff;
            height: 500px;
        }
    </style>
</head>

<body>
    <div>
        <h2>Frame No.1</h2>
    </div>
</body>

</html>
```

## Frame2:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            background-color: #4f4f2f;
            height: 500px;

        }
    </style>
</head>

<body>
    <div>
        <h2>Frame No.2</h2>
    </div>
</body>

</html>
```

## Frame3:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            background-color: #0fdd0f;
            height: 500px;
        }
    </style>
</head>

<body>
    <div>
        <h2>Frame No. 3</h2>
    </div>
</body>

</html>
```

## Output:

## HTML Horizontal Frame example:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTMK Horizontal tag</title>
    <frameset rows="25%, 50%, 25%">
        <frame name="top" src="frame1.html" >
        <frame name="main" src="frame2.html">
        <frame name="bottom" src="frame3.html">
      </frameset>
</head>
<body>

</body>
</html>
```

## Output:
