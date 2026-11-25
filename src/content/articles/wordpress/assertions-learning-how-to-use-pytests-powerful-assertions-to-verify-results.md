---
title: "Assertions: Learning How to Use Pytest's Powerful Assertions to Verify Results"
description: "Assertions are the backbone of any testing framework, and when it comes to Pytest, they are the key to validating whether your code behaves as expected…"
lang: python
categories: ["Pytest"]
author: "Shakti Das"
pubDate: 2023-10-06T11:25:25Z
legacy: true
wpId: 4039
---

---

Assertions are the backbone of any testing framework, and when it comes to Pytest, they are the key to validating whether your code behaves as expected. In this blog post, we'll explore the world of assertions in Pytest and show you how to use its powerful assertion methods to verify results effectively.

## What Are Assertions?

Assertions are statements that help you check if a given condition or expression is `True`. In the context of testing, assertions are used to validate that the output or behavior of your code matches your expectations. When an assertion fails, it indicates that something is wrong with your code, and it's time to investigate and fix the issue.

## Pytest's Assertion Methods

Pytest provides a rich set of assertion methods that go beyond the built-in `assert` statement in Python. These methods offer more informative failure messages and can be a real lifesaver when debugging failing tests. Let's dive into some of the most commonly used Pytest assertion methods.

### 1. `assert`

The basic `assert` statement in Python checks if a given expression is `True`. Pytest extends this by providing more detailed information about what went wrong when the assertion fails.

```python
def test_simple_assertion():
    assert 1 + 1 == 2
```

### 2. `assert x == y`

You can use `assert` in combination with comparison operators to check if two values are equal.

```python
def test_equal_assertion():
    x = 5
    y = 5
    assert x == y
```

### 3. `assert x != y`

This assertion is used to check if two values are not equal.

```python
def test_not_equal_assertion():
    x = 5
    y = 10
    assert x != y
```

### 4. `assert x in y`

Verify that a value exists within an iterable, such as a list or string.

```python
def test_in_assertion():
    numbers = [1, 2, 3, 4, 5]
    assert 3 in numbers
```

### 5. `assert x not in y`

The opposite of the previous assertion checks if a value is not present in an iterable.

```python
def test_not_in_assertion():
    fruits = ["apple", "banana", "cherry"]
    assert "orange" not in fruits
```

### 6. `assert x is y`

Check if two variables reference the same object.

```python
def test_identity_assertion():
    a = [1, 2, 3]
    b = a
    assert a is b
```

### 7. `assert x is not y`

Confirm that two variables do not reference the same object.

```python
def test_not_identity_assertion():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a is not b
```

### 8. `assert math.isclose(x, y)`

For comparing floating-point numbers, Pytest offers `math.isclose` assertions, which account for potential floating-point rounding errors.

```python
import math

def test_float_assertion():
    x = 0.1 + 0.2
    assert math.isclose(x, 0.3, rel_tol=1e-9)
```

## Running Tests with Assertions

To run your tests and check the assertions, use the `pytest` command in your terminal:

```python
pytest
```

## Conclusion

Assertions are the heart of testing, and Pytest equips you with a robust set of assertion methods to verify your code's correctness. Understanding how to use these assertions effectively is essential for writing reliable tests and identifying issues in your code. So, go ahead, write some tests, and use Pytest's powerful assertions to ensure that your code behaves as expected. Happy testing! 🚀
