---
title: "HTML5 Canvas"
description: "The <canvas element is a part of the HTML5 standard that provides a drawing surface for rendering 2D graphics, such as charts, diagrams, and games. It is…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2022-12-28T15:24:02Z
legacy: true
wpId: 2643
---

The `<canvas>` element is a part of the HTML5 standard that provides a drawing surface for rendering 2D graphics, such as charts, diagrams, and games. It is a lightweight and versatile alternative to using images or Flash for rendering graphics on the web.

To use the `<canvas>` element, you first need to create the element in your HTML file:

```html
<canvas id="myCanvas" width="400" height="400"></canvas>
```

This creates a canvas with an ID of "myCanvas" and a width and height of 400 pixels.

Next, you can use JavaScript to draw on the canvas. To do this, you need to get a reference to the canvas element and its context:

```html
const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
```

The `getContext()` method returns a 2D drawing context, which you can use to draw on the canvas.

Once you have the context, you can use its various methods to draw shapes, lines, and images on the canvas. For example, you can use the `fillRect()` method to draw a filled rectangle:

```html
ctx.fillStyle = "red";
ctx.fillRect(0, 0, 100, 100);
```

This will draw a red rectangle that covers the entire canvas.

You can learn more about the `<canvas>` element and how to use it in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
