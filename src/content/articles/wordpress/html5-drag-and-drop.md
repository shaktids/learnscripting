---
title: "HTML5 Drag and Drop"
description: "The HTML5 Drag and Drop (DnD) feature allows users to drag and drop elements within a web page or between web pages. It is a part of the HTML5 standard…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2022-12-28T15:27:27Z
legacy: true
wpId: 2640
---

The HTML5 Drag and Drop (DnD) feature allows users to drag and drop elements within a web page or between web pages. It is a part of the HTML5 standard and is implemented using the `draggable` attribute and the `ondrag`, `ondragstart`, and `ondrop` event attributes.

To make an element draggable, you can set the `draggable` attribute to `true`:

```html
<div draggable="true">Drag me!</div>
```

To handle the drag and drop events, you can use the `ondrag`, `ondragstart`, and `ondrop` attributes to specify JavaScript event handlers:

```html
<div id="drag-source" draggable="true" ondragstart="dragStartHandler(event)">
  Drag me!
</div>
<div id="drop-target" ondrop="dropHandler(event)" ondragover="dragOverHandler(event)">
  Drop here!
</div>
```

In this example, the `dragStartHandler()` function is called when the drag starts, the `dragOverHandler()` function is called when the dragged element is over the drop target, and the `dropHandler()` function is called when the element is dropped.

Here is an example of how you can implement the `dragStartHandler()` function:

```html
function dragStartHandler(event) {
  event.dataTransfer.setData("text/plain", event.target.id);
  event.dataTransfer.effectAllowed = "move";
}
```

This function sets the data that will be transferred when the element is dropped and sets the allowed drag effect to "move".

You can learn more about the HTML5 Drag and Drop feature and how to use it in your web development projects by consulting the documentation on the W3C website or by searching online for tutorials and resources.
