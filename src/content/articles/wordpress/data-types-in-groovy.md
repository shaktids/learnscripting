---
title: "Data Types in Groovy"
description: "In any programming language, you need to use various variables to store various types of information. Variables are nothing but reserved memory locations…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2020-03-27T03:47:11Z
legacy: true
wpId: 1973
---

In any programming language, you need to use various variables to store various types of information. Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory to store the value associated with the variable.

You may like to store information on various data types like string, character, wide character, integer, floating-point, Boolean, etc. Based on the data type of a variable, the operating system allocates memory and decides what can be stored in the reserved memory.

## Built-in Data Types

Groovy offers a wide variety of built-in data types. Following is a list of data types which are defined in Groovy −

- **byte** − This is used to represent a byte value. An example is 2.
- **short** − This is used to represent a short number. An example is 10.
- **int** − This is used to represent whole numbers. An example is 1234.
- **long** − This is used to represent a long number. An example is 10000090.
- **float** − This is used to represent 32-bit floating-point numbers. An example is 12.34.
- double − This is used to represent 64-bit floating-point numbers which are longer decimal number representations which may be required at times. An example is 12.3456565.
- char − This defines a single character literal. An example is ‘a’.
- Boolean − This represents a Boolean value which can either be true or false.
- String − These are text literals that are represented in the form of a chain of characters. For example “Hello World”.

## Bound values

The following table shows the maximum allowed values for the numerical and decimal literals.

|  |  |
| --- | --- |
| byte | -128 to 127 |
| short | -32,768 to 32,767 |
| int | -2,147,483,648 to 2,147,483,647 |
| long | -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807 |
| float | 1.40129846432481707e-45 to 3.40282346638528860e+38 |
| double | 4.94065645841246544e-324d to 1.79769313486231570e+308d |

## Class Numeric

Types In addition to the primitive types, the following object types (sometimes referred to as wrapper types) are allowed −

- java.lang.Byte
- java.lang.Short
- java.lang.Integer
- java.lang.Long
- java.lang.Float
- java.lang.Double

In addition, the following classes can be used for supporting arbitrary precision arithmetic −

| Name | Description | Example |
| --- | --- | --- |
| java.math.BigInteger | Immutable arbitrary-precision signed integral numbers | 30g |
| java.math.BigDecimal | Immutable arbitrary-precision signed decimal numbers | 3.5g |

The following code example showcases how the different built-in data types can be used

```
class Example {
   static void main(String[] args) {
      //Example of a int datatype
      int x = 5;

      //Example of a long datatype
      long y = 100L;

      //Example of a floating point datatype
      float a = 10.56f;

      //Example of a double datatype
      double b = 10.5e40;

      //Example of a BigInteger datatype
      BigInteger bi = 30g;

      //Example of a BigDecimal datatype
      BigDecimal bd = 3.5g;

      println(x);
      println(y);
      println(a);
      println(b);
      println(bi);
      println(bd);
   }
}
```

When we run the above program, we will get the following result −

```
5
100
10.56
1.05E41
30
3.5
```
