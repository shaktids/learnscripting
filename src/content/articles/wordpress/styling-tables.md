---
title: "Styling Tables"
description: "Tables in HTML are used to display tabular data, such as lists of information or data in rows and columns. You can use CSS to style tables and table…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-12T23:04:33Z
updatedDate: 2022-12-28T15:07:00Z
legacy: true
wpId: 2708
---

Tables in HTML are used to display tabular data, such as lists of information or data in rows and columns. You can use CSS to style tables and table elements to change their appearance and layout.

Here are some common ways to style tables and table elements using CSS:

- Set the background color of the table using the `background-color` property.
- Set the width of the table and its cells using the `width` property.
- Set the border of the table and its cells using the `border` property.
- Set the padding of the table cells using the `padding` property.
- Set the text color and font properties of the table cells using the `color` and `font` properties.
- Set the alignment of the text within the table cells using the `text-align` property.

Here is an example of some CSS that styles a table:

```css
table {
  width: 100%;
  border: 1px solid black;
}

td {
  padding: 10px;
  text-align: center;
  border: 1px solid black;
}

th {
  background-color: lightgray;
  font-weight: bold;
  border: 1px solid black;
}
```

This CSS will set the width of the table to 100% of its container, add a 1px solid black border to the table and its cells, set the padding of the cells to 10px, align the text in the cells to the center, and give the table header cells a lightgray background and bold font weight.

You can also use CSS classes and IDs to style specific tables or table elements on your page. For example, you could give a table an ID of "customers" and use the ID selector to style that specific table:

```css
#customers {
  width: 50%;
  border: 2px solid red;
}
```

This would set the width of the table with an ID of "customers" to 50% of its container and give it a 2px solid red border.

You can learn more about styling tables and other HTML elements using CSS by consulting the documentation on the W3C website or by searching online for tutorials and resources.
