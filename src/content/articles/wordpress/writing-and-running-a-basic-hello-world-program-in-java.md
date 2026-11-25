---
title: "Writing and Running a Basic \"Hello World\" Program in Java"
description: "Starting your journey in programming with Java is an exciting endeavor. One of the first steps you'll take is to write and run a simple \"Hello World\"…"
lang: other
categories: ["Java"]
author: "Shakti Das"
pubDate: 2023-11-07T15:04:21Z
legacy: true
wpId: 4348
---

Starting your journey in programming with Java is an exciting endeavor. One of the first steps you'll take is to write and run a simple "Hello World" program. In this blog, we'll guide you through the process of creating a basic Java program that prints "Hello, World!" to the console.

### Setting Up Your Environment:
Before you write your first Java program, you need to ensure that your development environment is properly set up. This includes having the Java Development Kit (JDK) installed on your computer. We covered the JDK installation in a previous blog, so make sure you have it up and running.

### Writing Your First Java Program:
Open your favorite code editor or Integrated Development Environment (IDE) – such as Eclipse, IntelliJ IDEA, or even a simple text editor – and follow these steps to write your "Hello World" program:

**Step 1: Create a New Java Class**

In Java, programs are organized into classes. Each program should have a class definition that contains the main method, which is the entry point for your application. Here's a basic example:

```java
public class HelloWorld {
    public static void main(String[] args) {
        // Your code goes here
    }
}
```

In this code snippet, we've created a class named "HelloWorld" with a "main" method. The "public" and "static" keywords have specific meanings in Java and are necessary for the program to run.

**Step 2: Print "Hello, World!"**

Inside the "main" method, you'll add the code to print "Hello, World!" to the console. To do this, you use the "System.out.println()" method:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

The line "System.out.println("Hello, World!");" tells the program to display "Hello, World!" on the console.

**Step 3: Save Your Program**

Save your Java file with a ".java" extension, using the same name as your class. In this case, save it as "HelloWorld.java."

### Compiling and Running Your Program:
After writing your Java program, it's time to compile and run it:

**Step 1: Open the Command Prompt or Terminal**

Navigate to the directory where you saved your "HelloWorld.java" file using the command prompt (Windows) or terminal (macOS and Linux).

**Step 2: Compile the Java Code**

To compile your code, use the "javac" command followed by the name of your Java file:

```java
javac HelloWorld.java
```

This will compile your code into bytecode, which can be executed by the Java Virtual Machine (JVM).

**Step 3: Run the Java Program**

After successfully compiling your code, you can run it using the "java" command:

```java
java HelloWorld
```

The output should be "Hello, World!" displayed on your console.

### Conclusion:
Writing and running a "Hello World" program in Java is your first step towards mastering this powerful programming language. It introduces you to the basic structure of a Java program, the "main" method, and the essential "System.out.println()" statement for printing output. From here, you can explore and expand your Java programming skills, diving into more complex applications and understanding the many features that make Java such a versatile language for web development, mobile app development, and more. Happy coding!
