---
title: "Styling Text"
description: "One of the most common uses for CSS is to style text. Most webpages include text, after all, and changing the look of it can go a long way toward giving a…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-11T23:23:56Z
legacy: true
wpId: 2684
draft: true
---

One of the most common uses for CSS is to style text. Most webpages include text, after all, and changing the look of it can go a long way toward giving a webpage a more unique appearance. Without changing the HTML underneath, CSS can be used to alter the **size of** text, the font, theboldness, the alignmen**t**within a paragraph, and more.

- The **color** property is used to set the color of a text.
- The **direction** property is used to set the text direction.
- The **letter-spacing** property is used to add or subtract space between the letters that make up a word.
- The **word-spacing** property is used to add or subtract space between the words of a sentence.
- The **text-indent** property is used to indent the text of a paragraph.
- The **text-align** property is used to align the text of a document.
- The **text-decoration** property is used to underline, overline, and strikethrough text.
- The **text-transform** property is used to capitalize text or convert text to uppercase or lowercase letters.
- The **white-space** property is used to control the flow and formatting of text.
- The **text-shadow** property is used to set the text shadow around a text.

## Example of Text Color:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Style Tesxt</title>
    <style>
        body {
            color: blue;
        }

        h1 {
            color: green;
        }
    </style>
</head>

<body>
    <h1>This is heading</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente, minus illo iste voluptatibus impedit dolor!
    </p>
</body>

</html>
```

## Output:

## Example of Text Alignment:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            text-align: center;
        }

        h2 {
            text-align: left;
        }

        h3 {
            text-align: right;
        }
    </style>

</head>

<body>
    <h1>This is Heading1</h1>
    <h2>This is Heading2</h2>
    <h3>This is Heading3</h3>
</body>

</html>
```

## Output:

## When Text-align property is set to justify

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            border: 2px dotted rgb(196, 25, 25);
            padding: 10px;
            width: 200px;
            height: 200px;
            text-align: justify;
        }
    </style>
</head>

<body>
    <h1>This is Heading1</h1>

    <p>This is paragraph</p>

    <div>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto qui officiis repudiandae temporibus sed cum
        iusto dignissimos maxime sit odit repellat dolore, officia minus sapiente, adipisci placeat in molestias
        laudantium.
    </div>

</body>

</html>
```

## Output:

## Example of Text Decoration:

```css
<!DOCTYPE html>
<html>
<head>
<style>
h1 {
  text-decoration: overline;
}

h2 {
  text-decoration: line-through;
}

h3 {
  text-decoration: underline;
}
</style>
</head>
<body>

<h1>This is heading 1</h1>
<h2>This is heading 2</h2>
<h3>This is heading 3</h3>

</body>
</html>
```

## Output:

## Example of Text Transformation:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text CSS</title>
    <style>
        p.uppercase {
            text-transform: uppercase;
        }

        p.lowercase {
            text-transform: lowercase;
        }

        p.capitalize {
            text-transform: capitalize;
        }
    </style>
</head>

<body>
    <p class="uppercase">This is paragraph1.</p>
    <p class="lowercase">This is paragraph2.</p>
    <p class="capitalize">This is paragraph3.</p>

</body>

</html>
```

## Output:

## CSS Text Spacing:

## Text Indentation:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text CSS</title>
    <style>
        p {
            text-indent: 50px;
        }
    </style>
</head>

<body>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Assumenda vel aliquam blanditiis nam nulla nemo?</p>
</body>

</html>
```

## Output:

## Example of Letter Spacing:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text CSS</title>
    <style>
        h1 {
            letter-spacing: 3px;
        }

        h2 {
            letter-spacing: -3px;
        }
    </style>
</head>

<body>
    <h1>This is heading1</h1>
    <h2>This is heading22</h2>
</body>

</html>
```

## Output:

## Example of Line Height:

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text CSS</title>

</head>
<body>
  <p>
This is a paragraph with a standard line-height.<br>
The default line height in most browsers is about 110% to 120%.<br>
</p>

<p class="small">
This is a paragraph with a smaller line-height.<br>
This is a paragraph with a smaller line-height.<br>
</p>

<p class="big">
This is a paragraph with a bigger line-height.<br>
This is a paragraph with a bigger line-height.<br>
</p>

</body>
</html>
```

## Output:
