---
title: "Python Mutable vs Immutable"
description: "To get started, it’s important to understand that every object in Python has an ID (or identity), a type, and a value, as shown in the following snippet…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2020-04-10T12:20:10Z
legacy: true
wpId: 2040
---

To get started, it’s important to understand that every object in Python has an ID (or identity), a type, and a value, as shown in the following snippet:

```
age = 42
print(id(age))    # id
print(type(age))  # type
print(age)        # value
[Out:]
10966208
<class ‘int’>
42
```

Once created, the ID of an object never changes. It is a unique identifier for it, and it is used behind the scenes by Python to retrieve the object when we want to use it.

The type also never changes. The type tells what operations are supported by the object and the possible values that can be assigned to it.

The value can either change or not. If it can, the object is said to be mutable, while when it cannot, the object is said to be immutable.

Let’s take a look at an example:

```
age = 42
print(id(age))
print(type(age))
print(age)age = 43
print(age)
print(id(age))
[Out:]
10966208
<class ‘int’>
42
43
10966240
```

Has the value of `age` changed? Well, no. `42` is an integer number, of the type `int`, which is immutable. So, what happened is really that on the first line, `age` is a name that is set to point to an `int` object, whose value is `42`.

When we type `age = 43`, what happens is that another object is created, of the type `int` and value `43` (also, the `id` will be different), and the name `age` is set to point to it. So, we didn’t change that `42` to `43`. We actually just pointed `age` to a different location.

As you can see from printing `id(age)` before and after the second object named `age` was created, they are different.

Now, let’s see the same example using a mutable object.

```
x = [1, 2, 3]
print(x)
print(id(x))x.pop()
print(x)
print(id(x))
[Out:]
[1, 2, 3]
139912816421064
[1, 2]
139912816421064
```

For this example, we created a list named `m` that contains 3 integers, `1`, `2`, and `3`. After we change `m` by “popping” off the last value `3`, the ID of `m` stays the same!

So, objects of type `int` are immutable and objects of type `list` are mutable. Now let’s discuss other immutable and mutable data types!
