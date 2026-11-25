---
title: "How to make Multithreading in Python To run Multiple Methods Simultaneously"
description: "In Python Achiveing multithrading is simple enough as to create two defination.We will describe the multi threading concept in the python in this How to…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2018-06-08T09:31:52
legacy: true
wpId: 1160
draft: true
---

In Python Achiveing multithrading is simple enough as to create two defination.We will describe the multi threading concept in the python in this **How to make Multithreading in Python To run Multiple Methods Simultaneously** post.

1.To achive multi threading in python we need to declare the definations

```
import threading

data=50
def firstDef():
    data=60

    print "Inside the one def"

def secondDef(self, var=None):
    print "Inside second def", var
    print(self)

t1 = threading.Thread(target=firstDef)
t2 = threading.Thread(target=secondDef, args=(10, 20))
#To Start the Threads
t1.start()
t2.start()
```
