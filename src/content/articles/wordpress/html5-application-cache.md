---
title: "HTML5 Application Cache"
description: "The HTML5 Application Cache (also known as the AppCache) is a mechanism that allows web applications to cache their resources (such as HTML, CSS, and…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2022-12-28T15:35:49Z
legacy: true
wpId: 2653
---

The HTML5 Application Cache (also known as the AppCache) is a mechanism that allows web applications to cache their resources (such as HTML, CSS, and JavaScript files) locally in the user's browser. This allows the application to work offline or with a poor network connection, as the resources are loaded from the cache instead of being fetched from the server.

To use the Application Cache, you need to create a cache manifest file that lists the resources that should be cached. The manifest file is a simple text file with a `.appcache` extension that is linked to the HTML file using the `manifest` attribute of the `<html>` element:

```html
<html manifest="/cache.appcache">
  ...
</html>
```

Here is an example of a simple cache manifest file:

```html
CACHE MANIFEST
# version 1.0

CACHE:
index.html
style.css
script.js

NETWORK:
*
```

This manifest file specifies that the `index.html`, `style.css`, and `script.js` files should be cached, while all other resources should be fetched from the network.

When the user visits the application, the browser downloads the manifest file and caches the listed resources. Subsequent visits to the application will use the cached resources unless the manifest file has changed.

You can learn more about the HTML5 Application Cache and how to use it in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
