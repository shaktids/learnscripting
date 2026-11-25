---
title: "Tricky C programs Question & Answers Part 2"
description: "Add Two Numbers Without Using the Addition Operator Generally, for the sum of two numbers, we use the addition (+) operator. In this tricky C programs, we…"
lang: other
categories: ["C"]
author: "Shakti Das"
pubDate: 2021-01-18T05:48:47
legacy: true
wpId: 2104
draft: true
---

### Add Two Numbers Without Using the Addition Operator
Generally, for the sum of two numbers, we use the addition (+) operator. In this tricky C programs, we will write a C program to add two numbers without using the addition operator.

```
#include<stdio.h>
#include<stdlib.h>
int main()
{
  int x, y;
  printf("Enter two number: ");
  scanf("%d %d",&x,&y);

  // method 1
  printf("%d\n", x-(-y));

  // method 2
  printf("%d\n", -(-x-y));

  // method 3
  printf("%d\n", abs(-x-y));

  // method 4
  printf("%d", x-(~y)-1);

  return 0;
}
```

Minus multiplied with minus gives a positive value, this concept is applied in the first method. Here, a-(-b) will become a+b. So, the addition of variables a and b is displayed on the screen. In the second method, the same concept is used. In 3rd method, pre-defined function abs() is used.

The abs() function is defined in `stdlib.h` header file. It returns the absolute value of a number. In the 4th method, the bitwise complement operator is used. *The bitwise complement of the number N is equal to -(N+1)*. So, a-(~b)-1 is equal to a-(-(b+1))-1 => a+b+1-1 => a+b. Know more about:- [Bitwise Complement operator](https://www.knowprogram.com/c-programming/bitwise-operators-in-c/#Complement_operator)

Method5:- **Addition of two numbers Using a recursive function**

```
#include<stdio.h>
int add(int x, int y)
{
   if(y == 0)
     return x;
   else
     return add( x^y, (x & y) << 1);
}
int main()
{
   int a, b, sum;
   printf("Enter two numbers: ");
   scanf("%d %d", &a, &b);
   sum = add(a,b);
   printf("Sum = %d\n",sum);
   return 0;
}
```

We used a function add() to add two numbers without using the addition operator. [Bitwise XOR Operator](https://www.knowprogram.com/c-programming/bitwise-operators-in-c/#XOR) adds both numbers.

This method does not work with float data types, Because [Bitwise operators](https://www.knowprogram.com/c-programming/bitwise-operators-in-c/) can not apply to float data types in C Programming.

### Subtract Two Number Without Using Subtraction Operator
```
#include<stdio.h>
#include<stdlib.h>
int main()
{
   int x, y;
   printf("Enter two number: ");
   scanf("%d %d",&x,&y);
   printf("%d", x+(~y)+1);
   return 0;
}
```

The bitwise complement operator is used in this program. The bitwise complement of number ~y=-(y+1). So, expression will become x+(-(y+1))+1=x-y-1+1=x-y

### Multiply an Integer Number by 2 Without Using Multiplication Operator
```
#include<stdio.h>
int main()
{
   int x;
   printf("Enter a number: ");
   scanf("%d",&x);
   printf("%d", x<<1);
   return 0;
}
```

The left shift operator shifts all bits towards left by a certain number of specified bits. The expression x&lt;&lt;1 always returns x\*2. Note that shift operator doesn’t work on floating-point values.

For multiple of x by 4, use x&lt;&lt;2. Similarly x&lt;&lt;3 multiply x by 8. For multiple of the number x by 2^n, use x&lt;&lt;n. Know more about:- [Left shift operator](https://www.knowprogram.com/c-programming/bitwise-operators-in-c/#Left_Shift_Operator)

### Divide an Integer Number by 2 Without Using Division Operator
```
#include<stdio.h>
int main()
{
   int x;
   printf("Enter a number: ");
   scanf("%d",&x);
   printf("%d", x>>1);
   return 0;
}
```

The right shift operator shifts all bits towards the right by a certain number of specified bits. To divide x by 4, use x>>2. Similarly, x>>3 divide x by 8. To divide the number x by 2^n, use x>>n. Know more about:- [Right shift operator](https://www.knowprogram.com/c-programming/bitwise-operators-in-c/#Right_Shift_Operator)

### Multiply Two Number Without Using Multiplication Operator
Multiplying two numbers is nothing but adding the same number repeatedly. For example:- 5\*3 is similar to 5+5+5; 7\*5 is similar to 7+7+7+7+7; So, we can develop a recursive function which will execute repeatedly. In this tricky C programs, one recursive function multiply() is used to multiply the two numbers.

Base case and the general case for multiplication of number x and y,
base case
`if(y=0) then multiplication = 0;`
general case
`if(y>0) then multiplication = x + multiplication(x, y-1);
if(y&lt;0) then multiplication = x + multiplication(x, -y);`

```
#include<stdio.h>
float multiply(float x, float y);
int main()
{
   float a, b;
   printf("Enter two number: ");
   scanf("%f %f",&a, &b);
   float result = multiply(a,b);
   printf("Result = %.2f",result);
   return 0;
}

// Recursive function to find
// multiplication of two numbers
float multiply(float x, float y)
{
   if(y==0) return 0;
   else if(y>0) return( x+ multiply(x,y-1) );
   else return -multiply(x,-y);
}
```

Output for different test-cases:-

Enter two number: `3 2`
Result = 6

Enter two number: `5.5 2`
Result = 11.00

Enter two number: `135.268 235`
Result = 31787.91

Enter two number:`5.5 -2`
Result = -11.00

#### Execution of the program

1st call of multiply() function,
multiply(3,2);
x=3, y=2;
y>0 return(3+multiply(3,2-1);

2nd call of recursive function multiply()
multiply(3,1);
x=3, y=1;
y>0 return(3+multiply(3,1-1);

3rd call of recursive function multiply()
multiply(3,0);
x=3, y=0;
y==0 return 0;

Now, control back to 2nd call,
return(3+0);
Control back to 1st call,
retunrn(3+3+0);
Finally 6 is returned to the main function.

Know more about:- [Recursive function in C](https://www.knowprogram.com/c-programming/recursion-c/)

### Divide Two Integer Number Without Using the Division Operator
In this tricky C programs, we will write a program to divide two integer numbers without using the division operator. In this program, one pre-defined function abs() is used, which returns the absolute value of a number. One user-defined function divide() is developed to solve the problem.

The division is nothing but subtracting the second operand form first operand until the first operand becomes lesser than the second operator. The number of times we subtract is our result. For example:- 11/3; So, 11-3=8; 8-3=5; 5-3=2; Now, 2 is lesser than 3. We subtract 3 times so, 11/3=3 and in last we got remainder 2. If you understand this process then this and next program, you will understand easily.

```
#include<stdio.h>
#include<stdlib.h>
int main()
{
   int a, b;
   printf("Enter two number: ");
   scanf("%d %d",&a, &b);

   int result = divide(a,b);
   printf("Result = %d",result);

   return 0;
}

// function to find division of two number
int divide(int x, int y)
{
  int count = 0;
  int sign = ((x<0)^(y<0))?-1:1;

  x = abs(x);
  y = abs(y);

  while (x>=y)
  {
     x = x-y;
     count++;
  }

  return sign*count;
}
```

Output for the different test-cases:-

Enter two number: 10 5
Result = 2

Enter two number: 452 23
Result = 19

In mathematics, the division of two numbers returns negative value when exactly any one of the operands is negative. So, to find the exactly anyone operand is negative or not, bitwise XOR operator(^) is used inside divide() function. The statement `sign = ((x&lt;0)^(y&lt;0))?-1:1`; checks store the result into the variable sign. Bitwise operator doesn’t work correctly on floating-point values, so for floating-point values, you may get some lesser value than expected value.

Now, both operand is converted to positive using abs() function. The division is nothing but the subtraction of the 2nd number from the 1st number. For example:- if we want to calculate 5/2 then 5-2=3, 3-2=1; Now, 1 is less than 2. So, we subtract two times hence the result will be 2. Know more about:- [Bitwise XOR operator in C](https://www.knowprogram.com/c-programming/bitwise-operators-in-c/#Bitwise_XOR_operator)

### Remainder of Two Integer Number Without Using the Modulus Operator
Using the previous program we can also calculate the remainder of two numbers without using % operator. Inside divide() function, return x value. It is the remainder of the two numbers.

```
int rem(int x, int y)
{
  int count = 0;
  int sign = ((x<0)^(y<0))?-1:1;
  x = abs(x);
  y = abs(y);
  while (x>=y)
  {
    x = x-y;
    count++;
  }
  return x;
}
```

Output for the different test-cases:-

Enter two number: 816 23
Result = 11

## Tricky C programs:- Check Two Numbers are Equal or not
Program description:- Write a C program to **check two numbers are EQUAL or not without using arithmetic operators or comparison operators**.

To check two numbers are equal or not we can use bitwise XOR operators. The bitwise XOR operators return 0 for similar bits. For two similar numbers, all bits will be the same and due to this bitwise XOR operator will return false.

```
#include<stdio.h>
int main()
{
   int a, b;
   printf("Enter two numbers:");
   scanf("%d %d",&a, &b);
   if(a^b) printf("Numbers are different.");
   else printf("Both numbers are the same.");
   return 0;
}
```

Output for the different test-cases:-

Enter two numbers:`5 5`
Both numbers are the same.

Enter two numbers:`12 15`
Numbers are different.

## Tricky C programs:- Check Even or Odd
Program description:- Write a C program to **check whether the number is EVEN or ODD, without using any arithmetic or relational operators**.

The bitwise and(&) operator can be used to quickly check the number is odd or even.

```
#include<stdio.h>
int main()
{
   int x;
   printf("Enter a number: ");
   scanf("%d", &x);
   (x&1)?printf("Odd"):printf("Even");
   return 0;
}
```

Output for the different test-cases:-

Enter a number: 5
Odd

Enter a number: 10
Even

## Tricky C programs:- Maximum and Minimum of Two Numbers
Program description:- Write a C program to **find the maximum and minimum of two numbers without using any loop or condition**.

The minimum and maximum of two number can be found as min = ((x+y)-abs(x-y))/2 and max = ((x+y)+abs(x-y))/2; For example:- The minimum of 10 and 20 is ((10+20)-abs(10-20))/2 = (30-10)/2 = 10; Similarly, maximum of 10 and 20 is ((10+20)+abs(10-20))/2 = (30+10)/2 = 20;

```
#include<stdio.h>
#include<stdlib.h>
int main()
{
   int x, y;
   printf("Enter two numbers: ");
   scanf("%d %d",&x, &y);

   int max = ((x+y)+abs(x-y))/2;
   int min = ((x+y)-abs(x-y))/2;

   printf("Minimum = %d \nMaximum = %d",min,max);

   return 0;
}
```

Output for the different test-cases:-

Enter two numbers: `10 20`
Minimum = 10
Maximum = 20

Enter two numbers: `5 -15`
Minimum = -15
Maximum = -5

## Tricky C programs:- Display Text Within Double Quotes
Here we will write tricky C programs for displaying some texts within double-quotes (`" "`). The double quotation is used for displaying String inside the printf() function, and it doesn’t display the double quotation. For displaying double quotes, we should use escape sequence character \” it displays quotes on the screen.

```
#include<stdio.h>
int main()
{
   printf("\"Hello World\"");
   printf("\nWelcome to \"Knowprogram.com\" ");
   return 0;
}
```

Output:-

“Hello World”
Welcome to “Knowprogram.com”
