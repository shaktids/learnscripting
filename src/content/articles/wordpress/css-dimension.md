---
title: "CSS Dimension"
description: "All HTML elements in a box model are represented as rectangular boxes. The dimensions of the box model are calculated by using the height and width of the…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T17:25:03Z
legacy: true
wpId: 2755
---

All HTML elements in a [box model](https://codescracker.com/css/css-box-model.htm) are represented as rectangular boxes. The dimensions of the box model are calculated by using the height and width of the content area that gets applied to the element.

Each box is associated with a content area and many optional areas, such as [padding](https://codescracker.com/css/css-padding.htm), [border](https://codescracker.com/css/css-border.htm), and [margin](https://codescracker.com/css/css-margin.htm).

We have the following properties that allow you to control the dimensions of a box.

- The **height** property is used to set the height of a box.
- The **width** property is used to set the width of a box.
- The **line-height** property is used to set the height of a line of text.
- The **max-height** property is used to set a maximum height that a box can be.
- The **min-height** property is used to set the minimum height that a box can be.
- The **max-width** property is used to set the maximum width that a box can be.
- The **min-width** property is used to set the minimum width that a box can be.

## Example of CSS Height and Width:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Dimension</title>
    <style>
        div {
            height: 200px;
            width: 50%;
            background-color: powderblue;
        }
    </style>
</head>

<body>
    <h2>Set the height and width of an element</h2>

    <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque, animi.</div>
</body>

</html>
```

## Output:

## Example of CSS Max-Width:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Dimension</title>
    <style>
        div {
            height: 200px;
            width: 500px;
            background-color: powderblue;
        }
    </style>
</head>

<body>
    <h2>Set the max width of an element</h2>

    <div>Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloremque, animi.</div>
</body>

</html>
```

## Output:
