---
title: "Python Variable Declaration Rules and Syntax"
description: "Variable and Value A variable is a memory location where a programmer can store a value. Example : roll no, amount, name etc. Value is either string…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2018-04-29T13:02:18Z
legacy: true
wpId: 89
---

## Variable and Value

- A variable is a memory location where a programmer can store a value. Example : roll\_no, amount, name etc.
- Value is either string, numeric etc. Example : "Sara", 120, 25.36
- Variables are created when first assigned.
- Variables must be assigned before being referenced.
- The value stored in a variable can be accessed or updated later.
- No declaration required
- The type (string, int, float etc.) of the variable is determined by Python
- The interpreter allocates memory on the basis of the data type of a variable.

## Python Variable Name Rules

- Must begin with a letter (a - z, A - B) or underscore (\_)
- Other characters can be letters, numbers or \_
- Case Sensitive
- Can be any (reasonable) length
- There are some reserved words which you cannot use as a variable name because Python uses them for other things.

## Good Variable Name

- Choose meaningful name instead of short name. roll\_no is better than rn.
- Maintain the length of a variable name. Roll\_no\_of\_a-student is too long?
- Be consistent; roll\_no or or RollNo
- Begin a variable name with an underscore(\_) character for a special case.

### Variable assignment

We use the [assignment operator](https://www.programiz.com/python-programming/operators#arithmetic_operators "Python Assignment Operators") (=) to assign values to a variable. Any type of value can be assigned to any valid variable.

```python
a = 5
b = 3.2
c = "Hello"
```

Here, we have three assignment statements. `5` is an integer assigned to the variable a.

Similarly, `3.2` is a floating point number and `"Hello"` is a string (sequence of characters) assigned to the variables b and c respectively.

### Multiple assignments

In Python, multiple assignments can be made in a single statement as follows:

```python
a, b, c = 5, 3.2, "Hello"
```

If we want to assign the same value to multiple variables at once, we can do this as

```python
x = y = z = "same"
```

This assigns the "same" string to all the three variables.

## If  you have any further clarification on this topic please give comment bellow Python Variable Declaration Rules and Syntax
