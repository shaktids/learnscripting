---
title: "Python Naming Convention Rules"
description: "1. General Avoid using names that are too general or too wordy. Strike a good balance between the two. Bad: data structure, my list, info map, dictionary…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2019-09-15T06:55:58Z
legacy: true
wpId: 1808
---

## 1. General

- Avoid using names that are too general or too wordy. Strike a good balance between the two.
- Bad: data\_structure, my\_list, info\_map, dictionary\_for\_the\_purpose\_of\_storing\_data\_representing\_word\_definitions
- Good: user\_profile, menu\_options, word\_definitions
- Don’t be a jackass and name things “O”, “l”, or “I”
- When using CamelCase names, capitalize all letters of an abbreviation (e.g. HTTPServer)

## 2. Packages

- Package names should be all lower case
- When multiple words are needed, an underscore should separate them
- It is usually preferable to stick to 1 word names

## 3. Modules

- Module names should be all lower case
- When multiple words are needed, an underscore should separate them
- It is usually preferable to stick to 1 word names

## 4. Classes

- Class names should follow the UpperCaseCamelCase convention
- Python’s built-in classes, however are typically lowercase words
- Exception classes should end in “Error”

## 5. Global (module-level) Variables

- Global variables should be all lowercase
- Words in a global variable name should be separated by an underscore

## 6. Instance Variables

- Instance variable names should be all lower case
- Words in an instance variable name should be separated by an underscore
- Non-public instance variables should begin with a single underscore
- If an instance name needs to be mangled, two underscores may begin its name

## 7. Methods

- Method names should be all lower case
- Words in an method name should be separated by an underscore
- Non-public method should begin with a single underscore
- If a method name needs to be mangled, two underscores may begin its name

## 8. Method Arguments

- Instance methods should have their first argument named ‘self’.
- Class methods should have their first argument named ‘cls’

## 9. Functions

- Function names should be all lower case
- Words in a function name should be separated by an underscore

## 10. Constants

- Constant names must be fully capitalized
- Words in a constant name should be separated by an underscore
