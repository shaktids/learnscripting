---
title: "HTML Head and HTML meta"
description: "The head of an HTML document is the part that is not displayed in the web browser when the page is loaded. It contains information such as the page <title…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-09T20:55:12
legacy: true
wpId: 2593
draft: true
---

The head of an HTML document is the part that is not displayed in the web browser when the page is loaded. It contains information such as the page &lt;title>, links to CSS(if we choose to style our HTML content with CSS), links to custom favicons, and other metadata (data about the HTML, such as the author, and important keywords that describe the document.)

Following is a list of tags used in metadata:

- &lt;title>
- &lt;style>
- &lt;meta>
- &lt;link>
- &lt;script>
- &lt;base>

## HTML &lt;title> Element:

The &lt;title> HTML element defines the document's title that is shown in a browser's title bar or a page's tab. It only contains text; tags within the element are ignored.

## Syntax:

```
<title>Document</title>
```

## HTML &lt;style> Element:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            background-color: powderblue;
        }

        h1 {
            color: green;
        }

        p {
            color: yellow;
        }
    </style>
</head>

<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>

</body>

</html>
```

## Output:

## HTML &lt;link>Element:

The &lt;link> element defines the relationship between the current document and an external resource.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>

</body>

</html>
```

## HTML &lt;meta> Element:

**Define the character set used:**

```
 <meta charset="UTF-8">
```

**Define keywords for search engines:**

```
<meta name="keywords" content="HTML, CSS, JavaScript">
```

**Define the author of a page:**

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

**Refresh document every 30 seconds:**

```
<meta http-equiv="refresh" content="30">
```

**Setting the viewport to make your website look good on all devices:**

```
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Example of &lt;meta> Element:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h3>This is a meta tag</h3>
</body>

</html>
```

## Output:

## Setting The Viewport:

The viewport is the user's visible area of a web page. It varies with the device - it will be smaller on a mobile phone than on a computer screen.

We should include the following&lt;meta> element in all your web pages:

```
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Example of with and without viewport:
