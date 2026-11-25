---
title: "CSS Rounded Border"
description: "The border radius property is used to add rounded borders to an element: 1.Normal border 2. Round border 3. Rounder border 4.Roundest border Example…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T08:31:00Z
legacy: true
wpId: 2733
---

The `border-radius` property is used to add rounded borders to an element:

1.Normal border

2. Round border

3. Rounder border

4.Roundest border

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
            border: 2px solid red;
            border-radius: 5px;
        }

        p.two {
            border: 2px solid rgb(76, 0, 255);
            border-radius: 8px;
        }

        p.three {
            border: 2px solid rgb(0, 255, 34);
            border-radius: 12px;
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
