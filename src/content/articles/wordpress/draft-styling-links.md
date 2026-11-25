---
title: "Styling Links"
description: "Links can be styled with any CSS property, such as color , font family , font size , and padding . The four links states are: a:link a normal, unvisited…"
lang: other
categories: ["CSS"]
author: "Shakti Das"
pubDate: 2021-06-12T08:05:25Z
legacy: true
wpId: 2696
draft: true
---

Links can be styled with any CSS property, such as `color`, `font-family`, `font-size`, and `padding`.

The four links states are:

- `a:link` - a normal, unvisited link
- `a:visited` - a link the user has visited
- `a:hover` - a link when the user mouses over it
- `a:active` - a link the moment it is clicked

### Example:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styling Links</title>
    <style>
        /* unvisited link */
        a:link {
            color: red;
        }

        /* visited link */
        a:visited {
            color: green;
        }

        /* mouse over link */
        a:hover {
            color: hotpink;
        }

        /* selected link */
        a:active {
            color: blue;
        }
    </style>
</head>

<body>
    <h2>CSS Links</h2>
    <p><b><a href="https://learnscripting.org/wp-admin/post.php?post=2667&action=edit" target="_blank">This is a
                link</a></b></p>
    <p><b>Note:</b> a:hover MUST come after a:link and a:visited in the CSS definition in order to be effective.</p>
    <p><b>Note:</b> a:active MUST come after a:hover in the CSS definition in order to be effective.</p>

</body>

</html>
```

## Output:

## Example of Text-Decoration:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styling Links</title>
    <style>
        a:link {
            text-decoration: none;
        }

        a:visited {
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        a:active {
            text-decoration: underline;
    </style>
</head>

<body>
    <h2>CSS Links</h2>
    <p><b><a href="https://learnscripting.org/wp-admin/post.php?post=2667&action=edit" target="_blank">This is a
                link</a></b></p>
    <p><b>Note:</b> a:hover MUST come after a:link and a:visited in the CSS definition in order to be effective.</p>
    <p><b>Note:</b> a:active MUST come after a:hover in the CSS definition in order to be effective.</p>

</body>

</html>
```

## Output:

## Example of Background-color:

```css
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Styling Links</title>
    <style>
        a:link {
            background-color: rgb(153, 0, 255);
        }

        a:visited {
            background-color: rgb(255, 196, 0);
        }

        a:hover {
            background-color: lightgreen;
        }

        a:active {
            background-color: hotpink;
        }
    </style>
</head>

<body>
    <h2>CSS Links</h2>
    <p><b><a href="https://learnscripting.org/wp-admin/post.php?post=2667&action=edit" target="_blank">This is a
                link</a></b></p>
    <p><b>Note:</b> a:hover MUST come after a:link and a:visited in the CSS definition in order to be effective.</p>
    <p><b>Note:</b> a:active MUST come after a:hover in the CSS definition in order to be effective.</p>

</body>

</html>
```

## Output:

## Example of Links Buttons:

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS Links</title>
    <style>
        a:link, a:visited {
          background-color: #9bf436;
          color: rgb(255, 255, 255);
          padding: 14px 25px;
          text-align: center;
          text-decoration: none;
          display: inline-block;
        }
     </style>
</head>
<body>
    <body>

        <h2>Link Button</h2>
        <p>A link styled as a button:</p>
        <a href="https://learnscripting.org/wp-admin/post.php?post=2667&action=edit" target="_blank">This is a link</a>

</body>
</html>
```

Output:
