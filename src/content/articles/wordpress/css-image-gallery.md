---
title: "CSS Image Gallery"
description: "Image Gallery is used to store and display collection of pictures. This example create a responsive Image Gallery using HTML and CSS. Example: Output:"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-15T07:58:29Z
legacy: true
wpId: 2781
---

Image Gallery is used to store and display collection of pictures. This example create a responsive Image Gallery using HTML and CSS.

## Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>
        div.gallery {
            margin: 5px;
            border: 2px solid #ccc;
            float: left;
            width: 180px;
        }

        div.gallery:hover {
            border: 1px solid #777;
        }

        div.gallery img {
            width: 100%;
            height: auto;
        }

        div.desc {
            padding: 15px;
            text-align: center;
        }
    </style>
</head>
</head>

<body>
    <div class="gallery">
        <a target="_blank" href="sky.jpeg">
            <img src="sky.jpeg" alt="sky" width="600" height="400">
        </a>
        <div class="desc">This is a image of sky</div>
    </div>

    <div class="gallery">
        <a target="_blank" href="mountain.jpg">
            <img src="mountain.jpg" alt="mountain" width="600" height="400">
        </a>
        <div class="desc">This is a image of Mountain</div>
    </div>

    <div class="gallery">
        <a target="_blank" href="river.jpg">
            <img src="river.jpg" alt="river" width="600" height="400">
        </a>
        <div class="desc">This is a image of river</div>
    </div>

    <div class="gallery">
        <a target="_blank" href="forest.jpeg">
            <img src="forest.jpeg" alt="forest" width="600" height="400">
        </a>
        <div class="desc">This is image of forest</div>
    </div>

</body>

</html>
```

## Output:
