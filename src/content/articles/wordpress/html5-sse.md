---
title: "HTML5 SSE"
description: "Server Sent Events (SSE) is a technology that allows a web server to send events to a web page in real time. It is a part of the HTML5 standard and is…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2022-12-28T15:12:15Z
legacy: true
wpId: 2659
---

Server-Sent Events (SSE) is a technology that allows a web server to send events to a web page in real-time. It is a part of the HTML5 standard and is implemented using the `EventSource` interface.

To use SSE in an HTML page, you first need to create an `EventSource` object and specify the URL of the server-side script that will be sending the events. For example:

```html
const source = new EventSource("/events");
```

Next, you can set up an event listener to handle the events as they are received. For example:

```html
source.addEventListener("message", (event) => {
  console.log(event.data);
});
```

This will log the data of each event to the console as it is received.

On the server-side, you can use a script or a server-side language, such as PHP or Node.js, to send events to the client. The events are sent as a stream of text over a persistent connection, and each event is separated by a newline character.

Here is an example of a PHP script that sends an event every 5 seconds:

```html
header("Content-Type: text/event-stream");
header("Cache-Control: no-cache");

while (true) {
  echo "event: message\n";
  echo "data: This is a message from the server\n\n";
  ob_flush();
  flush();
  sleep(5);
}
```

This script sends an event with the type "message" and the data "This is a message from the server" every 5 seconds.

You can learn more about SSE and how to use it in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
