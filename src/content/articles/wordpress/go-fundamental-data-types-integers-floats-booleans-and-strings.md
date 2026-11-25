---
title: "Go Fundamental Data Types: Integers, Floats, Booleans, and Strings"
description: "In Go, understanding fundamental data types is essential for working with data and performing operations in your programs. Go provides a set of primitive…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2023-11-02T00:07:19Z
legacy: true
wpId: 4255
---

In Go, understanding fundamental data types is essential for working with data and performing operations in your programs. Go provides a set of primitive data types, including integers, floats, booleans, and strings. In this blog, we'll explore these fundamental data types, their usage, and some basic operations.

## Integers
Integers are used to represent whole numbers in Go. Go supports both signed and unsigned integers of different sizes, which are primarily categorized as follows:

### Signed Integers
1. **int8:** 8-bit signed integer with a range of -128 to 127.
2. **int16:** 16-bit signed integer with a range of -32,768 to 32,767.
3. **int32:** 32-bit signed integer with a range of -2,147,483,648 to 2,147,483,647.
4. **int64:** 64-bit signed integer with a larger range.
5. **int:** Implementation-specific signed integer that's typically 32 or 64 bits.

### Unsigned Integers
1. **uint8:** 8-bit unsigned integer with a range of 0 to 255.
2. **uint16:** 16-bit unsigned integer with a range of 0 to 65,535.
3. **uint32:** 32-bit unsigned integer.
4. **uint64:** 64-bit unsigned integer.
5. **uint:** Implementation-specific unsigned integer, often the same size as `int`.

Here's how you can declare and initialize integer variables in Go:

```go
var age int = 30
count := 100
```

## Floats
Floats are used to represent numbers with decimal points. Go supports two primary types of floating-point numbers:

1. **float32:** A 32-bit single-precision floating-point number.
2. **float64:** A 64-bit double-precision floating-point number (default for floating-point literals).

Declaring and initializing float variables in Go:

```go
var temperature float64 = 25.5
humidity := 55.7
```

## Booleans
Booleans represent binary values, true or false. Booleans are crucial for decision-making and controlling program flow.

```go
var isSunny bool = true
cloudy := false
```

## Strings
Strings in Go are sequences of characters. They are enclosed in double quotes (`"`) or backticks (``) for raw string literals. Go's strings are UTF-8 encoded, making it suitable for handling a wide range of characters.

```go
var message string = "Hello, World!"
greeting := `Welcome to "Go" programming`
```

### String Operations
Go provides various operations for working with strings:

- **Concatenation:** You can concatenate strings using the `+` operator. `greeting := "Hello, " name := "Alice" welcome := greeting + name`
- **Length:** The `len()` function returns the length of a string. `message := "This is a sample message." length := len(message) // Returns the length of the string.`
- **Accessing Characters:** You can access individual characters in a string by indexing it, where the index starts at 0. `text := "Gopher" firstChar := text[0] // Accesses the first character 'G'.`
- **String Comparison:** Use the `==` operator to compare two strings for equality. `str1 := "apple" str2 := "apple" equal := str1 == str2 // true`

Go's rich standard library provides extensive support for working with strings, making it easy to perform tasks like splitting, joining, and searching within strings.

## Conclusion
Understanding Go's fundamental data types—integers, floats, booleans, and strings—is vital for writing efficient and effective programs. These data types allow you to handle a wide range of data and perform various operations to build versatile and reliable software in Go. Whether you're working with numbers, making decisions, or processing textual data, Go's data types provide the foundation for effective programming.
