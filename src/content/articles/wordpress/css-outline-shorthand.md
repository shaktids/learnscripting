---
title: "CSS Outline Shorthand"
description: "CSS Outline Shorthand property The outline property is a shorthand property for setting the following individual outline properties: outline width outline…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T10:27:16Z
legacy: true
wpId: 2742
---

## CSS Outline - Shorthand property

The `outline` property is a shorthand property for setting the following individual outline properties:

- `outline-width`
- `outline-style` (required)
- `outline-color`

The `outline` property is specified as one, two, or three values from the list above. The order of the values does not matter.

## Example

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Outline Shorthand</title>
    <style>
        p.one {
            outline: dashed;
        }

        p.two {
            outline: dotted rgb(195, 0, 255);
        }

        p.three {
            outline: 5px solid green;
        }

        p.four {
            outline: thick ridge pink;
        }
    </style>
</head>

<body>
    <p class=one>www.learscripting.org</p>
    <p class=two>www.learscripting.org</p>
    <p class=three>www.learscripting.org</p>
    <p class=four>www.learscripting.org</p>
</body>

</html>
```
