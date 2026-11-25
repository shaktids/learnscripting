---
title: "Java Script Basic operators, maths"
description: "Exploring JavaScript Basic Operators and Math Functions JavaScript is a versatile language that powers much of the interactivity on the web. At its core…"
lang: javascript
categories: ["JavaScript"]
author: "Shakti Das"
pubDate: 2021-05-30T07:01:43Z
updatedDate: 2024-03-28T01:58:47Z
legacy: true
wpId: 2420
---

### Exploring JavaScript Basic Operators and Math Functions

JavaScript is a versatile language that powers much of the interactivity on the web. At its core are fundamental operators and math functions that allow developers to manipulate data and create dynamic web applications. Whether you're just starting with JavaScript or looking to expand your knowledge, understanding these basics is essential. Let's dive into JavaScript's basic operators and math functions.

#### Basic Operators

JavaScript provides several basic operators for performing operations on variables and values. These operators include arithmetic, assignment, comparison, logical, and more.

##### 1. Arithmetic Operators

Arithmetic operators perform mathematical operations on numeric operands.

- **Addition (`+`)**: Adds two operands.
- **Subtraction (`-`)**: Subtracts the second operand from the first.
- **Multiplication (`*`)**: Multiplies two operands.
- **Division (`/`)**: Divides the first operand by the second.
- **Modulus (`%`)**: Returns the division remainder.

Example:

```javascript
let num1 = 10;
let num2 = 5;
let sum = num1 + num2; // 15
let difference = num1 - num2; // 5
let product = num1 * num2; // 50
let quotient = num1 / num2; // 2
let remainder = num1 % num2; // 0
```

##### 2. Assignment Operators

Assignment operators assign values to JavaScript variables.

- **Assignment (`=`)**: Assigns the value of the right operand to the left operand.
- **Addition Assignment (`+=`)**: Adds the right operand to the left operand and assigns the result.
- **Subtraction Assignment (`-=`)**: Subtracts the right operand from the left operand and assigns the result.
- **Multiplication Assignment (`*=`)**: Multiplies the left operand by the right operand and assigns the result.
- **Division Assignment (`/=`)**: Divides the left operand by the right operand and assigns the result.

Example:

```javascript
let x = 10;
x += 5; // x is now 15
x -= 3; // x is now 12
x *= 2; // x is now 24
x /= 4; // x is now 6
```

##### 3. Comparison Operators

Comparison operators compare two values and return a Boolean result.

- **Equal (`==`)**: Returns true if the operands are equal.
- **Not Equal (`!=`)**: Returns true if the operands are not equal.
- **Strict Equal (`===`)**: Returns true if the operands are equal and of the same type.
- **Strict Not Equal (`!==`)**: Returns true if the operands are not equal or not of the same type.
- **Greater Than (`>`)**: Returns true if the left operand is greater than the right operand.
- **Less Than (`<`)**: Returns true if the left operand is less than the right operand.
- **Greater Than or Equal (`>=`)**: Returns true if the left operand is greater than or equal to the right operand.
- **Less Than or Equal (`<=`)**: Returns true if the left operand is less than or equal to the right operand.

Example:

```javascript
let a = 5;
let b = 10;

console.log(a == b); // false
console.log(a != b); // true
console.log(a === b); // false
console.log(a !== b); // true
console.log(a > b); // false
console.log(a < b); // true
console.log(a >= b); // false
console.log(a <= b); // true
```

##### 4. Logical Operators

Logical operators are used to combine or negate Boolean values.

- **Logical AND (`&&`)**: Returns true if both operands are true.
- **Logical OR (`||`)**: Returns true if at least one of the operands is true.
- **Logical NOT (`!`)**: Returns the opposite of the operand's Boolean value.

Example:

```javascript
let x = 5;
let y = 10;
let z = 15;

console.log(x < y && y < z); // true
console.log(x < y || y > z); // true
console.log(!(x > y)); // true
```

#### Math Functions

JavaScript also provides a built-in `Math` object with a variety of useful mathematical functions.

##### 1. `Math.abs()`

Returns the absolute (positive) value of a number.

```javascript
let num = -10;
let absNum = Math.abs(num); // 10
```

##### 2. `Math.pow()`

Returns the base to the exponent power.

```javascript
let base = 2;
let exponent = 3;
let result = Math.pow(base, exponent); // 8 (2^3)
```

##### 3. `Math.sqrt()`

Returns the square root of a number.

```javascript
let number = 16;
let squareRoot = Math.sqrt(number); // 4
```

##### 4. `Math.max()` and `Math.min()`

Returns the maximum or minimum value from a list of numbers.

```javascript
let maxNumber = Math.max(10, 20, 30); // 30
let minNumber = Math.min(10, 20, 30); // 10
```

##### 5. `Math.round()`, `Math.floor()`, and `Math.ceil()`

- `Math.round()` rounds a number to the nearest integer.
- `Math.floor()` rounds a number down to the nearest integer.
- `Math.ceil()` rounds a number up to the nearest integer.

```javascript
let decimal = 5.7;
let rounded = Math.round(decimal); // 6
let floored = Math.floor(decimal); // 5
let ceiled = Math.ceil(decimal); // 6
```

##### 6. `Math.random()`

Generates a random number between 0 (inclusive) and 1 (exclusive).

```javascript
let randomNum = Math.random(); // 0.12345 (example)
```

#### Conclusion

JavaScript's basic operators and math functions are foundational to building dynamic and interactive web applications. By mastering these concepts, you gain the ability to perform arithmetic operations, make comparisons, and utilize powerful math functions. Whether you're creating a calculator, handling user input, or developing complex algorithms, understanding these fundamentals is key to becoming a proficient JavaScript developer. As you continue your JavaScript journey, these tools will serve as valuable building blocks for creating innovative and functional web experiences.
