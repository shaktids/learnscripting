---
title: "Shell Scripting Basic | Understanding Linux Shell"
description: "Simply definition, the shell is a program that takes inputs as commands from the keyboard and gives them to the operating system to perform action . In…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2019-06-23T14:54:28Z
legacy: true
wpId: 1639
---

Simply definition, the shell is a program that takes inputs as commands from the keyboard and gives them to the operating system to perform action . In the older days, it was the only way of user interface available on a Unix-like system such as Linux. Nowadays, we have *graphical user interfaces (GUIs)* in addition to *command line interfaces (CLIs)* such as the shell. In this post we discuss about the different terminology related to shell scripting.

1. **Shell**:The shell scripting is a Command-Line Interpreter which connects a user to **Operating System**.By which the user execute the commands.Which has executed by the compiler.
2. **Process**: Any task that a user run in the system is called a process. Which execute inside a processor with some protocol. A process is little more complex than just a task.
3. **File**:A file is something which resides on hard disk (HDD) and contains data owned by a **user**.
4. **X-windows aka windows**: A mode of Linux where screen (**monitor**) can be split in small “**parts**” called **windows**, that allow a **user** to do several things at the same time and/or switch from one task to another easily and view graphics in a nice way.
5. **Text terminal**: A monitor that has only the capability of displaying text stuff in black and white, where no graphics or a very basic graphics display.
6. **Session**: The period between **logging** **on** and **logging out** of the system.

### Types of Shell on a Standard Linux Distribution

**Bourne shell** : The Bourne shell was one of the major shells used in early versions and became a de facto standard. It was written by **Stephen Bourne** at **Bell Labs**. Every Unix-like system has at least one shell compatible with the Bourne shell. The Bourne shell program name is “**sh**” and it is typically located in the file system hierarchy at **/bin/sh**.

**C shell**: The **C shell** was developed by **Bill Joy** for the **Berkeley Software Distribution**. Its syntax is modeled after the **C** programming language. It is used primarily for interactive terminal use, but less frequently for scripting and operating system control. **C** shell has many interactive commands.

### Linux Shell Pathway for Automation

There exist thousands of commands for command-line user, how about remembering all of them? Hmmm! Simply you can not. The real power of computer is to ease the ease your work, you need to automate the process and hence you need scripts.

Scripts are collections of commands, stored in a file. The shell can read this file and act on the commands as if they were typed at the keyboard. The shell also provides a variety of useful programming features to make scripts truly powerful.
