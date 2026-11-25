---
title: "HTML URL Encode"
description: "URL encoding, also known as percent encoding, is a mechanism for encoding information in a Uniform Resource Identifier (URI) under certain circumstances…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2023-01-02T16:26:23Z
legacy: true
wpId: 2607
---

URL encoding, also known as percent-encoding, is a mechanism for encoding information in a Uniform Resource Identifier (URI) under certain circumstances. It is used to encode special characters in URLs, for example when an URL contains characters that are not allowed in a standard URL or when the URL contains spaces or other characters that need to be encoded.

To encode a URL in HTML, you can use the `encodeURIComponent()` function in JavaScript. This function takes a string as input and returns the encoded version of the string.

Here is an example of how to use `encodeURIComponent()`:

```
<a href="https://www.example.com/search?q=<script>">Link</a>
```

This example creates a link to a search page with a query parameter containing an invalid script element. To fix this, you can use `encodeURIComponent()` to encode the query parameter:

```
<a href="https://www.example.com/search?q=%3Cscript%3E">Link</a>
```

In this example, the script element is encoded as `%3Cscript%3E`, which is the URL-encoded version of `<script>`.

You can also use the `decodeURIComponent()` function to decode a URL-encoded string.

For more information about URL encoding and decoding in JavaScript, you can refer to the following resources:

- MDN's encodeURIComponent() documentation: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent>
- W3Schools' encodeURIComponent() tutorial: <https://www.w3schools.com/jsref/jsref_encodeURIComponent.asp>
- MDN's decodeURIComponent() documentation: <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent>
- W3Schools' decodeURIComponent() tutorial: <https://www.w3schools.com/jsref/jsref_decodeuricomponent.asp>
