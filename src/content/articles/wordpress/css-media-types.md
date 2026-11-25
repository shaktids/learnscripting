---
title: "CSS Media Types"
description: "One of the most important features of style sheets is that, we can specify separate style sheets for different media types. This is one of the best ways…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-15T09:49:24Z
legacy: true
wpId: 2789
draft: true
---

One of the most important features of style sheets is that, we can specify separate style sheets for different media types. This is one of the best ways to build printer friendly Web pages — Just assign a different style sheet for the "print" media type.

Some CSS properties are only designed for certain media. For example, the [`page-break-after`](https://www.tutorialrepublic.com/css-reference/css-page-break-after-property.php) property only applies to paged media. However there are several properties that may be shared by different media types, but may require different values for that property. The [`font-size`](https://www.tutorialrepublic.com/css-reference/css-font-size-property.php) property for example can be used for both screen and print media, but possibly with different values.

A document usually needs a larger font on a computer screen as compared to the paper for better readability, also sans-serif fonts are considered easier to read on the screen, while serif fonts are popular for printing. Therefore it is necessary to specify that a style sheet, or a set of style rules, applies to certain media types.

## The @media rule:

```css
<style tyle = "text/css">
   <!--
      @media print {
         body { font-size: 10pt }
      }

      @media screen {
         body { font-size: 12pt }
      }
      @media screen, print {
         body { line-height: 1.2 }
      }
   -->
</style>
```

## Creating Media Dependent Style Sheets:

```css
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Example of CSS media types</title>
<style>
	@media screen{
        body {
            color: #32cd32;
			font-family: Arial, sans-serif;
            font-size: 14px;
        }
    }
    @media print {
        body {
            color: #ff6347;
			font-family: Times, serif;
            font-size: 12pt;
        }
    }
    @media screen, print {
        body {
            line-height: 1.2;
        }
    }
</style>
</head>
<body>
    <h1>CSS Media Types</h1>
    <p><strong>Note:</strong> If you print (or print preview) this page the output of HTML code appears differently than it appears on the screen.</p>
</body>
</html>
```

## Output:

## Different Media Types:

| Media Type | Description |
| --- | --- |
| all | Used for all media type devices. |
| aural | Used for speech and sound synthesizers. |
| braille | Used for braille tactile feedback devices. |
| embossed | Used for paged braille printers. |
| handheld | Used for small or handheld devices — usually small screen devices such as mobile phones or PDAs. |
| print | Used for printers. |
| projection | Used for projected presentations, for example projectors. |
| screen | Used primarily for color computer screens. |
| tty | Used for media using a fixed-pitch character grid — such as teletypes, terminals, or portable devices with limited display capabilities. |
| tv | Used for television-type devices — low resolution, color, limited-scrollability screens, sound available. |
