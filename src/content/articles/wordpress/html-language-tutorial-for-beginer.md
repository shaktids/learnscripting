---
title: "HTML Language Tutorial  for Beginer"
description: "HTML Tutorial HTML stands for Hyper Text Markup Language, which is the most widely used language on Web to develop web pages. HTML was created by Berners…"
lang: other
categories: ["HTML"]
author: "Shakti Das"
pubDate: 2017-01-22T02:16:44Z
legacy: true
wpId: 29
---

# HTML Tutorial

HTML stands for Hyper Text Markup Language, which is the most widely used language on Web to develop web pages. HTML was created by Berners-Lee in late 1991 but "HTML 2.0" was the first standard HTML specification which was published in 1995. HTML 4.01 was a major version of HTML and it was published in late 1999. Though HTML 4.01 version is widely used but currently we are having HTML-5 version which is an extension to HTML 4.01, and this version was published in 2012.

# Audience

This tutorial is designed for the aspiring Web Designers and Developers with a need to understand the HTML in enough detail along with its simple overview, and practical examples. This tutorial will give you enough ingredients to start with HTML from where you can take yourself at higher level of expertise.

# Prerequisites

Before proceeding with this tutorial you should have a basic working knowledge with Windows or Linux operating system, additionally you must be familiar with −

- Experience with any text editor like notepad, notepad++, or Edit plus etc.
- How to create directories and files on your computer.
- How to navigate through different directories.
- How to type content in a file and save them on a computer.
- Understanding about images in different formats like JPEG, PNG format.

HTML stands for **H**yper**t**ext **M**arkup **L**anguage, and it is the most widely used language to write Web Pages.

- **Hypertext** refers to the way in which Web pages (HTML documents) are linked together. Thus, the link available on a webpage is called Hypertext.
- As its name suggests, HTML is a **Markup Language** which means you use HTML to simply "mark-up" a text document with tags that tell a Web browser how to structure it to display.

Originally, HTML was developed with the intent of defining the structure of documents like headings, paragraphs, lists, and so forth to facilitate the sharing of scientific information between researchers.

Now, HTML is being widely used to format web pages with the help of different tags available in HTML language.

## Basic HTML Document

In its simplest form, following is an example of an HTML document −

