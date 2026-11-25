---
title: "CSS Outline Offset"
description: "The CSS outline offset Property sets the amount of space between an outline and the edge or border of an element. An outline is a line drawn around…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T10:34:25Z
legacy: true
wpId: 2745
---

The CSS outline-offset Property sets the amount of space between an outline and the edge or border of an element.

An outline is a line drawn around elements outside the border edge. The space between the element and its outline is transparent. Also, the outline may be non-rectangular. The default value is 0.Example:

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Outline</title>
    <style>
        p.one {
            border: 1px solid black;
            outline-style: solid;
            outline-color: red;
            outline-width: thin;
        }

        p {
            border: 1px solid black;
            outline-style: solid;
            outline-color: red;
            outline-offset: 15px;
        }
    </style>
</head>
</head>

<body>
    <p>www.learnscripting.org</p>

</body>

</html>
```

## Output:
