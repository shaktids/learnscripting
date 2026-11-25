---
title: "Tricky C programs Question & Answers Part 1"
description: "We may come across various tricky programs in our day to day life. May be in technical interviews, coding tests, or in C/C++ classrooms. Here is a list of…"
lang: other
categories: ["C", "Questions"]
author: "Shakti Das"
pubDate: 2021-01-18T05:43:22
legacy: true
wpId: 2101
draft: true
---

We may come across various tricky programs in our day to day life. May be in technical interviews, coding tests, or in C/C++ classrooms.
Here is a list of such programs :-

1. Print text within double quotes (” “).
   This may seem easy but beginners may get puzzled while printing text within double-quotes.*filter\_noneeditplay\_arrowbrightness\_4*`// CPP program to print double quotes #include<iostream>`  `int` `main() { std::cout << "\"geeksforgeeks\""; return` `0; }` Output:"geeksforgeeks"
2. To check if two numbers are equal without using arithmetic operators or comparison operators.
   The simplest solution for this is using Bitwise XOR operator (^). We know that, for two equal numbers XOR operator returns 0. We will use this trick to solve this problem.*filter\_noneeditplay\_arrowbrightness\_4*`// C program to check if two numbers are equal  // without using arithmetic operators or  // comparison operators #include<stdio.h>`  `int` `main() { int` `x = 10; int` `y = 10; if` `( !(x ^ y) ) printf(" x is equal to y "); else` `printf(" x is not equal to y "); return` `0; }` Output:

   x is equal to y
3. Print all natural numbers upto N without using semi-colon.
   We use the idea of recursively calling main function.*filter\_noneeditplay\_arrowbrightness\_4*`// CPP program to print all natural numbers upto  // N without using semi-colon #include<iostream>`  `using` `namespace` `std; int` `N = 10;`  `int` `main() { static` `int` `x = 1; if` `(cout << x << " "` `&& x++ < N && main()) { } return` `0; }` Output:1 2 3 4 5 6 7 8 9 10
4. To Swap the values of two variables without using any extra variable.*filter\_noneeditplay\_arrowbrightness\_4*`// C++ program to check if two numbers are equal  #include<iostream>`  `int` `main() { int` `x = 10; int` `y = 70;`  `x = x + y; y = x - y; x = x - y;`  `cout << "X : "` `<< x << "\n"; cout << "Y : "` `<< y << "\n";`  `return` `0; }` Output:X : 70 Y : 10
5. Program to find Maximum and minimum of two numbers without using any loop or condition.
   The simplest trick is-*filter\_noneeditplay\_arrowbrightness\_4*`// CPP program to find maximum and minimum of // two numbers without using loop and any // condition. #include<bits/stdc++.h>`  `int` `main () { int` `a = 15, b = 20; printf("max = %d\n", ((a + b) + abs(a - b)) / 2); printf("min = %d", ((a + b) - abs(a - b)) / 2); return` `0; }` Output:max = 20 min = 15
6. Print the maximum value of an unsigned int using One’s Compliment (~) Operator in C.
   Here is a trick to find maximum value of an unsigned int using one’s compliment operator:*filter\_noneeditplay\_arrowbrightness\_4*`// C program to print maximum value of // unsigned int. #include<stdio.h>`  `int` `main() { unsigned int` `max; max = 0; max = ~max; printf("Max value : %u ",  max); return` `0; }`
7. To find sum of two integers without using ‘+’ operator.
   This is a very easy mathematics trick.
   We know that a + b = – (-a-b). So this will work as a trick for us.*filter\_noneeditplay\_arrowbrightness\_4*`// CPP program to print sum of two integers // withtout + #include<iostream>`  `using` `namespace` `std; int` `main() { int` `a = 5; int` `b = 5; int` `sum = -( -a-b ); cout << sum; return` `0; }` Output:10
8. Program to verifies the condition inside if block.*filter\_noneeditplay\_arrowbrightness\_4*`// CPP program to verifies the condition inside if block // It just verifies the condition inside if block,  // i.e., cout << "geeks" which returns a non-zero value,  // !(non-zero value) is false, hence it executes else // Hence technically it only executes else block  #include<iostream>`  `using` `namespace` `std; int` `main() { if` `(!(cout << "geeks"))  cout <<" geeks ";  elsecout << "forgeeks ";`  `return` `0; }` Output:geeksforgeeks
9. Program to divide an integer by 4 without using ‘/’ operator.
   One of the most efficient way to divide an integer by 4 is to use right shift operator (“>>”).*filter\_noneeditplay\_arrowbrightness\_4*`// CPP program to divide a number by 4 // without using '/' #include<iostream>`  `using` `namespace` `std; int` `main() { int` `n = 4; n = n >> 2; cout << n; return` `0; }` Output:1
10. Program to check endianness of the computer.*filter\_noneeditplay\_arrowbrightness\_4*`// C program to find if machine is little // endian or big endian. #include <stdio.h>`  `int` `main()  { unsigned int` `n = 1; char` `*c = (char*)&n; if` `(*c)     printf("LITTLE ENDIAN"); elseprintf("BIG ENDIAN"); return` `0; }`
