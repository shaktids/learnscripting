---
title: "Python List & Dictionary  Comprehension"
description: "List Comprehension List comprehension is a smart way to define and create a list in python in a single line. We can create lists just like mathematical…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2022-12-27T06:39:46Z
legacy: true
wpId: 3361
---

### List Comprehension

List comprehension is a smart way to define and create a list in python in a single line. We can create lists just like mathematical statements and in one line only. The syntax of list comprehension is easier to grasp.

A list comprehension generally consists of these parts :

***[ ***value*** for (value) in iterable condition ]***

1. Output expression,
2. Input sequence,
3. A variable representing a member of the input sequence and
4. An optional predicate part.

Let us take an example.

```python
squares = [x**2 for x in range(12)]
print(squares)
```

```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
```

From this above, we are calculating the square of all the numbers from 0-11 as this is a range function.

Let's add the last optional condition to this statement. We are doing a filter if the number is even we will take it.

```python
squares = [x**2 for x in range(12) if x%2==0]
print(squares)
```

```python
[0, 4, 16, 36, 64, 100]
```

### Dictionary Comprehension

Like List Comprehension, Python allows dictionary comprehension. We can create dictionaries using simple expressions. A dictionary comprehension takes the form we give { } brackets.

***{key: value for (key, value) in iterable}***

Lets take the example of the list comprehension

```python
squares = { x**2:x**2%2==0  for x in range(12) }
print(squares)
```

```python
{0: True, 1: False, 4: True, 9: False, 16: True, 25: False, 36: True, 49: False, 64: True, 81: False, 100: True, 121: False}
```
