---
title: "Shell Scripting Conditional statements"
description: "In shell scripting, conditional statements are used to perform different actions based on the outcome of a comparison or test. There are several types of…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2023-01-15T06:10:24Z
legacy: true
wpId: 3486
---

In shell scripting, conditional statements are used to perform different actions based on the outcome of a comparison or test. There are several types of conditional statements that can be used, including `if`, `if-else`, `if-elif-else`, and `case`.

1. **if statement**: The `if` statement is used to perform an action if a certain condition is true. For example:

```bash
if [ "$x" -gt "0" ]; then
    echo "x is greater than 0."
fi
```

2. **if-else statement**: The `if-else` statement is used to perform one action if a condition is true and another action if the condition is false. For example:

```bash
if [ "$x" -gt "0" ]; then
    echo "x is greater than 0."
else
    echo "x is not greater than 0."
fi
```

3. **if-elif-else statement**: The `if-elif-else` the statement is used to perform different actions based on multiple conditions. For example:

```bash
if [ "$x" -gt "0" ]; then
    echo "x is greater than 0."
elif [ "$x" -eq "0" ]; then
    echo "x is equal to 0."
else
    echo "x is less than 0."
fi
```

4. **case statement**: The `case` statement is used to perform different actions based on a single variable. For example:

```bash
case $x in
    1) echo "x is 1.";;
    2) echo "x is 2.";;
    *) echo "x is not 1 or 2.";;
esac
```

It's important to note that the test conditions used in the if, if-else, if-elif-else and case statements are enclosed in square brackets (`[]`) and not paranthesis (`()`) as used in other programming languages. Also, it's good practice to use double paranthesis (`[[ ]]`) instead of single paranthesis (`[]`) for more advanced tests, as it provides additional functionality.

It's also good practice to use quotes around variables in the test conditions to prevent errors caused by spaces or special characters in the variable's value.
