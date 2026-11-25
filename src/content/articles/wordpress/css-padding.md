---
title: "CSS Padding"
description: "Padding is used to create space around an element's content, inside of any defined borders. CSS has properties for specifying the padding for each side of…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T10:53:50Z
legacy: true
wpId: 2751
---

Padding is used to create space around an element's content, inside of any defined borders.

CSS has properties for specifying the padding for each side of an element:

- `padding-top`
- `padding-right`
- `padding-bottom`
- `padding-left`

All the padding properties can have the following values:

- *length* - specifies a padding in px, pt, cm, etc.
- *%* - specifies a padding in % of the width of the containing element
- inherit - specifies that the padding should be inherited from the parent element

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Padding</title>
    <style>
        p {
            background-color: rgb(153, 206, 28);
        }

        p.padding {
            padding-top: 50px;
            padding-right: 100px;
            padding-bottom: 150px;
            padding-left: 200px;
        }
    </style>
</head>

<body>
    <p>This is a paragraph with no specified padding.</p>
    <p class="padding">Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam, accusamus?</p>
</body>

</html>
```

## Output:
