---
title: "HTML5 Audio"
description: "The <audio HTML element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-10T19:03:12
legacy: true
wpId: 2638
draft: true
---

The &lt;audio> HTML element is used to embed sound content in documents. It may contain one or more audio sources, represented using the src attribute or the &lt;source>element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a MediaStream.

## Example:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <audio controls>
        <source src="horse.ogg" type="audio/ogg">
        <source src="horse.mp3" type="audio/mpeg">
      Your browser does not support the audio element.
      </audio>

</body>
</html>
```

Output:
