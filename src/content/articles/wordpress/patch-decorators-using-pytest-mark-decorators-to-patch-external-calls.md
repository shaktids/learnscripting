---
title: "Patch Decorators: Using @pytest.mark Decorators to Patch External Calls"
description: "Introduction Unit testing is a fundamental practice in software development, helping ensure that individual units of code function correctly in isolation…"
lang: python
categories: ["Pytest"]
author: "Shakti Das"
pubDate: 2023-10-07T00:00:57Z
legacy: true
wpId: 4081
---

Introduction

Unit testing is a fundamental practice in software development, helping ensure that individual units of code function correctly in isolation. However, testing code that relies on external dependencies, such as APIs, databases, or external services, can be challenging. In Python, the `@pytest.mark` decorators provide a powerful way to address this issue by patching external calls and controlling their behavior during testing. In this blog post, we'll explore how to use `@pytest.mark` decorators to patch external calls in your pytest-based unit tests.

## The Challenge of External Dependencies

When writing unit tests, it's essential to isolate the code under test from external dependencies. External dependencies can be unpredictable, slow, or unavailable during testing, leading to unreliable and slow test suites.

One common way to address this challenge is to use "mocks" or "stubs" to simulate the behavior of external dependencies. In pytest, you can achieve this using the `@pytest.mark` decorators.

## What are @pytest.mark Decorators?

Pytest is a popular testing framework for Python that provides various features and plugins to make testing more manageable and efficient. `@pytest.mark` decorators are a feature of pytest that allows you to add metadata or markers to your test functions. These markers provide instructions to pytest, indicating how it should treat the test functions during test execution.

## Using @pytest.mark.parametrize

One commonly used `@pytest.mark` decorator is `@pytest.mark.parametrize`. While it is not directly related to patching external calls, it's worth mentioning because it allows you to parameterize your test functions with different sets of input data. This can be useful when you want to test your code with various inputs and expected outputs without writing separate test functions for each case.

Here's an example of how to use `@pytest.mark.parametrize`:

```python
import pytest

@pytest.mark.parametrize("input, expected", [
    ("input_data_1", "expected_output_1"),
    ("input_data_2", "expected_output_2"),
    # Add more test cases here
])
def test_my_function(input, expected):
    result = my_function(input)
    assert result == expected
```

In this example, the `test_my_function` test is run multiple times, once for each set of input and expected output values provided in the parameterized list.

## Using @pytest.mark.patch

While `@pytest.mark.parametrize` is useful for parameterizing test cases, `@pytest.mark.patch` (or `@pytest.mark.patch.object`) is used for patching external calls and controlling their behavior during testing.

To use `@pytest.mark.patch`, follow these steps:

1. **Import pytest and the necessary modules:**

```python
   import pytest
   from unittest.mock import patch
```

2. **Apply the decorator to your test function:**

```python
   @pytest.mark.patch("module_name.function_name")
   def test_my_function(mock_function):
       # Use mock_function in your test
```

Replace `module_name.function_name` with the actual module and function you want to patch.

3. **Use the mock in your test:** Inside your test function, you can use `mock_function` as if it were the real function. You can set the behavior of the mock using `mock_function.return_value` or other mock attributes.

Here's an example of using `@pytest.mark.patch` to patch an external API call using the `requests` library:

```python
import pytest
from unittest.mock import patch
import requests

@pytest.mark.patch("requests.get")
def test_fetch_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"key": "value"}

    result = fetch_data()

    assert result == {"key": "value"}
```

In this example, `@pytest.mark.patch` is used to patch the `requests.get` function. The mock's behavior is controlled using `mock_get.return_value`, allowing you to simulate a successful API call.

## Conclusion

`@pytest.mark` decorators, including `@pytest.mark.patch`, are powerful tools in pytest that allow you to control external calls and isolate your code under test from external dependencies. By patching external calls, you can make your unit tests more reliable, predictable, and faster, as you have full control over the behavior of external dependencies during testing. Incorporating these decorators into your pytest-based unit tests will help you write more effective and maintainable test suites for your Python projects.
