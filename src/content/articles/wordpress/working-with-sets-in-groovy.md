---
title: "Working with Sets in Groovy"
description: "Introduction Groovy is a powerful and dynamic programming language that runs on the Java Virtual Machine (JVM). It offers a range of data structures and…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2023-10-07T02:52:30Z
legacy: true
wpId: 4125
---

Introduction

Groovy is a powerful and dynamic programming language that runs on the Java Virtual Machine (JVM). It offers a range of data structures and collections for working with data efficiently. Sets, a fundamental collection type, are commonly used for storing unique elements in Groovy. In this blog post, we will explore how to work with sets in Groovy, covering creation, manipulation, and common operations.

## Creating Sets

In Groovy, you can create sets using the `Set` constructor or by using set literals enclosed in curly braces `{}`.

```groovy
// Creating a set using the Set constructor
def fruitSet = new HashSet<String>()
fruitSet.add("apple")
fruitSet.add("banana")
fruitSet.add("cherry")

// Creating a set using set literals
def colors = ["red", "green", "blue"]
```

## Adding and Removing Elements

You can add elements to a set using the `add` method and remove elements using the `remove` method.

```groovy
def animals = ["cat", "dog", "elephant"]
animals.add("giraffe")  // Add an element

if (animals.contains("dog")) {
    animals.remove("dog")  // Remove an element
}
```

## Set Operations

Groovy sets support common set operations like union, intersection, and difference.

```groovy
def set1 = [1, 2, 3, 4, 5]
def set2 = [3, 4, 5, 6, 7]

// Union
def union = set1 + set2  // [1, 2, 3, 4, 5, 6, 7]

// Intersection
def intersection = set1.intersect(set2)  // [3, 4, 5]

// Difference
def difference = set1 - set2  // [1, 2]
```

## Iterating Over Sets

You can iterate over sets using various methods, including loops and Groovy's collection methods.

```groovy
def planets = ["Earth", "Mars", "Venus"]

// Using a for-each loop
for (planet in planets) {
    println(planet)
}

// Using the each method
planets.each { println(it) }

// Using the collect method to transform elements
def upperCasePlanets = planets.collect { it.toUpperCase() }
```

## Set Operations and Methods

Groovy provides a rich set of methods for working with sets, making operations more convenient:

- `addAll`: Adds all elements from another collection to the set.
- `retainAll`: Retains only the elements present in both the set and another collection.
- `removeAll`: Removes all elements in the set that are also present in another collection.
- `containsAll`: Checks if the set contains all elements from another collection.
- `size`: Returns the number of elements in the set.

```groovy
def setA = [1, 2, 3]
def setB = [2, 3, 4]

setA.addAll(setB)      // [1, 2, 3, 4]
setA.retainAll(setB)   // [2, 3]
setA.removeAll(setB)   // [2, 3]
setA.containsAll(setB) // false
setA.size()            // 2
```

## Converting Sets to Lists and vice versa

You can easily convert sets to lists and vice versa in Groovy.

```groovy
def setToConvert = [1, 2, 3, 4, 5]

// Convert set to list
def listFromSet = setToConvert.toList()  // [1, 2, 3, 4, 5]

// Convert list to set
def setFromList = listFromSet.toSet()    // [1, 2, 3, 4, 5]
```

## Conclusion

Working with sets in Groovy is straightforward, and it offers a range of methods and operations to handle unique collections of data efficiently. Whether you need to perform set operations, iterate over elements, or convert sets to lists, Groovy provides a flexible and expressive way to work with sets in your code.
