---
title: "Examples of Test Automation Tasks: Harnessing the Power of Built-in Keywords"
description: "In today's fast paced software development landscape, test automation has become a crucial component of ensuring software quality. Test automation not…"
lang: other
categories: ["Robot Framework"]
author: "Shakti Das"
pubDate: 2023-10-04T16:21:34Z
legacy: true
wpId: 3860
---

In today's fast-paced software development landscape, test automation has become a crucial component of ensuring software quality. Test automation not only saves time and effort but also enhances test coverage and reliability. One of the key aspects of successful test automation is the use of built-in keywords that simplify the automation process. In this blog, we will explore practical examples of test automation tasks and demonstrate how to automate them using built-in keywords.

## What Are Built-in Keywords?

Before we dive into examples, let's briefly understand what built-in keywords are. Built-in keywords are pre-defined functions or actions provided by test automation frameworks or tools. These keywords enable testers to interact with the application under test (AUT) and perform various actions without writing complex code from scratch. They serve as building blocks for creating automated test scripts.

## Example 1: Logging into a Web Application

**Objective:** Automate the process of logging into a web application.

**Solution:** To achieve this, we can use built-in keywords like `Open Browser`, `Input Text`, `Click Button`, and `Verify Text` (for validation).

```
*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Login to Web Application
    Open Browser    https://example.com    Chrome
    Input Text      id=username    your_username
    Input Text      id=password    your_password
    Click Button    id=loginButton
    Verify Text     css=.welcome-message    Welcome, User!
    Close Browser
```

In this example, we open a browser, enter the username and password, click the login button, verify the welcome message, and then close the browser—all with the help of built-in keywords.

## Example 2: Testing APIs

**Objective:** Automate API testing by sending a GET request and validating the response.

**Solution:** For API testing, we can use keywords like `Create Session`, `GET Request`, and `Should Be Equal` (for validation).

```
*** Settings ***
Library           RequestsLibrary

*** Test Cases ***
Test API Endpoint
    Create Session    api_session    https://api.example.com
    ${response}    GET Request    api_session    /endpoint
    Should Be Equal    ${response.status_code}    200
    Should Be Equal    ${response.json().key}    expected_value
```

This script establishes a session with the API, sends a GET request, and validates the response status code and a specific JSON key.

## Example 3: Data-Driven Testing

**Objective:** Automate a test scenario with multiple sets of data.

**Solution:** Utilize built-in keywords like `Run Keyword And Continue On Failure` and `Run Keyword If`.

```
*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Data-Driven Test
    [Template]    Test with Data
    username    password
    user1       pass1
    user2       pass2

*** Keywords ***
Test with Data
    [Arguments]    ${username}    ${password}
    Open Browser    https://example.com    Chrome
    Input Text      id=username    ${username}
    Input Text      id=password    ${password}
    Click Button    id=loginButton
    Run Keyword And Continue On Failure    Verify Login Success

Verify Login Success
    Verify Text     css=.welcome-message    Welcome, User!
    Close Browser
```

In this example, we perform data-driven testing by iterating through different sets of username and password combinations.

## Example 4: Mobile App Automation

**Objective:** Automate interactions with a mobile app.

**Solution:** Use keywords provided by mobile automation libraries like `AppiumLibrary`.

```
*** Settings ***
Library           AppiumLibrary

*** Test Cases ***
Automate Mobile App
    Open Application    platform=iOS    app=MyApp.app
    Input Text          id=username_field    my_username
    Input Text          id=password_field    my_password
    Click Element       id=login_button
    Wait Until Page Contains Element    id=welcome_message
    Capture Screenshot
    Close Application
```

This script demonstrates the automation of a mobile app, from launching the app to capturing a screenshot.

## Example 5: Database Testing

**Objective:** Automate database testing by querying the database and validating results.

**Solution:** Utilize keywords like `Connect To Database` and `Query`.

```
*** Settings ***
Library           DatabaseLibrary

*** Test Cases ***
Test Database
    Connect To Database    psycopg2    dbname=mydb    user=myuser    password=mypassword    host=localhost
    @{result}    Query    SELECT * FROM users WHERE age > 30
    Should Contain    ${result}    John Doe
    Close All Database Connections
```

This script connects to a database, queries it, and validates the presence of specific data.

## Conclusion

Test automation is a powerful tool in modern software development, and built-in keywords play a vital role in simplifying the automation process. In this blog, we've explored practical examples of test automation tasks, ranging from web and API testing to mobile app and database testing. By harnessing the power of built-in keywords, testers can create efficient, reliable, and maintainable automated test scripts, thereby improving the quality of their software products and accelerating the release cycle.
