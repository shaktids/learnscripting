---
title: "Introduction to NumPy, SciPy, and Matplotlib"
description: "Before we can talk about concrete machine learning algorithms, we have to talk about how best to store the data we will chew through. This is important as…"
lang: other
categories: ["Machine Learning"]
author: "Shakti Das"
pubDate: 2018-05-06T06:06:48Z
legacy: true
wpId: 109
---

Before we can talk about concrete machine learning algorithms, we have to talk about how best to store the data we will chew through. This is important as the most advanced learning algorithm will not be of any help to us if they will never finish. This may be simply because accessing the data is too slow. Or maybe its
representation forces the operating system to swap all day. Add to this that Python is an interpreted language (a highly optimized one, though) that is slow for many numerically heavy algorithms compared to C or Fortran. So we might ask why on earth so many scientists and companies are betting their fortune on Python even in the highly computation-intensive areas? The answer is that in Python, it is very easy to ofﬂoad number-crunching tasks to the lower layer in the form of a C or Fortran extension.

That is exactly what **NumPy** and **SciPy** do (http://scipy.org/install.html). In this tandem, NumPy provides the support of highly optimized multidimensional arrays, which are the basic data structure of most state-of-the-art algorithms. SciPy uses those arrays to provide a set of fast numerical recipes. Finally, Matplotlib (http://matplotlib.org/) is probably the most convenient and feature-rich library to plot high-quality graphs using Python.

**Installing Python** **Luckily**, for all the major operating systems, namely Windows, Mac, and Linux,
there are targeted installers for NumPy, SciPy, and Matplotlib. If you are unsure about the installation process, you might want to install Enthought Python Distribution (https://www.enthought.com/products/epd\_free.php) or Python(x,y) (http://code.google.com/p/pythonxy/wiki/Downloads), which
come with all the earlier mentioned packages included. Chewing data effciently with NumPy and
intelligently with SciPy Let us quickly walk through some basic NumPy examples and then take a look at
what SciPy provides on top of it. On the way, we will get our feet wet with plotting using the marvelous Matplotlib package.

You will find more interesting examples of what NumPy can offer at

http://www.scipy.org/Tentative\_NumPy\_Tutorial. You will also fnd the book NumPy Beginner's Guide - Second Edition, Ivan Idris,Packt Publishing very valuable.

Additional tutorial style guides are at http://scipy-lectures.github.com;

you may also visit the offcial SciPy tutorial at
http://docs.scipy.org/doc/scipy/reference/tutorial.
