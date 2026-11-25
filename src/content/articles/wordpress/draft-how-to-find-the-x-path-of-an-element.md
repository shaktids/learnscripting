---
title: "How to Find the X-Path of an Element"
description: "Hello in this tutorial we will deep dive into the idea behind the findings of the element in an on a document or a webpage. The tricky thing of knowing…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2020-07-18T11:20:10
legacy: true
wpId: 2073
draft: true
---

Hello in this tutorial we will deep dive into the idea behind the findings of the element in an on a document or a webpage. The tricky thing of knowing the mechanism of finding an element in the webpage or an XML file. Where the documents are organized in order of hierarchy.

## What is an X-Path ?

It is a path or a string by which the program or the interpreter will locate the element on an element.

## Types of X-Path

**1) Absolute XPath**

**2) Relative XPath**

### Absolute XPath:

- It is the direct approach to find an element with respect to its location If the location of an element changed its quite impossible to maintain the X-Paths.
- The disadvantage of the absolute XPath is that if there are any changes made in the path of the element then that XPath gets failed.
- Always we need to travel from the root of an element to go any location. Which may consume more resources for the operation.

The key characteristic of XPath is that it begins with the single forward-slash(/), which means you can select the element from the root node."/" helps the program to tells that the label of the element in the document tree.

### Relative xpath:

- It starts with the double forward-slash (//), which means it can search the element anywhere on the webpage. With the help of some functions.
- Any changes in the location of the elements don't need any modification in the X-Path.
- For Relative Xpath the path starts from the middle of the HTML DOM structure.
- You can start from the middle of the HTML DOM structure and no need to write long XPath.

## Syntax for X-Path

| Expression | Description |
| --- | --- |
| *nodename* | Selects all nodes with the name "*nodename*" |
| / | Selects from the root node |
| // | Selects nodes in the document from the current node that match the selection no matter where they are |
| . | Selects the current node |
| .. | Selects the parent of the current node |
| @ | Selects attributes |

In the table below we have listed some path expressions and the result of the expressions:

| Path Expression | Result |
| --- | --- |
| bookstore | Selects all nodes with the name "bookstore" |
| /bookstore | Selects the root element bookstore**Note:** If the path starts with a slash ( / ) it always represents an absolute path to an element! |
| bookstore/book | Selects all book elements that are children of bookstore |
| //book | Selects all book elements no matter where they are in the document |
| bookstore//book | Selects all book elements that are descendant of the bookstore element, no matter where they are under the bookstore element |
| //@lang | Selects all attributes that are named lang |

---

---

## Predicates

Predicates are used to find a specific node or a node that contains a specific value.

Predicates are always embedded in square brackets.

In the table below we have listed some path expressions with predicates and the result of the expressions:

| Path Expression | Result |
| --- | --- |
| /bookstore/book[1] | Selects the first book element that is the child of the bookstore element.**Note:** In IE 5,6,7,8,9 first node is[0], but according to W3C, it is [1]. To solve this problem in IE, set the SelectionLanguage to XPath:*In JavaScript: xml*.setProperty("SelectionLanguage","XPath"); |
| /bookstore/book[last()] | Selects the last book element that is the child of the bookstore element |
| /bookstore/book[last()-1] | Selects the last but one book element that is the child of the bookstore element |
| /bookstore/book[position()&lt;3] | Selects the first two book elements that are children of the bookstore element |
| //title[@lang] | Selects all the title elements that have an attribute named lang |
| //title[@lang='en'] | Selects all the title elements that have a "lang" attribute with a value of "en" |
| /bookstore/book[price>35.00] | Selects all the book elements of the bookstore element that have a price element with a value greater than 35.00 |
| /bookstore/book[price>35.00]/title | Selects all the title elements of the book elements of the bookstore element that have a price element with a value greater than 35.00 |

---

## Selecting Unknown Nodes

XPath wildcards can be used to select unknown XML nodes.

| Wildcard | Description |
| --- | --- |
| \* | Matches any element node |
| @\* | Matches any attribute node |
| node() | Matches any node of any kind |

In the table below we have listed some path expressions and the result of the expressions:

| Path Expression | Result |
| --- | --- |
| /bookstore/\* | Selects all the child element nodes of the bookstore element |
| //\* | Selects all elements in the document |
| //title[@\*] | Selects all title elements which have at least one attribute of any kind |

---

## Selecting Several Paths

By using the | operator in an XPath expression you can select several paths.

In the table below we have listed some path expressions and the result of the expressions:

| Path Expression | Result |
| --- | --- |
| //book/title | //book/price | Selects all the title AND price elements of all book elements |
| //title | //price | Selects all the title AND price elements in the document |
| /bookstore/book/title | //price | Selects all the title elements of the book element of the bookstore element AND all the price elements in the document |
