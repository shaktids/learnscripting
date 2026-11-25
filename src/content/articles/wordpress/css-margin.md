---
title: "CSS Margin"
description: "The margin property defines the space around an HTML element. It is possible to use negative values to overlap content. The values of the margin property…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T10:46:06Z
legacy: true
wpId: 2748
---

The *margin* property defines the space around an HTML element. It is possible to use negative values to overlap content.

The values of the margin property are not inherited by the child elements. Remember that the adjacent vertical margins (top and bottom margins) will collapse into each other so that the distance between the blocks is not the sum of the margins, but only the greater of the two margins or the same size as one margin if both are equal.

We have the following properties to set an element margin.

- The **margin** specifies a shorthand property for setting the margin properties in one declaration.
- The **margin-bottom** specifies the bottom margin of an element.
- The **margin-top** specifies the top margin of an element.
- The **margin-left** specifies the left margin of an element.
- The **margin-right** specifies the right margin of an element.

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Margin</title>
    <style>
        div {
            border: 2px solid black;
            margin-top: 100px;
            margin-bottom: 100px;
            margin-right: 150px;
            margin-left: 80px;
            background-color: lightblue;
        }
    </style>
</head>
</style>
</head>

<body>
    <h2>CSS Margin </h2>
    <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure blanditiis earum sapiente non dicta consequatur
        nostrum hic maiores alias. Asperiores sunt perferendis illo? Quia ab temporibus quas tempore accusantium vel
        autem nostrum repellat eum adipisci, ullam minima asperiores voluptas corrupti, doloremque laboriosam, aperiam
        eos vero sunt perferendis sint. Vitae, quos!</div>
</body>

</html>
```

## Output:
