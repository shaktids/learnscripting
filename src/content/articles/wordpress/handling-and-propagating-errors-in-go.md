---
title: "Handling and Propagating Errors in Go"
description: "Introduction Error handling is an essential aspect of writing robust and maintainable software. Go's simplicity in error handling, using its error type…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2024-05-26T06:02:08Z
legacy: true
wpId: 5196
---

## Introduction

Error handling is an essential aspect of writing robust and maintainable software. Go's simplicity in error handling, using its `error` type, allows developers to write clear and straightforward code for dealing with errors. This blog will delve into various techniques for handling and propagating errors in Go, offering best practices to help you write resilient applications.

## Basic Error Handling

### Returning Errors

In Go, functions that can encounter errors typically return an error as their last return value. This allows the caller to check and handle the error appropriately.

```go
package main

import (
    "fmt"
    "os"
)

func readFile(filename string) ([]byte, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }
    return data, nil
}

func main() {
    data, err := readFile("example.txt")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println("File content:", string(data))
}
```

### Checking Errors

Always check the error returned by a function before using the other return values.

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    file, err := os.Open("example.txt")
    if err != nil {
        fmt.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    // Proceed with file operations
}
```

## Propagating Errors

### Returning Wrapped Errors

Go 1.13 introduced error wrapping with the `fmt.Errorf` function and the `%w` verb. Wrapping errors provide additional context while preserving the original error.

```go
package main

import (
    "fmt"
    "os"
)

func readFile(filename string) ([]byte, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("readFile: %w", err)
    }
    return data, nil
}

func main() {
    _, err := readFile("example.txt")
    if err != nil {
        fmt.Println("Error:", err)
    }
}
```

### Unwrapping Errors

The `errors` package provides functions like `errors.Is` and `errors.As` to check and match specific error types.

```go
package main

import (
    "errors"
    "fmt"
    "os"
)

func readFile(filename string) ([]byte, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("readFile: %w", err)
    }
    return data, nil
}

func main() {
    _, err := readFile("example.txt")
    if err != nil {
        if errors.Is(err, os.ErrNotExist) {
            fmt.Println("File does not exist")
        } else {
            fmt.Println("Error:", err)
        }
    }
}
```

## Custom Error Types

Creating custom error types allows you to include additional context or metadata with your errors.

### Defining Custom Error Types

Define a struct that implements the `error` interface.

```go
package main

import (
    "fmt"
)

type ValidationError struct {
    Field   string
    Message string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("Validation error on field '%s': %s", e.Field, e.Message)
}

func validateAge(age int) error {
    if age < 0 {
        return &ValidationError{Field: "age", Message: "Age cannot be negative"}
    }
    return nil
}

func main() {
    err := validateAge(-1)
    if err != nil {
        fmt.Println(err)
    }
}
```

### Using Custom Errors

Use custom errors to provide detailed error information and context.

```go
package main

import (
    "fmt"
)

type MyError struct {
    Code    int
    Message string
}

func (e *MyError) Error() string {
    return fmt.Sprintf("Error %d: %s", e.Code, e.Message)
}

func performAction() error {
    return &MyError{Code: 403, Message: "Forbidden"}
}

func main() {
    err := performAction()
    if err != nil {
        fmt.Println("Error:", err)
    }
}
```

## Handling Multiple Errors

In some cases, you might want to aggregate multiple errors. You can do this by creating an error type that holds a slice of errors.

```go
package main

import (
    "fmt"
    "strings"
)

type MultiError struct {
    Errors []error
}

func (e *MultiError) Error() string {
    var errorMessages []string
    for _, err := range e.Errors {
        errorMessages = append(errorMessages, err.Error())
    }
    return strings.Join(errorMessages, "; ")
}

func validateFields(fields map[string]string) error {
    var errs MultiError
    for field, value := range fields {
        if value == "" {
            errs.Errors = append(errs.Errors, fmt.Errorf("field %s cannot be empty", field))
        }
    }
    if len(errs.Errors) > 0 {
        return &errs
    }
    return nil
}

func main() {
    fields := map[string]string{"username": "", "password": ""}
    err := validateFields(fields)
    if err != nil {
        fmt.Println("Validation errors:", err)
    }
}
```

## Error Logging

Proper error logging is crucial for diagnosing issues in production. Use logging libraries to capture and report errors.

```go
package main

import (
    "log"
    "os"
)

func readFile(filename string) ([]byte, error) {
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, fmt.Errorf("readFile: %w", err)
    }
    return data, nil
}

func main() {
    _, err := readFile("example.txt")
    if err != nil {
        log.Printf("Error reading file: %v", err)
    }
}
```

## Best Practices for Error Handling

1. **Check Errors**: Always check and handle errors returned by functions.
2. **Provide Context**: Use error wrapping and custom error types to provide additional context.
3. **Avoid Silent Failures**: Do not ignore errors; handle them or propagate them up the call stack.
4. **Use Descriptive Messages**: Ensure error messages are clear and informative.
5. **Log Errors**: Ensure errors are logged with sufficient detail to aid in debugging.

## Conclusion

Handling and propagating errors effectively is crucial for building reliable and maintainable Go applications. By following best practices and leveraging Go's error handling capabilities, you can write code that gracefully handles errors and provides clear, actionable feedback. Remember to check and handle errors, provide context, use custom error types, and log errors appropriately. Happy coding!
