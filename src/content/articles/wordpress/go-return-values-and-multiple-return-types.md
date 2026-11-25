---
title: "Go Return Values and Multiple Return Types"
description: "Go is known for its simplicity and efficiency, and one of its distinctive features is its ability to return multiple values from a function. This allows…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2023-11-02T00:49:42Z
legacy: true
wpId: 4279
---

Go is known for its simplicity and efficiency, and one of its distinctive features is its ability to return multiple values from a function. This allows you to efficiently package and exchange related data in a single function call. In this blog, we'll explore how Go handles return values and the concept of multiple return types.

## Single Return Values

In Go, a function can return a single value. This is the most basic form of returning a result from a function. The return type of the function is specified in the function signature, and that's what gets returned. Here's an example:

```go
package main

import "fmt"

func add(a, b int) int {
    return a + b
}

func main() {
    result := add(5, 3)
    fmt.Println("5 + 3 =", result)
}
```

In this example, the `add` function takes two integer parameters and returns their sum as a single integer.

## Multiple Return Values

Go allows a function to return multiple values, which is a powerful feature for simplifying code and improving error handling. To return multiple values, you list the return types separated by commas in the function signature. Here's an example:

```go
package main

import "fmt"

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10.0, 2.0)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Result:", result)
    }
}
```

In this example, the `divide` function returns two values: a floating-point result and an error. This makes it easy to handle exceptional cases and propagate errors throughout your program.

## Named Return Values

Go also allows you to name return values in a function's signature. Named return values are treated as variables within the function, and their values are automatically returned. This feature can make your code more readable. Here's an example:

```go
package main

import "fmt"

func divide(a, b float64) (result float64, err error) {
    if b == 0 {
        err = fmt.Errorf("division by zero")
        return
    }
    result = a / b
    return
}

func main() {
    result, err := divide(10.0, 2.0)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Result:", result)
    }
}
```

In this example, the `divide` function has named return values, `result` and `err`, which are initialized within the function and returned automatically.

## Handling Multiple Return Values

When you call a function that returns multiple values, you can capture and use those values in your code. Here's how you do it:

```go
result, err := divide(10.0, 2.0)
```

In this line of code, `result` and `err` are assigned the values returned by the `divide` function.

## Ignoring Return Values

If you want to call a function but ignore some or all of its return values, you can use the blank identifier (`_`). For example:

```go
_, err := divide(10.0, 0.0)
if err != nil {
    fmt.Println("Error:", err)
}
```

In this example, we're ignoring the result of the division operation and only checking for the error.

## Conclusion

Go's support for multiple return values, named return values, and error handling simplifies code and improves the robustness of your programs. Whether you're creating utility functions, complex algorithms, or working with external libraries, these features make Go a language that's both efficient and user-friendly. Understanding how to leverage multiple return values is a key aspect of effective Go programming.
