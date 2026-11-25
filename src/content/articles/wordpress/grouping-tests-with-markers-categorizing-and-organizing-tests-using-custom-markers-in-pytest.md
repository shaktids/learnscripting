---
title: "Grouping Tests with Markers: Categorizing and Organizing Tests Using Custom Markers in Pytest"
description: "Efficient testing involves more than just writing test cases. It's essential to organize your tests in a meaningful way to make test maintenance…"
lang: python
categories: ["Pytest"]
author: "Shakti Das"
pubDate: 2023-10-06T11:34:06Z
legacy: true
wpId: 4046
---

---

Efficient testing involves more than just writing test cases. It's essential to organize your tests in a meaningful way to make test maintenance, reporting, and execution more manageable. In Pytest, you can achieve this by using custom markers to categorize and group your tests. In this blog post, we will explore the concept of grouping tests with markers, the benefits it offers, and how to implement it effectively.

## Understanding Test Markers

In Pytest, test markers are annotations or labels that you can attach to your test functions to categorize or group them. Markers help you:

- Organize your tests logically.
- Specify which tests to run selectively.
- Add metadata or attributes to tests, such as categories, priorities, or requirements.
- Extend Pytest's functionality with custom behaviors.

Markers are incredibly flexible and allow you to create custom markers tailored to your project's needs.

## Benefits of Grouping Tests with Markers

Grouping tests with markers provides several advantages:

1. **Organization:** Markers help you categorize tests into logical groups, making it easier to locate and manage specific test cases.
2. **Selective Execution:** You can run specific groups of tests by specifying the marker names, saving time during development and continuous integration processes.
3. **Documentation:** Markers can serve as documentation, providing information about the purpose or requirements of each test.
4. **Customization:** You can extend Pytest's functionality by creating custom markers that trigger specific behaviors or hooks during test execution.

## Implementing Custom Markers

To create and use custom markers in Pytest, follow these steps:

### Step 1: Define Custom Markers

In your test code, define custom markers using the `@pytest.mark` decorator. You can create as many markers as you need.

```python
import pytest

@pytest.mark.smoke  # Custom marker for smoke tests
@pytest.mark.regression  # Custom marker for regression tests
def test_example():
    assert True

@pytest.mark.performance  # Custom marker for performance tests
def test_performance():
    assert perform_action() < 1.0
```

### Step 2: Run Tests Using Markers

You can run tests with specific markers using the `-k` (keyword) option when executing Pytest:

```python
pytest -k "smoke or regression"
```

This command will run all tests marked with either `smoke` or `regression`. You can use logical operators like `and` and `or` to specify more complex conditions.

### Step 3: Create Custom Behaviors (Optional)

You can define custom behaviors associated with markers by using Pytest hooks. For example, you can create a custom fixture that performs setup specific to tests with a particular marker:

```python
import pytest

@pytest.fixture(scope="function")
def custom_setup_teardown(request):
    marker = request.node.get_closest_marker("performance")
    if marker:
        # Custom setup code for performance tests
        setup_performance_environment()
    yield
    if marker:
        # Custom teardown code for performance tests
        cleanup_performance_environment()
```

In this example, the `custom_setup_teardown` fixture detects the presence of the `performance` marker and performs corresponding setup and teardown actions.

### Step 4: Running Tests with Custom Behaviors

To run tests with custom behaviors associated with markers, simply use the markers in your test functions, and Pytest will execute the associated setup and teardown code automatically.

```python
@pytest.mark.performance
def test_performance(custom_setup_teardown):
    assert perform_action() < 1.0
```

## Conclusion

Grouping tests with markers in Pytest is a valuable technique for organizing, managing, and customizing your test suite. By defining custom markers, you can categorize tests based on their purpose, requirements, or attributes and use these markers to selectively execute tests and trigger custom behaviors. This approach enhances test organization and flexibility, making your testing efforts more efficient and effective. So, embrace custom markers and take control of your test suite's organization and execution. Happy testing! 🚀
