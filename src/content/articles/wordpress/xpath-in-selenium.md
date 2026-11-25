---
title: "How to find the XPATH of an element to automate the element"
description: "XPATH is a way to identify the element by navigating the entire html source code and identify the element using back end attribute. Syntax of XPATH // To…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T02:15:03Z
legacy: true
wpId: 25
---

XPATH is a way to identify the element by navigating the entire html source code and identify the element using back-end attribute.

Syntax of XPATH

// To go to entire html source code

/   Navigating from parent to child

[ ]  Attribute Declaration

[ ]   Navigating from child to parent

@   Attribute annonation

We can give the xpath of an element either by absolute or relative.

**Absolute XPATH**
Whenever the XPATH is written from parent to child it is known as absolute XPATH. In real time we will not move for absolute XPATH because if the requirement got changed  or location of the element got changed it will fail to identify the element.

Relative XPATH
//htmltag[@attribute=’value’]

Whenever the xpath is written by using back end attribute of the element it is known as relative xpath.

Using one attribute when we will get multiple matching node we will take help of other attribute present in the html source code.

Sometime using attribute it fails to identify the element so we will go and take of parent and first we will identify the parent and then navigate to its child.

**Function in XPATH**

### text()
Syntax- //html tag[text()=’value’]
eg- //h[text()=’username’]

These are the advance function to write the xpath whenever their is no attribute given in html source code only visible text is their we will go for text().

### contains()
It is used to handle the dynamic element present on the web page.
Generally is used to handle ajax application.
Ajax is a java framework which is used to develop dynamic element.

Syntax// htmltag[contains(test(),’value’)]

eg-//a[contains(@title,’com’)]

With the help of part of a string we will write the XPATH to handle dynamic element.
Contains function automatically remove the space present before the starting and after the string.

### normalize-space
It is used to remove the space present before the string and after the string present  in visible test or attribute value and compare the string with string  and return the .It is the supporting function of text function.
Syntax//htmltag[normalize-space(text()/@attribute)=’value’]
eg//td[normalize-space(text())=’Open Task’]

### preceding sibling
It is used to identify the previous element of a web element .

### When to use the following or preceding sibling
When the element attribute is dynamic and we are not able to identify the element using attribute we go for following or preceding sibling.

### following sibling
Following sibling is used to identify the next element of a web element.

### descendant
We use descendant to skip some html tag.

### ancestor
Ancestor lets you select any ancestors [e.g., Parent and Grandparent] of the current node.
//\*[@id=’regular-expression-syntax’]/ancestor::div[5]/div[2]
//\*[@id=’regular-expression-syntax’]/ancestor::\*

### ancestor-or-self
Ancestor-or-self lets you select any ancestors [e.g., Parent and Grandparent] of the current                      node including the current node.
//\*[@id=’regular-expression-syntax’]/ancestor-or-self::div[1]
//\*[@id=’regular-expression-syntax’]/ancestor-or-self::\*

### attribute
Attribute returns all the attributes in the current node.
//\*[@class=’sphinxsidebarwrapper’]/attribute::\*
//\*[@id=’sidebarbutton’]/attribute::title

### child
Child returns all the children in the current node.
//\*[@class=’sphinxsidebarwrapper’]/child::\*
//\*//child::h3

### following
Following returns all in the document after the closing tag of the current node.
//\*[@class=’clearer’]/following::\*

### namespace
Namespace returns all namespace nodes in the current node.
TBD

### parent
Parent returns the parent of the current node.
//\*[@class=’sphinxsidebar’]/parent::node()
//\*[@class=’bodywrapper’]/parent::\*
//\*[@class=’bodywrapper’]/parent::div[1]
//\*[@class=’bodywrapper’]/parent::div

### preceding
Preceding is a reverse of Following;  Preceding returns all in the document before the current node
//\*[@class=’bodywrapper’]/preceding::\*

### self
Self returns the current node.
//\*[@class=’footer’]/self::\*
//\*[@class=’footer’]/self::div
