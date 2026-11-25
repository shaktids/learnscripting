---
title: "CSS Border Color"
description: "The border color property in CSS is used to set the color of an element's border. The border is the line that surrounds an element and separates it from…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-13T08:07:20Z
updatedDate: 2022-12-28T15:00:34Z
legacy: true
wpId: 2724
---

The `border-color` property in CSS is used to set the color of an element's border. The border is the line that surrounds an element and separates it from other elements on the page.

You can set the border color of an element using the `border-color` property in your CSS. The property takes one or more values, separated by spaces, to specify the colors of the border on different sides of the element. The values can be specified using a color keyword, such as, or using hexadecimal, RGB, or HSL value.

For example, to set the border color of an element to red, you could use the following CSS:

```css
element {
    border-color: red;
}
```

You can also set different colors for each side of the border using the `border-top-color`, `border-right-color`, `border-bottom-color`, and `border-left-color` properties.

For example, to set the top border to red, the right border to green, the bottom border to blue, and the left border to yellow, you could use the following CSS:

```css
element {
    border-top-color: red;
    border-right-color: green;
    border-bottom-color: blue;
    border-left-color: yellow;
}
```

Alternatively, you can use the `border-color` property and specify the values in the following order: `top right bottom left`.

For example:

```css
element {
    border-color: red green blue yellow;
}
```

You can also use the `border` property to set the border width, style, and color at the same time. For example:

```css
element {
    border: 2px solid red;
}
```

This will set the border width to 2 pixels, the border style to solid, and the border color to red.

Note that the border color will only be visible if the border style is not set to `none`.
