---
title: "Data types in Python or Different Types of Objects in Python"
description: "Every language has its own data types and data structures. Depending upon the data when we create a variable that is known as static typing.Where we can…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2017-09-17T03:53:43Z
legacy: true
wpId: 925
---

Every language has its own data types and data structures. Depending upon the data when we create a variable that is known as static typing.Where we can not able to store any other types of data into the variable.But pyhton not operate the same way.It has the concept of dynamic typing where the data can be stored in the different data objects.We will go through the data types and the operation available for the particular data types.

Python has below standard Data Types:

- Numbers

- String

- List

- Set

- Tuple

- Dictionary

- Sets

- ByteArray

Python sets the variable type based on the value that is assigned to it. Unlike more riggers languages, Python will change the variable type if the variable value is set to another value. For example:

```python
var = 123 # This will create a number integer assignment
var = 'john' # the `var` variable is now a string type.
```

# Numbers

Python numbers variables are created by the standard Python method:

```python
var = 382
```

Most of the time using the standard Python number type is fine. Python will automatically convert a number from one type to another if it needs. But, under certain circumstances that a specific number type is needed (ie. complex, hexidecimal), the format can be forced into a format by using additional syntax in the table below:

|
 Type |
  |
  |
 Format |
  |
  |
 Description |

|
 int |
  |
  |
 a = 10 |
  |
  |
 Signed Integer |

|
 long |
  |
  |
 a = 345L |
  |
  |
 (L) Long integers, they can also be represented in octal and hexadecimal |

|
 float |
  |
  |
 a = 45.67 |
  |
  |
 (.) Floating point real values |

|
 complex |
  |
  |
 a = 3.14J |
  |
  |
 (J) Contains integer in the range 0 to 255. |

|
  |
  |
  |
  |
  |
  |
  |

Most of the time Python will do variable conversion automatically. You can also use Python conversion functions (int(), long(), float(), complex()) to convert data from one type to another. In addition, the `type` function returns information about how your data is stored within a variable.

```python
message = "Good morning"
num = 85
pi = 3.14159

print(type(message))  # This will return a string
print(type(n))  # This will return an integer
print(type(pi))  # This will return a float
```

# String

Create string variables by enclosing characters in quotes. Python uses single quotes `'` double quotes `"` and triple quotes `"""` to denote literal strings. Only the triple quoted strings `"""` also will automatically continue across the end of line statement.

```python
firstName = 'john'
lastName = "smith"
message = """This is a string that will span across multiple lines. Using newline characters
and no spaces for the next lines. The end of lines within this string also count as a newline when printed"""
```

Strings can be accessed as a whole string, or a substring of the complete variable using brackets ‘[]’. Here are a couple examples:

```python
var1 = 'Hello World!'
var2 = 'RhinoPython'

print var1[0] # this will print the first character in the string an `H`
print var2[1:5] # this will print the substring 'hinoP`
```

Python can use a special syntax to format multiple strings and numbers. The string formatter is quickly covered here because it is seen often and it is important to recognize the syntax.

```python
print "The item {} is repeated {} times".format(element,count))
```

The `{}` are placeholders that are substituted by the variables `element` and `count` in the final string. This compact syntax is meant to keep the code more readable and compact.

Python is currently transitioning to the format syntax above, but python can use an older syntax, which is being phased out, but is still seen in some example code:

```python
print "The item %i is repeated %i times"% (element,count)
```

For more information on the string formatter in Python see the article: PyFormat Website

For a more detailed look at string variables in Python, see the Tutorialspoint Python Tutorial on stings. Note: this article does use the older formatting syntax, but has a lot useful information.

##### String Formatting Operator

One of Python's coolest features is the string format operator %. This operator is unique to strings and makes up for the pack of having functions from C's printf() family. Following is a simple example −

```
#!/usr/bin/python

