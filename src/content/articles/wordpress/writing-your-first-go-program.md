---
title: "Writing Your First Go Program"
description: "Congratulations on installing Go on your system! Now that you have Go up and running, it's time to write your very first Go program. In this blog, we'll…"
lang: other
categories: ["Go"]
author: "Shakti Das"
pubDate: 2023-11-01T23:56:03Z
legacy: true
wpId: 4252
---

Congratulations on installing Go on your system! Now that you have Go up and running, it's time to write your very first Go program. In this blog, we'll guide you through the process of creating a simple "Hello, World!" program in Go. This classic introductory program will help you become familiar with Go's syntax and the essential steps for writing and running Go code.

## Step 1: Setting Up Your Workspace
Before you start writing Go code, it's a good practice to set up your workspace, also known as the GOPATH. Your workspace is where you'll organize your Go source code and dependencies. The GOPATH should point to the root directory of your workspace.

If you haven't already set up your workspace during the installation process, you can refer to our previous blog on "Installing Go on Your System" for details on how to do so.

## Step 2: Create a New Directory
Open your terminal or command prompt and navigate to the directory where you want to create your Go project. You can use the `cd` command to change your working directory. For example, to create a directory called "hello" for your Go project, you can run:

```go
mkdir hello
cd hello
```

## Step 3: Writing the "Hello, World!" Program
Now that you're in your project directory, it's time to write your first Go program. Create a new file called "hello.go" using your preferred text editor or integrated development environment (IDE). You can use a simple text editor like Notepad or a specialized Go IDE like Visual Studio Code.

Add the following code to your "hello.go" file:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

This Go program consists of a `main` function, which is the entry point of your application. It imports the "fmt" package, which provides functionality for formatted I/O, and then prints "Hello, World!" to the console using `fmt.Println`.

## Step 4: Compiling and Running Your Program
To compile and run your Go program, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where your "hello.go" file is located. For example:

```go
   cd path/to/your/project/directory
```

3. To compile your program, run the following command:

```go
   go build hello.go
```

This will generate an executable binary named "hello" in your project directory.

4. To run your program, execute the binary:

```go
   ./hello
```

You should see the output "Hello, World!" displayed in your terminal.

Congratulations! You've written and executed your first Go program. You've experienced the simplicity and readability of Go's syntax and learned the basics of creating a Go project, writing code, compiling it, and running the resulting binary.

As you continue your journey with Go, you'll explore more advanced features and build a wide range of applications, from web services to system tools. The Go programming language offers an efficient and enjoyable development experience, making it an excellent choice for various software projects. Happy coding!
