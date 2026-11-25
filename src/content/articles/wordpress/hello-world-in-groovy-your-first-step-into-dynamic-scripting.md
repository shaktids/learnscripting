---
title: "Hello World in Groovy: Your First Step into Dynamic Scripting"
description: "Introduction Groovy, known for its simplicity and expressive syntax, is a dynamic programming language that runs on the Java Virtual Machine (JVM). In…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2023-10-05T13:38:38Z
legacy: true
wpId: 3967
---

Introduction

Groovy, known for its simplicity and expressive syntax, is a dynamic programming language that runs on the Java Virtual Machine (JVM). In this blog post, we'll embark on a journey into the world of Groovy by writing the classic "Hello, World!" program. By the end of this tutorial, you'll have a basic understanding of Groovy syntax and be ready to explore its versatile features further.

## Prerequisites

Before we start, make sure you have the following prerequisites in place:

1. **Java Development Kit (JDK)**: Groovy requires the Java runtime, so ensure that you have Java 8 or later installed on your system.
2. **Groovy Installed**: Follow the steps in our previous blog post on "Setting Up the Groovy Development Environment" to install Groovy and set up your environment.

## Writing Your First Groovy Script

Let's dive into writing your first Groovy program. Follow these simple steps:

### Step 1: Create a New File

Open your favorite text editor or integrated development environment (IDE). Create a new file and save it with a ".groovy" extension. You can name it "HelloWorld.groovy."

### Step 2: Write the Code

In the newly created file, enter the following code:

```groovy
class HelloWorld {
    static void main(String[] args) {
        println "Hello, World!"
    }
}
```

Let's break down this code:

- `class HelloWorld`: In Groovy, you define classes using the `class` keyword. Here, we're creating a class named `HelloWorld`.
- `static void main(String[] args)`: This line defines the `main` method, which serves as the entry point for our program, just like in Java. The `String[] args` parameter allows you to accept command-line arguments, although we're not using them in this simple example.
- `println "Hello, World!"`: Inside the `main` method, we use the `println` statement to print "Hello, World!" to the console.

### Step 3: Save the File

After writing the code, save the file.

### Step 4: Run the Program

To execute your Groovy program, open a terminal or command prompt, navigate to the directory where your "HelloWorld.groovy" file is located, and run the following command:

```groovy
groovy HelloWorld.groovy
```

You should see the output "Hello, World!" displayed in the terminal, confirming the successful execution of your first Groovy script.

Conclusion

Congratulations! You've just written and executed your first "Hello, World!" program in Groovy. While this example is simple, it demonstrates the clean and concise syntax that Groovy offers. Groovy's dynamic nature, combined with its compatibility with Java libraries and frameworks, makes it a versatile language for various applications, from scripting and automation to web development. Now that you've taken your first step into the world of Groovy, you're ready to explore its powerful features and capabilities further. Happy coding!