print "My name is %s and weight is %d kg!" % ('Zara', 21)
```

When the above code is executed, it produces the following result −

```
My name is Zara and weight is 21 kg!
```

Here is the list of complete set of symbols which can be used along with % −

|
 Format Symbol |
 Conversion |

|
 %c |
 character |

|
 %s |
 string conversion via str() prior to formatting |

|
 %i |
 signed decimal integer |

|
 %d |
 signed decimal integer |

|
 %u |
 unsigned decimal integer |

|
 %o |
 octal integer |

|
 %x |
 hexadecimal integer (lowercase letters) |

|
 %X |
 hexadecimal integer (UPPERcase letters) |

|
 %e |
 exponential notation (with lowercase 'e') |

|
 %E |
 exponential notation (with UPPERcase 'E') |

|
 %f |
 floating point real number |

|
 %g |
 the shorter of %f and %e |

|
 %G |
 the shorter of %f and %E |

Other supported symbols and functionality are listed in the following table −

|
 Symbol |
 Functionality |

|
 \* |
 argument specifies width or precision |

|
 - |
 left justification |

|
 + |
 display the sign |

|
 &lt;sp> |
 leave a blank space before a positive number |

|
 # |
 add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used. |

|
 0 |
 pad from left with zeros (instead of spaces) |

|
 % |
 '%%' leaves you with a single literal '%' |

|
 (var) |
 mapping variable (dictionary arguments) |

|
 m.n. |
 m is the minimum total width and n is the number of digits to display after the decimal point (if appl.) |

##### String Special Operators

Assume string variable **a** holds 'Hello' and variable **b** holds 'Python', then −

|
 Operator |
 Description |
 Example |

|
 + |
 Concatenation - Adds values on either side of the operator |
 a + b will give HelloPython |

|
 \* |
 Repetition - Creates new strings, concatenating multiple copies of the same string |
 a\*2 will give -HelloHello |

|
 [] |
 Slice - Gives the character from the given index |
 a[1] will give e |

|
 [ : ] |
 Range Slice - Gives the characters from the given range |
 a[1:4] will give ell |

|
 in |
 Membership - Returns true if a character exists in the given string |
 H in a will give 1 |

|
 not in |
 Membership - Returns true if a character does not exist in the given string |
 M not in a will give 1 |

|
 r/R |
 Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark. |
 print r'\n' prints \n and print R'\n'prints \n |

|
 % |
 Format - Performs String formatting |
 See at next section |

#### Built-in String Methods

Python includes the following built-in methods to manipulate strings −

|
 SN |
 Methods with Description |

|
 1 |
 capitalize()  Capitalizes first letter of string |

|
 2 |
 center(width, fillchar) |

Returns a space-padded string with the original string centered to a total of width columns.

|
 3 |
 count(str, beg= 0,end=len(string)) |

Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.

|
 4 |
 decode(encoding='UTF-8',errors='strict') |

Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

|
 5 |
 encode(encoding='UTF-8',errors='strict') |

Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

|
 6 |
 endswith(suffix, beg=0, end=len(string))  Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise. |

|
 7 |
 expandtabs(tabsize=8) |

Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

|
 8 |
 find(str, beg=0 end=len(string)) |

Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.

|
 9 |
 index(str, beg=0, end=len(string)) |

Same as find(), but raises an exception if str not found.

|
 10 |
 isalnum() |

Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

|
 11 |
 isalpha() |

Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

|
 12 |
 isdigit() |

Returns true if string contains only digits and false otherwise.

|
 13 |
 islower() |

Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

|
 14 |
 isnumeric() |

Returns true if a unicode string contains only numeric characters and false otherwise.

|
 15 |
 isspace() |

Returns true if string contains only whitespace characters and false otherwise.

|
 16 |
 istitle() |

Returns true if string is properly "titlecased" and false otherwise.

|
 17 |
 isupper() |

Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

|
 18 |
 join(seq) |

Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

|
 19 |
 len(string) |

Returns the length of the string

|
 20 |
 ljust(width[, fillchar]) |

Returns a space-padded string with the original string left-justified to a total of width columns.

|
 21 |
 lower() |

Converts all uppercase letters in string to lowercase.

|
 22 |
 lstrip() |

Removes all leading whitespace in string.

|
 23 |
 maketrans() |

Returns a translation table to be used in translate function.

|
 24 |
 max(str) |

Returns the max alphabetical character from the string str.

|
 25 |
 min(str) |

Returns the min alphabetical character from the string str.

|
 26 |
 replace(old, new [, max]) |

Replaces all occurrences of old in string with new or at most max occurrences if max given.

|
 27 |
 rfind(str, beg=0,end=len(string)) |

Same as find(), but search backwards in string.

|
 28 |
 rindex( str, beg=0, end=len(string)) |

Same as index(), but search backwards in string.

|
 29 |
 rjust(width,[, fillchar]) |

Returns a space-padded string with the original string right-justified to a total of width columns.

|
 30 |
 rstrip() |

Removes all trailing whitespace of string.

|
 31 |
 split(str="", num=string.count(str)) |

Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.

|
 32 |
 splitlines( num=string.count('\n')) |

Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

|
 33 |
 startswith(str, beg=0,end=len(string)) |

Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

|
 34 |
 strip([chars]) |

Performs both lstrip() and rstrip() on string

|
 35 |
 swapcase() |

Inverts case for all letters in string.

|
 36 |
 title() |

Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

|
 37 |
 translate(table, deletechars="") |

Translates string according to translation table str(256 chars), removing those in the del string.

|
 38 |
 upper() |

Converts lowercase letters in string to uppercase.

|
 39 |
 zfill (width) |

Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).

|
 40 |
 isdecimal() |

Returns true if a unicode string contains only decimal characters and false otherwise.

# List

Lists are a very useful variable type in Python. A list can contain a series of values. List variables are declared by using brackets `[ ]` following the variable name.

```python
A = [ ] # This is a blank list variable
B = [1, 23, 45, 67] # this list creates an initial list of 4 numbers.
C = [2, 4, 'john'] # lists can contain different variable types.
```

All lists in Python are zero-based indexed. When referencing a member or the length of a list the number of list elements is always the number shown plus one.

```python
mylist = ['Rhino', 'Grasshopper', 'Flamingo', 'Bongo']
B = len(mylist) # This will return the length of the list which is 3. The index is 0, 1, 2, 3.
print mylist[1] # This will return the value at index 1, which is 'Grasshopper'
print mylist[0:2] # This will return the first 3 elements in the list.
```

You can assign data to a specific element of the list using an index into the list. The list index starts at zero. Data can be assigned to the elements of an array as follows:

```python
mylist = [0, 1, 2, 3]
mylist[0] = 'Rhino'
mylist[1] = 'Grasshopper'
mylist[2] = 'Flamingo'
mylist[3] = 'Bongo'
print mylist[1]
```

Lists aren’t limited to a single dimension. Although most people can’t comprehend more than three or four dimensions. You can declare multiple dimensions by separating an with commas. In the following example, the MyTable variable is a two-dimensional array :

```python
MyTable = [[], []]
```

In a two-dimensional array, the first number is always the number of rows; the second number is the number of columns.

For a detailed look at managing lists, take a look at the article

- Python Lists - Google developer

- TutorialPoint Python Lists

#### Built-in List Functions & Methods:

Python includes the following list functions −

|
 SN |
 Function with Description |

|
 1 |
 cmp(list1, list2) |

Compares elements of both lists.

|
 2 |
 len(list) |

Gives the total length of the list.

|
 3 |
 max(list) |

Returns item from the list with max value.

|
 4 |
 min(list) |

Returns item from the list with min value.

|
 5 |
 list(seq) |

Converts a tuple into list.

Python includes following list methods

|
 SN |
 Methods with Description |

|
 1 |
 list.append(obj) |

Appends object obj to list

|
 2 |
 list.count(obj) |

Returns count of how many times obj occurs in list

|
 3 |
 list.extend(seq) |

Appends the contents of seq to list

|
 4 |
 list.index(obj) |

Returns the lowest index in list that obj appears

|
 5 |
 list.insert(index, obj) |

Inserts object obj into list at offset index

|
 6 |
 list.pop(obj=list[-1]) |

Removes and returns last object or obj from list

|
 7 |
 list.remove(obj) |

Removes object obj from list

|
 8 |
 list.reverse() |

Reverses objects of list in place

|
 9 |
 list.sort([func]) |

# Tuple

Tuples are a group of values like a list and are manipulated in similar ways. But, tuples are fixed in size once they are assigned. In Python the fixed size is considered immutable as compared to a list that is dynamic and mutable. Tuples are defined by parenthesis ().

```python
myGroup = ('Rhino', 'Grasshopper', 'Flamingo', 'Bongo')
```

Here are some advantages of tuples over lists:

1. Elements to a tuple. Tuples have no append or extend method.

2. Elements cannot be removed from a tuple.

3. You can find elements in a tuple, since this doesn’t change the tuple.

4. You can also use the in operator to check if an element exists in the tuple.

5. Tuples are faster than lists. If you’re defining a constant set of values and all you’re ever going to do with it is iterate through it, use a tuple instead of a list.

6. It makes your code safer if you “write-protect” data that does not need to be changed.

It seems tuples are very restrictive, so why are they useful? There are many datastructures in Rhino that require a fixed set of values. For instance a Rhino point is a list of 3 numbers `[34.5, 45.7, 0]`. If this is set as tuple, then you can be assured the original 3 number structure stays as a point `(34.5, 45.7, 0)`. There are other datastructures such as lines, vectors, domains and other data in Rhino that also require a certain set of values that do not change. Tuples are great for this.

A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also. For example −

```
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
```

The empty tuple is written as two parentheses containing nothing −

```
tup1 = ();
```

To write a tuple containing a single value you have to include a comma, even though there is only one value −

```
tup1 = (50,);
```

Like string indices, tuple indices start at 0, and they can be sliced, concatenated, and so on.

## Accessing Values in Tuples:

To access values in tuple, use the square brackets for slicing along with the index or indices to obtain value available at that index. For example −

```
#!/usr/bin/python

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
```

When the above code is executed, it produces the following result −

```
tup1[0]:  physics
tup2[1:5]:  [2, 3, 4, 5]
```

## Updating Tuples

Tuples are immutable which means you cannot update or change the values of tuple elements. You are able to take portions of existing tuples to create new tuples as the following example demonstrates −

```
#!/usr/bin/python

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3
```

When the above code is executed, it produces the following result −

```
(12, 34.56, 'abc', 'xyz')
```

## Delete Tuple Elements

Removing individual tuple elements is not possible. There is, of course, nothing wrong with putting together another tuple with the undesired elements discarded.

To explicitly remove an entire tuple, just use the **del** statement. For example:

```
#!/usr/bin/python

