---
title: "Python Operator – Types of Operators in Python"
description: "Being a high level language where it can fit into most of the system it has the capability to handle the all data types.To handle this data the operators…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2019-02-15T16:05:34Z
legacy: true
wpId: 1496
---

Being a high level language where it can fit into most of the system it has the capability to handle the all data types.To handle this data the operators are categorized into below 7 categories .

- Python Arithmetic Operator
- Python Relational Operator
- Python Assignment Operator
- Python Logical Operator
- Python Membership Operator
- Python Identity Operator
- Python Bitwise Operator

### Python Arithmetic Operator

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication etc.

| Operator | Meaning | Example |
| --- | --- | --- |
| + | Add two operands or unary plus | x + y +2 |
| - | Subtract right operand from the left or unary minus | x - y -2 |
| \* | Multiply two operands | x \* y |
| / | Divide left operand by the right one (always results into float) | x / y |
| % | Modulus - remainder of the division of left operand by the right | x % y (remainder of x/y) |
| // | Floor division - division that results into whole number adjusted to the left in the number line | x // y |
| \*\* | Exponent - left operand raised to the power of right | x\*\*y (x to the power y) |

### Python Relational Operator

Relational operators are used to compare values. It either returns `True` or `False` according to the condition.

| Operator | Meaning | Example |
| --- | --- | --- |
| > | Greater that - True if left operand is greater than the right | x > y |
| &lt; | Less that - True if left operand is less than the right | x &lt; y |
| == | Equal to - True if both operands are equal | x == y |
| != | Not equal to - True if operands are not equal | x != y |
| >= | Greater than or equal to - True if left operand is greater than or equal to the right | x >= y |
| &lt;= | Less than or equal to - True if left operand is less than or equal to the right | x &lt;= y |

### Python Assignment Operator

Assignment operators are used in Python to assign values to variables.

`a = 5` is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

There are various compound operators in Python like `a += 5` that adds to the variable and later assigns the same. It is equivalent to `a = a + 5`.

| Operator | Example | Equivatent to |
| --- | --- | --- |
| = | x = 5 | x = 5 |
| += | x += 5 | x = x + 5 |
| -= | x -= 5 | x = x - 5 |
| \*= | x \*= 5 | x = x \* 5 |
| /= | x /= 5 | x = x / 5 |
| %= | x %= 5 | x = x % 5 |
| //= | x //= 5 | x = x // 5 |
| \*\*= | x \*\*= 5 | x = x \*\* 5 |
| &= | x &= 5 | x = x & 5 |
| |= | x |= 5 | x = x | 5 |
| ^= | x ^= 5 | x = x ^ 5 |
| >>= | x >>= 5 | x = x >> 5 |
| &lt;&lt;= | x &lt;&lt;= 5 | x = x &lt;&lt; 5 |

---

## Python Logical Operator

Logical operators are the `and`, `or`, `not` operators.

| Operator | Meaning | Example |
| --- | --- | --- |
| and | True if both the operands are true | x and y |
| or | True if either of the operands is true | x or y |
| not | True if operand is false (complements the operand) | not x |

### Python Membership Operator

`in` and `not in` are the membership operators in Python. They are used to test whether a value or variable is found in a sequence ([string](https://www.programiz.com/python-programming/string), [list](https://www.programiz.com/python-programming/list), [tuple](https://www.programiz.com/python-programming/tuple), [set](https://www.programiz.com/python-programming/set) and [dictionary](https://www.programiz.com/python-programming/dictionary)).

In a dictionary we can only test for presence of key, not the value.

| Operator | Meaning | Example |
| --- | --- | --- |
| in | True if value/variable is found in the sequence | 5 in x |
| not in | True if value/variable is not found in the sequence | 5 not in x |

### Python Identity Operator

`is` and `is not` are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

| Operator | Meaning | Example |
| --- | --- | --- |
| is | True if the operands are identical (refer to the same object) | x is True |
| is not | True if the operands are not identical (do not refer to the same object) | x is not True |

### Python Bitwise Operator

Bitwise operators act on operands as if they were string of binary digits. It operates bit by bit, hence the name.

For example, 2 is `10` in binary and 7 is `111`.

**In the table below:** Let x = 10 (`0000 1010` in binary) and y = 4 (`0000 0100` in binary)

| Operator | Meaning | Example |
| --- | --- | --- |
| & | Bitwise AND | x& y = 0 (`0000 0000`) |
| | | Bitwise OR | x | y = 14 (`0000 1110`) |
| ~ | Bitwise NOT | ~x = -11 (`1111 0101`) |
| ^ | Bitwise XOR | x ^ y = 14 (`0000 1110`) |
| >> | Bitwise right shift | x>> 2 = 2 (`0000 0010`) |
| &lt;&lt; | Bitwise left shift | x&lt;&lt; 2 = 40 (`0010 1000`) |

---
