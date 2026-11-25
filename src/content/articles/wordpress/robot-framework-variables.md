---
title: "Robot Framework Variables"
description: "Different types of variables The variable name consists of the type identifier ( $ , @ , & , % ), curly braces ( { , } ) and the variable name between the…"
lang: other
categories: ["Robot Framework"]
author: "Shakti Das"
pubDate: 2022-03-31T18:53:20Z
legacy: true
wpId: 3166
---

## Different types of variables

The variable name consists of the type identifier (`$`, `@`, `&`, `%`), curly braces (`{`, `}`) and the variable name between the braces. Use capital letters with global variables in the `*** Variables ***` section (`${SEARCH_URL}`). Use small letters with local variables that are only available in certain tasks or user keywords (`${search_url}`).

- Scalar: `${var}`
- List: `@{var}`
- Dictionary: `&{var}`
- Environment: `%{var}`

## Assigning variables

```
*** Settings ***
Documentation     Assigning variables.
Library           Collections
# You can create variables in a Python file and import them:
#Variables        variables.py

*** Keywords ***
What Does The Cat Say
    [Return]    Meow!

*** Tasks ***
Assign variables
    ${string}    Set Variable    Hello, world!    # ${string} = Hello, world!
    @{list}    Create List    a    b    c    # @{list} = [ a | b | c ]
    &{dict}    Create Dictionary    key1=val1    key2=val2    # &{dict} = { key1=val1 | key2=val2 }
    ${a}    ${b}    ${c}    Create List    a    b    c    # ${a} = a, ${b} = b, ${c} = c
    ${cat_says}    What Does The Cat Say    # ${cat_says} = Meow!
    ${evaluate}    Evaluate    datetime.date.today()    # ${evaluate} = 2020-09-08
    ${inline_evaluation}
    ...    Set Variable
    ...    ${{datetime.date.today() + datetime.timedelta(1)}}    # ${inline_evaluation} = 2020-09-09
```

> Expressions are evaluated using Python's [`eval`](https://docs.python.org/3/library/functions.html#eval) function. All Python built-in functions are available. All unrecognized Python variables are considered to be modules that are automatically imported. It is possible to use all available Python modules, including the standard modules and any installed third party modules.

## Built-in variables

| Variable | Description |
| --- | --- |
| `${CURDIR}` | The path to the task data file directory. |
| `${EMPTY}` | Like the `${SPACE}`, but without the space. Used to [pass empty arguments.](https://robocorp.com/docs/languages-and-frameworks/robot-framework/syntax#handling-empty-values) |
| `${EXECDIR}` | The path to the task execution directory. |
| `${False}` | Boolean `False`. |
| `${None}` | Python `None`. |
| `${null}` | Java `null`. |
| `${SPACE}` | ASCII space (`\x20`). |
| `${TEMPDIR}` | The path to the temporary directory. |
| `${True}` | Boolean `True`. |
| `${/}` | The directory path separator. `/` in UNIX-like systems and `\` in Windows. |
| `${:}` | The path element separator. `:` in UNIX-like systems and `;` in Windows. |
| `${\n}` | The line separator. `\n` in UNIX-like systems and `\r\n` in Windows. |

## Runtime variables

| Variable | Description |
| --- | --- |
| `${DEBUG_FILE}` | [Debug file](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#debug-file). |
| `${KEYWORD_MESSAGE}` | The error message of the current keyword. |
| `${KEYWORD_STATUS}` | The status of the current keyword, either `PASS` or `FAIL`. |
| `${LOG_FILE}` | [Logfile](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#log-file). |
| `${LOG_LEVEL}` | [Log level](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#log-levels) |
| `${OUTPUT_DIR}` | [Output directory](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#output-directory). |
| `${OUTPUT_FILE}` | [Output file](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#output-file). |
| `${PREV_TEST_MESSAGE}` | The error message of the previous task. |
| `${PREV_TEST_NAME}` | The name of the previous task, or an empty string if no tasks have been executed yet. |
| `${PREV_TEST_STATUS}` | The status of the previous task: `PASS`, `FAIL`, or an empty string when no tasks have been executed. |
| `${REPORT_FILE}` | [Report file](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#report-file). |
| `${SUITE_DOCUMENTATION}` | The documentation of the current task suite. |
| `${SUITE_MESSAGE}` | The full message of the current task suite, including statistics. |
| `&{SUITE_METADATA}` | The metadata of the current task suite. |
| `${SUITE_NAME}` | The full name of the current task suite. |
| `${SUITE_SOURCE}` | The path to the suite file or directory. |
| `${SUITE_STATUS}` | The status of the current task suite, either `PASS` or `FAIL`. |
| `${TEST_DOCUMENTATION}` | The documentation of the current task. |
| `${TEST_MESSAGE}` | The message of the current task. |
| `${TEST_NAME}` | The name of the current task. |
| `${TEST_STATUS}` | The status of the current task, either `PASS` or `FAIL`. |
| `@{TEST_TAGS}` | The tags of the current task are in alphabetical order. |
