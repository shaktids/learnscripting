---
title: "HTML Images"
description: "In HTML, you can add images in a webpage using the <img tag. The <img is an empty tag which means it does not have a closing tag. This tag requires some…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-04T19:23:15
legacy: true
wpId: 2487
draft: true
---

In HTML, you can add images in a webpage using the &lt;img> tag. The &lt;img> is an empty tag which means it does not have a closing tag. This tag requires some set of attributes to specify the size, alignment, and other properties of an image.

## Attributes of HTML image tag are:

1.src :

This is an important attribute which describes the path of the image.

2. alt :

This optional attribute is used to specify alternate text in case the image does not appear.

3.width :

This is an attribute which specifies the width of the image.

4.height :

This is an attribute which  specifies the height of the image.

5.align :

This attribute specifies the alignment of the image. Possible values could be *left*, *right*, *center* etc. By default, it is set as *left.*

## HTML image Example from another website:

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML image</title>
</head>
<body>
<h2>HTML image example</h2>
<img src="https://images.pexels.com/photos/3876407/pexels-photo-3876407.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" height="180" width="300" alt="nature image">
</body>
</html>
```

## Output:

## HTML image Example from another directory/folder:

In HTML, if we want to show a image in the web page, we must put the image and html file in the same folder. If we

Forget to put it in same folder then we have to put the file path in the src location.

```
<img src="E:/images/download.jpg" height="180" width="300" alt="nature image">
```

## Example of image tag where we put the HTML file and image in same folder:
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HTML image</title>
</head>
<body>
<h2>HTML image example</h2>
<img src="download.jpg" height="180" width="300">
</body>
</html>
```

## Output:
