---
title: "How to write If Else Statement In Python"
description: "An if else statement is a control flow statement that allows you to execute different blocks of code based on a boolean condition. In Python, the if else…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2022-12-27T12:27:47Z
legacy: true
wpId: 966
---

An if-else statement is a control flow statement that allows you to execute different blocks of code based on a boolean condition. In Python, the if-else statement is written using the following syntax:

```python
if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false
```

Here, the `condition` is a boolean expression that is evaluated to determine whether the code in the `if` block should be executed or not. If the condition is `True`, the code in the `if` block is executed; if the condition is `False`, the code in the `else` block is executed.

Here is an example of an if-else statement in Python:

```python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

In this example, the condition `x > 5` is `True`, so the code in the `if` block is executed and the message "x is greater than 5" is printed to the console.

You can also use multiple conditions and nested if-else statements to create more complex control flow. For example:

```python
x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
```

In this example, the condition `x > y` is `False`, so the code in the `elif` the block is executed and the message "x is less than y" is printed to the console.

That's it! You now know how to write an if-else statement in Python. Remember to always use proper indentation to define the blocks of code that are executed based on the conditions.
