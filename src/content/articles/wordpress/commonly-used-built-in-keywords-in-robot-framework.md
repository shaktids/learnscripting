---
title: "Commonly Used Built-In Keywords in Robot Framework"
description: "Robot Framework simplifies test automation with a wealth of built in keywords that cover a wide range of testing needs. These keywords provide ready to…"
lang: other
categories: ["Robot Framework"]
author: "Shakti Das"
pubDate: 2023-10-04T06:00:29Z
legacy: true
wpId: 3842
---

Robot Framework simplifies test automation with a wealth of built-in keywords that cover a wide range of testing needs. These keywords provide ready-to-use functionality, saving you time and effort in test case development. In this blog post, we'll explore some commonly used built-in keywords in Robot Framework across different categories, including web testing, file operations, string manipulation, and more.

## Web Testing Keywords

### `Open Browser`

The `Open Browser` keyword does precisely what its name suggests: it opens a web browser to a specified URL. It's the first step in most web automation tests.

```
Open Browser    https://example.com    Chrome
```

### `Input Text`

The `Input Text` keyword allows you to enter text into a text field on a web page, which is a fundamental action in form testing.

```
Input Text    id=username    myusername
```

### `Click Button`

To interact with buttons or elements that trigger actions on a web page, you can use the `Click Button` keyword.

```
Click Button    id=login-button
```

### `Page Should Contain`

The `Page Should Contain` keyword verifies that a specific text or element is present on the page, ensuring that the expected content is visible.

```
Page Should Contain    Welcome, User
```

## File Operations Keywords

### `File Should Exist`

For file-related tests, the `File Should Exist` keyword checks if a file exists at the specified path.

```
File Should Exist    /path/to/file.txt
```

### `Copy File`

The `Copy File` keyword allows you to copy a file from one location to another, which can be useful for test setup or teardown.

```
Copy File    /source/file.txt    /destination/file.txt
```

### `Append To File`

To add content to an existing file, you can use the `Append To File` keyword.

```
Append To File    /path/to/file.txt    This is new content.
```

## String Manipulation Keywords

### `Should Be Equal As Strings`

The `Should Be Equal As Strings` keyword compares two strings for equality, a basic yet critical operation for validating text in tests.

```
Should Be Equal As Strings    Actual Text    Expected Text
```

### `Get Substring`

To extract a portion of a string, the `Get Substring` keyword can be used. It's helpful for parsing and verifying text.

```
${substring}=    Get Substring    My full name is John Doe    16    19
```

## Conditional Keywords

### `Run Keyword If`

The `Run Keyword If` keyword allows you to conditionally execute other keywords based on a specified condition. This is valuable for handling different scenarios in your tests.

```
Run Keyword If    '${variable}' == 'Expected Value'    Keyword to Execute
```

### `Fail If`

The `Fail If` keyword fails a test if a specified condition is met. It's useful for explicitly marking a test as failed when certain conditions are not met.

```
Fail If    '${variable}' != 'Expected Value'    Custom Failure Message
```

## Looping Keywords

### `FOR`

The `FOR` keyword provides a way to create loops in Robot Framework. It's helpful for iterating through lists, data sets, or other collections.

```
FOR    ${item}    IN    @{list}
    Log    ${item}
END
```

### `Continue For Loop If`

The `Continue For Loop If` keyword allows you to skip the rest of the current iteration and continue to the next iteration in a loop.

```
FOR    ${item}    IN    @{list}
    Continue For Loop If    '${item}' == 'Skip'
    Log    Processing: ${item}
END
```

## Conclusion

Robot Framework's extensive library of built-in keywords simplifies test automation across various domains. These commonly used keywords enable testers and developers to create efficient, maintainable, and comprehensive test cases without having to write custom code for every scenario. By leveraging these built-in keywords, you can streamline your test automation efforts and ensure the reliability and quality of your software. Happy testing! 🤖🔧
