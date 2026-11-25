---
title: "Looping in Go: for and range"
description: "Looping is a fundamental concept in programming, and Go provides two primary loop constructs: the for loop and the range loop. In this blog, we'll explore…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2023-11-02T00:43:20Z
legacy: true
wpId: 4258
---

Looping is a fundamental concept in programming, and Go provides two primary loop constructs: the `for` loop and the `range` loop. In this blog, we'll explore these looping mechanisms, their syntax, and how to use them effectively in your Go programs.

## The `for` Loop

The `for` loop in Go is a versatile construct that allows you to repeatedly execute a block of code while a specified condition is `true`. The basic structure of a `for` loop is as follows:

```go
for initialization; condition; post {
    // Code to be executed repeatedly
}
```

- `Initialization`: This section is executed once before the loop begins and is often used to initialize loop control variables.
- `Condition`: The loop continues executing as long as the condition is `true`. If the condition becomes `false`, the loop terminates.
- `Post`: The post statement is executed after each iteration and is typically used to update loop control variables.

### Example of a `for` Loop

Let's look at a simple example of a `for` loop that prints numbers from 1 to 5:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 5; i++ {
        fmt.Println(i)
    }
}
```

In this example, the loop initializes `i` to 1, checks if `i` is less than or equal to 5, and increments `i` by 1 in each iteration. It continues until `i` is no longer less than or equal to 5.

## The `range` Loop

The `range` loop is a specialized construct used to iterate over elements of a collection, such as an array, slice, map, or string. It simplifies the process of iterating through these collections, providing both the index and value of each element. The basic structure of a `range` loop is as follows:

```go
for index, value := range collection {
    // Code to be executed for each element
}
```

- `Index`: This variable represents the index or key of the current element in the collection (applicable to arrays, slices, and maps).
- `Value`: This variable holds the value of the current element.

### Example of a `range` Loop

Let's see how the `range` loop can be used to iterate over the elements of a slice:

```go
package main

import "fmt"

func main() {
    fruits := []string{"apple", "banana", "cherry", "date"}

    for index, fruit := range fruits {
        fmt.Printf("Index: %d, Fruit: %s\n", index, fruit)
    }
}
```

In this example, the `range` loop iterates over the elements of the `fruits` slice, providing both the index and value for each element.

## Exiting a Loop Early

Sometimes you may need to exit a loop prematurely if a specific condition is met. In Go, you can use the `break` statement to do this. Here's an example:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 10; i++ {
        if i == 5 {
            break // Exit the loop when i equals 5
        }
        fmt.Println(i)
    }
}
```

In this example, the loop will exit when `i` equals 5 due to the `break` statement.

## Skipping an Iteration

You can also skip the current iteration of a loop and move to the next one using the `continue` statement. Here's an example:

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 5; i++ {
        if i == 3 {
            continue // Skip the current iteration when i equals 3
        }
        fmt.Println(i)
    }
}
```

In this example, the loop will skip printing 3 and continue to the next iteration.

## Infinite Loops

In some situations, you may need to create an infinite loop, which continues until an external condition is met. You can achieve this with a `for` loop by omitting the initialization, condition, and post sections. Here's an example:

```go
package main

import "fmt"

func main() {
    i := 1
    for {
        fmt.Println(i)
        i++
        if i > 5 {
            break // Exit the loop when i exceeds 5
        }
    }
}
```

In this example, the loop will continue indefinitely until `i` exceeds 5, at which point it exits.

## Conclusion

Loops are an essential part of Go programming, and the `for` and `range` loops provide powerful tools for iterating through collections, performing repetitive tasks, and controlling program flow. Whether you're processing data, searching for information, or creating iterative algorithms, these loop constructs are valuable assets in your Go programming toolkit.