[Live Demo](http://tpcg.io/tryL9g)

```
<!DOCTYPE html>
<html>

   <head>
      <title>This is document title</title>
   </head>

   <body>
      <h1>This is a heading</h1>
      <p>Document content goes here.....</p>
   </body>

</html>
```

[Open embedded content](https://www.tutorialspoint.com/html/src/basic_html_document.htm)

## HTML Tags

As told earlier, HTML is a markup language and makes use of various tags to format the content. These tags are enclosed within angle braces **&lt;Tag Name>**. Except few tags, most of the tags have their corresponding closing tags. For example, **&lt;html>** has its closing tag **&lt;/html>** and **&lt;body>** tag has its closing tag **&lt;/body>** tag etc.

Above example of HTML document uses the following tags −

|
 Sr.No |
 Tag & Description |

|
 1 |
 **&lt;!DOCTYPE...>**This tag defines the document type and HTML version. |

|
 2 |
 **&lt;html>**This tag encloses the complete HTML document and mainly comprises of document header which is represented by &lt;head>...&lt;/head> and document body which is represented by &lt;body>...&lt;/body> tags. |

|
 3 |
 **&lt;head>**This tag represents the document's header which can keep other HTML tags like &lt;title>, &lt;link> etc. |

|
 4 |
 **&lt;title>**The &lt;title> tag is used inside the &lt;head> tag to mention the document title. |

|
 5 |
 **&lt;body>**This tag represents the document's body which keeps other HTML tags like &lt;h1>, &lt;div>, &lt;p> etc. |

|
 6 |
 **&lt;h1>**This tag represents the heading. |

|
 7 |
 **&lt;p>**This tag represents a paragraph. |

To learn HTML, you will need to study various tags and understand how they behave, while formatting a textual document. Learning HTML is simple as users have to learn the usage of different tags in order to format the text or images to make a beautiful webpage.

World Wide Web Consortium (W3C) recommends to use lowercase tags starting from HTML 4.

## HTML Document Structure

A typical HTML document will have the following structure −

```
<html>

   <head>
      Document header related tags
   </head>

   <body>
      Document body related tags
   </body>

</html>
```

We will study all the header and body tags in subsequent chapters, but for now let's see what is document declaration tag.

## The &lt;!DOCTYPE> Declaration

The &lt;!DOCTYPE> declaration tag is used by the web browser to understand the version of the HTML used in the document. Current version of HTML is 5 and it makes use of the following declaration −

```
<!DOCTYPE html>
```

There are many other declaration types which can be used in HTML document depending on what version of HTML is being used. We will see more details on this while discussing &lt;!DOCTYPE...> tag along with other HTML tags.

## Heading Tags

Any document starts with a heading. You can use different sizes for your headings. HTML also has six levels of headings, which use the elements **&lt;h1>, &lt;h2>, &lt;h3>, &lt;h4>, &lt;h5>,** and **&lt;h6>**. While displaying any heading, browser adds one line before and one line after that heading.

### Example

 [Live Demo](http://tpcg.io/Oevfe8)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Heading Example</title>
   </head>

   <body>
      <h1>This is heading 1</h1>
      <h2>This is heading 2</h2>
      <h3>This is heading 3</h3>
      <h4>This is heading 4</h4>
      <h5>This is heading 5</h5>
      <h6>This is heading 6</h6>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/heading_tag.htm)

## Paragraph Tag

The **&lt;p>** tag offers a way to structure your text into different paragraphs. Each paragraph of text should go in between an opening &lt;p> and a closing &lt;/p> tag as shown below in the example −

### Example

 [Live Demo](http://tpcg.io/Uo5jZe)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Paragraph Example</title>
   </head>

   <body>
      <p>Here is a first paragraph of text.</p>
      <p>Here is a second paragraph of text.</p>
      <p>Here is a third paragraph of text.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/paragraph_tag.htm)

## Line Break Tag

Whenever you use the **&lt;br />** element, anything following it starts from the next line. This tag is an example of an **empty** element, where you do not need opening and closing tags, as there is nothing to go in between them.

The &lt;br /> tag has a space between the characters **br** and the forward slash. If you omit this space, older browsers will have trouble rendering the line break, while if you miss the forward slash character and just use &lt;br> it is not valid in XHTML.

### Example

 [Live Demo](http://tpcg.io/aWg5PG)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Line Break  Example</title>
   </head>

   <body>
      <p>Hello<br />
         You delivered your assignment ontime.<br />
         Thanks<br />
         Mahnaz</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/line_break_tag.htm)

## Centering Content

You can use **&lt;center>** tag to put any content in the center of the page or any table cell.

### Example

 [Live Demo](http://tpcg.io/mVrRPS)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Centring Content Example</title>
   </head>

   <body>
      <p>This text is not in the center.</p>

      <center>
         <p>This text is in the center.</p>
      </center>
   </body>

</html>
```

This will produce following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/centering_content.htm)

## Horizontal Lines

Horizontal lines are used to visually break-up sections of a document. The **&lt;hr>** tag creates a line from the current position in the document to the right margin and breaks the line accordingly.

For example, you may want to give a line between two paragraphs as in the given example below −

### Example

 [Live Demo](http://tpcg.io/4iAnXc)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Horizontal Line Example</title>
   </head>

   <body>
      <p>This is paragraph one and should be on top</p>
      <hr />
      <p>This is paragraph two and should be at bottom</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/horizontal_lines.htm)

Again **&lt;hr />** tag is an example of the **empty** element, where you do not need opening and closing tags, as there is nothing to go in between them.

The **&lt;hr />** element has a space between the characters **hr** and the forward slash. If you omit this space, older browsers will have trouble rendering the horizontal line, while if you miss the forward slash character and just use **&lt;hr>** it is not valid in XHTML

## Preserve Formatting

Sometimes, you want your text to follow the exact format of how it is written in the HTML document. In these cases, you can use the preformatted tag **&lt;pre>**.

Any text between the opening **&lt;pre>** tag and the closing **&lt;/pre>** tag will preserve the formatting of the source document.

### Example

 [Live Demo](http://tpcg.io/e3k3sG)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Preserve Formatting Example</title>
   </head>

   <body>
      <pre>
         function testFunction( strText ){
            alert (strText)
         }
      </pre>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/preserve_formatting.htm)

Try using the same code without keeping it inside **&lt;pre>...&lt;/pre>** tags

## Nonbreaking Spaces

Suppose you want to use the phrase "12 Angry Men." Here, you would not want a browser to split the "12, Angry" and "Men" across two lines −

```
An example of this technique appears in the movie "12 Angry Men."
```

In cases, where you do not want the client browser to break text, you should use a nonbreaking space entity **&nbsp;** instead of a normal space. For example, when coding the "12 Angry Men" in a paragraph, you should use something similar to the following code −

### Example

 [Live Demo](http://tpcg.io/OhhfWR)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Nonbreaking Spaces Example</title>
   </head>

   <body>
      <p>An example of this technique appears in the movie "12&nbsp;Angry&nbsp;Men."</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/nonbreaking_spaces.htm)

An **HTML element** is defined by a starting tag. If the element contains other content, it ends with a closing tag, where the element name is preceded by a forward slash as shown below with few tags −

|
 Start Tag |
 Content |
 End Tag |

|
 &lt;p> |
 This is paragraph content. |
 &lt;/p> |

|
 &lt;h1> |
 This is heading content. |
 &lt;/h1> |

|
 &lt;div> |
 This is division content. |
 &lt;/div> |

|
 &lt;br /> |
  |
  |

So here **&lt;p>....&lt;/p>** is an HTML element, **&lt;h1>...&lt;/h1>** is another HTML element. There are some HTML elements which don't need to be closed, such as **&lt;img.../>**, **&lt;hr />** and **&lt;br />** elements. These are known as **void elements**.

HTML documents consists of a tree of these elements and they specify how HTML documents should be built, and what kind of content should be placed in what part of an HTML document.

## HTML Tag vs. Element

An HTML element is defined by a *starting tag*. If the element contains other content, it ends with a *closing tag*.

For example, **&lt;p>** is starting tag of a paragraph and **&lt;/p>** is closing tag of the same paragraph but **&lt;p>This is paragraph&lt;/p>** is a paragraph element.

## Nested HTML Elements

It is very much allowed to keep one HTML element inside another HTML element −

### Example

 [Live Demo](http://tpcg.io/RWo6kx)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Nested Elements Example</title>
   </head>

   <body>
      <h1>This is <i>italic</i> heading</h1>
      <p>This is <u>underlined</u> paragraph</p>
   </body>

</html>
```

This will display the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/nested_html_elements.htm)

We have seen few HTML tags and their usage like heading tags **&lt;h1>, &lt;h2>,** paragraph tag **&lt;p>** and other tags. We used them so far in their simplest form, but most of the HTML tags can also have attributes, which are extra bits of information.

An attribute is used to define the characteristics of an HTML element and is placed inside the element's opening tag. All attributes are made up of two parts − a **name** and a **value**

- The **name** is the property you want to set. For example, the paragraph **&lt;p>** element in the example carries an attribute whose name is **align**, which you can use to indicate the alignment of paragraph on the page.

- The **value** is what you want the value of the property to be set and always put within quotations. The below example shows three possible values of align attribute:  **left, center** and **right**.

Attribute names and attribute values are case-insensitive. However, the World Wide Web Consortium (W3C) recommends lowercase attributes/attribute values in their HTML 4 recommendation.

### Example

 [Live Demo](http://tpcg.io/rJQ2Po)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Align Attribute  Example</title>
   </head>

   <body>
      <p align = "left">This is left aligned</p>
      <p align = "center">This is center aligned</p>
      <p align = "right">This is right aligned</p>
   </body>

</html>
```

This will display the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/attributes.htm)

## Core Attributes

The four core attributes that can be used on the majority of HTML elements (although not all) are −

- Id

- Title

- Class

- Style

### The Id Attribute

The **id** attribute of an HTML tag can be used to uniquely identify any element within an HTML page. There are two primary reasons that you might want to use an id attribute on an element −

- If an element carries an id attribute as a unique identifier, it is possible to identify just that element and its content.

- If you have two elements of the same name within a Web page (or style sheet), you can use the id attribute to distinguish between elements that have the same name.

We will discuss style sheet in separate tutorial. For now, let's use the id attribute to distinguish between two paragraph elements as shown below.

**Example**

```
<p id = "html">This para explains what is HTML</p>
<p id = "css">This para explains what is Cascading Style Sheet</p>
```

### The title Attribute

The **title** attribute gives a suggested title for the element. They syntax for the **title** attribute is similar as explained for **id** attribute −

The behavior of this attribute will depend upon the element that carries it, although it is often displayed as a tooltip when cursor comes over the element or while the element is loading.

**Example**

[Live Demo](http://tpcg.io/Xq2ok1)

```
<!DOCTYPE html>
<html>

   <head>
      <title>The title Attribute Example</title>
   </head>

   <body>
      <h3 title = "Hello HTML!">Titled Heading Tag Example</h3>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/title_attribute.htm)

Now try to bring your cursor over "Titled Heading Tag Example" and you will see that whatever title you used in your code is coming out as a tooltip of the cursor.

### The class Attribute

The **class** attribute is used to associate an element with a style sheet, and specifies the class of element. You will learn more about the use of the class attribute when you will learn Cascading Style Sheet (CSS). So for now you can avoid it.

The value of the attribute may also be a space-separated list of class names. For example −

```
class = "className1 className2 className3"
```

### The style Attribute

The style attribute allows you to specify Cascading Style Sheet (CSS) rules within the element.

[Live Demo](http://tpcg.io/FreFRI)

```
<!DOCTYPE html>
<html>

   <head>
      <title>The style Attribute</title>
   </head>

   <body>
      <p style = "font-family:arial; color:#FF0000;">Some text...</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/style_attribute.htm)

At this point of time, we are not learning CSS, so just let's proceed without bothering much about CSS. Here, you need to understand what are HTML attributes and how they can be used while formatting content.

## Internationalization Attributes

There are three internationalization attributes, which are available for most (although not all) XHTML elements.

- dir

- lang

- xml:lang

### The dir Attribute

The **dir** attribute allows you to indicate to the browser about the direction in which the text should flow. The dir attribute can take one of two values, as you can see in the table that follows −

|
 Value |
 Meaning |

|
 ltr |
 Left to right (the default value) |

|
 rtl |
 Right to left (for languages such as Hebrew or Arabic that are read right to left) |

**Example**

[Live Demo](http://tpcg.io/a9JBAz)

```
<!DOCTYPE html>
<html dir = "rtl">

   <head>
      <title>Display Directions</title>
   </head>

   <body>
      This is how IE 5 renders right-to-left directed text.
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/dir_attribute.htm)

When *dir* attribute is used within the &lt;html> tag, it determines how text will be presented within the entire document. When used within another tag, it controls the text's direction for just the content of that tag.

### The lang Attribute

The **lang** attribute allows you to indicate the main language used in a document, but this attribute was kept in HTML only for backwards compatibility with earlier versions of HTML. This attribute has been replaced by the **xml:lang** attribute in new XHTML documents.

The values of the *lang* attribute are ISO-639 standard two-character language codes. Check [**HTML Language Codes: ISO 639**](https://www.tutorialspoint.com/html/language_iso_codes.htm) for a complete list of language codes.

**Example**

[Live Demo](http://tpcg.io/Hf0XPh)

```
<!DOCTYPE html>
<html lang = "en">

   <head>
      <title>English Language Page</title>
   </head>

   <body>
      This page is using English Language
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/lang_attribute.htm)

## The xml:lang Attribute

The *xml:lang* attribute is the XHTML replacement for the *lang* attribute. The value of the *xml:lang* attribute should be an ISO-639 country code as mentioned in previous section.

### Generic Attributes

Here's a table of some other attributes that are readily usable with many of the HTML tags.

|
 Attribute |
 Options |
 Function |

|
 align |
 right, left, center |
 Horizontally aligns tags |

|
 valign |
 top, middle, bottom |
 Vertically aligns tags within an HTML element. |

|
 bgcolor |
 numeric, hexidecimal, RGB values |
 Places a background color behind an element |

|
 background |
 URL |
 Places a background image behind an element |

|
 id |
 User Defined |
 Names an element for use with Cascading Style Sheets. |

|
 class |
 User Defined |
 Classifies an element for use with Cascading Style Sheets. |

|
 width |
 Numeric Value |
 Specifies the width of tables, images, or table cells. |

|
 height |
 Numeric Value |
 Specifies the height of tables, images, or table cells. |

|
 title |
 User Defined |
 "Pop-up" title of the elements. |

We will see related examples as we will proceed to study other HTML tags. For a complete list of HTML Tags and related attributes please check reference to [HTML Tags List](https://www.tutorialspoint.com/html/html_tags_reference.htm).

If you use a word processor, you must be familiar with the ability to make text bold, italicized, or underlined; these are just three of the ten options available to indicate how text can appear in HTML and XHTML.

## Bold Text

Anything that appears within **&lt;b>...&lt;/b>** element, is displayed in bold as shown below −

### Example

 [Live Demo](http://tpcg.io/5KMKkW)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Bold Text Example</title>
   </head>

   <body>
      <p>The following word uses a <b>bold</b> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/bold_text.htm)

## Italic Text

Anything that appears within **&lt;i>...&lt;/i>** element is displayed in italicized as shown below −

### Example

 [Live Demo](http://tpcg.io/OJgqcS)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Italic Text Example</title>
   </head>

   <body>
      <p>The following word uses an <i>italicized</i> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/italic_text.htm)

## Underlined Text

Anything that appears within **&lt;u>...&lt;/u>** element, is displayed with underline as shown below −

### Example

 [Live Demo](http://tpcg.io/5Y75MX)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Underlined Text Example</title>
   </head>

   <body>
      <p>The following word uses an <u>underlined</u> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/underlined_text.htm)

## Strike Text

Anything that appears within **&lt;strike>...&lt;/strike>** element is displayed with strikethrough, which is a thin line through the text as shown below −

### Example

 [Live Demo](http://tpcg.io/HIkU7n)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Strike Text Example</title>
   </head>

   <body>
      <p>The following word uses a <strike>strikethrough</strike> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/strike_text.htm)

## Monospaced Font

The content of a **&lt;tt>...&lt;/tt>** element is written in monospaced font. Most of the fonts are known as variable-width fonts because different letters are of different widths (for example, the letter 'm' is wider than the letter 'i'). In a monospaced font, however, each letter has the same width.

### Example

 [Live Demo](http://tpcg.io/7XdwHl)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Monospaced Font Example</title>
   </head>

   <body>
      <p>The following word uses a <tt>monospaced</tt> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/monospaced_font.htm)

## Superscript Text

The content of a **&lt;sup>...&lt;/sup>** element is written in superscript; the font size used is the same size as the characters surrounding it but is displayed half a character's height above the other characters.

### Example

 [Live Demo](http://tpcg.io/ASSDpm)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Superscript Text Example</title>
   </head>

   <body>
      <p>The following word uses a <sup>superscript</sup> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/superscript_text.htm)

## Subscript Text

The content of a **&lt;sub>...&lt;/sub>** element is written in subscript; the font size used is the same as the characters surrounding it, but is displayed half a character's height beneath the other characters.

### Example

 [Live Demo](http://tpcg.io/FS24k4)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Subscript Text Example</title>
   </head>

   <body>
      <p>The following word uses a <sub>subscript</sub> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/subscript_text.htm)

## Inserted Text

Anything that appears within **&lt;ins>...&lt;/ins>** element is displayed as inserted text.

### Example

 [Live Demo](http://tpcg.io/8WK66t)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Inserted Text Example</title>
   </head>

   <body>
      <p>I want to drink <del>cola</del> <ins>wine</ins></p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/inserted_text.htm)

## Deleted Text

Anything that appears within **&lt;del>...&lt;/del>** element, is displayed as deleted text.

### Example

 [Live Demo](http://tpcg.io/HAK4s7)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Deleted Text Example</title>
   </head>

   <body>
      <p>I want to drink <del>cola</del> <ins>wine</ins></p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/delete_text.htm)

## Larger Text

The content of the **&lt;big>...&lt;/big>** element is displayed one font size larger than the rest of the text surrounding it as shown below −

### Example

 [Live Demo](http://tpcg.io/XGxTMW)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Larger Text Example</title>
   </head>

   <body>
      <p>The following word uses a <big>big</big> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/larger_text.htm)

## Smaller Text

The content of the **&lt;small>...&lt;/small>** element is displayed one font size smaller than the rest of the text surrounding it as shown below −

### Example

 [Live Demo](http://tpcg.io/BtVDGJ)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Smaller Text Example</title>
   </head>

   <body>
      <p>The following word uses a <small>small</small> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/smaller_text.htm)

## Grouping Content

The **&lt;div>** and **&lt;span>** elements allow you to group together several elements to create sections or subsections of a page.

For example, you might want to put all of the footnotes on a page within a &lt;div> element to indicate that all of the elements within that &lt;div> element relate to the footnotes. You might then attach a style to this &lt;div> element so that they appear using a special set of style rules.

### Example

 [Live Demo](http://tpcg.io/tqWkee)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Div Tag Example</title>
   </head>

   <body>
      <div id = "menu" align = "middle" >
         <a href = "/index.htm">HOME</a> |
         <a href = "/about/contact_us.htm">CONTACT</a> |
         <a href = "/about/index.htm">ABOUT</a>
      </div>

      <div id = "content" align = "left" bgcolor = "white">
         <h5>Content Articles</h5>
         <p>Actual content goes here.....</p>
      </div>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/grouping_content.htm)

The &lt;span> element, on the other hand, can be used to group inline elements only. So, if you have a part of a sentence or paragraph which you want to group together, you could use the &lt;span> element as follows.

### Example

 [Live Demo](http://tpcg.io/R5ONzp)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Span Tag Example</title>
   </head>

   <body>
      <p>This is the example of <span style = "color:green">span tag</span>
         and the <span style = "color:red">div tag</span> alongwith CSS</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/span_tag.htm)

These tags are commonly used with CSS to allow you to attach a style to a section of a page.

If you use a word processor, you must be familiar with the ability to make text bold, italicized, or underlined; these are just three of the ten options available to indicate how text can appear in HTML and XHTML.

## Bold Text

Anything that appears within **&lt;b>...&lt;/b>** element, is displayed in bold as shown below −

### Example

 [Live Demo](http://tpcg.io/5KMKkW)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Bold Text Example</title>
   </head>

   <body>
      <p>The following word uses a <b>bold</b> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/bold_text.htm)

## Italic Text

Anything that appears within **&lt;i>...&lt;/i>** element is displayed in italicized as shown below −

### Example

 [Live Demo](http://tpcg.io/OJgqcS)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Italic Text Example</title>
   </head>

   <body>
      <p>The following word uses an <i>italicized</i> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/italic_text.htm)

## Underlined Text

Anything that appears within **&lt;u>...&lt;/u>** element, is displayed with underline as shown below −

### Example

 [Live Demo](http://tpcg.io/5Y75MX)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Underlined Text Example</title>
   </head>

   <body>
      <p>The following word uses an <u>underlined</u> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/underlined_text.htm)

## Strike Text

Anything that appears within **&lt;strike>...&lt;/strike>** element is displayed with strikethrough, which is a thin line through the text as shown below −

### Example

 [Live Demo](http://tpcg.io/HIkU7n)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Strike Text Example</title>
   </head>

   <body>
      <p>The following word uses a <strike>strikethrough</strike> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/strike_text.htm)

## Monospaced Font

The content of a **&lt;tt>...&lt;/tt>** element is written in monospaced font. Most of the fonts are known as variable-width fonts because different letters are of different widths (for example, the letter 'm' is wider than the letter 'i'). In a monospaced font, however, each letter has the same width.

### Example

 [Live Demo](http://tpcg.io/7XdwHl)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Monospaced Font Example</title>
   </head>

   <body>
      <p>The following word uses a <tt>monospaced</tt> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/monospaced_font.htm)

## Superscript Text

The content of a **&lt;sup>...&lt;/sup>** element is written in superscript; the font size used is the same size as the characters surrounding it but is displayed half a character's height above the other characters.

### Example

 [Live Demo](http://tpcg.io/ASSDpm)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Superscript Text Example</title>
   </head>

   <body>
      <p>The following word uses a <sup>superscript</sup> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/superscript_text.htm)

## Subscript Text

The content of a **&lt;sub>...&lt;/sub>** element is written in subscript; the font size used is the same as the characters surrounding it, but is displayed half a character's height beneath the other characters.

### Example

 [Live Demo](http://tpcg.io/FS24k4)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Subscript Text Example</title>
   </head>

   <body>
      <p>The following word uses a <sub>subscript</sub> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/subscript_text.htm)

## Inserted Text

Anything that appears within **&lt;ins>...&lt;/ins>** element is displayed as inserted text.

### Example

 [Live Demo](http://tpcg.io/8WK66t)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Inserted Text Example</title>
   </head>

   <body>
      <p>I want to drink <del>cola</del> <ins>wine</ins></p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/inserted_text.htm)

## Deleted Text

Anything that appears within **&lt;del>...&lt;/del>** element, is displayed as deleted text.

### Example

 [Live Demo](http://tpcg.io/HAK4s7)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Deleted Text Example</title>
   </head>

   <body>
      <p>I want to drink <del>cola</del> <ins>wine</ins></p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/delete_text.htm)

## Larger Text

The content of the **&lt;big>...&lt;/big>** element is displayed one font size larger than the rest of the text surrounding it as shown below −

### Example

 [Live Demo](http://tpcg.io/XGxTMW)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Larger Text Example</title>
   </head>

   <body>
      <p>The following word uses a <big>big</big> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/larger_text.htm)

## Smaller Text

The content of the **&lt;small>...&lt;/small>** element is displayed one font size smaller than the rest of the text surrounding it as shown below −

### Example

 [Live Demo](http://tpcg.io/BtVDGJ)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Smaller Text Example</title>
   </head>

   <body>
      <p>The following word uses a <small>small</small> typeface.</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/smaller_text.htm)

## Grouping Content

The **&lt;div>** and **&lt;span>** elements allow you to group together several elements to create sections or subsections of a page.

For example, you might want to put all of the footnotes on a page within a &lt;div> element to indicate that all of the elements within that &lt;div> element relate to the footnotes. You might then attach a style to this &lt;div> element so that they appear using a special set of style rules.

### Example

 [Live Demo](http://tpcg.io/tqWkee)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Div Tag Example</title>
   </head>

   <body>
      <div id = "menu" align = "middle" >
         <a href = "/index.htm">HOME</a> |
         <a href = "/about/contact_us.htm">CONTACT</a> |
         <a href = "/about/index.htm">ABOUT</a>
      </div>

      <div id = "content" align = "left" bgcolor = "white">
         <h5>Content Articles</h5>
         <p>Actual content goes here.....</p>
      </div>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/grouping_content.htm)

The &lt;span> element, on the other hand, can be used to group inline elements only. So, if you have a part of a sentence or paragraph which you want to group together, you could use the &lt;span> element as follows.

### Example

 [Live Demo](http://tpcg.io/R5ONzp)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Span Tag Example</title>
   </head>

   <body>
      <p>This is the example of <span style = "color:green">span tag</span>
         and the <span style = "color:red">div tag</span> alongwith CSS</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/span_tag.htm)

These tags are commonly used with CSS to allow you to attach a style to a section of a page.

HTML lets you specify metadata - additional important information about a document in a variety of ways. The META elements can be used to include name/value pairs describing properties of the HTML document, such as author, expiry date, a list of keywords, document author etc.

The **&lt;meta>** tag is used to provide such additional information. This tag is an empty element and so does not have a closing tag but it carries information within its attributes.

You can include one or more meta tags in your document based on what information you want to keep in your document but in general, meta tags do not impact physical appearance of the document so from appearance point of view, it does not matter if you include them or not.

## Adding Meta Tags to Your Documents

You can add metadata to your web pages by placing &lt;meta> tags inside the header of the document which is represented by **&lt;head>** and **&lt;/head>** tags. A meta tag can have following attributes in addition to core attributes −

|
 Sr.No |
 Attribute & Description |

|
 1 |
 **Name** |

Name for the property. Can be anything. Examples include, keywords, description, author, revised, generator etc.

|
 2 |
 **content** |

Specifies the property's value.

|
 3 |
 **scheme** |

Specifies a scheme to interpret the property's value (as declared in the content attribute).

|
 4 |
 **http-equiv** |

Used for http response message headers. For example, http-equiv can be used to refresh the page or to set a cookie. Values include content-type, expires, refresh and set-cookie.

## Specifying Keywords

You can use &lt;meta> tag to specify important keywords related to the document and later these keywords are used by the search engines while indexing your webpage for searching purpose.

### Example

Following is an example, where we are adding HTML, Meta Tags, Metadata as important keywords about the document.

[Live Demo](http://tpcg.io/Mvd7Nk)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

This will produce the following result −

[Open embedded content](https://www.tutorialspoint.com/html/src/specifying_keywords.htm)

## Document Description

You can use &lt;meta> tag to give a short description about the document. This again can be used by various search engines while indexing your webpage for searching purpose.

### Example

 [Live Demo](http://tpcg.io/J78g6J)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

## Document Revision Date

You can use &lt;meta> tag to give information about when last time the document was updated. This information can be used by various web browsers while refreshing your webpage.

### Example

 [Live Demo](http://tpcg.io/fxucEh)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "revised" content = "Tutorialspoint, 3/7/2014" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

## Document Refreshing

A &lt;meta> tag can be used to specify a duration after which your web page will keep refreshing automatically.

### Example

If you want your page keep refreshing after every 5 seconds then use the following syntax.

[Live Demo](http://tpcg.io/KuBkdG)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "revised" content = "Tutorialspoint, 3/7/2014" />
      <meta http-equiv = "refresh" content = "5" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

## Page Redirection

You can use &lt;meta> tag to redirect your page to any other webpage. You can also specify a duration if you want to redirect the page after a certain number of seconds.

### Example

Following is an example of redirecting current page to another page after 5 seconds. If you want to redirect page immediately then do not specify *content* attribute.

[Live Demo](http://tpcg.io/F7fndy)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "revised" content = "Tutorialspoint, 3/7/2014" />
      <meta http-equiv = "refresh" content = "5; url = http://www.tutorialspoint.com" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

## Setting Cookies

Cookies are data, stored in small text files on your computer and it is exchanged between web browser and web server to keep track of various information based on your web application need.

You can use &lt;meta> tag to store cookies on client side and later this information can be used by the Web Server to track a site visitor.

### Example

Following is an example of redirecting current page to another page after 5 seconds. If you want to redirect page immediately then do not specify *content* attribute.

[Live Demo](http://tpcg.io/8gIhsi)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "revised" content = "Tutorialspoint, 3/7/2014" />
      <meta http-equiv = "cookie" content = "userid = xyz;
         expires = Wednesday, 08-Aug-15 23:59:59 GMT;" />

   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

If you do not include the expiration date and time, the cookie is considered a session cookie and will be deleted when the user exits the browser.

**Note** − You can check [PHP and Cookies](http://www.tutorialspoint.com/php/php_cookies.htm) tutorial for a complete detail on Cookies.

## Setting Author Name

You can set an author name in a web page using meta tag. See an example below −

### Example

 [Live Demo](http://tpcg.io/W5TIEH)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "author" content = "Mahnaz Mohtashim" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

## Specify Character Set

You can use &lt;meta> tag to specify character set used within the webpage.

### Example

By default, Web servers and Web browsers use ISO-8859-1 (Latin1) encoding to process Web pages. Following is an example to set UTF-8 encoding −

[Live Demo](http://tpcg.io/muVyKF)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "author" content = "Mahnaz Mohtashim" />
      <meta http-equiv = "Content-Type" content = "text/html; charset = UTF-8" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```

To serve the static page with traditional Chinese characters, the webpage must contain a &lt;meta> tag to set Big5 encoding −

[Live Demo](http://tpcg.io/zHW42k)

```
<!DOCTYPE html>
<html>

   <head>
      <title>Meta Tags Example</title>
      <meta name = "keywords" content = "HTML, Meta Tags, Metadata" />
      <meta name = "description" content = "Learning about Meta Tags." />
      <meta name = "author" content = "Mahnaz Mohtashim" />
      <meta http-equiv = "Content-Type" content = "text/html; charset = Big5" />
   </head>

   <body>
      <p>Hello HTML5!</p>
   </body>

</html>
```
