---
title: "C++ Interview Questions Part 2"
description: "What are the differences between C and C++? 1) C++ is a kind of superset of C, most C programs except few exceptions (See this and this) work in C++ as…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-01-18T12:16:20Z
legacy: true
wpId: 2111
---

**What are the differences between C and C++?**
**1)** C++ is a kind of superset of C, most C programs except few exceptions (See this and this) work in C++ as well.
2) C is a procedural programming language, but C++ supports both procedural and Object-Oriented programming.
3) Since C++ supports object-oriented programming, it supports features like function overloading, templates, inheritance, virtual functions, friend functions. These features are absent in C.
4) C++ supports exception handling at the language level, in C exception handling, is done in the traditional if-else style.
5) C++ supports references, C doesn’t.
6) In C, scanf() and print() are mainly used input/output. C++ mainly uses streams to perform input and output operations. cin is a standard input stream and cut is a standard output stream.

There are many more differences, above is a list of main differences.

**What are the differences between references and pointers?**
Both references and pointers can be used to change local variables of one function inside another function. Both of them can also be used to save copying of big objects when passed as arguments to functions or returned from functions, to get efficiency gain.
Despite the above similarities, there are the following differences between references and pointers.

*References are less powerful than pointers*
1) Once a reference is created, it cannot be later made to reference another object; it cannot be reseated. This is often done with pointers.
2) References cannot be NULL. Pointers are often made NULL to indicate that they are not pointing to any valid thing.
3) A reference must be initialized when declared. There is no such restriction with pointers

Due to the above limitations, references in C++ cannot be used for implementing data structures like Linked List, Tree, etc. In Java, references don’t have above restrictions, and can be used to implement all data structures. References being more powerful in Java, is the main reason Java doesn’t need pointers.

*References are safer and easier to use:*
1) Safer: Since references must be initialized, wild references like wild pointers are unlikely to exist. It is still possible to have references that don’t refer to a valid location (See questions 5 and 6 in the below exercise )
2) Easier to use: References don’t need dereferencing operator to access the value. They can be used like normal variables. ‘&’ operator is needed only at the time of declaration. Also, members of an object reference can be accessed with dot operator (‘.’), unlike pointers where arrow operator (->) is needed to access members.

**What are virtual functions – Write an example?**
[Virtual functions](https://www.geeksforgeeks.org/virtual-functions-and-runtime-polymorphism-in-c-set-1-introduction/)are used with inheritance, they are called according to the type of the object pointed or referred to, not according to the type of pointer or reference. In other words, virtual functions are resolved late, at runtime. Virtual keyword is used to make a function virtual.

Following things are necessary to write a C++ program with runtime polymorphism (use of virtual functions)
1) A base class and a derived class.
2) A function with same name in base class and derived class.
3) A pointer or reference of base class type pointing or referring to an object of derived class.

For example, in the following program bp is a pointer of type Base, but a call to bp->show() calls show() function of Derived class, because bp points to an object of Derived class.*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `#include<iostream>` `using` `namespace` `std;`  `class` `Base {` `public``:` `virtual` `void` `show() { cout<<``" In Base \n"``; }` `};`  `class` `Derived:` `public` `Base {` `public``:` `void` `show() { cout<<``"In Derived \n"``; }` `};`  `int` `main(``void``) {` `Base *bp =` `new` `Derived;` `bp->show();` `// RUN-TIME POLYMORPHISM` `return` `0;` `}` |

Output:

```
In Derived
```

**What is this pointer?**
The [‘this’ pointer](https://www.geeksforgeeks.org/this-pointer-in-c/)is passed as a hidden argument to all nonstatic member function calls and is available as a local variable within the body of all nonstatic functions. ‘this’ pointer is a constant pointer that holds the memory address of the current object. ‘this’ pointer is not available in static member functions as static member functions can be called without any object (with class name).

**Can we do “delete this”?**
See <https://www.geeksforgeeks.org/delete-this-in-c/>

**What are VTABLE and VPTR?**
the vtable is a table of function pointers. It is maintained per class.
vptr is a pointer to the vtable. It is maintained per object (See this for an example).
The compiler adds additional code at two places to maintain and use vtable and vptr.
1) Code in every constructor. This code sets vptr of the object being created. This code sets vptr to point to the vtable of the class.
2) Code with polymorphic function call (e.g. bp->show() in above code). Wherever a polymorphic call is made, the compiler inserts code to first look for vptr using a base class pointer or reference (In the above example, since the pointed or referred object is of a derived type, vptr of the derived class is accessed). Once vptr is fetched, the vtable of a derived class can be accessed. Using vtable, the address of the derived class function show() is accessed and called.

You may also like:

- Practice [Quizzes](http://quiz.geeksforgeeks.org/quiz-corner/#C++%20Programming%20Mock%20Tests) on C++
- C/C++ [Articles](https://www.geeksforgeeks.org/category/c-puzzles/)

We will soon be covering more C++. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

Rated as one of the most sought after skills in the industry, own the basics of coding with our [**C++ STL**](https://practice.geeksforgeeks.org/courses/cpp-stl?utm_source=geeksforgeeks&utm_medium=article&utm_campaign=GFG_Article_Bottom_CPP_STL) Course and master the very concepts by intense problem-solving.
