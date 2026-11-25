---
title: "HTML Object"
description: "The <object element in HTML is used to embed external resources, such as multimedia (e.g., audio, video, Java applets), in an HTML page. It can also be…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2023-01-03T17:06:19Z
legacy: true
wpId: 2611
---

The `<object>` element in HTML is used to embed external resources, such as multimedia (e.g., audio, video, Java applets), in an HTML page. It can also be used to embed other types of documents, such as PDFs.

The `<object>` element is a container for the embedded resource, and it can have several attributes to specify the location of the resource and other properties of the object. The most important attributes are:

- `data`: This attribute specifies the URL of the resource to be embedded.
- `type`: This attribute specifies the MIME type of resource.
- `width` and `height`: These attributes specify the dimensions of the object.

Here is an example of how to use the `<object>` element to embed a PDF file in an HTML page:

```html
<object data="myfile.pdf" type="application/pdf" width="800" height="600">
  <p>It looks like you don't have a PDF plugin for this browser. You can <a href="myfile.pdf">click here to download the PDF file.</a></p>
</object>
```

In this example, the `<object>` the element will attempt to load the PDF file at the URL "myfile.pdf" and display it in an 800x600 pixel window. If the browser doesn't have a PDF plugin, the fallback content (the `<p>` element) will be displayed instead.

You can find more information about the `<object>` element in the HTML documentation.
