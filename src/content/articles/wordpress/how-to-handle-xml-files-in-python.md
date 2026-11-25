---
title: "How to Handle XML Files in Python"
description: "Introduction Xml (eXtensible Markup Language) is a markup language. XML is designed to store and transport data. Xml was released in late 90’s. it was…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2018-08-26T05:29:10Z
legacy: true
wpId: 148
---

#### Introduction
- Xml (eXtensible Markup Language) is a markup language.
- XML is designed to store and transport data.
- Xml was released in late 90’s. it was created to provide an easy to use and store self-describing data.
- XML became a W3C Recommendation on February 10, 1998.
- XML is not a replacement for HTML.
- XML is designed to be self-descriptive.
- XML is designed to carry data, not to display data.
- XML tags are not predefined. You must define your own tags.
- XML is platform independent and language independent.

### Sample XML File
*&lt;?***xmlversion=****"1.0"***?>*

&lt;**data**>

&lt;**country****name=****"Inida"**>

&lt;**rank****grade=****"22"**>1&lt;/**rank**>

&lt;**year****grade=****"33"**>2008&lt;/**year**>

&lt;**gdp****grade=****"33"**>141100&lt;/**gdp**>

&lt;**neighbor****name=****"Austria"****direction=****"E"**/>

&lt;**neighbor****name=****"Switzerland"****direction=****"W"**/>

&lt;/**country**>

&lt;**country****name=****"Singapore"**>

&lt;**rank****grade=****"225"**>1&lt;/**rank**>

&lt;**year****grade=****"335"**>208&lt;/**year**>

&lt;**gdp****grade=****"335"**>11100&lt;/**gdp**>

&lt;**neighbor****name=****"Malaysia"****direction=****"N"**/>

&lt;/**country**>

&lt;**country****name=****"US"**>

&lt;**rank**>68&lt;/**rank**>

&lt;**year**>2011&lt;/**year**>

&lt;**gdppc**>13600&lt;/**gdppc**>

&lt;**neighbor****name=****"Canada"****direction=****"W"**/>

&lt;**neighbor****name=****"Colombia"****direction=****"E"**/>

&lt;/**country**>

&lt;/**data**>

### Python Module ([xml.etree.ElementTree](https://docs.python.org/2/library/xml.etree.elementtree.html#module-xml.etree.ElementTree))
**Parse()**

This method will take the xml file as input  will parse to the python friendly tree.

**getroot()**

This will return us the roots of the tree element.

**Get()**

This method will return us the attribute of an particular root element.

![](file:///C:\Users\dasshak\AppData\Local\Temp\msohtmlclip1\01\clip_image001.png)

```
import xml.etree.ElementTree as ETT
tree = ETT.parse('ConData.xml')
root = tree.getroot()
for i in root:
    print(i.get('name'))
    #print(i)
    for j in i:
        #print(j.get('grade'))
        print(j.text)

# for country in root.findall('country'):
#     rank = country.find('rank').text
#     rank = country.find('rank')
#     name = country.get('name')
#     print (name, rank)
```

![](file:///C:\Users\dasshak\AppData\Local\Temp\msohtmlclip1\01\clip_image002.png)
