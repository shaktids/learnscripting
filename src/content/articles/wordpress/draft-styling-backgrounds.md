---
title: "Styling Backgrounds"
description: "Background plays an important role in the visual presentation of a web page. CSS provide several properties for styling the background of an element…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-11T21:02:28Z
legacy: true
wpId: 2677
draft: true
---

Background plays an important role in the visual presentation of a web page.

CSS provide several properties for styling the background of an element, including coloring the background, placing images in the background and managing their positioning, etc.

The background properties are `background-color, background-image, background-repeat, background-attachment and background-position`.

## Example of Background-color:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Background-color</title>
    <style>
        h2,
        p {
            background-color: #4391a7;
        }
    </style>
</head>

<body>
    <h2>www.learnscripting.org</h2>
    <p>Hello learnscripting</p>

</body>

</html>
```

## Output:

## Example of Background-image:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Backgroung-image</title>
    <style>
        body {
            background-image: url("bg2.jpg");
            margin-left: 100px;
        }
    </style>
</head>

<body>
    <h1>Python...............</h1>
</body>

</html>
```

## Output:

## Example of Background-repeat:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Backgroung-image</title>
    <style>
        body {
            background-image: url("bg2.jpg");
            background-repeat: repeat-x;
        }
    </style>
</head>

<body>
    <h1>Python...............</h1>
</body>

</html>
```

## Output:

## Example of Background-attachment:

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body  {
    background: white url('bg2.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    margin-left:200px;
    }
    </style>
<body>

<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
</body>
</html>
```

## Output:

## Background-position:

In CSS background-position property is mainly used to set an image at a certain position.

## Syntax:

```css
background-position: value;
```

**Property values:**
There are a few important property values which can be used to set the image at a certain position.

- initial
- inherit
- left top
- left center
- left bottom
- center top
- center center
- center bottom
- right top
- right center
- right bottom

## Example:

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body  {
    background: white url('bg2.jpg');
    background-repeat: no-repeat;
    background-attachment: fixed;
    margin-left:200px;
    }
    </style>
<body>

<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
<p>This is a fixed background-image. Scroll down the page.</p>
</body>
</html>
```

## Output:
