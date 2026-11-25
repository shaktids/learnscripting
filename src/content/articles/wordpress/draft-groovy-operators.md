---
title: "Groovy - Operators"
description: "An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations. Groovy has the following types of operators −…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2020-02-27T12:49:03
legacy: true
wpId: 1979
draft: true
---

An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations.

Groovy has the following types of operators −

- Arithmetic operators
- Relational operators
- Logical operators
- Bitwise operators
- Assignment operators

## Arithmetic Operators

The Groovy language supports the normal Arithmetic operators as any the language. Following are the Arithmetic operators available in Groovy −

| Operator | Description | Example |
| --- | --- | --- |
| + | Addition of two operands | 1 + 2 will give 3 |
| − | Subtracts second operand from the first | 2 − 1 will give 1 |
| \* | Multiplication of both operands | 2 \* 2 will give 4 |
| / | Division of numerator by denominator | 3 / 2 will give 1.5 |
| % | Modulus Operator and remainder of after an integer/float division | 3 % 2 will give 1 |
| ++ | Incremental operators used to increment the value of an operand by 1 | int x = 5;x++;x will give 6 |
| -- | Incremental operators used to decrement the value of an operand by 1 | int x = 5;x--;x will give 4 |

## Relational operators

Relational operators allow of the comparison of objects. Following are the relational operators available in Groovy −

| Operator | Description | Example |
| --- | --- | --- |
| == | Tests the equality between two objects | 2 == 2 will give true |
| != | Tests the difference between two objects | 3 != 2 will give true |
| &lt; | Checks to see if the left objects is less than the right operand. | 2 &lt; 3 will give true |
| &lt;= | Checks to see if the left objects is less than or equal to the right operand. | 2 &lt;= 3 will give true |
| > | Checks to see if the left objects is greater than the right operand. | 3 > 2 will give true |
| >= | Checks to see if the left objects is greater than or equal to the right operand. | 3 >= 2 will give true |

## Logical Operators

Logical operators are used to evaluate Boolean expressions. Following are the logical operators available in Groovy −

| Operator | Description | Example |
| --- | --- | --- |
| && | This is the logical “and” operator | true && true will give true |
| || | This is the logical “or” operator | true || true will give true |
| ! | This is the logical “not” operator | !false will give true |

## Bitwise Operators

Groovy provides four bitwise operators. Following are the bitwise operators available in Groovy −

| Sr.No | Operator & Description |
| --- | --- |
| 1 | **&**This is the bitwise “and” operator |
| 2 | **|**This is the bitwise “or” operator |
| 3 | **^**This is the bitwise “xor” or Exclusive or operator |
| 4 | **~**This is the bitwise negation operator |

Here is the truth table showcasing these operators.

| p | q | p & q | p | q | p ^ q |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 | 1 |

## Assignment operators

The Groovy language also provides assignment operators. Following are the assignment operators available in Groovy −

| Operator | Description | Example |
| --- | --- | --- |
| += | This adds right operand to the left operand and assigns the result to left operand. | def A = 5A+=3Output will be 8 |
| -= | This subtracts right operand from the left operand and assigns the result to left operand | def A = 5A-=3Output will be 2 |
| \*= | This multiplies right operand with the left operand and assigns the result to left operand | def A = 5A\*=3Output will be 15 |
| /= | This divides left operand with the right operand and assigns the result to left operand | def A = 6A/=3Output will be 2 |
| %= | This takes modulus using two operands and assigns the result to left operand | def A = 5A%=3Output will be 2 |

## Range Operators

Groovy supports the concept of ranges and provides a notation of range operators with the help of the .. notation. A simple example of the range operator is given below.

```
def range = 0..5
```

This just defines a simple range of integers, stored into a local variable called range with a lower bound of 0 and an upper bound of 5.

The following code snippet shows how the various operators can be used.

```
class Example {
   static void main(String[] args) {
      def range = 5..10;
      println(range);
      println(range.get(2));
   }
}
```

When we run the above program, we will get the following result −

From the **println** statement, you can see that the entire range of numbers which are defined in the range statement are displayed.

The get statement is used to get an object from the range defined which takes in an index value as the parameter.

```
[5, 6, 7, 8, 9, 10]
7
```

## Operator Precedence

The following table lists all groovy operators in order of precedence.

| Sr.No | Operators & Names |
| --- | --- |
| 1 | **++ -- + -**pre increment/decrement, unary plus, unary minus |
| 2 | **\* / %**multiply, div, modulo |
| 3 | **+ -**addition, subtraction |
| 4 | **== != &lt;=>**equals, not equals, compare to |
| 5 | **&**binary/bitwise and |
| 6 | **^**binary/bitwise xor |
| 7 | **|**binary/bitwise or |
| 8 | **&&**logical and |
| 9 | **||**logical or |
| 10 | **= \*\*= \*= /= %= += -= &lt;&lt;= >>= >>>= &= ^= |=**Various assignment operators |
