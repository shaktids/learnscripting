---
title: "HTML Iframes"
description: "An <iframe is an HTML element that allows you to embed another HTML document within the current document. It is often used to embed external resources…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2023-01-02T16:24:33Z
legacy: true
wpId: 2566
---

An `<iframe>` is an HTML element that allows you to embed another HTML document within the current document. It is often used to embed external resources such as videos, maps, and interactive content into a web page.

Here is an example of how to use an `<iframe>` element:

```html
<iframe src="https://www.example.com" width="600" height="400"></iframe>
```

This example will embed the webpage at "[https://www.example.com](https://www.example.com/)" into the current HTML document, with a width of 600 pixels and a height of 400 pixels.

You can also use the `srcdoc` attribute to specify the HTML content to be embedded, instead of an external URL:

```html
<iframe srcdoc="<h1>Hello, World!</h1>" width="600" height="400"></iframe>
```

In this example, the text "Hello, World!" will be displayed inside the iframe.

Note that iframes can be a security risk if they are used to embed untrusted content, as the embedded content has the same privileges as the main page and can potentially access sensitive information. It is important to only embed trusted content using iframes.

For more information about the `<iframe>` element and other HTML embedding elements, you can refer to the following resources:

- MDN's HTML Iframes Guide: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe>
- W3Schools' HTML Iframes Tutorial: <https://www.w3schools.com/html/html_iframe.asp>