tup = ('physics', 'chemistry', 1997, 2000);

print tup
del tup;
print "After deleting tup : "
print tup
```

This produces the following result. Note an exception raised, this is because after **del tup** tuple does not exist any more −

```
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print tup;
NameError: name 'tup' is not defined
```

## Basic Tuples Operations

Tuples respond to the + and \* operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.

In fact, tuples respond to all of the general sequence operations we used on strings in the prior chapter −

|
 Python Expression |
 Results |
 Description |

|
 len((1, 2, 3)) |
 3 |
 Length |

|
 (1, 2, 3) + (4, 5, 6) |
 (1, 2, 3, 4, 5, 6) |
 Concatenation |

|
 ('Hi!',) \* 4 |
 ('Hi!', 'Hi!', 'Hi!', 'Hi!') |
 Repetition |

|
 3 in (1, 2, 3) |
 True |
 Membership |

|
 for x in (1, 2, 3): print x, |
 1 2 3 |
 Iteration |

## Indexing, Slicing, and Matrixes

Because tuples are sequences, indexing and slicing work the same way for tuples as they do for strings. Assuming following input −

```
L = ('spam', 'Spam', 'SPAM!')
```

| Python Expression | Results | Description |
| --- | --- | --- |
| L[2] | 'SPAM!' | Offsets start at zero |
| L[-2] | 'Spam' | Negative: count from the right |
| L[1:] | ['Spam', 'SPAM!'] | Slicing fetches sections |

## No Enclosing Delimiters

Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples −

```
#!/usr/bin/python

print 'abc', -4.24e93, 18+6.6j, 'xyz'
x, y = 1, 2;
print "Value of x , y : ", x,y
```

When the above code is executed, it produces the following result −

```
abc -4.24e+93 (18+6.6j) xyz
Value of x , y : 1 2
```

## Built-in Tuple Functions

Python includes the following tuple functions −

| SN | Function with Description |
| --- | --- |
| 1 | cmp(tuple1, tuple2) Compares elements of both tuples. |

|
 2 |
 len(tuple) Gives the total length of the tuple. |

|
 3 |
 max(tuple) Returns item from the tuple with max value. |

|
 4 |
 min(tuple) Returns item from the tuple with min value. |

|
 5 |
 tuple(seq) Converts a list into tuple. |

# Dictionary

Dictionaries in Python are lists of `Key`:`Value` pairs. This is a very powerful datatype to hold a lot of related information that can be associated through `keys`. The main operation of a dictionary is to extract a value based on the `key` name. Unlike lists, where index numbers are used, dictionaries allow the use of a `key` to access its members. Dictionaries can also be used to sort, iterate and compare data.

Dictionaries are created by using braces ({}) with pairs separated by a comma (,) and the key values associated with a colon(:). In Dictionaries the `Key` must be unique. Here is a quick example on how dictionaries might be used:

```python
room_num = {'john': 425, 'tom': 212}
room_num['john'] = 645  # set the value associated with the 'john' key to 645
print (room_num['tom']) # print the value of the 'tom' key.
room_num['isaac'] = 345 # Add a new key 'isaac' with the associated value
print (room_num.keys()) # print out a list of keys in the dictionary
print ('isaac' in room_num) # test to see if 'issac' is in the dictionary.  This returns true.
```

Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: {}.

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

## Accessing Values in Dictionary:

To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Following is a simple example −

```
#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
```

When the above code is executed, it produces the following result −

```
dict['Name']:  Zara
dict['Age']:  7
```

If we attempt to access a data item with a key, which is not part of the dictionary, we get an error as follows −

```
#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Alice']: ", dict['Alice']
```

When the above code is executed, it produces the following result −

```
dict['Alice']:
Traceback (most recent call last):
   File "test.py", line 4, in <module>
      print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'
