---
title: "CSS Positioning"
description: "The CSS position property defines the position of an element where generally the top, right, bottom, and left properties will determine the position of…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T18:03:14Z
legacy: true
wpId: 2764
---

The CSS position property defines the position of an element where generally the top, right, bottom, and left properties will determine the position of the element.

## Syntax:

```css
position: value;
```

## Property of CSS Positioning:

| Value | Description |
| --- | --- |
| static | Normal position for the element (where top, right, bottom, and left have no effect) div { position: static; } |
| relative | Position the element relative to where its normal position would have been div { position: relative; top: 10px; left: 15px; } |
| absolute | Position the element absolutely relative to its container div { position: absolute; top: 10px; left: 15px; } |
| fixed | Position the element relative to the screen's viewport and stay fixed on screen when scrolling div { position: fixed; top: 10px; left: 15px; } |
| inherit | Indicates that the element will inherit the position from its parent element div { position: inherit; } |

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Poisitioning</title>
    <style>
        h2 {
            position: absolute;
            left: 100px;
            top: 150px;
        }
    </style>

</head>

<body>
    <h1>The position Property</h1>

    <h2>This is a heading with an absolute position</h2>

    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Optio, libero?</p>
</body>

</html>
```

## Output:
