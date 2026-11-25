---
title: "HTML fonts"
description: "Fonts play a very important role in making a website more user friendly and increasing content readability. The HTML <font tag defines the font size…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-04T07:35:22
legacy: true
wpId: 2472
draft: true
---

Fonts play a very important role in making a website more user friendly and increasing content readability. The HTML &lt;font> tag defines the font size, color and face of text in the HTML document.

## **Syntax**:

In HTML, the syntax for the **&lt;font> tag** is:

```
<body>
<p><font color="red" face=”cursive” size="+1">Your formatted text goes here</font></p>
</body>
```

## **Attributes**:

T he following is a list of attributes that are specific to the &lt;font> tag:

|  |  |  |
| --- | --- | --- |
| color | Color of text in either hexadecimal (ie: #RRGGBB format) or named color (ie: black, red, white) | HTML 4.01 |
| face | Font to use for text. Listed as one or more font names (comma separated) | HTML 4.01 |
| size | Font size expressed as either a numeric or relative value.  Numeric values range from 1 to 7 (1 is the smallest, 7 is the largest, 3 is the default). Relative values can be values such as +1 or -2, increasing by one font size or decreasing by 2 font sizes, respectively. | HTML 4.01 |

Example of font tag:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font tag</title>
</head>
<body>
    <h2>Example of font tag</h2>
    <p>This is normal text </p>
     <p>
       <font color="red">This is a font tag</font>
     </p>
     <p>
       <font size="6" color="green">This is another font tag</font>
     </p>
     <p>
       <font color="blue" face="cursive">This is a paragraph</font>
     </p>
</body>
</html>
```

## Output:
