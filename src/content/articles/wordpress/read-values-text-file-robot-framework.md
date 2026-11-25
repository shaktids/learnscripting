---
title: "How To Read Values From Text Files in Robot Framework"
description: "How to Extract Data from a Text File in Robot Framework Posted on September 22, 2017 by Shakti Das When working with Robot Framework, you can easily…"
lang: other
categories: ["Robot"]
author: "Shakti Das"
pubDate: 2017-09-22T06:28:38Z
updatedDate: 2023-11-08T04:17:13Z
legacy: true
wpId: 934
---

How to Extract Data from a Text File in Robot Framework

Posted on September 22, 2017 by Shakti Das

When working with Robot Framework, you can easily extract data from a text file using the "Get File" keyword from the Operating System Library. In this example, we will demonstrate how to read data from a text file named "doc.txt" located in your Robot project folder. This data may include sample Selenium test cases.

**The Robot Framework Code:**

```
*** Settings ***
Library OperatingSystem

*** Test Cases ***
Read Text File
    [Tags] test text
    ${TextFileContent}= Get File doc.txt
    Log ${TextFileContent}
```

In this code:

- We import the `OperatingSystem` library to use the "Get File" keyword.
- We create a test case named "Read Text File" with a "test text" tag.
- We use the "Get File" keyword to read the contents of the "doc.txt" file and store it in the `${TextFileContent}` variable.
- Finally, we log the content of the text file using the `Log` keyword.

**After executing this program, Robot Framework will produce the following output:**

```
Starting test: File. Read Text File
20170922 11:53:47.470 : INFO : Getting file 'C:\Users\Maa\robot\doc.txt'.
20170922 11:53:47.486 : INFO :
${TextFileContent} = *** Settings ***
Library Selenium2Library

*** Test Cases ***
Tc1
Open Browser http://www.google.com ff

20170922 11:53:47.486 : INFO :
*** Settings ***
Library Selenium2Library

*** Test Cases ***
Tc1
Open Browser http://www.google.com ff

Ending test: File. Read Text File
```

The output provides information about the test execution, including the file path and the content of "doc.txt." You can observe that the contents of the text file have been stored in the `${TextFileContent}` variable.

If you have any questions or need further assistance, please don't hesitate to ask. Feel free to share your queries in the comments section on how to read data from text files in Robot Framework.
