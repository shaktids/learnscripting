---
title: "Wait Statement in Selenium Different Types of Wait"
description: "Wait Statement is used in selenium to make some delay and during that period of time we need to do something and or to wait for presence of element.We can…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T07:44:54Z
legacy: true
wpId: 73
---

**Wait Statement** is used in selenium to make some delay and during that period of time we need to do something and or to wait for presence of element.We can make wait a website three types Implicit wait Explicit wait and Fluent Wait.All the waits statement are different function and different uses.

Normal Wait-**Thread .sleep(millisecond)** // It is also known as hard coded wait this wait statement will wait for a particular period of time.
This wait statement is not used in selenium script because of the element is displayed in the short duration of time it will wait unnecessary for rest of the time.

**[Example Link](http://learntowish.com/selenium-wait/)**

## Implicitly Wait-
syntax-**driver.manage.timeout.implicitlywait(second,Timeunit.SECOND).**
Implicitly wait will monitor the entire html source code and it will wait till page is loaded.Once the page is loaded within short duration of time it will not wait for rest of the time.And it will pass the control to the next line,But this implicit wait will not wait for ajax application.

**[Example Link](http://learntowish.com/selenium-wait/)**

It is used before get method .Before throwing page load timeout expectation.It will wait for page to load.If the page is not loaded in that duration of time it will throw expectation in the console,

## Explicitly Wait-
**WebDriverWait wait=new WebDriverWait(driver,20);**
 **wait.until(ExpectedCondition.presenseofElementLocated(By.XPATH("")));**

Explicit wait will wait for element to be present to be present on the user interface.It will check after every 500 millisecond.If the element is present on the user interface pass the control to next line .**[Example Link](http://learntowish.com/selenium-wait/)**

Implicit and Explicitly wait is also known as synchronization.

Another type of wait is **FluentWait** which is used to check the element is present or not dynamically at each polling interval with a timeout constraints.**[Example Link](http://learntowish.com/selenium-wait/)**
