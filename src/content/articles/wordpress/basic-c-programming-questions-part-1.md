---
title: "Basic c Programming Questions Part 1"
description: "What is the difference between declaration and definition of a variable/function Ans: Declaration of a variable/function simply declares that the…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-01-18T12:07:49Z
legacy: true
wpId: 2124
---

**What is the difference between declaration and definition of a variable/function**
**Ans:** Declaration of a variable/function simply declares that the variable/function exists somewhere in the program but the memory is not allocated for them. But the declaration of a variable/function serves an important role. And that is the type of the variable/function. Therefore, when a variable is declared, the program knows the data type of that variable. In case of function declaration, the program knows what are the arguments to that functions, their data types, the order of arguments and the return type of the function. So that’s all about declaration. Coming to the definition, when we define a variable/function, apart from the role of declaration, it also allocates memory for that variable/function. Therefore, we can think of definition as a super set of declaration. (or declaration as a subset of definition).

> // This is only declaration. y is not allocated memory by this statement
> extern int y;
>
> // This is both declaration and definition, memory to x is allocated by this statement.
> int x;

**What are different storage class specifiers in C?**
**Ans:** auto, register, static, extern

**What is scope of a variable? How are variables scoped in [C](http://www.geeksforgeeks.org/c/)?**
**Ans:** Scope of a variable is the part of the program where the variable may directly be accessible. In C, all identifiers are lexically (or statically) scoped. See [this](https://www.geeksforgeeks.org/scope-rules-in-c/)for more details.

**How will you print “Hello World” without semicolon?**
**Ans:***filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `#include <stdio.h>` `int` `main(``void``)` `{` `if` `(``printf``(``"Hello World"``)) {` `}` `}` |

See [print “Geeks for Geeks” without using a semicolon for answer](https://www.geeksforgeeks.org/write-a-c-program-to-print-geeks-for-geeks-without-using-a-semicolon/).

**When should we use pointers in a C program?**
**1.** To get address of a variable
***2.** For achieving pass by reference in C:* Pointers allow different functions to share and modify their local variables.
***3.** To pass large structures* so that complete copy of the structure can be avoided.
***4.** To implement “linked” data structures*like linked lists and binary trees.

**What is NULL pointer?**
**Ans:** NULL is used to indicate that the pointer doesn’t point to a valid location. Ideally, we should initialize pointers as NULL if we don’t know their value at the time of declaration. Also, we should make a pointer NULL when memory pointed by it is deallocated in the middle of a program.

**What is Dangling pointer?**
**Ans:** Dangling Pointer is a pointer that doesn’t point to a valid memory location. Dangling pointers arise when an object is deleted or deallocated, without modifying the value of the pointer, so that the pointer still points to the memory location of the deallocated memory. Following are examples.*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `// EXAMPLE 1` `int``* ptr = (``int``*)``malloc``(``sizeof``(``int``));` `..........................``free``(ptr);`  `// ptr is a dangling pointer now and operations like following are invalid` `*ptr = 10;` `// or printf("%d", *ptr);` |

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `// EXAMPLE 2` `int``* ptr = NULL` `{` `int` `x = 10;` `ptr = &x;` `}` `// x goes out of scope and memory allocated to x is free now.` `// So ptr is a dangling pointer now.` |

**What is memory leak? Why it should be avoided**
**Ans:** Memory leak occurs when programmers create a memory in heap and forget to delete it. Memory leaks are particularly serious issues for programs like daemons and servers which by definition never terminate.*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `/* Function with memory leak */``#include <stdlib.h>`  `void` `f()` `{` `int``* ptr = (``int``*)``malloc``(``sizeof``(``int``));`  `/* Do some work */` `return``;` `/* Return without freeing ptr*/``}` |

**What are local static variables? What is their use?**
**Ans:**A local static variable is a variable whose lifetime doesn’t end with a function call where it is declared. It extends for the lifetime of complete program. All calls to the function share the same copy of local static variables. Static variables can be used to count the number of times a function is called. Also, static variables get the default value as 0. For example, the following program prints “0 1”*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `#include <stdio.h>` `void` `fun()` `{` `// static variables get the default value as 0.` `static` `int` `x;` `printf``(``"%d "``, x);` `x = x + 1;` `}`  `int` `main()` `{` `fun();` `fun();` `return` `0;` `}` `// Output: 0 1` |

**What are static functions? What is their use?**
**Ans:**In C, functions are global by default. The “static” keyword before a function name makes it static. Unlike global functions in C, access to static functions is restricted to the file where they are declared. Therefore, when we want to restrict access to functions, we make them static. Another reason for making functions static can be reuse of the same function name in other files. See [this](https://www.geeksforgeeks.org/what-are-static-functions-in-c/)for examples and more details.

You may also like:
