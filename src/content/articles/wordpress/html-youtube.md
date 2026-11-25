---
title: "HTML YouTube"
description: "To embed a YouTube video in an HTML page, you can use the <iframe element. The src the attribute should contain the URL of the YouTube video, and the…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2023-01-03T17:01:05Z
legacy: true
wpId: 2618
---

To embed a YouTube video in an HTML page, you can use the `<iframe>` element. The `src` the attribute should contain the URL of the YouTube video, and the `width` and `height` attributes should specify the dimensions of the video player.

For example:

```html
<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" width="560" height="315" frameborder="0" allowfullscreen></iframe>
```

This will embed the YouTube video with the URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ` in the HTML page, with a width of 560 pixels and a height of 315 pixels. The `frameborder` attribute controls the border around the video player, and the `allowfullscreen` attribute allows the video to be played in full-screen mode.

You can also customize the video player using the `?` the parameter in the URL. For example, to hide the player controls and related videos when the video is finished, you can use the following URL:

```html
https://www.youtube.com/embed/dQw4w9WgXcQ?controls=0&rel=0
```

You can find more information about customizing the YouTube video player in the YouTube API documentation.
