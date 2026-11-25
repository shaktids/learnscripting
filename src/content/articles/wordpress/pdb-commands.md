---
title: "Pdb Commands"
description: "Python is a popular programming language used for developing web applications, scientific computing, artificial intelligence, and machine learning. While…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2023-04-24T09:48:36Z
legacy: true
wpId: 3579
---

Python is a popular programming language used for developing web applications, scientific computing, artificial intelligence, and machine learning. While coding in Python, you may face situations where you need to debug your code to find errors or issues in it. One of the most popular ways to debug Python code is by using the Python Debugger (PDB).

Python Debugger (PDB) is a command-line tool allowing you to interactively debug your Python code. It lets you set breakpoints, step through the code line by line, and inspect variables and expressions at runtime. In this blog post, we will discuss some of the most useful Python PDB commands that you can use to debug your Python code.

1. pdb.set\_trace()

The pdb.set\_trace() command sets a breakpoint in your Python code. When this command is executed, the Python debugger will stop execution at that point, and you can start debugging your code. This command is typically used in your code at the point where you want to start debugging.

Example:

```python
import pdb

def sum_numbers(a, b):
    pdb.set_trace()
    return a + b

print(sum_numbers(2, 3))
```

2. n (next)

The n (next) command is used to execute the current line of code and move to the next line. This command is typically used to step through your code line by line.

Example:

```python
(Pdb) n
> /path/to/your/code.py(4)sum_numbers()
-> return a + b
(Pdb)
```

3. s (step)

The s (step) command is used to step into a function call. If the current line of code contains a function call, the s command will execute the first line of the function and stop at the next line. This command is typically used to step into a function to debug it.

Example:

```python
(Pdb) s
--Call--
> /path/to/your/code.py(4)sum_numbers()
-> return a + b
(Pdb)
```

4. c (continue)

The c (continue) command is used to continue the execution of the Python code until the next breakpoint is reached. This command is typically used to skip over sections of code that are not relevant to the current debugging session.

Example:

```python
(Pdb) c
> /path/to/your/code.py(8)<module>()
-> print(sum_numbers(2, 3))
(Pdb)
```

5. l (list)

The l (list) command is used to display the current section of code being executed. This command is typically used to get an overview of the code being executed at the current point.

Example:

```python
(Pdb) l
  3     def sum_numbers(a, b):
  4  ->     return a + b
  5
  6     pdb.set_trace()
  7
  8  -> print(sum_numbers(2, 3))
```

6. p (print)

The p (print) command is used to display the value of a variable or expression at the current point in the code. This command is typically used to inspect the values of variables and expressions during runtime.

Example:

```python
(Pdb) p a
2
(Pdb) p b
3
(Pdb) p a + b
5
```

7. q (quit)

The q (quit) command is used to terminate the Python debugger and stop debugging your code.

Example:

```python
 (Pdb) q
```

|  |  |
| --- | --- |
| Startup and Help |  |
| python-mpdb.py[args] | begin the debugger |
| help[command] | View a list of commands, or view help for a specific command |
| within a Python file: import pdb … pdb.set\_trace() | Begin the debugger at this line when the file is run normally |
| l(ist) | list 11 lines surrounding the current line |
| w(here) | display the file and line number of the current line |
| n(ext) | execute the current line |
| s(tep) | step into functions called at the current line |
| r(eturn) | execute until the current function’s return is encountered |
| b[#] | create a breakpoint at line [#] |
| b | list breakpoints and their indices |
| c(ontinue) | execute until a breakpoint is encountered |
| clear[#] | clear breakpoint of index [#] |
| p&lt;name> | print value of the variable&lt;name> |
| !&lt;expr> | execute the expression&lt;expr> |
| run[args] | restart the debugger with sys.argv arguments [args] |
| q(uit) | exit the debugger |

In conclusion, the Python Debugger (PDB) is a powerful tool allowing you to interactively debug your Python code. By using the PDB commands discussed in this blog post, you can set breakpoints, step through your
