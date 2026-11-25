---
title: Variables, ifs and loops
description: The three ideas behind almost every script you will ever write, explained with tiny examples.
lang: general
step: 4
pubDate: 2026-11-09
---

Nearly every script, however big, is made of three simple ideas: **remembering** things, **deciding** things and **repeating** things.

## Variables: remembering

A variable is a labelled box that holds a value.

```python
name = "Sam"
age = 12
print(name, "is", age)
```

`name = "Sam"` puts the text `Sam` into a box labelled `name`. Later, writing `name` means "whatever is in that box". Text goes in quotes; numbers don't.

## If: deciding

`if` lets your script choose what to do.

```python
age = 12

if age >= 13:
    print("You can make an account.")
else:
    print("Ask a grown-up first.")
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

If age is 13 or more, print the first message. Otherwise, print the second. The indented lines (four spaces in) belong to the `if` or the `else` above them.

</div>

Python uses **indentation** to group lines. Other languages use curly brackets `{ }` or words like `fi`, but the idea is the same.

## Loops: repeating

A loop runs the same lines several times.

```python
for number in range(1, 6):
    print("Counting:", number)
```

This prints `Counting: 1` up to `Counting: 5`. `range(1, 6)` means "from 1 up to, but not including, 6".

You can loop over a list of things too:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
```

## Putting them together

```python
scores = [45, 82, 67, 91]

for score in scores:
    if score >= 50:
        print(score, "pass")
    else:
        print(score, "try again")
```

That's a variable, a loop and an if, all in six lines. Real scripts are mostly this, just with more interesting things inside.

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Write a loop that prints the numbers 1 to 20, but prints `Fizz` instead of the number when it can be divided by 3. Hint: `number % 3 == 0` is true when it divides evenly.

</div>
