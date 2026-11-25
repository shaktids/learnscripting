---
title: "Robot Framework Keywords and Arguments: A Guide to Built-In and Custom Keywords"
description: "Robot Framework, known for its keyword driven approach, simplifies test automation by allowing testers to use built in keywords and create custom ones. In…"
lang: other
categories: ["Robot Framework"]
author: "Shakti Das"
pubDate: 2023-10-04T05:49:29Z
legacy: true
wpId: 3820
---

Robot Framework, known for its keyword-driven approach, simplifies test automation by allowing testers to use built-in keywords and create custom ones. In this blog post, we'll explore the concepts of keywords and arguments in Robot Framework, covering the use of built-in keywords and how to create your custom keywords for efficient and maintainable test automation.

## Understanding Keywords

In Robot Framework, keywords are the fundamental building blocks of test cases. Keywords represent actions, verifications, or operations that you want to perform during your tests. There are three primary types of keywords:

1. **Built-In Keywords**: These keywords come prepackaged with Robot Framework and cover a wide range of common actions and verifications. They are part of the Robot Framework core and are readily available for use.
2. **User-Defined Keywords**: Testers can create their own custom keywords to encapsulate and reuse sequences of actions or verifications. User-defined keywords enhance test case modularity and maintainability.
3. **External Keywords**: External keywords are provided by libraries or external resources. Robot Framework supports integration with various libraries, such as SeleniumLibrary for web testing or DatabaseLibrary for database interactions. These libraries extend Robot Framework's capabilities with their own set of keywords.

## Using Built-In Keywords

Built-in keywords are readily available for use in Robot Framework, making it easy to perform common actions and verifications without writing custom code. These keywords are grouped into libraries based on their functionality. Here are some examples of commonly used built-in keywords:

- `Open Browser`: Opens a web browser.
- `Input Text`: Types text into a text field.
- `Click Button`: Clicks a button on a web page.
- `Page Should Contain`: Verifies that a web page contains specific text or elements.
- `Should Be Equal As Strings`: Compares two strings for equality.

Here's an example of a Robot Framework test case using built-in keywords:

```
*** Test Cases ***
Search for a Product
    [Documentation]    This test searches for a product on a website.
    Open Browser    https://example.com    Chrome
    Input Text    id=search-box    Robot Framework
    Click Button    id=search-button
    Page Should Contain    Results for "Robot Framework"
    Close Browser
```

In this test case:

- `Open Browser`, `Input Text`, `Click Button`, `Page Should Contain`, and `Close Browser` are built-in keywords.
- `https://example.com` and `Chrome` are arguments passed to the `Open Browser` keyword.
- `id=search-box`, `id=search-button`, and `Results for "Robot Framework"` are arguments passed to other keywords.

## Creating Custom Keywords

While built-in keywords cover a wide range of actions, there will be situations where you need to create custom keywords to encapsulate specific test steps or verifications. Creating custom keywords is a powerful feature of Robot Framework that enhances the maintainability and reusability of your test cases.

To create a custom keyword, you define it in the test suite's "Keywords" section. Here's an example of a user-defined keyword:

```
*** Keywords ***
Log In with Valid Credentials
    [Arguments]    ${username}    ${password}
    Input Text    id=username    ${username}
    Input Text    id=password    ${password}
    Click Button    id=login-button
    Page Should Contain    Welcome, User
```

In this example:

- `Log In with Valid Credentials` is the name of the custom keyword.
- `[Arguments]` specify the arguments the keyword accepts. `${username}` and `${password}` are placeholders for the actual values you'll provide when using the keyword.

Once you've defined a custom keyword, you can use it in your test cases like any built-in keyword:

```
*** Test Cases ***
Verify Successful Login
    [Documentation]    This test case verifies a successful login.
    Open Browser    https://example.com    Chrome
    Log In with Valid Credentials    myusername    mypassword
    Close Browser
```

In this test case:

- `Log In with Valid Credentials` is a custom keyword.
- `myusername` and `mypassword` are the actual values provided as arguments to the custom keyword.

## Conclusion

Robot Framework's keyword-driven approach simplifies test automation by providing a structured and readable way to define test cases. Built-in keywords cover common actions and verifications, while custom keywords allow testers to encapsulate and reuse sequences of steps.

Understanding how to use built-in keywords and create custom keywords is fundamental to mastering Robot Framework. By leveraging the power of keywords and arguments, you can create efficient and maintainable test cases that help you deliver high-quality software with confidence. Happy testing! 🤖🚀
