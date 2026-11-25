---
title: "Styling Lists"
description: "Lists in HTML are used to display a series of items, such as a list of menu options or a list of bullet points. You can use CSS to style lists and list…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2022-12-28T15:06:34Z
legacy: true
wpId: 2703
---

Lists in HTML are used to display a series of items, such as a list of menu options or a list of bullet points. You can use CSS to style lists and list elements to change their appearance and layout.

There are two main types of lists in HTML: ordered lists (`<ol>`) and unordered lists (`<ul>`). Ordered lists are numbered lists, while unordered lists use bullet points to separate the items.

Here are some common ways to style lists and list elements using CSS:

- Set the list item marker style using the `list-style-type` property. For example, you can set the marker to a bullet point using `list-style-type: disc`.
- Set the position of the list item marker using the `list-style-position` property. For example, you can set the marker to be inside the list item using `list-style-position: inside`.
- Set the color of the list item marker using the `color` property.
- Set the font properties of the list items using the `font` property.
- Set the background color of the list items using the `background-color` property.

Here is an example of some CSS that styles an unordered list:

```css
ul {
  list-style-type: square;
  list-style-position: inside;
  color: green;
}

li {
  font-size: 18px;
  font-weight: bold;
  background-color: lightgray;
}
```

This CSS will set the list item marker to squares, position the marker inside the list items, set the text color to green, set the font size and weight of the list items to 18px and bold, respectively, and give the list items a lightgray background color.

You can also use CSS classes and IDs to style specific lists or list elements on your page. For example, you could give a list an ID of "favorites" and use the ID selector to style that specific list:

```css
#favorites {
  list-style-type: circle;
  color: blue;
}
```

This would set the list item marker of the list with an ID of "favorites" to circles and set the text color to blue.

You can learn more about styling lists and other HTML elements using CSS by consulting the documentation on the W3C website or by searching online for tutorials and resources.
