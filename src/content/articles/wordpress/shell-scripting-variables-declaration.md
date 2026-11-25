---
title: "Shell Scripting  Variables Declaration"
description: "A variable is a character or a word where we store a value. The value assigned could be a number, text, filename, device, or any other data type. A…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2019-07-02T02:51:53Z
updatedDate: 2022-10-16T02:52:17Z
legacy: true
wpId: 1644
---

A variable is a character or a word where we store a value. The value assigned could be a number, text, filename, device, or any other data type.

A variable is nothing more than a pointer to the actual data stored. The shell enables you to create, assign, and delete variables. There is some predefined convention as follows to define variables.

## Variable Names

The name of a variable can contain only letters (a to z or A to Z), numbers ( 0 to 9), or the underscore character ( \_).

Unix shell variables should have their names in UPPERCASE.

Below are examples are valid variable names −

```
_SAMPLE
RANDOM_A
V_1
VAR_2
VARIABLE_3
```

Following are the examples of invalid variable names −

```
2_TEMP  -   Starts With numeric
-VAR    -   Starts with &contains -
VARABLE1-VAR2    -   Contains -
VAR_A!  -    Contains !
```

Why a variable cannot use other characters such as **!** **\***, or **-** is that these characters have a special meaning for the shell?

The special character other than "\_" is reversed in the shell for other uses.

## Defining Variables

Variables are defined with an = sing. The left part contains the variable's name and the right leg contains the variable's value.

```
Syntax   :   variable_name=variable_value
```

For example −

```
NAME="Zara Ali"
```

The above example defines the variable NAME and assigns the value "Zara Ali" to it. Variables of this type are called **scalar variables**. A scalar variable can hold only one value at a time.

Shell enables you to store any value you want in a variable. For example −

```
VAR1="Zara Ali"
VAR2=100
```

## Accessing Values

To access the value stored in a variable, prefix its name with the dollar sign (**$**) −

For example, the following script will access the value of the defined variable NAME and print it on STDOUT

```
#!/bin/sh

NAME="Shakti Das"
echo $NAME
```

The above script will produce the following value −

```
Shakti Das
```

## Read-only Variables

Shell provides a way to mark variables as read-only by using the read-only command. After a variable is marked read-only, its value cannot be changed.

For example, the following script generates an error while trying to change the value of NAME −

```bash
#!/bin/sh NAME="Shakti Das" readonly NAME NAME="Qadiri"
```

The above script will generate the following result −

```
/bin/sh: NAME: This variable is read only.
```

## Unsetting Variables

Unsetting or deleting a variable directs the shell to remove the variable from the list of variables that it tracks. Once you unset a variable, you cannot access the stored value in the variable.

Following is the syntax to unset a defined variable using the **unset** command −

```
unset variable_name
```

The above command unsets the value of a defined variable. Here is a simple example that demonstrates how the command works −

```bash
#!/bin/sh

NAME="Shakti Das"
unset NAME
echo $NAME
```

The above example does not print anything. You cannot use the unset command to **unset** variables that are marked **read-only**.
