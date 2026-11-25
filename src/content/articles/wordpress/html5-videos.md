---
title: "HTML5 Videos"
description: "HTML5 is the latest version of the HTML standard and it introduces several new features that make it easier to embed and play videos on a web page without…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2023-01-11T01:25:50Z
legacy: true
wpId: 2625
---

HTML5 is the latest version of the HTML standard and it introduces several new features that make it easier to embed and play videos on a web page without the need for additional plug-ins.

The `<video>` tag is the main way to embed videos in an HTML5 document. The `<video>` tag is used to embed video files, such as MP4, WebM, and Ogg, in a web page. The basic syntax for the `<video>` tag is:

```html
<video src="video-file.mp4"></video>
```

This will create a video player on the web page and the video will start playing automatically. The `src` attribute is used to specify the location of the video file, and the `controls` attribute can be added to show the video player controls.

```html
<video src="video-file.mp4" controls></video>
```

You can also specify multiple sources for the same video to support different video formats, this can be done by adding multiple `<source>` elements inside the `<video>` element.

```html
<video controls>
   <source src="video-file.mp4" type="video/mp4">
   <source src="video-file.webm" type="video/webm">
</video>
```

In addition to the basic embedding, you can also customize the appearance of the video player using CSS and you can use JavaScript to control the video, such as starting and stopping the video and jumping to specific parts of the video.

HTML5 videos also support captions and subtitles using the `<track>` element, this element allows you to add captions or subtitles to the video and can be used to display text translations for the video in different languages.

```html
<video controls>
  <source src="video-file.mp4" type="video/mp4">
  <track src="captions.vtt" kind="captions" label="English captions" srclang="en" default>
</video>
```

In summary, HTML5 makes it easy to embed and play videos on a web page without the need for additional plug-ins. The `<video>` tag is used to embed video files, and you can control the video player's appearance and behavior using CSS and JavaScript. HTML5 videos also support captions and subtitles using the `<track>` element. With these features, it's become very easy to put rich multimedia content on web pages.
