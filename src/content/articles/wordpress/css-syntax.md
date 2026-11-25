---
title: "CSS Syntax"
description: "CSS (Cascading Style Sheets) is a stylesheet language that is used to describe the appearance and layout of a document written in HTML or XML. CSS allows…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-11T08:11:41Z
updatedDate: 2022-12-28T15:16:48Z
legacy: true
wpId: 2664
---

CSS (Cascading Style Sheets) is a stylesheet language that is used to describe the appearance and layout of a document written in HTML or XML. CSS allows you to apply styles, such as colors, fonts, and layouts, to your web pages in a separate file, called a stylesheet, which makes it easier to maintain and update your site's design.

The syntax of CSS consists of rules, which specify how the styles should be applied to the elements in your document. A rule consists of a selector, which specifies the elements to which the styles should be applied, and a declaration block, which contains one or more declarations that specify the styles to be applied.

Here is an example of a simple CSS rule:

```css
h1 {
  font-size: 32px;
  color: blue;
  text-align: center;
}
```

In this example, the selector is `h1`, which specifies that the styles should be applied to all `<h1>` elements in the document. The declaration block contains three declarations: `font-size`, `color`, and `text-align`. Each declaration consists of a property, such as `font-size` or `color`, and a value, such as `32px` or `blue`.

You can also specify multiple rules in a stylesheet. For example:

```css
h1 {
  font-size: 32px;
  color: blue;
  text-align: center;
}

p {
  font-size: 18px;
  color: black;
  text-align: left;
}
```

This stylesheet contains two rules: one for `<h1>` elements and one for `<p>` elements.

You can apply stylesheets to your HTML documents using the `<link>` element in the `<head>` of the document, like this:

```css
<head>
  <link rel="stylesheet" href="/styles.css">
</head>
```

You can also apply styles directly to an HTML element using the `style` attribute:

```css
<h1 style="font-size: 32px; color: blue; text-align: center;">This is a heading</h1>
```

You can learn more about CSS syntax and how to use it in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
