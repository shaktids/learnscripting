---
title: "Parameterized Tests: Running the Same Test with Multiple Inputs Using @pytest.mark.parametrize"
description: "Effective software testing involves checking how your code behaves with various input scenarios. Writing individual test cases for each input can be time…"
lang: python
categories: ["Pytest"]
author: "Shakti Das"
pubDate: 2023-10-06T11:31:32Z
legacy: true
wpId: 4044
---

---

Effective software testing involves checking how your code behaves with various input scenarios. Writing individual test cases for each input can be time-consuming and repetitive. Pytest, a popular Python testing framework, provides a powerful feature called `@pytest.mark.parametrize` to simplify this process. In this blog post, we'll explore the concept of parameterized tests and learn how to use `@pytest.mark.parametrize` to run the same test with multiple inputs.

## The Need for Parameterized Tests

Consider a scenario where you have a function that calculates the sum of two numbers. You want to test this function with different input combinations to ensure its correctness. One way to approach this is by writing multiple test functions, each with a different set of inputs:

```python
def test_sum_positive_numbers():
    assert add(1, 2) == 3

def test_sum_negative_numbers():
    assert add(-1, -2) == -3

def test_sum_mixed_numbers():
    assert add(1, -2) == -1
```

While this approach works, it quickly becomes unwieldy as the number of input combinations grows. This is where parameterized tests shine.

## Using @pytest.mark.parametrize

With `@pytest.mark.parametrize`, you can define a single test function and specify multiple input combinations as parameters. Pytest will automatically generate and execute multiple test cases, each with a different set of inputs.

Here's how to use `@pytest.mark.parametrize`:

```python
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),        # Positive numbers
    (-1, -2, -3),     # Negative numbers
    (1, -2, -1),      # Mixed numbers
])
def test_sum(num1, num2, expected):
    assert add(num1, num2) == expected
```

In this example, we have a single `test_sum` function that takes three parameters: `num1`, `num2`, and `expected`. The `@pytest.mark.parametrize` decorator is used to specify multiple sets of inputs as a list of tuples.

Pytest will execute the `test_sum` function three times, once for each set of inputs defined in the list. It will automatically pass the values from each tuple to the test function, and the assertions will be checked for all cases.

## Benefits of Parameterized Tests

Parameterized tests offer several advantages:

1. **Concise Test Code:** You write one test function that handles multiple test cases, making your test suite more compact and maintainable.
2. **Easy to Add and Modify Test Cases:** You can easily add new test cases by adding more tuples to the parameterized list or modify existing ones.
3. **Clear Reporting:** Pytest generates clear and informative test reports, making it easy to identify which input combinations pass or fail.
4. **Reduced Duplication:** By reusing the same test logic for different inputs, you reduce code duplication and the likelihood of introducing errors in your test code.

## Conclusion

Parameterized tests with `@pytest.mark.parametrize` are a powerful tool in your testing toolbox. They enable you to efficiently test your code with multiple input combinations, improving test coverage and reducing code duplication. By using this feature, you can write more concise and maintainable test suites while ensuring the correctness of your software. So, embrace parameterized tests, and take your testing practices to the next level. Happy testing! 🚀
