---
title: "CSS floating"
description: "The float property places an element on the left or right side of its container, allowing text and inline elements to wrap around it. The element is…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T18:13:11Z
legacy: true
wpId: 2767
---

The float property places an element on the left or right side of its container, allowing text and inline elements to wrap around it. The element is removed from the normal flow of the page, though still remaining a part of the flow (in contrast to [absolute position](https://developer.mozilla.org/en-US/docs/Web/CSS/position#absolute_positioning)ing).

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS floating</title>
    <style>
        img {
            float: right;
        }
    </style>
</head>

<body>

    <body>
        <h1>The float Property</h1>

        <p>In this example, the image will float to the right in the text, and the text in the paragraph will wrap
            around the image.</p>

        <p><img src="download.jpg" alt="download" style="width:170px;height:170px;margin-left:15px;">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi
            lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue
            eget, auctor vitae massa. Fusce luctus vestibulum augue ut aliquet. Mauris ante ligula, facilisis sed ornare
            eu, lobortis in odio. Praesent convallis urna a lacus interdum ut hendrerit risus congue. Nunc sagittis
            dictum nisi, sed ullamcorper ipsum dignissim ac. In at libero sed nunc venenatis imperdiet sed ornare
            turpis. Donec vitae dui eget tellus gravida venenatis. Integer fringilla congue eros non fermentum. Sed
            dapibus pulvinar nibh tempor porta. Cras ac leo purus. Mauris quis diam velit.</p>
    </body>

</html>
```

## Output:
