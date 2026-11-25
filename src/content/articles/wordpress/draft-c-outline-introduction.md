---
title: "C OUTLINE INTRODUCTION"
description: "C LANGUAGE AND ITS ADVANTAGE 'C' was developed by Dennis Ritchie in 1972. It is a robust language. It is a low programming level language close to machine…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-05-30T07:07:39
legacy: true
wpId: 2349
draft: true
---

## C LANGUAGE AND ITS ADVANTAGE

- 'C' was developed by Dennis Ritchie in 1972.
- It is a robust language.
- It is a low programming level language close to machine language
- It is widely used in the software development field.
- It is a procedure and structure oriented language.
- It has the full support of various operating systems and hardware platforms.
- C language has variety of data types and powerful operators .Due to this ,programs written in C language are Efficient ,and easy to understand .
- C is highly portable language .
- C language is a system programming language because it can be used to do low-level programming (for example driver and kernel). It is generally used to create hardware devices, OS, drivers, kernels, etc. For example, Linux kernel is written in C. It can't be used for internet programming like Java, .Net, PHP, etc.
- C programming is Consider as the base for other Programming Languages that why it is known as mother language
  - It can be definedly by the following w

## Advantages in c

- **C programming language is the structured programming language, So, It helps you to think of the problem in terms of function modules or blocks, Collection of these modules makes a complete program, This modular structure makes the program debugging, testing and maintenance easier.**
- **C programming language is a building block for many other currently known languages, Python is a fully Object-Oriented High-Level programming language, It is written in C ( perhaps [C++](https://www.online-sciences.com/programming/c-programming-language-advantages-and-disadvantages/) too ) .**
- **C programming language is a small language, The concepts that it requires is quite short , There are 32 keywords in ANSI C only and its strength lies in its built-in functions, Many standard functions are available that can be used for developing the programs**.
- **C language has the ability to extend itself , It is the collection of functions which are supported by the C library this makes us easier to add our own functions to the C library, Because of the availability of a large number of functions , the programming task becomes simple.**
- **C language is the compiled language versus an interpreted language, Explained simply, So, The code is compacted into executable instruction rather than being translated on the fly at run time, This feature lends heavily to the speed of C programs and a lot of libraries are written in C.**
- **C Language is very much popular language around the world and best suitable for the programmer to learn at the first stage of the programming, There is not much vocabulary to learn, C language has easy syntax and it is easier to learn , It is still a practical and compact language and it comprises a good semantic**.
- **C programming language is easy to Learn ( Syntax is near to English Language ) , C language syntax is very easy to understand, It uses keywords that we are using in our day to day life to convey meaning or to get some decisions**
- **C Language is very near to assembly programming, the hard use of pointers, for example, is a very powerful mechanism, It has features that allow the programmer to organize the programs in a clear, easy, logical way .**
- **C language allows meaningful names for variables without any loss of efficiency , So , C language gives a complete freedom of programming style , including flexible ways of making the decisions and a set of flexible commands for performing tasks repetitively ( for , while , do ) .**
- **C programming language is procedure-oriented language, So, The user creates procedures or functions to execute their task, The procedure-oriented language is very much easy to learn because it follows an algorithm to execute your statements.**
- **To develop the program using procedure-oriented language , you need to draw/prepare the algorithm and then start converting it into procedure or functions .**
- **C programming language** **offers lots of functions that consist of system generated functions and user defined functions , C Compiler comes with list of header files that consist of many general functions that can be used to develop the program , while the programmer can create the function as per their requirements that is called as user generated/defined function .**
- **C compiler produces the machine code very fast compared to the other language compiler , C compiler can compile around 1000 lines of code in a seconds or two , One more benefit of the C Compiler is that it also optimize the code for faster execution .**
- **C programming language** **is portable, C Language setup is around 3-5 MB , So , It is very easy to install and operate , Its output is exe file that can be executed in any computer without any other framework/software.**
- **C programming language has a low level of abstraction, It is close enough to system hardware descriptions , you can see right through it and stare directly into the machine , learning C first , it is easier to find your way around how higher level languages work.**

## The Structure of a C program

**Structure** is a group of variables of different data types represented by a single name. Lets take an example to understand the need of a structure in C programming.

Lets say we need to store the data of students like student name, age, address, id etc. One way of doing this would be creating a different variable for each attribute, however when you need to store the data of multiple students then in that case, you would need to create these several variables again for each student. This is such a big headache to store data in this way.

We can solve this problem easily by using structure. We can create a structure that has members for name, id, address and age and then we can create the variables of this structure for each student. This may sound confusing, do not worry we will understand this with the help of example.

```
struct struct_name {
   DataType member1_name;
   DataType member2_name;
   DataType member3_name;
   …
};
Here struct_name can be anything of your choice. Members data type can be same or different. Once we have declared the structure we can use the struct name as a data type like int, float etc.
```

## C Programming Language

C is a Unix operating system by-product, and C language is a popular and widely used Programming language. From the beginning, C Programming language is used for operating systems, micro-controllers, applications, and graphics. In recent days, it was a trendy language in Automation.

The influence of C in current or modern Programming languages is very prominent. We can clearly say C Programming has a massive influence on C++, C#, Java, and Perl, and C++ is an extension to C.

## C Basics

The C Programming language is structural and procedural. Although this high-level language was designed for system applications, C language has proved that it is powerful and flexible enough to use in business applications.

1. comments
2. Escape Sequence

# Comments in C

Comments in C Programming are to provide a piece of information about the code. A comment can helps the other programmers to understand the program flow. In C Programming Language, there are two types of commenting options, and they are Single Line and Multi-line.

1-Singleline 2- Multi-line

## Single Line Comment Example

The Single Line comments start with two forward slashes(//). In this program we are displaying Hello World as the C Programming output. Here, we used a single line comment

```
Single line Comments in C Program
#include<stdio.h>

int main()                                                                 O
{
    // Printing Hello World Message as Output
    printf(" Hello World! \n");

    return 0;
}
OUTPUT- Hello World
                C MULTI-LINE COMMENTS EXAMPLE
The Multi-Line Comments placed in between /*……… */. Use this Slash and asterisk to write a multi-line comment.
    Multi Line Comments in C
#incle <stdio.h>
int main()
{
/*
print
message
as an output
Printf("welcome to c program /n");
return 0;
}
OTUPUT- Welcome to c program

```

## WRITING C PROGRAM

To write the first c program, open the C console and write the following code:

#include &lt;stdio.h>

int main(){

printf("Hello C Language")

return 0;

}

**#include &lt;stdio.h>** includes the **standard input output** library functions. The printf() function is defined in stdio.h .

**int main()** The **main() function is the entry point of every program** in c language.

**printf()** The printf() function is **used to print data** on the console.

**return 0** The return 0 statement, returns execution status to the OS. The 0 value is used for successful execution and 1 for unsuccessful execution.

## C Programming Operators

Operators in C Programming are nothing but the symbols used to perform some operations on the given values or operands. Some operators used for numeric calculations, and some to check the relations, etc. The following are the list of operators available in the C Programming Language.

1. Operators introduction
2. Arithmetic Operators
3. Relational Operators
4. Logical Operators
5. Assignment Operators
6. Increment & Decrement Operators
7. Conditional Operator
8. Bitwise Operators
9. Sizeof Operator

## DEBUGGING A C PROGRAM

**What Is Mean By Debugging ?**

Debugging is the routine process of **locating and removing computer program bugs, errors or abnormalities**, which is methodically handled by software programmers via debugging tools. Debugging checks, detects and corrects errors or bugs to allow proper program operation according to set specifications. Debugging is also known as debug.

**Intel parallel inspector** is used as a source of debugging for memory errors in C/C++ operations. The process of finding bugs or errors and fixing them in any application or software is called debugging.**Intel parallel inspector** is used as a source of debugging for memory errors in C/C++ operations. The process of finding bugs or errors and fixing them in any application or software is called debugging.

### Write a sample C program with errors for debugging purpose

To learn C program debugging, let us create the following C program that calculates and prints the factorial of a number. However this C program contains some errors in it for our debugging purpose.

```
$ vim factorial.c
# include <stdio.h>

int main()
{
	int i, num, j;
	printf ("Enter the number: ");
	scanf ("%d", &num );

	for (i=1; i<num; i++)
		j=j*i;

	printf("The factorial of %d is %d\n",num,j);
}
```

```
$ cc factorial.c

$ ./a.out
Enter the number: 3
The factorial of 3 is 12548672
```

## Examining An Running a C Application Program Data Types and Variables

**DATA TYPES**

Let's discuss about a very simple but very important concept available in almost all the programming languages which is called **data types**. As its name indicates, a data type represents a type of the data which you can process using your computer program. It can be numeric, alphanumeric, decimal, etc.

Let’s keep Computer Programming aside for a while and take an easy example of adding two whole numbers 10 & 20, which can be done simply as follows −

```
10 + 20
```

Let's take another problem where we want to add two decimal numbers 10.50 & 20.50, which will be written as follows −

```
10.50 + 20.50
```

The two examples are straightforward. Now let's take another example where we want to record student information in a notebook. Here we would like to record the following information −

```
Name:
Class:
Section:
Age:
Sex:
```

Now, let's put one student record as per the given requirement −

```
Name: Zara Ali
Class: 6th
Section: J
Age: 13
Sex: F
```

The first example dealt with whole numbers, the second example added two decimal numbers, whereas the third example is dealing with a mix of different data. Let's put it as follows −

- Student name "Zara Ali" is a sequence of characters which is also called a string.
- Student class "6th" has been represented by a mix of whole number and a string of two characters. Such a mix is called alphanumeric.
- Student section has been represented by a single character which is 'J'.
- Student age has been represented by a whole number which is 13.
- Student sex has been represented by a single character which is 'F'.

This way, we realized that in our day-to-day life, we deal with different types of data such as strings, characters, whole numbers (integers), and decimal numbers (floating point numbers).

Similarly, when we write a computer program to process different types of data, we need to specify its type clearly; otherwise the computer does not understand how different operations can be performed on that given data. Different programming languages use different keywords to specify different data types. For example, C and Java programming languages use **int** to specify integer data, whereas **char** specifies a character data type.

Subsequent chapters will show you how to use different data types in different situations. For now, let's check the important data types available in C, Java, and Python and the keywords we will use to specify those data types.

# Data Types in C

A data type specifies the type of data that a variable can store such as integer, floating, character, etc.

**There are the following data types in C language.**

| Types | Data Types |
| --- | --- |
| Basic Data Type | int, char, float, double |
| Derived Data Type | array, pointer, structure, union |
| Enumeration Data Type | enum |
| Void Data Type | void |

## Basic Data Types

The basic data types are integer-based and floating-point based. C language supports both signed and unsigned literals.

The memory size of the basic data types may change according to 32 or 64-bit operating system.

Let's see the basic data types. Its size is given **according to 32-bit architecture**.

| Data Types | Memory Size | Range |
| --- | --- | --- |
| **char** | 1 byte | −128 to 127 |
| signed char | 1 byte | −128 to 127 |
| unsigned char | 1 byte | 0 to 255 |
| **short** | 2 byte | −32,768 to 32,767 |
| signed short | 2 byte | −32,768 to 32,767 |
| unsigned short | 2 byte | 0 to 65,535 |
| **int** | 2 byte | −32,768 to 32,767 |
| signed int | 2 byte | −32,768 to 32,767 |
| unsigned int | 2 byte | 0 to 65,535 |
| **short int** | 2 byte | −32,768 to 32,767 |
| signed short int | 2 byte | −32,768 to 32,767 |
| unsigned short int | 2 byte | 0 to 65,535 |
| **long int** | 4 byte | -2,147,483,648 to 2,147,483,647 |
| signed long int | 4 byte | -2,147,483,648 to 2,147,483,647 |
| unsigned long int | 4 byte | 0 to 4,294,967,295 |
| **float** | 4 byte |  |
| **double** | 8 byte |  |
| **long double** | 10 byte |

# Variables in C

A **variable** is a name of the memory location. It is used to store data. Its value can be changed, and it can be reused many times.

Variables are the names you give to computer memory locations which are used to store values in a computer program.

For example, assume you want to store two values 10 and 20 in your program and at a later stage, you want to use these two values. Let's see how you will do it. Here are the following three simple steps −

It is a way to represent memory location through symbol so that it can be easily identified.

Let's see the syntax to declare a variable:

1. type variable\_list;

The example of declaring the variable is given below:

1. **int** a;
2. **float** b;
3. **char** c;

Here, a, b, c are variables. The int, float, char are the data types.

We can also provide values while declaring the variables as given below:

1. **int** a=10,b=20;//declaring 2 variable of integer type
2. **float** f=20.8;
3. **char** c='A';

## Rules for defining variables

- A variable can have alphabets, digits, and underscore.
- A variable name can start with the alphabet, and underscore only. It can't start with a digit.
- No whitespace is allowed within the variable name.
- A variable name must not be any reserved word or keyword, e.g. int, float, etc.

**Valid variable names:**

1. **int** a;
2. **int** \_ab;
3. **int** a30;

**Invalid variable names:**

1. **int** 2;
2. **int** a b;
3. **int** **long**;

|  |
| --- |
| Types of Variables in C 1-local variable 2-global variable 3-static variable 4-automatic variable 5-external variable |

### Local Variable

A variable that is declared inside the function or block is called a local variable.

void function(){

int x=10;://local variable

}

It must be declared at the start of

### Global Variable

A variable that is declared outside the function or block is called a global variable. Any function can change the value of the global variable. It is available to all the functions.

It must be declared at the start of the block**int** value=20;//global variable

**void** function1(){

**int** x=10;//local variable

int value =20 ;global variable .

void function(){

int x=10;//local varible

}

### Static Variable

A variable that is declared with the static keyword is called static variable.

ADVERTISEMENT

It retains its value between multiple function calls.

void Function1(){

int x=10;//local variable

static int y=10;// static variable

x=x+1;

y=y+1

printf (''%d ,%d",x,y);

}

If you call this function many times, the **local variable will print the same value** for each function call, e.g, 11,11,11 and so on. But the **static variable will print the incremented value** in each function call, e.g. 11, 12, 13 and so on.

### Automatic Variable

All variables in C that are declared inside the block, are automatic variables by default. We can explicitly declare an automatic variable using **auto keyword**.

void main(){

int x=10://local variable (also automatic)

auto int y=20;//automatic variable

}

### External Variable

We can share a variable in multiple C source files by using an external variable. To declare an external variable, you need to use **extern keyword**.

*myfile.h*

Extern int intx=10;//external variable (also global)

#include "myfile.h"

#include &lt;stdio.h>

void print value(){

printf("global variable :%d",global -variable );

}

Variables In Basically 3 types that is

- Create variables with appropriate names.
- Store your values in those two variables.
- Retrieve and use the stored values from the variables

## Creating variables

Creating variables is also called **declaring variables** in C programming. Different programming languages have different ways of creating variables inside a program. For example, C programming has the following simple way of creating variables −

```
#include <stdio.h>

int main() {
   int a;
   int b;
}
```

The above program creates two variables to reserve two memory locations with names **a** and **b**. We created these variables using **int** keyword to specify variable **data type** which means we want to store integer values in these two variables. Similarly, you can create variables to store **long**, **float**, **char** or any other data type. For example −

```
/* variable to store long value */
long a;

/* variable to store float value */
float b;
```

You can create variables of similar type by putting them in a single line but separated by comma as follows −

```
#include <stdio.h>

int main() {
   int a, b;
}
```

Listed below are the key points about variables that you need to keep in mind −

- A variable name can hold a single type of value. For example, if variable **a** has been defined **int** type, then it can store only integer.
- C programming language requires a variable creation, i.e., declaration before its usage in your program. You cannot use a variable name in your program without creating it, though programming language like Python allows you to use a variable name without creating it.
- You can use a variable name only once inside your program. For example, if a variable **a** has been defined to store an integer value, then you cannot define **a** again to store any other type of value.
- There are programming languages like Python, PHP, Perl, etc., which do not want you to specify data type at the time of creating variables. So you can store integer, float, or long without specifying their data type.
- You can give any name to a variable like **age**, **sex**, **salary**, **year1990** or anything else you like to give, but most of the programming languages allow to use only limited characters in their variables names. For now, we will suggest to use only **a....z, A....Z, 0....9** in your variable names and start their names using alphabets only instead of digits.
- Almost none of the programming languages allow to start their variable names with a digit, so **1990year** will not be a valid variable name whereas **year1990** or **ye1990ar** are valid variable names.

Every programming language provides more rules related to variables and you will learn them when you will go in further detail of that programming language.

## Store Values in Variables

You have seen how we created variables in the previous section. Now, let's store some values in those variables −

```
#include <stdio.h>

int main() {
   int a;
   int b;

   a = 10;
   b = 20;
}
```

The above program has two additional statements where we are storing 10 in variable **a** and 20 is being stored in variable **b**. Almost all the programming languages have similar way of storing values in variable where we keep variable name in the left hand side of an equal sign = and whatever value we want to store in the variable, we keep that value in the right hand side.

Now, we have completed two steps, first we created two variables and then we stored required values in those variables. Now variable **a** has value 10 and variable **b** has value 20. In other words we can say, when above program is executed, the memory location named **a** will hold 10 and memory location **b** will hold 20.

## Access stored values in variables

If we do not use the stored values in the variables, then there is no point in creating variables and storing values in them. We know that the above program has two variables **a** and **b** and they store the values 10 and 20, respectively. So let's try to print the values stored in these two variables. Following is a C program, which prints the values stored in its variables −[Live Demo](http://tpcg.io/jLUDNX)

```
#include <stdio.h>

int main() {
   int a;
   int b;

   a = 10;
   b = 20;

   printf( "Value of a = %d\n", a );
   printf( "Value of b = %d\n", b );
}
```

When the above program is executed, it produces the following result −

```
Value of a = 10
Value of b = 20
```

You must have seen **printf()** function in the previous chapter where we had used it to print "Hello, World!". This time, we are using it to print the values of variables. We are making use of **%d**, which will be replaced with the values of the given variable in printf() statements. We can print both the values using a single printf() statement as follows −[Live Demo](http://tpcg.io/n3avFP)

```
#include <stdio.h>

int main() {
   int a;
   int b;

   a = 10;
   b = 20;

   printf( "Value of a = %d and value of b = %d\n", a, b );
}
```

When the above program is executed, it produces the following result −

```
Value of a = 10 and value of b = 20
```

If you want to use **float** variable in C programming, then you will have to use **%f** instead of **%d**, and if you want to print a character value, then you will have to use **%c**. Similarly, different data types can be printed using different % and characters.

## Variables in Java

Following is the equivalent program written in Java programming language. This program will create two variables **a** and **b** and very similar to C programming, it will assign 10 and 20 in these variables and finally print the values of the two variables in two ways −[Live Demo](http://tpcg.io/3anWpT)

```
public class DemoJava {
   public static void main(String []args) {
      int a;
      int b;

      a = 10;
      b = 20;

      System.out.println("Value of a = " + a);
      System.out.println("Value of b = " + b);
      System.out.println("Value of a = " + a + " and value of b = " + b);
   }
}
```

When the above program is executed, it produces the following result −

```
Value of a = 10
Value of b = 20
Value of a = 10 and value of b = 20
```

## Variables in Python

Following is the equivalent program written in Python. This program will create two variables **a** and **b** and at the same time, assign 10 and 20 in those variables.

Python does not want you to specify the data type at the time of variable creation and there is no need to create variables in advance.[Live Demo](http://tpcg.io/EkvhAy)

```
a = 10
b = 20

print "Value of a = ", a
print "Value of b = ", b
print "Value of a = ", a, " and value of b = ", b
```

When the above program is executed, it produces the following result −

```
Value of a =  10
Value of b =  20
Value of a =  10  and value of b =  20
```

You can use the following syntax in C and Java programming to declare variables and assign values at the same time −[Live Demo](http://tpcg.io/HHpLt8)

```
#include <stdio.h>

int main() {
   int a = 10;
   int b = 20;

   printf( "Value of a = %d and value of b = %d\n", a, b );
}
```

When the above program is executed, it produces the following result −

```
Value of a = 10 and value of b = 20

```

## OPERANDS ,OPERATORS ,AND ARITHMETIC EXPRESSION INPUT /OUTPUT MANAGEMENT

# C Operators

An operator is simply a symbol that is used to perform operations. There can be many types of operations like arithmetic, logical, bitwise, etc.

There are following types of operators to perform different types of operations in C language.

- Arithmetic Operators
- Relational Operators
- Shift Operators
- Logical Operators
- Bitwise Operators
- Ternary or Conditional Operators
- Assignment Operator
- Misc Operator

## Precedence of Operators in C

The precedence of operator species that which operator will be evaluated first and next. The associativity specifies the operator direction to be evaluated; it may be left to right or right to left.

Let's understand the precedence by the example given below:

1. **int** value=10+20\*10;

The value variable will contain **210** because \* (multiplicative operator) is evaluated before + (additive operator).

The precedence and associativity of C operators is given below:

| Category | Operator | Associativity |
| --- | --- | --- |
| Postfix | () [] -> . ++ - - | Left to right |
| Unary | + - ! ~ ++ - - (type)\* & sizeof | Right to left |
| Multiplicative | \* / % | Left to right |
| Additive | + - | Left to right |
| Shift | &lt;&lt; >> | Left to right |
| Relational | &lt; &lt;= > >= | Left to right |
| Equality | == != | Left to right |
| Bitwise AND | & | Left to right |
| Bitwise XOR | ^ | Left to right |
| Bitwise OR | | | Left to right |
| Logical AND | && | Left to right |
| Logical OR | || | Left to right |
| Conditional | ?: | Right to left |
| Assignment | = += -= \*= /= %=>>= &lt;&lt;= &= ^= |= | Right to left |
| Comma | , | Left to right |

## ARITHMETIC OPERATORS

The arithmetic operators in the C language are used to perform basic mathematical operations. It is used in a C arithmetic expression involving at least two operands and an operator.

An expression is C statement that evaluates to a single value. You can use this value in another C expression or output to the console.

For example,

```
A = 10;

B = 20;

C = A + B; /* This is an arithmetic expression involving two

Two operands and + operator */
```

In the above example, the expression A and B will be replaced with 10 + 20, when the program executes and the expression will evaluate to 30. This is assigned to variable C.

## Arithmetic Operators

A list of arithmetic operators is given below. The mathematical symbol is actual mathematical operation perform in real world. The C operator is equivalent of that mathematical operation.

| **Math Symbol** | **C Operator** | **Description** |
| --- | --- | --- |
| + | + | Addition |
| – | – | Subtraction |
| x | \* | Multiplication |
| ÷ | / | Division |
| mod | % | Modulo |

**Addition**

The addition operator perform simple addition on two numbers. It requires two operands of type – *integers or real numbers.*

For example,

```
sum = number1 + number2 ;

sum = 10 + 23;

sum = 12.4 + 53.33;
```

The above are valid C expressions involving addition (+) operator.

**Subtraction**

The subtraction is similar to addition and perform simple subtraction on integers or real numbers.

For example,

```
result = number2 – number1;

result = 23.4 – 33.55;

result = 32 – 2;
```

These are some valid examples of C expression involving the subtraction (-) operator.

**Multiplication**

The multiplication is the first operation performed when an arithmetic expression is evaluated. We will learn more about operator precedence in future lessons.

The multiplication operator requires at least two operands to perform the multiplication and the result can be output to console and used in another expression.

For example,

```
C = A * B;

C = 34 * 100;

result = 23.44 * 34.545;
```

The above expressions are some valid expressions involving multiplication (\*) operator.

**Division operator**

The division requires two operands – a dividend and a divisor. The dividend is divided using divisor and result is a quotient and remainder.

It is assumed that the dividend is always greater than the divisor, but it’s not necessarily true. Sometimes, dividend is a smaller value than divisor, but this does not produce wrong results.

For example,

```
result = number2 / number1;

result = 56.33/6.55;

result = 32 /22;
```

These are some valid examples of C expression involving the division (/) operator.

The third example will result in quotient = 1 and remainder = 10, but C division operator during an integer division only output quotient, not remainder.

**THE INPUT/OUTPUT CONCEPT**

 Input and Output. Input means to provide the program with some data to be used in the program and Output means to **display data on screen or write the data to a printer or a file**.

**C PROGRAM INPUT/OUTPUT CONCEPT**

Now we'll create a program that adds two numbers. We'll solve this problem in C with the following steps:
**Step 1 :**Allocate memory for storing three numbers
**Step 2 :**Store first number in computer memory
**Step 3 :**Store second number in computer memory
**Step 4 :**Add these two numbers together and store the result of the addition in a third memory location
**Step 5 :**Print the result

#### Step 1

Now first we'll allocate memory for storing numbers.

Location of the computer memory which is used to store data and is given a symbolic name for reference is known as variable. We need three variables, two for storing input and third for storing result. Before a variable is used in a program, we must declare it. This activity enables the compiler to make available the appropriate type of location in the memory.

Following statements declare three variables of type integer to store whole numbers.

`int x;
int y;
int z;`

You can declare more than one variable of same type in a single statement like :

`int x, y, z;`

#### Step 2

Following statement stores value in first variable

`x = 25;`

#### Step 3

Following statement stores value in second variable

`y = 10;`

#### Step 4

Now, add these two numbers together and store the result of the addition in third variable

`z = x + y;`

#### Step 5

Print the result

`printf("The sum is %d", z);`
You can output integer variables in a similar way as you output strings by tying %d instead of any text. The %d a placeholder that tells the printf() command to print an integer value.
