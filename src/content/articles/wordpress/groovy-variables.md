---
title: "Groovy - Variables"
description: "Variables in Groovy can be defined in two ways − using the native syntax for the data type or the next is by using the def keyword . For variable…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2020-03-27T03:51:02Z
legacy: true
wpId: 1983
---

Variables in Groovy can be defined in two ways − using the **native syntax** for the data type or the next is **by using the def keyword**. For variable definitions, it is mandatory to either provide a type name explicitly or to use "def" in replacement. This is required by the Groovy parser.

There are following basic types of variable in Groovy as explained in the previous chapter −

- **byte** − This is used to represent a byte value. An example is 2.
- **short** − This is used to represent a short number. An example is 10.
- **int** − This is used to represent whole numbers. An example is 1234.
- **long** − This is used to represent a long number. An example is 10000090.
- **float** − This is used to represent 32-bit floating-point numbers. An example is 12.34.
- **double** − This is used to represent 64-bit floating-point numbers which are longer decimal number representations which may be required at times. An example is 12.3456565.
- **char** − This defines a single character literal. An example is ‘a’.
- **Boolean** − This represents a Boolean value which can either be true or false.
- **String** − These are text literals that are represented in **the form** of a chain of characters. For example “Hello World”.

Groovy also allows for additional types of variables such as arrays, structures, and classes which we will see in the subsequent chapters.

## Variable Declarations

A variable declaration tells the compiler where and how much to create the storage for the variable.

Following is an example of variable declaration

```
class Example {
   static void main(String[] args) {
      // x is defined as a variable
      String x = "Hello";

      // The value of the variable is printed to the console
      println(x);
   }
}
```

When we run the above program, we will get the following result −

```
Hello
```

## Naming Variables

The name of a variable can be composed of letters, digits, and the underscore character. It must begin with either a letter or an underscore. Upper and lowercase letters are distinct because Groovy, just like Java is a case-sensitive programming language.

```
class Example {
   static void main(String[] args) {
      // Defining a variable in lowercase
      int x = 5;

      // Defining a variable in uppercase
      int X = 6;

      // Defining a variable with the underscore in it's name
      def _Name = "Joe";

      println(x);
      println(X);
      println(_Name);
   }
}
```

When we run the above program, we will get the following result −

```
5
6
Joe
```

We can see that **x** and **X** are two different variables because of case sensitivity and in the third case, we can see that \_Name begins with an underscore.

## Printing Variables

You can print the current value of a variable with the println function. The following example shows how this can be achieved.

```
class Example {
   static void main(String[] args) {
      //Initializing 2 variables
      int x = 5;
      int X = 6;

      //Printing the value of the variables to the console
      println("The value of x is " + x + "The value of X is " + X);
   }
}
```

When we run the above program, we will get the following result −

```
The value of x is 5 The value of X is 6
```
