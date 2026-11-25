---
title: "Array interview questions in C/C++"
description: "This article is mainly focused on the most repeatedly asked and the latest updated Array Interview Questions in C/C++ that are appearing in most of the…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-01-18T07:02:28
legacy: true
wpId: 2122
draft: true
---

This article is mainly focused on the most repeatedly asked and the latest updated Array Interview Questions in C/C++  that are appearing in most of the C/C++ interviews.

If you are looking for “Array Interview Questions in C/C++” or “advanced questions on array in C/C++, then you at the right place. Here I have tried to create some collection of “interview questions with answers related to the array in C/C++ ” that might ask by your interviewer.

I hope these C array interview questions with the answer will be helpful. If you have any other important questions related to the array in C/C++ programming and concept, then please write in the comment box. It will be helpful for others.

### Q) What is Array in C?

### Ans:

An array is essentially a collection of elements. The data type of all elements must be the same and store at the contiguous memory location. So each array can store only one type of data. At the time of the array declaration, you must specify the type of data with the array name.

In array, we can access the elements using an index in square brackets. The index of the array always starts with 0. It means if you want to get the first element of the array then the index must be 0.

**Note:** In array first element at the lowest address and the last element at the highest address.

#### Syntax fo array declaration in C:

**Data\_Type Array\_Name [size];**

for example, if you want to create an array of 10 integers, you have to declare an array as below expression. You can take an array name as your choice (but must follow the naming rule).

**int arr[10];**

### Q) Advantages and disadvantages of Array?

### Ans:

There are many advantages and disadvantages to the array. I am mentioning a few of them.

#### Advantage of Array:

- You can easily store multiple data items of the same type under a single name.
- Using the array index we can randomly access the array elements and Iterating the arrays using their index is faster compared to any other methods like linked list etc.
- We can store and fetch value at run time using the array index.
- It allocates memory in contiguous memory locations for its elements. It does not allocate any extra space/ memory for its elements. Hence there is no memory overflow or shortage of memory in arrays.
- With the help of array, we can implement other data structures like linked lists, stacks, queues, trees, graphs, etc.
- The array can be multidimensional 2D, 3D, …etc.

#### Disadvantages of Array:

- We have to declare the size of an array in advance.
- The array is a static structure. It means array size is always fixed, so we cannot increase or decrease memory allocation.
- Array elements stored at contiguous memory locations so insertion and deletion are quite difficult in an array as the shifting operation is costly.
- Allocating more memory than the requirement leads to wastage of memory space and less allocation of memory also leads to a problem.

### Q) How do you access the values within an array?

### Ans:

Array elements store in a sequential manner, so using the array index we can access the array elements.

Suppose you declare an integer array of size 5.

int data [5];

The first element is data [0], the second element is data [1] and so on. Let’s see the example code,**#include&lt;stdio.h>****int** main(){ **int** data[5]= {1,2,3,4,5}; printf("First Element = %d\n",data[0]); printf("Second Element = %d\n",data[1]); **return** 0;}

**Output:**

First Element = 1
Second Element = 2

### Q) Difference between pointer and array in C?

### Ans:

