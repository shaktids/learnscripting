---
title: "Chewing data Efficiently with NumPy and intelligently with SciPy"
description: "In this following tutorial we will learn about Chewing data Efficiently with NumPy and intelligently with SciPy and the NumPy. Let us quickly walk through…"
lang: other
categories: ["Machine Learning"]
author: "Shakti Das"
pubDate: 2018-05-17T07:28:27Z
legacy: true
wpId: 121
---

In this following tutorial we will learn about Chewing data Efficiently with NumPy and intelligently with SciPy and the NumPy. Let us quickly walk through some basic NumPy examples and then take a look at what SciPy provides on top of it. On the way, we will get our feet wet with plotting using the marvelous Matplotlib package.
You will fnd more interesting examples of what NumPy can offer at

    http://www.scipy.org/Tentative\_NumPy\_Tutorial.

You will also fnd the book NumPy Beginner's Guide - Second Edition, Ivan Idris,Packt Publishing very valuable. Additional tutorial style guides are at http://scipy-lectures.github.com; you may also visit the offcial SciPy tutorial at http://docs.scipy.org/doc/scipy/reference/tutorial.

In this blog, we will use NumPy Version 1.6.2 and SciPy Version 0.11.0.
Learning NumPy
So let us import NumPy and play a bit with it. For that, we need to start the Python
interactive shell.

      >>> import numpy
>>> numpy.version.full\_version
1.6.2

As we do not want to pollute our namespace, we certainly should not do the following:

      >>> from numpy import \*

The numpy.array array will potentially shadow the array package that is included

in standard Python. Instead, we will use the following convenient shortcut:
> >> import numpy as np
> >>> a = np.array([0,1,2,3,4,5])
> >>> a
> array([0, 1, 2, 3, 4, 5])
> >>> a.ndim
> 1
> >>> a.shape
> (6,)

We just created an array in a similar way to how we would create a list in Python.However, NumPy arrays have additional information about the shape. In this case,it is a one-dimensional array of fve elements. No surprises so far.

We can now transform this array in to a 2D matrix.
>>> b = a.reshape((3,2))
>>> b
array([[0, 1],
[2, 3],
[4, 5]])
>>> b.ndim
2
>>> b.shape
(3, 2)

The funny thing starts when we realize just how much the NumPy package is
optimized. For example, it avoids copies wherever possible.
> >> b[1][0]=77
> >>> b
> array([[ 0, 1],
> [77, 3],
> [ 4, 5]])
> >>> a
> array([ 0, 1, 77, 3, 4, 5])

In this case, we have modifed the value 2 to 77 in b, and we can immediately see
the same change reﬂected in a as well. Keep that in mind whenever you need a
true copy.
> >> c = a.reshape((3,2)).copy()
> >>> c
> array([[ 0, 1],
> [77, 3],
> [ 4, 5]])
> >>> c[0][0] = -99
> >>> a
> array([ 0, 1, 77, 3, 4, 5])
> >>> c
> array([[-99, 1],
> [ 77, 3],
> [ 4, 5]])

Here, c and a are totally independent copies.
Another big advantage of NumPy arrays is that the operations are propagated
to the individual elements.
> >> a\*2
> array([ 2, 4, 6, 8, 10])
> >>> a\*\*2
> array([ 1, 4, 9, 16, 25])
> Contrast that to ordinary Python lists:
> >>> [1,2,3,4,5]\*2
> [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
> >>> [1,2,3,4,5]\*\*2
> Traceback (most recent call last):
> File "&lt;stdin>", line 1, in &lt;module>
> TypeError: unsupported operand type(s) for \*\* or pow(): 'list' and
> 'int'

Of course, by using NumPy arrays we sacrifce the agility Python lists offer. Simple
operations like adding or removing are a bit complex for NumPy arrays. Luckily,
we have both at our disposal, and we will use the right one for the task at hand.
Indexing

Part of the power of NumPy comes from the versatile ways in which its arrays can
be accessed.
In addition to normal list indexing, it allows us to use arrays themselves as indices.
> >> a[np.array([2,3,4])]
> array([77, 3, 4])
> In addition to the fact that conditions are now propagated to the individual elements,
> we gain a very convenient way to access our data.
> >>> a>4
> array([False, False, True, False, False, True], dtype=bool)
> >>> a[a>4]
> array([77, 5])
> This can also be used to trim outliers.
> >>> a[a>4] = 4
> >>> a
> array([0, 1, 4, 3, 4, 4])

As this is a frequent use case, there is a special clip function for it, clipping the values
at both ends of an interval with one function call as follows:
> >> a.clip(0,4)
> array([0, 1, 4, 3, 4, 4])

Handling non-existing values
The power of NumPy's indexing capabilities comes in handy when pre processing data that we have just read in from a text fle. It will most likely contain invalid values, which we will mark as not being a real number using numpy.NAN as follows:

c = np.array([1, 2, np.NAN, 3, 4]) # let's pretend we have read this
from a text file
>>> c
array([ 1., 2., nan, 3., 4.])
>>> np.isnan(c)
array([False, False, True, False, False], dtype=bool)
>>> c[~np.isnan(c)]
array([ 1., 2., 3., 4.])
>>> np.mean(c[~np.isnan(c)])
2.5

Comparing runtime behaviors Let us compare the runtime behavior of NumPy with normal Python lists. In the
ollowing code, we will calculate the sum of all squared numbers of 1 to 1000 and see how much time the calculation will take. We do it 10000 times and report the total time so that our measurement is accurate enough.

import timeit
normal\_py\_sec = timeit.timeit('sum(x\*x for x in xrange(1000))',
number=10000)
naive\_np\_sec = timeit.timeit('sum(na\*na)',
setup="import numpy as np; na=np.
arange(1000)",
number=10000)
good\_np\_sec = timeit.timeit('na.dot(na)',
setup="import numpy as np; na=np.
arange(1000)",
number=10000)
print("Normal Python: %f sec"%normal\_py\_sec)
print("Naive NumPy: %f sec"%naive\_np\_sec)
print("Good NumPy: %f sec"%good\_np\_sec)
Normal Python: 1.157467 sec
Naive NumPy: 4.061293 sec
Good NumPy: 0.033419 sec

We make two interesting observations. First, just using NumPy as data storage (Naive NumPy) takes 3.5 times longer, which is surprising since we believe it must be much faster as it is written as a C extension. One reason for this is that the access of individual elements from Python itself is rather costly. Only when we are able to apply algorithms inside the optimized extension code do we get speed improvements, and
tremendous ones at that: using the dot() function of NumPy, we are more than 25 times faster. In summary, in every algorithm we are about to implement, we should always look at how we can move loops over individual elements from Python to some of the highly optimized NumPy or SciPy extension functions.

However, the speed comes at a price. Using NumPy arrays, we no longer have the incredible ﬂexibility of Python lists, which can hold basically anything. NumPy arrays always have only one datatype.
>>> a = np.array([1,2,3])
>>> a.dtype
dtype('int64')
If we try to use elements of different types, NumPy will do its best to coerce them to the most reasonable common datatype:
>>> np.array([1, "stringy"])
array(['1', 'stringy'], dtype='|S8')
>>> np.array([1, "stringy", set([1,2,3])])
array([1, stringy, set([1, 2, 3])], dtype=object)
