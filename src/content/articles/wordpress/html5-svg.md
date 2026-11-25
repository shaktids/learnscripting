---
title: "HTML5 SVG"
description: "Scalable Vector Graphics (SVG) is a part of the HTML5 standard that allows you to create vector graphics, such as charts, diagrams, and icons, on the web…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2022-12-28T15:30:10Z
legacy: true
wpId: 2646
---

Scalable Vector Graphics (SVG) is a part of the HTML5 standard that allows you to create vector graphics, such as charts, diagrams, and icons, on the web. It uses a simple XML-based format that can be easily edited and styled using CSS.

To use SVG in an HTML file, you can use the `<svg>` element to define the graphics container and the `<path>` element to define the shapes and lines that make up the graphic. You can then use the `d` attribute of the `<path>` element to define the path data using a series of commands and coordinates.

Here is an example of an SVG graphic that draws a red triangle:

```html
<svg width="100" height="100">
  <path d="M 10,10 L 90,90 L 10,90 Z" fill="red" />
</svg>
```

This example defines a container with a width and height of 100 pixels and a `<path>` element that draws a triangle using the "move to", "line to", and "close path" commands. The `fill` attribute is used to set the fill color to red.

You can also use CSS to style and animate SVG graphics. For example, you can use the `fill`, `stroke`,
