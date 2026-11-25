---
title: "CSS Border width"
description: "The border width property sets the width of an element's four borders. This property can have from one to four values. Examples border width: thin medium…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-13T07:59:25Z
legacy: true
wpId: 2721
draft: true
---

The `border-width` property sets the width of an element's four borders. This property can have from one to four values.

Examples

- **border-width: thin medium thick 10px;**
  - top border is thin
  - right border is medium
  - bottom border is thick
  - left border is 10px
- **border-width: thin medium thick;**
  - top border is thin
  - right and left borders are medium
  - bottom border is thick
- **border-width: thin medium;**
  - top and bottom borders are thin
  - right and left borders are medium
- **border-width: thin;**
  - all four borders are thin

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
            border-style: solid;
            border-width: 5px;
        }

        p.two {
            border-style: solid;
            border-width: medium;
        }

        p.three {
            border-style: solid;
            border-width: 1px;
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
