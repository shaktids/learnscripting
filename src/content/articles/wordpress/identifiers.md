---
title: "Identifiers in Groovy"
description: "Identifiers are used to define variables, functions or other user defined variables. Identifiers start with a letter, a dollar or an underscore. They…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2020-03-27T02:41:55Z
legacy: true
wpId: 1961
---

Identifiers are used to define variables, functions or other user-defined variables. Identifiers start with a letter, a dollar or an underscore. They cannot start with a number. Here are some examples of valid identifiers −

```
def employeename
def student1
def student_name
```

where **def** is a keyword used in Groovy to define an identifier.

Here is a code example of how an identifier can be used in our Hello World program.

```
class Example {
   static void main(String[] args) {
      // One can see the use of a semi-colon after each statement
      def x = 5;
      println('Hello World');
   }
}
```

In the above example, the variable **x** is used as an identifier.
