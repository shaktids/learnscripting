---
title: "CSS Display"
description: "Every HTML element is represented by a box that contains content and determines the amount of spacing around the content. The CSS display property…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T17:36:37Z
legacy: true
wpId: 2759
---

Every HTML element is [represented by a box](https://blog.hubspot.com/website/css-box-model) that contains content and determines the amount of spacing around the content. The CSS **display** property specifies how this box appears on the web page relative to other elements, as well as the behavior of its child elements (i.e. the elements inside it).

In CSS there are two “levels” this box can adopt: block and inline. **Block-level** elements exist on their own line and span the entire width of the page unless another width is specified. **&lt;div>** and **&lt;p>** are examples of block-level elements.

**Inline-level** elements do not break the flow of content — multiple inline elements can exist on the same line. **&lt;span>**, **&lt;b>**, and **&lt;a>** are inline-level elements.

The **display** property targets these levels and lets us change them for our styling needs. A **display** rule is written like so:

display: value;

...where **value** specifies the way the element appears — in other words, its level.

## Property values:

| Value | Description |
| --- | --- |
| inline | It is used to displays an element as an inline element. |
| block | It is used to displays an element as a block element |
| contents | It is used to disappear the container. |
| flex | It is used to display an element as a block-level flex container. |
| grid | It is used to display an element as a block-level grid container. |
| inline-block | It is used to display an element as an inline-level block container. |
| inline-flex | It is used to display an element as an inline-level flex container. |
| inline-grid | It is used to display an element as an inline-level grid container. |
| inline-table | It is used to display an inline-level table |
| list-item | It is used to display all the elements in &lt;li> element. |
| run-in | It is used to display an element inline or block level, depending on the context. |
| table | It is used to set the behavior as &lt;table> for all elements. |
| table-caption | It is used to set the behavior as &lt;caption> for all elements. |
| table-column-group | It is used to set the behavior as &lt;column> for all elements. |
| table-header-group | It is used to set the behavior as &lt;header> for all elements. |
| table-footer-group | It is used to set the behavior as &lt;footer> for all elements. |
| table-row-group | It is used to set the behavior as &lt;row> for all elements. |
| table-cell | It is used to set the behavior as &lt;td> for all elements. |
| table-column | It is used to set the behavior as &lt;col> for all elements. |
| table-row | It is used to set the behavior as &lt;tr> for all elements. |
| none | It is used to remove the element. |
| initial | It is used to set the default value. |
| inherit | It is used to inherit the property from it’s parents’ elements. |

## Example:

```css
<!DOCTYPE html>
<html>
<head>
<style>
p {color: red;}

p.ex1 {display: none;}
p.ex2 {display: inline;}
p.ex3 {display: block;}
p.ex4 {display: inline-block;}
</style>
</head>
<body>
<h1>The display Property</h1>

<h2>display: none:</h2>
<div>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam semper diam at erat pulvinar, at pulvinar felis blandit. <p class="ex1">HELLO WORLD!</p> Vestibulum volutpat tellus diam, consequat gravida libero rhoncus ut.
</div>

<h2>display: inline:</h2>
<div>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam semper diam at erat pulvinar, at pulvinar felis blandit. <p class="ex2">HELLO WORLD!</p> Vestibulum volutpat tellus diam, consequat gravida libero rhoncus ut.
</div>

<h2>display: block:</h2>
<div>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam semper diam at erat pulvinar, at pulvinar felis blandit. <p class="ex3">HELLO WORLD!</p> Vestibulum volutpat tellus diam, consequat gravida libero rhoncus ut.
</div>

<h2>display: inline-block:</h2>
<div>
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam semper diam at erat pulvinar, at pulvinar felis blandit. <p class="ex4">HELLO WORLD!</p> Vestibulum volutpat tellus diam, consequat gravida libero rhoncus ut.
</div>

</body>
</html>
```

## Output:
