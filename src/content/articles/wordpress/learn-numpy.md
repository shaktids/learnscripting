---
title: "Learn Numpy"
description: "Numpy is a general purpose array processing package. It provides a high performance multidimensional array object, and tools for working with these…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2019-08-03T12:31:35Z
legacy: true
wpId: 1729
---

**Numpy**is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.
Besides its obvious scientific uses, Numpy can also be used as an efficient multi-dimensional container of generic data.

## Numpy Array

Array in Numpy is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers. In Numpy, number of dimensions of the array is called rank of the array.A tuple of integers giving the size of the array along each dimension is known as shape of the array. An array class in Numpy is called as **ndarray**. Elements in Numpy arrays are accessed by using square brackets and can be initialized by using nested Python Lists.

**Creating a Numpy Array**
Arrays in Numpy can be created by multiple ways, with various number of Ranks, defining the size of the Array. Arrays can also be created with the use of various data types such as lists, tuples, etc. The type of the resultant array is deduced from the type of the elements in the sequences.

Below are some of the basic numpy functions available for the mathematical operation on the data.

1.np.array
2.np.shape
3.np.zeros
4.np.empty
5np.eye

## 1.np.array(list)-To convert the python list to numpy array.
`numpy.``array`(*object*, *dtype=None*, *copy=True*, *order=’K’*, *subok=False*, *ndmin=0*)

Create an array.

|  |  |
| --- | --- |
| Parameters: | **object** : array\_like An array, any object exposing the array interface, an object whose \_\_array\_\_ method returns an array, or any (nested) sequence. **dtype** : data-type, optional The desired data-type for the array. If not given, then the type will be determined as the minimum type required to hold the objects in the sequence. This argument can only be used to ‘upcast’ the array. For downcasting, use the .astype(t) method. **copy** : bool, optional If true (default), then the object is copied. Otherwise, a copy will only be made if \_\_array\_\_ returns a copy, if obj is a nested sequence, or if a copy is needed to satisfy any of the other requirements ([`dtype`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html#numpy.dtype), *order*, etc.). **order** : {‘K’, ‘A’, ‘C’, ‘F’}, optional Specify the memory layout of the array. If object is not an array, the newly created array will be in C order (row major) unless ‘F’ is specified, in which case it will be in Fortran order (column major). If object is an array the following holds. order no copy copy=True ‘K’ unchanged F & C order preserved, otherwise most similar order ‘A’ unchanged F order if input is F and not C, otherwise C order ‘C’ C order C order ‘F’ F order F order When `copy=False` and a copy is made for other reasons, the result is the same as if `copy=True`, with some exceptions for *A*, see the Notes section. The default order is ‘K’. **subok** : bool, optional If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array (default). **ndmin** : int, optional Specifies the minimum number of dimensions that the resulting array should have. Ones will be pre-pended to the shape as needed to meet this requirement. |
| Returns: | **out** : ndarray An array object satisfying the specified requirements. |

Below Example of creating numpy array from the single list

```
import numpy as np
ls=[1,2,34,5]
print("Type of ls=",type(ls))
np_arr=np.array(ls)
print("Printing Numpy Array:",np_arr)
print("Type of numpy Array",type(np_arr))
print("Dimension of numpy array",np_arr.ndim)
```

Output

“C:\Python 37\python.exe” C:/Users/shakdas/PycharmProjects/untitled/NumpyTest/Sample1.py
Type of ls=
Printing Numpy Array: [ 1 2 34 5]
Type of numpy Array
Dimension of numpy array 1

Process finished with exit code 0

**Below Example of creating numpy array form the multiple list**

```
import numpy as np
ls=[1,2,34,5]
ls1=[6,7,8,9]
ls2=[ls,ls1]
print("Type of ls=",type(ls2))
np_arr=np.array(ls2)
print("Printing Numpy Array:",np_arr)
print("Type of numpy Array",type(np_arr))
print("Dimension of numpy array",np_arr.ndim)
```

Output

“C:\Python 37\python.exe” C:/Users/shakdas/PycharmProjects/untitled/NumpyTest/Sample1.py
Type of ls=
Printing Numpy Array: [[ 1 2 34 5]
[ 6 7 8 9]]
Type of numpy Array
Dimension of numpy array 2

Process finished with exit code 0

## 2. ndarray.shape
Tuple of array dimensions.

The shape property is usually used to get the current shape of an array, but may also be used to reshape the array in-place by assigning a tuple of array dimensions to it. As with [`numpy.reshape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html#numpy.reshape), one of the new shape dimensions can be -1, in which case its value is inferred from the size of the array and the remaining dimensions. Reshaping an array in-place will fail if a copy is required.

See also[`numpy.reshape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html#numpy.reshape) similar function [`ndarray.reshape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape) similar method

```
import numpy as np
ls=[1,2,34,5]
ls1=[6,7,8,9]
ls2=[ls,ls1]
np_arr=np.array(ls2)
print("Shape of Numpy Array",np_arr.shape)
```

Output

“C:\Python 37\python.exe” C:/Users/shakdas/PycharmProjects/untitled/NumpyTest/Sample1.py
Shape of Numpy Array (2, 4)

Process finished with exit code 0

## **3.** numpy.zeros (*shape*, *dtype=float*, *order=’C’*)

Return a new array of given shape and type, filled with zeros.

|  |  |
| --- | --- |
| Parameters: | **shape** : int or tuple of ints Shape of the new array, e.g., `(2, 3)` or `2`. **dtype** : data-type, optional The desired data-type for the array, e.g., `numpy.int8`. Default is `numpy.float64`. **order** : {‘C’, ‘F’}, optional, default: ‘C’ Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory. |
| Returns: | **out** : ndarray Array of zeros with the given shape, dtype, and order. |

```
import numpy as np
np_arr=np.zeros(5)
print(np_arr)
print("Type of numpy array:",np_arr.dtype)
print("Shape of Numpy Array",np_arr.shape)
```

Output

“C:\Python 37\python.exe” C:/Users/shakdas/PycharmProjects/untitled/NumpyTest/Sample1.py
[0. 0. 0. 0. 0.]
Type of numpy array float64
Shape of Numpy Array (5,)

Process finished with exit code 0

## 4.numpy.empty(*shape*, *dtype=float*, *order=’C’*)

Return a new array of given shape and type, without initializing entries.

|  |  |
| --- | --- |
| Parameters: | **shape** : int or tuple of int Shape of the empty array, e.g., `(2, 3)` or `2`. **dtype** : data-type, optional Desired output data-type for the array, e.g, `numpy.int8`. Default is `numpy.float64`. **order** : {‘C’, ‘F’}, optional, default: ‘C’ Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory. |
| Returns: | **out** : ndarray Array of uninitialized (arbitrary) data of the given shape, dtype, and order. Object arrays will be initialized to None. |

## 5.numpy.eye (*N*, *M=None*, *k=0*, *dtype=&lt;class ‘float’>*, *order=’C’*)

Return a 2-D array with ones on the diagonal and zeros elsewhere.

|  |  |
| --- | --- |
| Parameters: | **N** : int Number of rows in the output. **M** : int, optional Number of columns in the output. If None, defaults to *N*. **k** : int, optional Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal. **dtype** : data-type, optional Data-type of the returned array. **order** : {‘C’, ‘F’}, optional Whether the output should be stored in row-major (C-style) or column-major (Fortran-style) order in memory. New in version 1.14.0. |
| Returns: | **I** : ndarray of shape (N,M) An array where all elements are equal to zero, except for the *k*-th diagonal, whose values are equal to one. |

```
import numpy as np
np_arr=np.eye(5)
print(np_arr)
print("Type of numpy array:",np_arr.dtype)
print("Shape of Numpy Array:",np_arr.shape)
```

Output
[[1. 0. 0. 0. 0.]
[0. 1. 0. 0. 0.]
[0. 0. 1. 0. 0.]
[0. 0. 0. 1. 0.]
[0. 0. 0. 0. 1.]]
Type of numpy array: float64
Shape of Numpy Array: (5, 5)

## Numpy Mathematical Functions

#### Adding two numpy array

Adding two numpy array is as simple as adding two matrixes by adding the corresponding positions of the elements.

```python
a=np.array([[2,5,6,4],[4,3,3,4]])
print (a)
print ("---------------------------------")
print (a+a)
```

```
[[2 5 6 4]
 [4 3 3 4]]
---------------------------------
[[ 4 10 12  8]
 [ 8  6  6  8]]
```

#### Substracting two numpy array

```
import numpy as np
a=np.array([[2,5,6,4],[4,3,3,4]])
b=np.array([[2,4,5,6],[4,5,6,7]])
print (a)
print ("---------------------------------")
print (b)
print ("---------------------------------")
print (a-b)
```

```
[[2 5 6 4]
 [4 3 3 4]]
---------------------------------
[[2 4 5 6]
 [4 5 6 7]]
---------------------------------
[[ 0  1  1 -2]
 [ 0 -2 -3 -3]]
```

#### Multiplying two numpy array

```
import numpy as np
a=np.array([[2,5,6,4],[4,3,3,4]])
b=np.array([[2,4,5,6],[4,5,6,7]])
print (a)
print ("---------------------------------")
print (b)
print ("---------------------------------")
print (a*b)
```

```
[[2 5 6 4]
 [4 3 3 4]]
---------------------------------
[[2 4 5 6]
 [4 5 6 7]]
---------------------------------
[[ 4 20 30 24]
 [16 15 18 28]]
```

#### Dividing two numpy array

```
import numpy as np
a=np.array([[2,5,6,4],[4,3,3,4]])
b=np.array([[2,4,5,6],[4,5,6,7]])
print (a)
print ("---------------------------------")
print (b)
print ("---------------------------------")
print (a/b)
```

```
[[2 5 6 4]
 [4 3 3 4]]
---------------------------------
[[2 4 5 6]
 [4 5 6 7]]
---------------------------------
[[1.         1.25       1.2        0.66666667]
 [1.         0.6        0.5        0.57142857]]
```

#### Powring numpy array

```
import numpy as np
a=np.array([[2,5,6,4],[4,3,3,4]])
b=np.array([[2,4,5,6],[4,5,6,7]])
print (a)
print ("---------------------------------")
print (a**2)
print ("---------------------------------")
print (a**3)
```

```
[[2 5 6 4]
 [4 3 3 4]]
---------------------------------
[[ 4 25 36 16]
 [16  9  9 16]]
---------------------------------
[[  8 125 216  64]
 [ 64  27  27  64]]
```

# numpy.arange[¶](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html#numpy-arange)

`numpy.``arange`([*start*, ]*stop*, [*step*, ]*dtype=None*)

Return evenly spaced values within a given interval.

Values are generated within the half-open interval `[start, stop)` (in other words, the interval including *start* but excluding *stop*). For integer arguments, the function is equivalent to the Python built-in *range* function, but returns an ndarray rather than a list.

When using a non-integer step, such as 0.1, the results will often not be consistent. It is better to use [`numpy.linspace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html#numpy.linspace) for these cases.

|  |  |
| --- | --- |
| Parameters: | **start** : number, optionalStart of interval. The interval includes this value. The default start value is 0.**stop** : numberEnd of interval. The interval does not include this value, except in some cases where *step* is not an integer and floating point round-off affects the length of *out*.**step** : number, optionalSpacing between values. For any output *out*, this is the distance between two adjacent values, `out[i+1] - out[i]`. The default step size is 1. If *step* is specified as a position argument, *start* must also be given.**dtype** : dtypeThe type of the output array. If [`dtype`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html#numpy.dtype) is not given, infer the data type from the other input arguments. |
| Returns: | **arange** : ndarrayArray of evenly spaced values.For floating point arguments, the length of the result is `ceil((stop - start)/step)`. Because of floating point overflow, this rule may result in the last element of *out* being greater than *stop*. |

```
import numpy as np
a=np.arange(0,11)
print (a)
a=np.arange(0,11,2)
print (a)
```

```
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 0  2  4  6  8 10]
```
