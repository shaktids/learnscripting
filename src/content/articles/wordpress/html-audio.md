---
title: "HTML Audio"
description: "HTML <audio element is used to embed sound content in web pages. It may contain one or more audio sources, represented using the src attribute or the…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2023-01-08T16:15:26Z
legacy: true
wpId: 2609
---

HTML `<audio>` element is used to embed sound content in web pages. It may contain one or more audio sources, represented using the `src` attribute or the `<source>` element. The browser will choose the most suitable source based on the type and codec specified.

Here is an example of how to use the `<audio>` element:

```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
  <source src="song.ogg" type="audio/ogg">
  Your browser does not support the audio element.
</audio>
```

The `controls` attribute adds audio controls, such as play, pause, and volume. The text between the `<audio>` and `</audio>` tags will only be displayed in browsers that do not support the `<audio>` element.

You can also use the `<audio>` element to add sound effects to your web page by using the `autoplay`, `loop`, and `muted` attributes.

For more information and examples, you can refer to the [MDN documentation on the `<audio>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio).
