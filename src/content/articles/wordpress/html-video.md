---
title: "HTML Video"
description: "To add a video to an HTML page, you can use the <video element. This element allows you to embed video files into your web page and customize the way they…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2023-01-02T16:17:20Z
legacy: true
wpId: 2614
---

To add a video to an HTML page, you can use the `<video>` element. This element allows you to embed video files into your web page and customize the way they are displayed.

Here is an example of how to use the `<video>` element:

```html
<video src="myvideo.mp4" width="320" height="240" controls></video>
```

This example will embed a video file called "myvideo.mp4" into the HTML page, with a width of 320 pixels and a height of 240 pixels. The "controls" attribute adds video controls (play/pause, volume, etc.) to the video player.

You can also use the `<source>` element to specify multiple sources for the video, in case the browser does not support the first format:

```html
<video width="320" height="240" controls>
  <source src="myvideo.mp4" type="video/mp4">
  <source src="myvideo.webm" type="video/webm">
  Your browser does not support the video tag.
</video>
```

In this example, the browser will try to play the MP4 file first, and if it is not supported, it will try the WEBM file. If neither file is supported, the text "Your browser does not support the video tag." will be displayed.

For more information about the `<video>` element and other HTML media elements, you can refer to the following resources:

- MDN's HTML Video Guide: <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Using_HTML5_audio_and_video>
- W3Schools' HTML Video Tutorial: <https://www.w3schools.com/html/html5_video.asp>
- HTML5 Rocks' Video and Audio Content: <https://www.html5rocks.com/en/tutorials/video/basics/>
