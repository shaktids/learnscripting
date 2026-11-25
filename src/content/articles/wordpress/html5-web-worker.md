---
title: "HTML5 Web Worker"
description: "A Web Worker is a part of the HTML5 standard that allows web applications to run background tasks in a separate thread, without interfering with the main…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2022-12-28T15:37:00Z
legacy: true
wpId: 2655
---

A Web Worker is a part of the HTML5 standard that allows web applications to run background tasks in a separate thread, without interfering with the main UI thread. This can be useful for tasks that are computationally intensive or that take a long time to complete, as it allows the application to remain responsive while the tasks are being executed.

To use Web Workers in your web application, you need to create a worker script that contains the code that you want to run in the background. The worker script is a separate JavaScript file that is loaded and executed by the main UI thread.

Here is an example of a simple worker script that calculates the sum of an array of numbers:

```html
// Worker script
self.addEventListener("message", function(event) {
  const numbers = event.data;
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  self.postMessage(sum);
});
```

To start the worker, you can use the `Worker` constructor in JavaScript:

```html
Copy codeconst worker = new Worker("worker.js");
```

You can then use the `postMessage()` method to send data to the worker and the `onmessage` event to receive data from the worker:

```html
// Send data to worker
worker.postMessage([1, 2, 3, 4, 5]);

// Receive data from worker
worker.onmessage = function(event) {
  console.log("Sum:", event.data);
};
```

You can learn more about Web Workers and how to use them in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
