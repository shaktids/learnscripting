---
title: "Selective Test Execution: Running Specific Tests or Groups of Tests Using Markers in Pytest"
description: "In the world of software testing, executing all tests in your suite every time can be time consuming and inefficient. Pytest, a popular Python testing…"
lang: python
categories: ["Pytest"]
author: "Shakti Das"
pubDate: 2023-10-06T11:38:37Z
legacy: true
wpId: 4064
---

---

In the world of software testing, executing all tests in your suite every time can be time-consuming and inefficient. Pytest, a popular Python testing framework, offers a solution to this problem through the use of markers. Markers allow you to categorize and tag your tests, enabling you to selectively run specific tests or groups of tests based on their characteristics. In this blog post, we'll explore how to use markers in Pytest for selective test execution and discuss its benefits.

## The Need for Selective Test Execution

In a real-world software project, you might have hundreds or even thousands of tests. Running all of them for every code change or in every test cycle can be impractical. There are several scenarios where you might want to execute only specific tests:

- **Focused Testing:** You want to run only a subset of tests that are relevant to the code changes you made. This speeds up development and provides quick feedback.
- **Regression Testing:** During regression testing, you often want to rerun only the tests affected by recent code changes to verify that nothing broke.
- **Smoke Testing:** Smoke tests are typically a small set of critical tests that check if the application's core functionality is working. Running these tests quickly is crucial for detecting major issues early.

## Using Markers for Selective Execution

Marking tests in Pytest involves assigning labels or tags to them using the `@pytest.mark` decorator. You can create custom markers to categorize your tests based on different criteria, such as functional areas, priority, or characteristics like performance or stability.

### Defining Custom Markers

To define custom markers, add marker definitions to your test code. For example:

```python
import pytest

@pytest.mark.smoke
def test_critical_functionality():
    # Test logic here

@pytest.mark.regression
def test_new_feature():
    # Test logic here
```

In this example, we've created two custom markers: `@pytest.mark.smoke` and `@pytest.mark.regression`.

### Running Tests with Markers

You can execute tests with specific markers by using the `-k` (keyword) option followed by the marker's name when running Pytest. For example:

```python
pytest -k smoke
```

This command will run all tests marked with `@pytest.mark.smoke`.

You can also use logical operators like `or` to run tests with multiple markers:

```python
pytest -k "smoke or regression"
```

This command will execute tests marked with either `@pytest.mark.smoke` or `@pytest.mark.regression`.

### Combining Markers

You can use multiple markers on the same test function to categorize it in different ways. For example:

```python
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_critical_functionality():
    # Test logic here
```

This test will be included when running both `@pytest.mark.smoke` and `@pytest.mark.regression`.

## Benefits of Selective Test Execution with Markers

Selective test execution with markers offers several benefits:

1. **Efficiency:** You can focus on running only the tests that matter, saving time and resources during development and testing.
2. **Quick Feedback:** Running only relevant tests provides rapid feedback on code changes, helping to identify issues early in the development process.
3. **Regression Testing:** You can easily rerun only the tests affected by recent code changes to verify that new features or bug fixes didn't introduce regressions.
4. **Custom Categorization:** Create custom markers to categorize your tests based on project-specific criteria, such as performance, security, or stability.
5. **Test Organization:** Markers help organize your test suite, making it easier to locate and manage tests.

## Conclusion

Selective test execution using markers in Pytest is a valuable practice for efficient testing and test management. By tagging your tests with markers, you can categorize them based on various criteria and choose which tests to run, depending on your testing needs. This approach improves development speed, provides quick feedback, and enhances your ability to maintain and manage your test suite. So, embrace markers in Pytest and gain control over your test execution. Happy testing! 🚀
