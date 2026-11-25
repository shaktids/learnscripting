---
title: "Looping in Python"
description: "Single Statement Suites If the suite of an if clause consists only of a single line, it may go on the same line as the header statement. Here is an…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2018-04-29T15:38:19Z
legacy: true
wpId: 94
---

## Single Statement Suites

If the suite of an **if** clause consists only of a single line, it may go on the same line as the header statement.

Here is an example of a **one-line if** clause −

Live Demo

```
#!/usr/bin/python

var = 100
if ( var == 100 ) : print "Value of expression is 100"
print "Good bye!"
```

When the above code is executed, it produces the following result −

```
Value of expression is 100
Good bye!
```

In general, statements are executed sequentially − The first statement in a function is executed first, followed by the second, and so on. There may be a situation when you need to execute a block of code several number of times.

Programming languages provide various control structures that allow more complicated execution paths.

A loop statement allows us to execute a statement or group of statements multiple times. The following diagram illustrates a loop statement −

![Loop Architecture](/images/wp/loop-architecture-18b6f7a4.jpg)

Python programming language provides the following types of loops to handle looping requirements.

|
 S.No. |
 Loop Type & Description |

|
 1 |
 while loopRepeats a statement or group of statements while a given condition is TRUE. It tests the condition before executing the loop body. |

|
 2 |
 for loopExecutes a sequence of statements multiple times and abbreviates the code that manages the loop variable. |

|
 3 |
 nested loopsYou can use one or more loop inside any another while, or for loop. |

## Loop Control Statements

The Loop control statements change the execution from its normal sequence. When the execution leaves a scope, all automatic objects that were created in that scope are destroyed.

Python supports the following control statements.

|
 S.No. |
 Control Statement & Description |

|
 1 |
 break statementTerminates the loop statement and transfers execution to the statement immediately following the loop. |

|
 2 |
 continue statementCauses the loop to skip the remainder of its body and immediately retest its condition prior to reiterating. |

|
 3 |
 pass statementThe pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute. |

Let us go through the loop control statements briefly.

## Iterator and Generator

**Iterator** is an object which allows a programmer to traverse through all the elements of a collection, regardless of its specific implementation. In Python, an iterator object implements two methods, **iter()** and **next()**.

String, List or Tuple objects can be used to create an Iterator.

```
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it)) #prints next available element in iterator
Iterator object can be traversed using regular for statement
!usr/bin/python3
for x in it:
   print (x, end=" ")
or using next() function
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit() #you have to import sys module for this
```

A **generator** is a function that produces or yields a sequence of values using yield method.

When a generator function is called, it returns a generator object without even beginning execution of the function. When the next() method is called for the first time, the function starts executing until it reaches the yield statement, which returns the yielded value. The yield keeps track i.e. remembers the last execution and the second next() call continues from previous value.

### Example

The following example defines a generator, which generates an iterator for all the Fibonacci numbers.

```
!usr/bin/python3
import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
```
