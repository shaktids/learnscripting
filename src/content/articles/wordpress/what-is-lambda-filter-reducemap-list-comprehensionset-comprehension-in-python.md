---
title: "What is Lambda, Filter, Reduce,Map & List Comprehension,Set Comprehension in Python"
description: "Although we all know that in python def(): is used to create a function,We can use a def() as er our requirement and modify accordingly.Sometimes its…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2018-10-20T04:20:33Z
legacy: true
wpId: 132
---

*Although we all know that in python def(): is used to create a function,We can use a def() as er our requirement and modify accordingly.Sometimes its necessary to create a one line function known as Lambda.Which can be created by just in demand situation where it can  behave like an normal definition.* We can see the result: lambda, map() and filter() are still part of core Python. Only reduce() had to go it is moved into the module `functools`.

- There is an equally powerful alternative to lambda, filter, map and reduce, i.e. list comprehension

- List comprehension is more evident and easier to understand

- Having both list comprehension and "Filter, map, reduce and lambda" is transgressing the Python motto "There should be one obvious way to solve a problem"

## Lambda
Some like it, others feels complicated lambda operator. The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name. These functions are throw-away functions, i.e. they are just needed where they have been created. Lambda functions are mainly used in combination with the functions filter(), map() and reduce(). The lambda feature was added to Python due to the demand from Lisp programmers.

The general syntax of a lambda function is quite simple:

### `lambda argument_list: expression`

The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments. You can assign the function to a variable to give it a name.

The following example of a lambda function returns the average of its two arguments:

```
xx=lambda y:y*5
print(xx(55))
```

The above example might look like a plaything for a mathematician. A formalism which turns an easy to comprehend issue into an abstract harder to grasp formalism. Above all, we could have had the same effect by just using the following conventional function definition:

```
def xx(y):
    return y*5
print(xx(55))
```

We can assure you that the advantages of this approach will be apparent, when you will have learnt to use the map() function.

https://www.youtube.com/watch?v=X95asa6veXQ&feature=youtu.be

## Lambda with if condition

https://www.youtube.com/watch?v=V-LLcffaSro&t

## The map() Function

The lambda operator can be seen when it is used in combination with the map() function.The map() is a function which takes two arguments the first one is the function and second one on which it needs to map the function.

### r = map(func, seq)
The first argument *func* is the name of a function and the second a sequence (e.g. a list) *seq*. *map()* applies the function *func* to all the elements of the sequence *seq*. Before Python3, map() used to return a list, where each element of the result list was the result of the function *func* applied on the corresponding element of the list or tuple "seq". With Python 3, map() returns an iterator.

In the below example we are calculating the total travel cost.Our `distance=[30,50,80,12,90,40,60,20]` list contain the number of distances.We are calculating the distance by car and bike and storing inside the respective list.We are using the lambda for creating inline function.And by using map we are mapping the function over the list of n elements.

`distance=[30,50,80,12,90,40,60,20]`
`costByCar=[]`
`costByBike=[]`
`car=lambda x:x*4`
`costByCar=map(car,distance)`
`print(list(costByCar))`
`bike=lambda x:x*2`
`costByBike=map(bike,distance)`
`print(list(costByBike))`

The below lines of code are the generic way of python definition to create a function and do same thing

`def calcostByCar():`
`for i in distance:`
`#Per kilomeater i am considering 4$ as traveliing cost`
`costByCar.append(i*4)`
`calcostByCar()`
`print("Cost by car :",costByCar)`
`def calcostByBike():`
`for i in distance:`
`#Per kilomeater i am considering 2$ as traveliing cost`
`costByBike.append(i*2)`
`calcostByBike()`
`print("Cost by bike :",costByBike)`

Output of the above program is as below.
[120, 200, 320, 48, 360, 160, 240, 80]
[60, 100, 160, 24, 180, 80, 120, 40]

## Filtering

The function

`filter(function, sequence)`

offers an elegant way to filter out all the elements of a sequence "sequence", for which the function *function* returns True. i.e. an item will be produced by the iterator result of filter(function, sequence) if item is included in the sequence "sequence" and if function(item) returns True.

In other words: The function filter(f,l) needs a function f as its first argument. f has to return a Boolean value, i.e. either True or False. This function will be applied to every element of the list *l*. Only if f returns True will the element be produced by the iterator, which is the return value of filter(function, sequence).

In the following example, we filter out first the odd and then the even elements of the sequence of the first 11 Fibonacci numbers:

```
>>> fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
>>> odd_numbers = list(filter(lambda x: x % 2, fibonacci))
>>> print(odd_numbers)
[1, 1, 3, 5, 13, 21, 55]
>>> even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]
>>>
>>>
>>> # or alternatively:
...
>>> even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]
>>>
```

## Reducing a List

As we mentioned in the introduction of this chapter of our tutorial. reduce() had been dropped from the core of Python when migrating to Python 3. Guido van Rossum hates reduce(), as we can learn from his statement in a posting, March 10, 2005, in artima.com:
> *"So now reduce(). This is actually the one I've always hated most, because, apart from a few examples involving + or \*, almost every time I see a reduce() call with a non-trivial function argument, I need to grab pen and paper to diagram what's actually being fed into that function before I understand what the reduce() is supposed to do. So in my mind, the applicability of reduce() is pretty much limited to associative operators, and in all other cases it's better to write out the accumulation loop explicitly."*

