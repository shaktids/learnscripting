---
title: "The Structure of a C Program"
description: "A C program is a set of functions, data type definitions, and variable declarations contained in a set of files. A C program always starts its execution…"
lang: other
categories: ["C"]
author: "Shakti Das"
pubDate: 2021-05-30T05:53:38Z
legacy: true
wpId: 2400
---

A C program is a set of functions, data type definitions, and variable declarations contained in a set of files. A C program always starts its execution by the function with the name `main`. Any function can invoke any other function and the variables declared outside the function are either global or local to the current file (if they are declared with the prefix). The following figure shows the structure of a C program contained in several files.

![](/images/wp/c-program-files-en-1e8851dd.png)

The C compiler is the program that translates a set of functions, definitions and declarations in multiple files into an executable file. The C compiler has a surprisingly simple behavior and performs much less work than expected when compared with others such as the Java compiler. To create an executable, the compiler processes the source files one by one independently. This means that the defined variables and functions ***are not remembered when processing another file***. Furthermore, the compiler performs a single pass over the text, only those definitions up to the current compilation point are visible.

As a consequence of this behavior, a variable cannot be used unless it has been previously declared in the same file. Analogously, a function cannot be invoked unless its code has been previously included in the same file. To allow the division of code in multiple files the language allows the definition of “function prototypes” (the type of the result followed by the function name and the parameter types in parenthesis) without including the code, and also the definition of variables as “external”, that is, present in a different file. It follows an example of two files in which function `fill_in` and variable `table` are defined in one file but used inside in the `main` function.

| `File1.c` | `File2.c` |
| --- | --- |
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ﻿#define SIZE 100 /\* Array of 100 integers (Global)\*/ int table[SIZE]; /\* Fills an array with zeros \*/ void fill\_in(int \*t, int size) { int i; for (i = 0; i &lt; size; i++) { t[i] = 0; } return; } | 1 2 3 4 5 6 7 8 9 10 11 12 #define SIZE 100 /\* Global variable declared in other file \*/ extern int table[SIZE]; /\* Function declared in other file \*/ void fill\_in(int \*, int); /\* Program entry point \*/ int main(int argc, char \*argv[]) { fill\_in(table, SIZE); return 0; } |

Line 3 in File2.c notifies the compiler that there exist an array of 100 integers with name table defined in another file. Line 6 is a function prototype. It contains the result type (void) followed by the function name (fill\_in) and the type and name of the parameters in parenthesis (int \*t, int size). This line informs the compiler that a function with this definition is in a different location in the program. Thanks to these definitions, Line 11 is correct. The function `fill_in` can be invoked, and the variable `table` is known.

Line 1 of both files (`#define`) corresponds to a preprocessor directive, which tells the preprocessor to replace every occurrence of a particular character string (in this case, `SIZE`) with a specified value (in this case, `100`). The C preprocessor runs before the compiler and is in charge of these replacements. Use the `#define` directive when you have to define constants in your program, especially for size arrays. Write these constants in upper case always, in order to be easily readable.
