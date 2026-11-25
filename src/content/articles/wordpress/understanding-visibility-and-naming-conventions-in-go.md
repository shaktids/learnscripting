---
title: "Understanding Visibility and Naming Conventions in Go"
description: "Introduction Go, or Golang, is a statically typed, compiled language known for its simplicity and efficiency. One of its key features is the clear and…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2024-05-26T05:57:27Z
legacy: true
wpId: 5193
---

## Introduction

Go, or Golang, is a statically typed, compiled language known for its simplicity and efficiency. One of its key features is the clear and straightforward rules for naming conventions and visibility, which are essential for writing clean, maintainable code. This blog will explore Go's visibility rules and naming conventions, helping you write better Go code.

## Visibility in Go

Visibility in Go is determined by the case of the first letter of the identifier (variable, function, type, constant, etc.). This simple yet powerful rule dictates whether an identifier is exported (public) or unexported (private).

### Exported Identifiers

An identifier is exported (visible outside the package) if it starts with an uppercase letter.

```go
package mypackage

// Exported function
func PublicFunction() {
    // Function implementation
}

// Exported variable
var PublicVariable = "I am visible outside the package"
```

### Unexported Identifiers

An identifier is unexported (visible only within the package) if it starts with a lowercase letter.

```go
package mypackage

// Unexported function
func privateFunction() {
    // Function implementation
}

// Unexported variable
var privateVariable = "I am not visible outside the package"
```

### Example: Using Exported and Unexported Identifiers

Consider a package `mypackage` with both exported and unexported identifiers.

```go
// mypackage/mypackage.go
package mypackage

import "fmt"

// Exported function
func Greet() {
    fmt.Println("Hello from mypackage!")
}

// Unexported function
func greet() {
    fmt.Println("hello from mypackage")
}
```

Now, in another package, you can use the exported `Greet` function but not the unexported `greet` function.

```go
// main.go
package main

import (
    "mypackage"
)

func main() {
    mypackage.Greet() // Works
    // mypackage.greet() // Does not work, greet is unexported
}
```

## Naming Conventions in Go

Go emphasizes readability and simplicity, and its naming conventions reflect these principles. Here are some key conventions:

### Package Names

Package names should be short, concise, and lowercased. They should describe the functionality provided by the package.

```go
// Correct
package math

// Incorrect
package MathUtilities
```

### Variable and Function Names

Variable and function names should be descriptive and use camelCase.

```go
// Correct
var userName string

func calculateTotal() int {
    // Function implementation
}

// Incorrect
var UserName string

func CalculateTotal() int {
    // Function implementation
}
```

### Constants

Constants are typically written in camelCase if they are unexported, and in mixed caps (CamelCase) if they are exported.

```go
// Correct
const defaultTimeout = 5 // Unexported
const MaxConnections = 10 // Exported

// Incorrect
const DEFAULT_TIMEOUT = 5
const maxConnections = 10
```

### Structs and Interfaces

Struct and interface names should be in CamelCase. If the struct or interface is exported, it should start with an uppercase letter; otherwise, it should start with a lowercase letter.

```go
// Correct
type User struct {
    FirstName string
    LastName  string
}

type database interface {
    connect() error
}

// Incorrect
type user struct {
    FirstName string
    LastName  string
}

type Database interface {
    connect() error
}
```

### Acronyms

When using acronyms in names, use mixed caps (CamelCase) and treat them as a single word.

```go
// Correct
func getHTTPResponse() {}

// Incorrect
func getHttpResponse() {}
```

## Example: Putting It All Together

Let's create a simple package to demonstrate the naming conventions and visibility rules in practice.

```go
// greeter/greeter.go
package greeter

import "fmt"

// Exported struct
type Greeter struct {
    Name string
}

// Exported function
func NewGreeter(name string) *Greeter {
    return &Greeter{Name: name}
}

// Exported method
func (g *Greeter) Greet() {
    fmt.Printf("Hello, %s!\n", g.Name)
}

// Unexported helper function
func formatGreeting(name string) string {
    return fmt.Sprintf("Hello, %s!", name)
}
```

Using the `greeter` package in another file:

```go
// main.go
package main

import "myproject/greeter"

func main() {
    g := greeter.NewGreeter("World")
    g.Greet() // Outputs: Hello, World!
}
```

## Conclusion

Understanding and following Go's visibility rules and naming conventions are crucial for writing clean, maintainable, and idiomatic Go code. By adhering to these guidelines, you ensure that your code is easily understandable and usable by other developers. Keep practicing these conventions in your projects to become a proficient Go developer. Happy coding!