The function

### `reduce(func, seq)`

continually applies the function func() to the sequence seq. It returns a single value.

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:

- At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]

- In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
  The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]

- Continue like this until just one element is left and return this element as the result of reduce()

If n is equal to 4 the previous explanation can be illustrated like this: ![Reduce](/images/wp/reduce-79a5c752.png)

We want to illustrate this way of working of reduce() with a simple example. We have to import functools to be capable of using reduce:

```
>>> import functools
>>> functools.reduce(lambda x,y: x+y, [47,11,42,13])
113
>>>
```

The following diagram shows the intermediate steps of the calculation:

![Reduce: Method of operating](/images/wp/reduce-diagram-d87e0427.png)

### Examples of reduce()

Determining the maximum of a list of numerical values by using reduce:

```
>>> from functools import reduce
>>> f = lambda a,b: a if (a > b) else b
>>> reduce(f, [47,11,42,102,13])
102
>>>
```

Calculating the sum of the numbers from 1 to 100:

```
>>> from functools import reduce
>>> reduce(lambda x, y: x+y, range(1,101))
5050
```

It's very simple to change the previous example to calculate the product (the factorial) from 1 to a number, but do not choose 100. We just have to turn the "+" operator into "\*":

```
>>> reduce(lambda x, y: x*y, range(1,49))
12413915592536072670862289047373375038521486354677760000000000
```

If you are into lottery, here are the chances to win a 6 out of 49 drawing:

```
>>> reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7))
13983816.0
>>>
```

## List Comprehension

### Introduction

![alternative to map, filter, reduce and lambda](/images/wp/alternative-lambda-map-e2e05947.png) We learned  "Lambda Operator, Filter, Reduce and Map" that Guido van Rossum prefers list comprehensions to constructs using map, filter, reduce and lambda. In this chapter we will cover the essentials about list comprehensions. List comprehensions were added with Python 2.0. Essentially, it is Python's way of implementing a well-known notation for sets as used by mathematicians.
In mathematics the square numbers of the natural numbers are, for example, created by { x2 | x ∈ ℕ } or the set of complex integers { (x,y) | x ∈ ℤ ∧ y ∈ ℤ }.

List comprehension is an elegant way to define and create list in Python. These lists have often the qualities of sets, but are not in all cases sets.

List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce(). For most people the syntax of list comprehension is easier to be grasped.

### Examples

In the chapter on lambda and map() we had designed a map() function to convert Celsius values into Fahrenheit and vice versa. It looks like this with list comprehension:

```
>>> Celsius = [39.2, 36.5, 37.3, 37.8]
>>> Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
>>> print Fahrenheit
[102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
>>>
```

The following list comprehension creates the Pythagorean triples:

```
>>> [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]
>>>
```

Cross product of two sets:

```
>>> colours = [ "red", "green", "yellow", "blue" ]
>>> things = [ "house", "car", "tree" ]
>>> coloured_things = [ (x,y) for x in colours for y in things ]
>>> print coloured_things
[('red', 'house'), ('red', 'car'), ('red', 'tree'), ('green', 'house'), ('green', 'car'), ('green', 'tree'), ('yellow', 'house'), ('yellow', 'car'), ('yellow', 'tree'), ('blue', 'house'), ('blue', 'car'), ('blue', 'tree')]
>>>
```

## Generator Comprehension

Generator comprehensions were introduced with Python 2.6. They are simply a generator expression with a parenthesis - round brackets - around it. Otherwise, the syntax and the way of working is like list comprehension, but a generator comprehension returns a generator instead of a list.

```
>>> x = (x **2 for x in range(20))
>>> print(x)
 at 0xb7307aa4>
>>> x = list(x)
>>> print(x)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
```

### A more Demanding Example

Calculation of the prime numbers between 1 and 100 using the sieve of Eratosthenes:

```
>>> noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
>>> primes = [x for x in range(2, 100) if x not in noprimes]
>>> print primes
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
>>>
```

We want to bring the previous example into more general form, so that we can calculate the list of prime numbers up to an arbitrary number n:

```
>>> from math import sqrt
>>> n = 100
>>> sqrt_n = int(sqrt(n))
>>> no_primes = [j for i in range(2,sqrt_n) for j in range(i*2, n, i)]
```

If we have a look at the content of no\_primes, we can see that we have a problem. There are lots of double entries contained in this list:

```
>>> no_primes
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
>>>
```

The solution to this intolerable problem comes with the set comprehension, which we will cover in the next section.

## Set Comprehension

A set comprehension is similar to a list comprehension, but returns a set and not a list. Syntactically, we use curly brackets instead of square brackets to create a set. Set comprehension is the right functionality to solve our problem from the previous subsection. We are able to create the set of non primes without doublets:

```
>>> from math import sqrt
>>> n = 100
>>> sqrt_n = int(sqrt(n))
>>> no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
>>> no_primes
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99}
>>> primes = {i for i in range(n) if i not in no_primes}
>>> print(primes)
{0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
>>>
```

### Recursive Function to Calculate the Primes

The following Python script uses a recursive function to calculate the prime numbers. It incorporates the fact that it is enough to examine the multiples of the prime numbers up to the square root of n:

```
from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in xrange(i*2, n+1, i)}
        p = {x for x in xrange(2, n + 1) if x not in no_p}
    return p

for i in range(1,50):
    print i, primes(i)
```