```

## Updating Dictionary

You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown below in the simple example −

```
#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
```

When the above code is executed, it produces the following result −

```
dict['Age']:  8
dict['School']:  DPS School
```

## Delete Dictionary Elements

You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation.

To explicitly remove an entire dictionary, just use the **del** statement. Following is a simple example −

```
#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']
```

This produces the following result. Note that an exception is raised because after **del dict** dictionary does not exist any more −

```
dict['Age']:
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print "dict['Age']: ", dict['Age'];
TypeError: 'type' object is unsubscriptable
```

**Note:** del() method is discussed in subsequent section.

## Properties of Dictionary Keys

Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. However, same is not true for the keys.

There are two important points to remember about dictionary keys −

**(a)** More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. For example −

```
#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}

print "dict['Name']: ", dict['Name']
```

When the above code is executed, it produces the following result −

```
dict['Name']:  Manni
```

**(b)** Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example:

```
#!/usr/bin/python

dict = {['Name']: 'Zara', 'Age': 7}

print "dict['Name']: ", dict['Name']
```

When the above code is executed, it produces the following result −

```
Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'Zara', 'Age': 7};
TypeError: list objects are unhashable
```

## Built-in Dictionary Functions & Methods −

Python includes the following dictionary functions −

| SN | Function with Description |
| --- | --- |
| 1 | cmp(dict1, dict2) Compares elements of both dict. |

|
 2 |
 len(dict) Gives the total length of the dictionary. This would be equal to the number of items in the dictionary. |

|
 3 |
 str(dict) Produces a printable string representation of a dictionary |

|
 4 |
 type(variable) Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type. |

Python includes following dictionary methods −

|
 SN |
 Methods with Description |

|
 1 |
 dict.clear() Removes all elements of dictionary *dict* |

|
 2 |
 dict.copy() Returns a shallow copy of dictionary *dict* |

|
 3 |
 dict.fromkeys() Create a new dictionary with keys from seq and values *set* to *value*. |

|
 4 |
 dict.get(key, default=None) For *key* key, returns value or default if key not in dictionary |

|
 5 |
 dict.has\_key(key) Returns *true* if key in dictionary *dict*, *false* otherwise |

|
 6 |
 dict.items() Returns a list of *dict*'s (key, value) tuple pairs |

|
 7 |
 dict.keys() Returns list of dictionary dict's keys |

|
 8 |
 dict.setdefault(key, default=None) Similar to get(), but will set dict[key]=default if *key* is not already in dict |

|
 9 |
 dict.update(dict2) Adds dictionary *dict2*'s key-values pairs to *dict* |

|
 10 |
 dict.values() Returns list of dictionary *dict*'s values |

# Sets
