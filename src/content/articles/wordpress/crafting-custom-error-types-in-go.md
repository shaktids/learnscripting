---
title: "Crafting Custom Error Types in Go"
description: "Introduction Error handling is a crucial part of developing robust and maintainable software. While Go provides a simple built in error type, creating…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2024-05-26T06:00:30Z
legacy: true
wpId: 5195
---

## Introduction

Error handling is a crucial part of developing robust and maintainable software. While Go provides a simple built-in `error` type, creating custom error types can significantly enhance the clarity and precision of your error handling. This blog will guide you through the process of defining and using custom error types in Go, ensuring your applications handle errors gracefully and informatively.

## Why Use Custom Error Types?

Custom error types allow you to:

1. **Add Context**: Include additional information about the error, such as an error code or metadata.
2. **Differentiate Errors**: Distinguish between different types of errors and handle them accordingly.
3. **Improve Readability**: Make your code more readable and maintainable by clearly defining what each error represents.

## Defining Custom Error Types

### Basic Custom Error Type

To create a custom error type, define a struct that implements the `error` interface. The `error` interface requires a single method: `Error() string`.

```go
package main

import (
    "fmt"
)

// Define a custom error type
type MyError struct {
    Code    int
    Message string
}

// Implement the Error() method
func (e *MyError) Error() string {
    return fmt.Sprintf("Code %d: %s", e.Code, e.Message)
}

func main() {
    // Create an instance of MyError
    err := &MyError{Code: 404, Message: "Resource not found"}

    // Check and handle the error
    if err != nil {
        fmt.Println(err)
    }
}
```

### Adding Context to Errors

You can enhance your custom error types by including additional context or metadata.

```go
package main

import (
    "fmt"
)

// Define a custom error type with additional context
type MyError struct {
    Code    int
    Message string
    Context string
}

// Implement the Error() method
func (e *MyError) Error() string {
    return fmt.Sprintf("Code %d: %s - %s", e.Code, e.Message, e.Context)
}

func main() {
    // Create an instance of MyError with context
    err := &MyError{Code: 500, Message: "Internal Server Error", Context: "Database connection failed"}

    // Check and handle the error
    if err != nil {
        fmt.Println(err)
    }
}
```

### Using Custom Errors with Functions

Functions that may encounter errors should return an `error` value. Here's an example of how to use custom errors in a function:

```go
package main

import (
    "fmt"
)

// Define a custom error type
type ValidationError struct {
    Field   string
    Message string
}

// Implement the Error() method
func (e *ValidationError) Error() string {
    return fmt.Sprintf("Validation error on field '%s': %s", e.Field, e.Message)
}

// Function that returns a custom error
func validateAge(age int) error {
    if age < 0 {
        return &ValidationError{Field: "age", Message: "Age cannot be negative"}
    }
    if age > 130 {
        return &ValidationError{Field: "age", Message: "Age seems unrealistic"}
    }
    return nil
}

func main() {
    // Call the function and handle the error
    if err := validateAge(-1); err != nil {
        fmt.Println(err)
    }
}
```

### Wrapping Errors

Go 1.13 introduced error wrapping with the `fmt.Errorf` function and the `%w` verb. Wrapping errors allows you to provide additional context while preserving the original error.

```go
package main

import (
    "errors"
    "fmt"
)

// Define a custom error type
type MyError struct {
    Code    int
    Message string
}

// Implement the Error() method
func (e *MyError) Error() string {
    return fmt.Sprintf("Code %d: %s", e.Code, e.Message)
}

func performAction() error {
    return &MyError{Code: 403, Message: "Forbidden"}
}

func main() {
    // Wrap the custom error with additional context
    err := performAction()
    if err != nil {
        wrappedErr := fmt.Errorf("performAction failed: %w", err)
        fmt.Println(wrappedErr)
    }
}
```

### Unwrapping Errors

The `errors` package provides the `errors.Unwrap` function to retrieve the original error, and `errors.Is` and `errors.As` to check and match specific error types.

```go
package main

import (
    "errors"
    "fmt"
)

// Define a custom error type
type MyError struct {
    Code    int
    Message string
}

// Implement the Error() method
func (e *MyError) Error() string {
    return fmt.Sprintf("Code %d: %s", e.Code, e.Message)
}

func performAction() error {
    return &MyError{Code: 403, Message: "Forbidden"}
}

func main() {
    // Wrap the custom error with additional context
    err := performAction()
    if err != nil {
        wrappedErr := fmt.Errorf("performAction failed: %w", err)

        // Check if the error is a MyError
        var myErr *MyError
        if errors.As(wrappedErr, &myErr) {
            fmt.Printf("Caught a MyError: %v\n", myErr)
        }

        // Unwrap the original error
        originalErr := errors.Unwrap(wrappedErr)
        fmt.Printf("Original error: %v\n", originalErr)
    }
}
```

## Best Practices for Custom Error Types

1. **Keep It Simple**: Only create custom error types when you need additional information or behavior.
2. **Provide Context**: Use custom error types to include context that can help with debugging.
3. **Document Your Errors**: Clearly document what each custom error type represents.
4. **Leverage Wrapping**: Use error wrapping to add context while preserving the original error.

## Conclusion

Custom error types in Go offer a powerful way to enhance your error handling by providing additional context and differentiating between different error scenarios. By following the practices outlined in this blog, you can create clear, maintainable, and robust error handling in your Go applications. Happy coding!
