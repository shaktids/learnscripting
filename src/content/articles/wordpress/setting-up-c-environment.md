---
title: "Setting Up C Environment"
description: "In this chapter, we are going to learn Environment Setup using IDE in C development environment using DevC++ tool in your machine and how to compile and…"
lang: other
categories: ["C"]
author: "Shakti Das"
pubDate: 2021-09-04T07:11:37Z
legacy: true
wpId: 2984
---

In this chapter, we are going to learn Environment Setup using IDE in C development environment using DevC++ tool in your machine and how to compile and execute a C program on your own. Below topics are covered on this page.

1. What is C compiler?
2. List of C/C++ compilers for Windows Operating System
3. Steps to install DevC++ tool to compile and execute C programs
4. List of C/C++ compilers for UNIX/LINUX Operating System

**Note:**

- Nowadays, both C and C++ compilers are integrated together in same development environment.
- For example, Turbo C++, Borland C++ and DevC++ provides Integrated Development Environment with compiler for both C and C++ programming language.
- So, we can compile and execute both C and C++ programs in same Integrated Development Environment (IDE).

#### 1. WHAT IS C COMPILER?
- C Compiler is a program that converts human readable code into machine readable code. This process is called compilation.
- Human readable code is a program that consists of letters, digits and special characters that we type in program window. Machine readable code is in 0’s & 1’s

- For example, let’s assume that we type ” HELLO” in program window. We know that we have typed “HELLO” in program window.
- But, processor knows only 01001000 for letter “H”, 01000101 for letter “E”, 01001100 for letter “L”, 01001100 for letter “L”, 01001111 for letter “O”
- Because, all C programs are executed by processor which is available in CPU.
- So, entire C source code should be converted into 0’s and 1’s as processor can understand only 0’s and 1’s.
- So, compiler converts entire source code into 0’s and 1’s during compilation.
- Output produced by compiler is in the form of 0’s and 1’s which is saved in .exe file. This file is called as executable or binary file.
- This binary file is executed by processor as per logic written in source code and the output is displayed in output window.

#### 2. LIST OF C/C++ COMPILERS FOR WINDOWS:
There are so many compilers available in the market for Windows operating system. We are listing some of them here for your reference.

1. AMPC
2. CCS C Compiler
3. ch
4. clang
5. Cygwin
6. Digital mars
7. GCC compiler
8. MikroC Compiler
9. Portable C Compiler, Power C, QuickC, Ritchie C Compiler, Small-C

#### 3. STEPS TO INSTALL DEV C++****:
Dev C++ is a free C & *C++* IDE (Integrated Development Environment) for Windows and Linux.  It supports the compilation and execution of C & C++ languages. It is available with GCC compiler which is used to compile both C and C++ programs.

You can follow the below steps one by one to install Dev C++ in your local machine and you can start compiling and executing C programs.

1. Download Dev-C++ IDE from <http://www.bloodshed.net/dev/devcpp.html>

2. Click on source forge link under “Downloads -> **Dev-C++ 5.0 beta 9.2 (4.9.9.2) (9.0 MB) with Mingw/GCC**”

3. Save the .exe file in your local machine.

4. Double click on the exe file.

5. Start the installation by clicking the Next button and I Agree on button.

![](/images/wp/env-1-b3efc3d8.jpg)

6. Choose the destination folder as “C:\Dev-Cpp” (It is there by default) and click the “Install’ button and finally click the Finish button. You can modify this destination folder path if you want.

7. Once installation is completed, go to your desktop and right-click on My Computer -> properties -> advanced system settings -> advanced tab. Then, click on the “Environment Variables” button and then “New”. You will get a popup window as shown below.

Change the System variable as given below.

Variable name: PATH
Variable value: C:\Dev-Cpp\bin;

![](/images/wp/env-2-efac49a8.jpg)

8. Once you are done with the above settings, then you can start Dev C++ by clicking start –> Dev C++ as shown below.

9.Open Dev C++ window and click on file -> new -> project. Then, select Console Application. Choose “C project” and “Make Default Language” check boxes.

![](/images/wp/env-3-a3ce1f32.jpg)

10. Click on file -> new -> source file and type a sample program and save it as sample.c

![](/images/wp/env-5-be120c37.jpg)

11. Click on the “Compile & Run” button to compile and execute our program as shown below.

![](/images/wp/env-4-d29c7906.jpg)

12. Output window will be opened as below when there is no compilation error. Use “Enter” button to come back to the program window.

![](/images/wp/env-6-7a8bf482.jpg)

#### 4. LIST OF C/C++ COMPILERS FOR UNIX/LINUX OPERATING SYSTEM:
There are so many compilers available on the market for UNIX/LINUX operating system. We are listing some of them here for your reference.

1. AMPC
2. CCs C compiler
3. ch, clang
4. GCC C compiler
5. Interactive C compiler
6. Mikro C compiler
7. Portable C compiler
8. Small C and XL C Compilers etc.
