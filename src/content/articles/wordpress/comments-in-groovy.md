---
title: "Comments in Groovy"
description: "Comments are used to document your code. Comments in Groovy can be single line or multiline. // Single line comments are identified by using the // at any…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2020-03-27T03:44:13Z
legacy: true
wpId: 1957
---

Comments are used to document your code. Comments in Groovy can be single line or multiline.

#### //

Single line comments are identified by using the **//** at any position in the line. An example is shown below −

```
class Example {
   static void main(String[] args) {
      // Using a simple println statement to print output to the console
      println('Hello World');
   }
}
```

#### /\* \*/

Multiline comments are identified with **/\*** in the beginning and **\*/** to identify the end of the multiline comment.

```
class Example {
   static void main(String[] args) {
      /* This program is the first program
      This program shows how to display hello world */
      println('Hello World');
   }
}
```
