---
title: "CSS Align"
description: "The CSS align content property sets the distribution of space between and around content items along a flexbox's cross axis or a grid's block axis…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-14T12:05:28Z
legacy: true
wpId: 2771
---

The **CSS align**-content property sets the distribution of space between and around content items along a flexbox's cross-axis or a grid's block axis.

## Syntax:

```css
align-content: stretch|center|flex-start|flex-end|space-between|space-around|initial|inherit;
```

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS align</title>
    <style>
        #main {
            width: 70px;
            height: 300px;
            border: 1px solid #cf9c9c;
            display: flex;
            flex-wrap: wrap;
            align-content: center;
        }

        #main div {
            width: 70px;
            height: 70px;
        }
    </style>
</head>
</head>

<body>
    <h1>The align-content Property</h1>

    <div id="main">
        <div style="background-color:rgb(156, 80, 255);"></div>
        <div style="background-color:rgb(208, 230, 173);"></div>
        <div style="background-color:rgb(241, 18, 55);"></div>
    </div>
</body>

</html>
```

## Output:
