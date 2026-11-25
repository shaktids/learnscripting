---
title: "Fizz Buzz Implementation Part 1"
description: "Fizz Buzz is a very simple programming task, asked in software developer job interviews. A typical round of Fizz Buzz can be: Write a program that prints…"
lang: other
categories: ["Questions"]
author: "Shakti Das"
pubDate: 2021-01-18T11:39:06Z
legacy: true
wpId: 2121
---

Fizz Buzz is a very simple programming task, asked in software developer job interviews.

**A typical round of Fizz Buzz can be:**
Write a program that prints the numbers from 1 to 100 and for multiples of ‘3’ print “Fizz” instead of the number and for the multiples of ‘5’ print “Buzz”.

```
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26,
Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...
```

[Recommended: Please try your approach on ***{IDE}*** first, before moving on to the solution.](https://ide.geeksforgeeks.org/)

## C++

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `// CPP program to print Fizz Buzz``#include <stdio.h>` `int` `main(``void``)``{``int` `i;``for` `(i=1; i<=100; i++)``{``// number divisible by 3 and 5 will``// always be divisible by 15, print` `// 'FizzBuzz' in place of the number``if` `(i%15 == 0)` `printf` `(``"FizzBuzz\t"``);`  `// number divisible by 3? print 'Fizz'``// in place of the number``else` `if` `((i%3) == 0)` `printf``(``"Fizz\t"``);`  `// number divisible by 5, print 'Buzz'` `// in place of the number``else` `if` `((i%5) == 0)` `printf``(``"Buzz\t"``);`  `else` `// print the number` `printf``(``"%d\t"``, i);`  `}` `return` `0;``}` |

## C++ Using STL

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `// CPP program to print Fizz Buzz``#include <iostream>``#include <algorithm>``#include <vector>` `int` `main()``{``// dynamic array(range) of size 100 of int type``std :: vector<``int``> range(100);`  `// 'iota' to fill the vector in increasing manner``std :: iota(range.begin(), range.end(), 1);`  `// initializing dynamic array of string type``std :: vector<std::string> values;`  `// resize the vector(values) as that of vector(range)` `values.resize(range.size());`  `//'auto' to deduce the type of the variable` `auto` `fizzbuzz = [](``int` `i) -> std::string` `{``// number divisible by 15(will also be` `// divisible by both 3 and 5), print 'FizzBuzz'``if` `((i%15) == 0)``return` `"FizzBuzz"``;` `// number divisible by 5, print 'Buzz'``if` `((i%5) == 0)``return` `"Buzz"``;` `// number divisible by 3, print 'Fizz'``if` `((i%3) == 0)``return` `"Fizz"``;` `// to print other numbers``return` `std::to_string(i);``};` `// Operation to each of the elements in the` `// range [begin(), end()) and stores the` `// value returned by each operation in the` `// range that begins at values.begin().``std :: transform(range.begin(), range.end(),` `values.begin(), fizzbuzz);` `for` `(``auto``& str: values)` `std::cout << str << std::endl;` `return` `0;` `}` |

## Java

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `// Java program to print Fizz Buzz``import` `java.util.*;``class` `FizzBuzz``{``public` `static` `void` `main(String args[])``{` `int` `n =` `100``;` `// loop for 100 times``for` `(``int` `i=``1``; i<=n; i++)` `{``//number divisible by 15(divisible by``// both 3 & 5), print 'FizzBuzz' in``// place of the number``if` `(i%``15``==``0``)` `System.out.print(``"FizzBuzz"``+``" "``);` `// number divisible by 5, print 'Buzz'` `// in place of the number``else` `if` `(i%``5``==``0``)` `System.out.print(``"Buzz"``+``" "``);`  `// number divisible by 3, print 'Fizz'` `// in place of the number``else` `if` `(i%``3``==``0``)` `System.out.print(``"Fizz"``+``" "``);` `else` `// print the numbers``System.out.print(i+``" "``);` `}``}``}` |

## Python

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `# Python program to print Fizz Buzz` `# Loop for 100 times i.e. range``for` `fizzbuzz` `in` `range``(``100``):`  `# Number divisible by 15,(divisible` `# by both 3 & 5), print 'FizzBuzz'` `# in place of the number``if` `fizzbuzz` `%` `15` `=``=` `0``:` `print``(``"FizzBuzz"``)` `continue` `# Number divisible by 3, print 'Fizz'``# in place of the number``elif` `fizzbuzz` `%` `3` `=``=` `0``:` `print``(``"Fizz"``)` `continue` `# Number divisible by 5,` `# print 'Buzz' in``# place of the number``elif` `fizzbuzz` `%` `5` `=``=` `0``:` `print``(``"Buzz"``)` `continue` `# Print numbers``print``(fizzbuzz)` |

## C#

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `// C# program to print Fizz Buzz``using` `System;` `class` `GFG{` `// Driver Code``public` `static` `void` `Main()``{` `int` `n = 100;` `// Loop for 100 times``for``(``int` `i = 1; i <= n; i++)` `{` `// Number divisible by 15(``// divisible by both 3 & 5),` `// print 'FizzBuzz' in place``// of the number``if` `(i % 15 == 0)` `Console.Write(``"FizzBuzz"` `+` `" "``);`  `// Number divisible by 3,` `// print 'Fizz' in place` `// of the number``else` `if` `(i % 3 == 0)` `Console.Write(``"Fizz"` `+` `" "``);`  `// Number divisible by` `// 5, print 'Buzz'``// in place of the number``else` `if` `(i % 5 == 0)` `Console.Write(``"Buzz"` `+` `" "``);`  `// Print the numbers` `else``Console.Write(i +` `" "``);` `}``}``}` `// This code is contributed``// by shiv_bhakt.` |

## PHP

*filter\_none*

*edit*

*play\_arrow*

*brightness\_4*

|  |
| --- |
| `<?php``// PHP program to print Fizz Buzz` `$i``;``for` `(``$i` `= 1;` `$i` `<= 100;` `$i``++)``{``// number divisible by 3 and``// 5 will always be divisible` `// by 15, print 'FizzBuzz' in``// place of the number``if` `(``$i` `% 15 == 0)` `echo` `"FizzBuzz"` `.` `"  "``;`  `// number divisible by 3? print` `// 'Fizz' in place of the number``else` `if` `((``$i` `% 3) == 0)` `echo` `"Fizz"` `.` `"  "``;`  `// number divisible by 5, print` `// 'Buzz' in place of the number``else` `if` `((``$i` `% 5) == 0)` `echo` `"Buzz"` `.` `"  "``;`  `else` `// print the number` `echo` `$i``,``"  "` `;` `}` `// This code is contributed by m_kit``?>` |