You can read this Article “[Array vs Pointer](https://aticleworld.com/difference-between-pointer-and-array-in-c/)“.

### Q) Can we pass an array in function as a parameter?

### Ans:

Yes, we can pass.

### Q) What is the output of the below program?

//Assuming size of integer pointer is 4 bytes.**#include &lt;stdio.h>****int** main( **void** ){ //Declare 2D array **int** aiData [3][3]= {1}; printf("%ld\n\n",\*\*aiData); printf("%ld\n\n",\*\*aiData+1); printf("%ld\n\n",\*(\*aiData+1)); printf("%ld\n\n",\*(\*aiData+1)+1); **return** 0;}

### Ans:

1, 2, 0, 1

### Q) What is the output of the below program?

//Assuming the size of the integer is 4 bytes and the beginning address of the array is 0.#include &lt;stdio.h>int main( **void** ){ //Declare 2D array int aiData [3][3]= {1}; printf("%u\n\n",\*aiData); printf("%u\n\n",\*aiData+1); **return** 0;}

### Ans:

0, 4

### Q) What is the output of the below program?

//Assuming the size of the integer is 4 bytes and beginning address of the array is 0.#include &lt;stdio.h>int main(){ //Declare 2D array int aiData [3][3]= {1}; printf("%ld\n\n",aiData); printf("%ld\n\n",aiData+1); **return** 0;}

### Ans:

0, 12

### Q) What is the output of the below program?

//Assuming the size of the integer is 4 bytes and beginning address of the array is 0.**#include &lt;stdio.h>****int** main(){ //Declare 2D array **int** aiData [3][3]= {1}; printf("%ld\n\n",&aiData); printf("%ld\n\n",&aiData+1); **return** 0;}

### Ans:

0, 36

### Question:

Consider a 2d array char arr[10][100];

If the beginning address of the array 0 and size of char is 1 byte, the address of arr[5][25] is?

### Answer:

525

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **int** arr[] = {1,2,3,4,5,6,7,8}; ++\*arr; printf("%u", \*arr); **return** 0;}

### Answer:

2

### Q)What is the output of the below program?

**#include&lt;stdio.h>****int** main(){ **char** acData[11] = "Aticleworld"; printf("%s", acData); **return** 0;}

### Answer:

The behavior of the program unpredictable because you are crossing the array boundary. It might print Aticleworld with garbage value or Aticleworld or get a segmentation fault.

### Q ) What is the difference between array\_name and &array\_name?

### Ans:

To understand this question let’s take an example, suppose arr is an integer array of 5 elements.

**int arr[5];**

If you print arr and &arr then you found the same result but both have different types.

**arr=>**The name of the array is a pointer to its first element. So here arr split as the pointer to the integer.
**&arr=>** It split into the pointer to an array that means &arrwill be similar to int(\*)[5];**#include&lt;stdio.h>****int** main(){ **int** arr[5] = {0}; printf("arr= %u\n\n", arr); printf("&arr= %u\n\n", &arr); printf("arr+1 = %u\n\n", arr+1); printf("&arr+1 = %u\n\n", &arr+1); **return** 0;}

When you compile the above code, you will find arr and &arris same but the output of arr+1 and &arr+1 will be not the same due to the different pointer type.

### Q) Why is it faster to process a sorted array than an unsorted array?

### Ans:

Read this article “[Why sorted array process faster than unsorted array](https://aticleworld.com/faster-process-sorted-array-unsorted-array/)“.

### Q) How to pass an array 1D and 2D as a parameter in C?

### Ans:

You can read this link “[How to pass an array in function as a parameter](https://aticleworld.com/passing-2d-array-to-function/)“.

### Q) What is the output of the C programming (Assumed int size is 4bytes)?

**#include&lt;stdio.h>****int** main(){ **int** (\*arr)[5][4]; //Suppose integer size 4 bytes printf("\*arr size %d", sizeof(\*arr)); **return** 0;}

### Ans:

**\*arr size 80**

**Explanation:**

int (\*arr)[5][4] is a pointer to an array. The total number of elements the 4\*5 and if the integer size is 4 bytes then the size of \*arr will be 80.

### Q) How to find the size of an array in C without using the sizeof operator?

**#include &lt;stdio.h>****int** main(){ **int** ArraySize = 0 ; **int** arr[] = {10, 20, 30, 40, 50, 60}; //Calculate array size using pointer arithmetic ArraySize = \*(&arr + 1) - arr; printf("Array size = %d",ArraySize); **return** 0;}

### Ans:

Array size = 6

### Q) What are the advantages of using an array of pointers to string instead of an array of strings?

### Ans:

An array of pointers to string is useful when sorting the strings, we need to swap only pointers instead of swapping the whole string which helps in the efficient use of memory and time.

### Q) What is the output of the below program?

**#include&lt;stdio.h>****#define VAR\_SIZE 3****int** main(){ **char** \*arr[VAR\_SIZE + ~0] = { "amlendra", "aticleworld" }; **char** \*pchr = arr[1 + ~0]; printf("%s", ++pchr); **return** 0;}

### Answer:

mlendra

### Q) What is the output of the below program?

**#include&lt;stdio.h>****int** main(){ **int** arr[2][3][2]= {9,1,0,3,19,2,6,7,8,78,14,11}; printf("%d",arr[1][0][0]); **return** 0;}

### Ans:

6

### Q) Create a macro to calculate the size of the array.

### Ans:

**#include &lt;stdio.h>****#define SIZEOF(x) ((char\*)(&x + 1) -(char\*)&x)****int** main(){ **int** ArraySize = 0 ; **int** arr[] = {10, 20, 30, 40, 50, 60}; ArraySize = SIZEOF(arr)/SIZEOF(arr[0]); printf("Array Size = %d",ArraySize); **return** 0;}

### Q) What is the difference between pointer to an array and array of pointers?

### Ans:

You can read this Article “[Pointer to an array vs Array of pointers](https://aticleworld.com/difference-between-pointer-to-an-array-and-array-of-pointers/)“.

### Q) What is the output of the program?

**#include &lt;stdio.h>****int** main(**void**){ **char** acData[5] = {'A','B','C','D','E'}; printf("%c ",\*++acData); **return** 0;}

### Ans:

compiler error: lvalue required as increment operand

### Q) How to access a two-dimensional array using pointers in C?

### Ans:

You can read this Article “[Access two-dimensional Array in C](https://aticleworld.com/access-two-dimensional-array-using-pointers-in-c/)“.

### Q) What is the output of the below program?

**#include&lt;stdio.h>****int** main(){ **int** acData[2][3] = {1, 2, 15, 200, 215, 400}; **int**(\*pcData)[2][3] = &acData; printf("%d\t", \*\*\*pcData); printf("%d\t", \*\*\*(pcData + 1)); printf("%d\t", \*\*(\*pcData + 1)); printf("%d\t", \*(\*(\*pcData + 1) + 2)); **return** 0;}

### Ans:

1 ,Garbage value ,200 ,400

### Q) What is a flexible array in C?

### Ans:

A very good feature that is introduced by C99 is a flexible array member. This feature enables the user to create an empty array in a structure, the size of the empty array can be changed at runtime as per the user requirements. This empty array should be declared as the last member of the structure and the structure must contain at least one more named member.**struct** userData{ **int** iTrackNumber; **float** fAmount; //flexible array member **char** acAddress[];};

### Q) What are the rules for declaring a flexible array member?

### Ans:

There are following rules to create a flexible array member in C.

- The flexible array member must be the last member of the structure.
- There must be at least one other member.
- The flexible array is declared like an ordinary array, except that the brackets are empty.

You can read this article for more detail “[flexible array in C](https://aticleworld.com/flexible-array-member/)“.

### Q) How to replace nested switches with the multi-dimensional array in C?

### Ans:

You can read this Article “[Replace the nested switch with Array](https://aticleworld.com/replacing-nested-switches/)“.

### Q) What is the output of the below program?

#include &lt;stdio.h>**void** PrintValue(int arr[]){ int num = sizeof(arr)/sizeof(arr[0]); int index = 0; **for** (index = 0; index &lt; num; index++) { printf("%d ", arr[index]); }}int main(){ int arr[] = {10,20,30,40,50}; PrintValue(arr); **return** 0;}

### Ans:

10

### Q) Can we omit a row of 2D array in C?

### Ans:

Yes, we can omit row.

### Q) Can we declare an array size as a negative number in C language?

### Ans:

No

### Q) What is designated Initializers in array?

### Ans:

The C99 introduces a new mechanism to initialize the elements of the array. It allows you to initialize specific elements of the array in any sequence, you don’t need to initialize the array from the beginning.

In this method, if the size of the array is not given, then the largest initialized position becomes the size of the array (length of the array is the highest value specified plus one), and all uninitialized position initialized with 0.

To specify an array index, write ‘[index] =’ before the element value. For example,**int** a[6] = {[4] = 29, [2] = 15 }; or**int** a[6] = {[4]29 , [2]15 };

The above statement is equivalent to, //It is equivalent to the above expression**int** a[6] = { 0, 0, 15, 0, 29, 0 };

**Note:-** The index values must be constant expressions.

You can read this article for detailed information “[Designated Initializers in C](https://aticleworld.com/designated-initializers-in-cyou-should-know/)“.

### Q) What is the output of the below program?

//Assuming size of integer pointer is 4 bytes.**#include&lt;stdio.h>****int** main(){ **int** arr[] = {10, 20, 30, 40, 50, 60}; **int** \*ptr = (**int**\*)(&arr+1); printf("%d ", \*(ptr - 2) ); **return** 0;}

### Ans:

50

### Q) Can we create an array of a void type?

### Ans:

No.

### Q) What is the output of the below program?

**# include &lt;stdio.h>****int** main(){ **int** index =0 ; **int** aiData[4] = {10}; **for** (index= 0; index &lt; 4; index++) { printf("%d\n", aiData[index]); } **return** 0;}

### Ans:

10 ,0 ,0 ,0

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **int** data = 0; **int** arr[] = {11, 12, 13, 14, 15, 16, 17,18,19}; data = (arr + 3)[1]; printf("%d\n", data); **return** 0;}

### Ans:

15

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **int** index = 0; **int** aiData[10] = {0}; **for** (index = 0; index &lt; 12; index++) { printf("%d ", aiData[index]); } **return** 0;}

### Ans:

Undefined Behaviour (Crossing Array boundary)

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **char** \*pcData="aticleworld"; printf("%c ",6[pcData]); **return** 0;}

### Ans:

w

### Q) What is the output of the below program?

**#include &lt;stdio.h>**//Size of the static array**#define ARRAY\_SIZE sizeof(arr)/sizeof(arr[0])****int** main(){ **int** arr[5] = {[2] = 9, [3] = 8}; **int** i = 0; **for**(i=0; i &lt; ARRAY\_SIZE ; i++) { printf("arr[%d] = %d\n",i, arr[i]); } **return** 0;}

### Ans:

0 , 0 ,9 ,8 ,0  (C99 and above)

### Q) What is the output of the below program?

**#include &lt;stdio.h>****void** Test(**int** n){ **int** i = 0; **int** arr[n]; **for** (i=0; i&lt;n; i++) { arr[i] = i; printf("%d ",arr[i]); }}**int** main(){ Test(3); **return** 0;}

### Ans:

0 , 1 ,2  (C99 and above)

### Q) What is the output of the below program?

**#include &lt;stdio.h>****void** Test(**int** n){ **int** i = 0; **int** arr[n] = {0}; **for** (i=0; i&lt;n; i++) { arr[i] = i; printf("%d ",arr[i]); }}**int** main(){ Test(3); **return** 0;}

### Ans:

Compiler error: a variable-sized object may not be initialized

### Q)What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **static****int** aiData[5]; **int** i=0; aiData[++i]=++i; **for**(i=0; i&lt;5; i++) { printf("%d ",aiData[i]); } **return** 0;}

### Ans:

0 ,0 ,2 ,0 ,0

### Q) What is the output of the below program?

#include &lt;stdio.h>int main(){ int aiData[3][2]= {1,2,3,4,5,6}; printf("%d %d",\*(aiData+1)[1],\*\*(aiData+2)); **return** 0;}

### Ans:

5, 5

### Q) What is the output of the below program?

#include &lt;stdio.h>int size = 4;int arr[size];int main(){ **if**(arr[0]) { printf("Initialized to ZERO"); } **else** { printf("Not initialized to ZERO"); } **return** 0;}

### Ans:

Compile error because the size of the array has been defined using a variable outside of any function.

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main (){ **char** a[] = "aticleworld"; **int** i, j; **for** (i = 0, j = 11; i &lt; j; a [i++] = a [j--]); printf ("%s\n", a); **return** 0;}

### Ans:

Due to null char in the beginning nothing will print.

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main (){ **int** i, j; **int** arr [8] = {10, 20, 30, 40, 50, 60, 70, 80}; **for**(i = 0; i &lt; 3; i++) { arr[i] = arr[i] + 10; i++; } i--; **for** (j = 7; j > 4; j--) { **int** i = j/2; arr[i] = arr[i] - 10; } printf ("%d, %d", i, arr[i]); **return** 0;}

### Ans:

3, 20

### Q) What is the output of the below program?

#include &lt;stdio.h>int main (){ int i, j; char acData1 [2] [3] = {{'a', 'b', 'c'}, {'d', 'e', 'f'}}; char acData2 [3] [2]; char \*pcData = \*acData2; **for** (i = 0; i &lt; 2; i++) { **for** (j = 0; j &lt; 3; j++) { \*(pcData + 2\*j + i) = acData1 [i] [j]; } } **for** (i = 0; i &lt; 3; i++) { **for** (j = 0; j &lt; 2; j++) { printf("%c",acData2[i][j]); } } **return** 0;}

### Ans:

adbecf

### Q) Write is the right way to Initialize array?

### Ans:

See the below example,**int** arr[6] = {1, 9, 3, 7, 41, 15 }; OR **int** arr[] = {9, 3, 7, 41, 15,35};

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main (){ **int** a[] = {2, 1, 6, 9, 5}; **int** i, j, m; i = ++a[1]; j = a[1]++; m = a[i++]; printf("%d, %d, %d, %d", j, i, m,a[1]); **return** 0;}

### Ans:

2 ,3 ,6 ,3

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **char** acData[] = "aticle\0world"; printf("%s", acData); **return** 0;}

### Ans:

aticle

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **int** aiData[5] = {10,20,30,40}; printf("%d", aiData[4]); **return** 0;}

### Ans:

0

### Q)What is the size of the array?

//suppose int size is 4 byte#include &lt;stdio.h>typedef int ArrType[30];ArrType arr[20];int main(){ printf("%d", sizeof(arr)); **return** 0;}

### Ans:

2400

### Question:

What does the below declaration mean?
int (\*ptr)[5];

### Ans:

ptr is a pointer to an array of 5 integers.

### Q) What is the output of the below program?

**#include &lt;stdio.h>****int** main(){ **int** a[5]; printf("%d %d", a[-2], a[7]); **return** 0;}

### Ans:

Undefined behavior

### Q) What is the output of the below program?

**#include&lt;stdio.h>****union** sInfo{ **int** a; **char** b[2];};**int** main(){ **union** sInfo s1; s1.a=512; printf("%d %d %d ",s1.a,s1.b[0]++,s1.b[1]++); **return** 0;}

### Ans:

Depend on endianness

### Q) What is the output of the below program?

**#include&lt;stdio.h>****int** main(){ **int** arr[]= {299,6,0,6,9,4}; **int** \*ptr = arr; \*((**char**\*)ptr)++; printf("%d %d ",arr[0],arr[1]); **return** 0;}

### Ans:

error: lvalue required as increment operand.

### Q) What is the output of the below program?

**#include&lt;stdio.h>****int** main(){ **int** arr[]= {299,6,0,6,9,4}; **int** \*ptr = arr; \*((**char**\*)ptr++) = 1; printf("%d %d ",arr[0],arr[1]); **return** 0;}

### Ans:

257 ,6

I believe that the above-mentioned array of interview questions were helpful. Some unsolved array interview questions for you. If you want you can check the solution by clicking the link. But I want you to try these interview questions on an array without seeing the solution. You can match your solution with mine. Also if have any suggestion and feedback, please write in the comment box. Thanks for your supports and love.
