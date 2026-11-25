---
title: "Mathematical Expressions in shell Scripting"
description: "In shell scripting, mathematical expressions can be evaluated using the expr command or the $((...)) notation. The expr command is used to evaluate…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2023-01-15T06:04:55Z
legacy: true
wpId: 3482
---

In shell scripting, mathematical expressions can be evaluated using the `expr` command or the `$((...))` notation.

The `expr` command is used to evaluate mathematical expressions and return the result. The expression must be enclosed in quotes and can include operators such as +, -, \*, /, and % for addition, subtraction, multiplication, division, and modulus, respectively. For example:

```bash
result=$(expr 2 + 2)
echo "The result is $result"
```

Alternatively, you can use the `$((...))` notation to evaluate mathematical expressions. This notation is more concise and easier to read than the `expr` command. For example:

```bash
result=$((2 + 2))
echo "The result is $result"
```

You can also use the `let` command:

```bash
Copy codelet result=2+2
echo "The result is $result"
```

You can also use the double paranthesis for more complex mathematical expressions. For example:

```bash
result=$(( (2 + 2) * (3 - 1) / 2 ))
echo "The result is $result"
```

You can also use the more advanced command like awk or bc for more complex mathematical operations.

Keep in mind that the `expr` command and the `$((...))` notation can only handle integers and not floating point numbers, if you need to deal with floating point numbers then you can use commands like `bc` or `awk` for more complex mathematical operations.
