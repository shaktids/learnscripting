---
title: "Creating Your First Test: Writing and Running a Basic Pytest Test Case"
description: "Welcome to the exciting world of software testing! Writing and running your first test case using Pytest is an essential step in becoming a proficient…"
lang: python
categories: ["Pytest"]
author: "Shakti Das"
pubDate: 2023-10-06T11:23:57Z
legacy: true
wpId: 4037
---

---

Welcome to the exciting world of software testing! Writing and running your first test case using Pytest is an essential step in becoming a proficient tester. In this blog, we'll guide you through the process of creating a basic Pytest test case, helping you gain confidence in your testing skills.

## What is Pytest?

[Pytest](https://pytest.org/) is a popular testing framework for Python that simplifies the process of writing and running tests. It provides a clean and concise way to define test cases and offers a wide range of powerful features for test automation.

## Prerequisites

Before you get started, ensure you have Python and Pytest installed as explained in our previous blog post, ["Setting Up the Environment: Installing Python and Pytest, and Creating a Test Project"](https://www.example.com/setting-up-environment).

## Creating Your First Test

Let's dive into creating your first Pytest test case. We'll start with a simple example to demonstrate the basics.

### Step 1: Project Structure

Ensure you have a project directory structure set up, as discussed in the previous blog post. Your directory structure should look something like this:

```python
my_test_project/
    ├── tests/
    │   ├── test_sample.py
    │   └── ...
    ├── app_code/
    │   └── ...
    └── requirements.txt
```

### Step 2: Writing the Test Case

1. Inside the `tests` directory, create a Python file for your test. We'll call it `test_sample.py`.
2. In `test_sample.py`, import the necessary libraries and write your first test function. Let's create a simple test to check if adding two numbers results in the expected sum.

```python
# Import the function or module you want to test (e.g., from app_code.calculator import add)
# If you don't have actual code to test yet, you can create a simple test like this:

def test_addition():
    assert 1 + 1 == 2
```

This test case is straightforward. It asserts that the result of `1 + 1` is equal to `2`. If this condition holds, the test will pass.

### Step 3: Running the Test

Now, it's time to run your test using Pytest. Open your terminal, navigate to your project directory, and run the following command:

```python
pytest
```

Pytest will automatically discover and execute your test cases. In this case, it will find `test_sample.py` and run the `test_addition` function. If everything is set up correctly, you should see output indicating that the test has passed:

```python
======================== test session starts ========================
platform ...
...

collected 1 item

tests/test_sample.py .                                        [100%]

========================= 1 passed in X.XXs ==========================
```

Congratulations! You've successfully written and run your first Pytest test case. You can now start adding more test cases to cover different aspects of your codebase and ensure its reliability.

## Conclusion

Testing is a crucial part of the software development process, and Pytest makes it easy to get started. In this blog, you've learned how to create a basic test case, write assertions, and run tests using Pytest. As you gain experience, you'll discover the power and flexibility Pytest offers for more complex testing scenarios. So, keep exploring and testing your code to deliver high-quality software to your users. Happy testing! 🚀
