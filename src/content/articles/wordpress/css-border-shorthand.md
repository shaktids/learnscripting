---
title: "CSS Border Shorthand"
description: "To shorten the code, it is also possible to specify all the individual border properties in one property. The border property is a shorthand property for…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T08:20:50Z
legacy: true
wpId: 2730
---

To shorten the code, it is also possible to specify all the individual border properties in one property.

The `border` property is a shorthand property for the following individual border properties:

- `border-width`
- `border-style` (required)
- `border-color`

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Border Width</title>
    <style>
        p.one {
            border: dotted red;
        }

        p.two {
            border: 15px solid green;
        }

        p.three {
            border: dashed blue;
        }
    </style>
</head>

<body>
    <p class="one">www.learnscripting.org</p>
    <p class="two">www.learnscripting.org</p>
    <p class="three">www.learnscripting.org</p>
</body>

</html>
```

## Output:
