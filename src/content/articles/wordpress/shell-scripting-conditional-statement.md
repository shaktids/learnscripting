---
title: "Shell Scripting Conditional Statement"
description: "Conditional Statements: There are total 5 conditional statements available in the bash programming,Which can be implemented in the different situation in…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2019-08-11T03:51:37Z
legacy: true
wpId: 1744
---

**Conditional Statements:** There are total 5 conditional statements available in the bash programming,Which can be implemented in the different situation in the bash/shell programming.

1. if statement
2. if-else statement
3. if..elif..else..fi statement (Else If ladder)
4. if..then..else..if..then..fi..fi..(Nested if)
5. switch statement

## if statement
If statement is the simplest statement in the series.Where it is used to compare the two variable. This block will process if specified condition is true.
***Syntax:***

```bash
if [ expression ]
then
   statement
fi
```

## if-else statement
If specified condition is not true in if part then else part will be execute.This can be helpful when we have 3 variables and need to compare between
***Syntax***

```bash
if [ expression ]
then
   statement1
else
   statement2
fi
```

## if..elif..else..fi statement (Else If ladder)
We can use to compare more than 3 variables by using this block.To use multiple conditions in one if-else block, then elif keyword is used in shell. If expression1 is true then it executes statement 1 and 2, and this process continues. If none of the condition is true then it processes else part.
***Syntax***

```bash
if [ expression1 ]
then
   statement1
   statement2
   .
elif [ expression2 ]
then
   statement3
   statement4
   .
else
   statement5
fi
```

## if..then..else..if..then..fi..fi..(Nested if)
Generally Nested block is used for comparison of multiple nested conditions. if-else block can be used when, one condition is satisfies then it again checks another condition. In the syntax, if expression1 is false then it processes else part, and again expression2 will be check.
***Syntax:***

```bash
if [ expression1 ]
then
   statement1
   statement2
   .
else
   if [ expression2 ]
   then
      statement3
      .
   fi
fi
```

## switch statement
case statement works as a switch statement if specified value match with the pattern then it will execute a block of that particular pattern
When a match is found all of the associated statements until the double semicolon (;;) is executed.
A case will be terminated when the last command is executed.
If there is no match, the exit status of the case is zero.

***Syntax:***

```bash
case  in
   Pattern 1) Statement 1;;
   Pattern n) Statement n;;
esac
```
