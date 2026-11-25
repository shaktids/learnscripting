---
title: "CSS Introduction"
description: "CSS (Cascading Style Sheets) is a stylesheet language that is used to describe the appearance and layout of a document written in HTML or XML. It allows…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2023-01-01T20:46:29Z
updatedDate: 2022-12-28T15:16:37Z
legacy: true
wpId: 2662
---

CSS (Cascading Style Sheets) is a stylesheet language that is used to describe the appearance and layout of a document written in HTML or XML. It allows you to apply styles, such as colors, fonts, and layouts, to your web pages in a separate file, called a stylesheet, which makes it easier to maintain and update your site's design.

CSS works by matching elements in your HTML or XML document with rules in your stylesheet. Each rule consists of a selector, which specifies the elements to which the styles should be applied, and a declaration block, which contains one or more declarations that specify the styles to be applied.

For example, you can use the following CSS rule to make all `<h1>` elements blue and center-aligned:

```css
Copy codeh1 {
  color: blue;
  text-align: center;
}
```

You can apply this rule to your HTML document by linking to the stylesheet using the `<link>` element in the `<head>` of the document:

```css
Copy code<head>
  <link rel="stylesheet" href="/styles.css">
</head>
```

You can also apply styles directly to an HTML element using the `style` attribute:

```css
Copy code<h1 style="color: blue; text-align: center;">This is a heading</h1>
```

CSS has a wide range of properties and features that allow you to customize the appearance and layout of your web pages. You can learn more about CSS and how to use it in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
