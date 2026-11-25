---
title: "CSS Outline"
description: "CSS Outline Properties An outline is a line drawn around an element outside the border. This can be use to make an element \"stand out\". The CSS outline…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-13T10:19:00Z
legacy: true
wpId: 2736
---

## CSS Outline Properties

An outline is a line drawn around an element - outside the border. This can be use to make an element "stand out".

The CSS `outline` properties specify the style, color, and width of an outline.

## Outline Style

The `outline-style` property specifies the style of the outline.

The `outline-style` property can have one of the following values:

- `dotted` - Defines a dotted outline
- `dashed` - Defines a dashed outline
- `solid` - Defines a solid outline
- `double` - Defines a double outline
- `groove` - Defines a 3D grooved outline. The effect depends on the outline-color value
- `ridge` - Defines a 3D ridged outline. The effect depends on the outline-color value
- `inset` - Defines a 3D inset outline. The effect depends on the outline-color value
- `outset` - Defines a 3D outset outline. The effect depends on the outline-color value
- `none` - Defines no outline
- `hidden` - Defines a hidden outline

## Example:

```css
<!DOCTYPE html>
<html>
<head>
<style>
p {
    border: 1px solid black;
    outline-color:rgb(153, 0, 255);
}
p.dotted {outline-style: dotted;}
p.dashed {outline-style: dashed;}
p.solid {outline-style: solid;}
p.double {outline-style: double;}
p.groove {outline-style: groove;}
p.ridge {outline-style: ridge;}
p.inset {outline-style: inset;}
p.outset {outline-style: outset;}
</style>
</head>
<body>

<h2>The outline-style Property</h2>

<p class="dotted">A dotted outline</p>
<p class="dashed">A dashed outline</p>
<p class="solid">A solid outline</p>
<p class="double">A double outline</p>
<p class="groove">A groove outline</p>
<p class="ridge">A ridge outline</p>
<p class="inset">An inset outline</p>
<p class="outset">An outset outline</p>

</body>
</html>
```

## Output:
