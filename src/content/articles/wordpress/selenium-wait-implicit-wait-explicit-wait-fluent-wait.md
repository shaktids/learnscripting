---
title: "Selenium Wait Implicit Wait Explicit Wait Fluent Wait"
description: "Selenium Wait Command is used in Selenium WebDriver to wait a particular amount of time defined by user. Selenium Wait can be divided into two categories…"
lang: other
categories: ["Java", "Selenium"]
author: "Shakti Das"
pubDate: 2017-03-11T12:38:23Z
legacy: true
wpId: 483
---

**Selenium Wait** Command is used in Selenium **WebDriver** to wait a particular amount of time defined by user.**Selenium Wait** can be divided into two categories **Implicit wait** and **Explicit wait** and another type of hybrid wait is Fluent Wait.In the implicit wait selenium **WebDriver** wait for a fixed amount of time before executing next command or throwing an **exception** . Where in all other Selenium Wait type of  **WebDriver** will execute the next line of command if it found that element.

## Implicit wait
This is the **Selenium Wait** statement gives command to the browser to wait for an certain period of time in that time if the element is located in the page the execution will take place or else the "**WebDriver** **wait"** for a specific amount of time to check whether the element is located on that page or not.

```
driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
```

[codesyntax lang="java"]

```
package tesng;
public class robot { protected WebDriver driver;
 @Test public void tutorials() throws InterruptedException {
System.setProperty("webdriver.gecko.driver", "D:\\geckodriver.exe");
 driver = new FirefoxDriver(); driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
driver.get("http://www.marketwatch.com/"); System.out.println(driver.findElement(By.linkText("The Moneyologist")).getTagName()); } }
```

[/codesyntax]

In above example  the **WebDriver wait** for 10 Second to find the link text is present or not.

**Note for implicit-**From Selenium 3.0.1 release the WebDriver is not throwing the exception **"Element not Found Exception"** instead of  it is waiting for element to be present.

## Explicit wait
An explicit wait is a wait statement let the user to define for a certain condition and predefined time to wait for  proceeding further in the code. The Explicit wait wait for an particular event to occur in that period of time to perform any operation on that  web element.

```
   WebElement DynamicElement = (new WebDriverWait(driver, 10))
                .until(ExpectedConditions.presenceOfElementLocated(By.xpath(".//input[@type='text']")));
```

[codesyntax lang="java"]

```
package tesng;

public class explicit_wait {
 protected WebDriver driver;
 @Test     public void guru99tutorials() throws InterruptedException {
      System.setProperty("webdriver.gecko.driver", "D:\\geckodriver.exe");
     driver = new FirefoxDriver();        driver.get("http://www.google.co.in");
      WebElement DynamicElement = (new WebDriverWait(driver, 10)).until(ExpectedConditions.presenceOfElementLocated(By.xpath(".//input[@type='text']")));     } }
```

[/codesyntax]

The WebDriver will for a  maximum 10 second to check the presence of the element located by xpath if in between 10 seconds the driver is finding that element it will execute the next step.

## Selenium Fluent Wait
**Fluent Wait** is an special type of **Selenium Wait** used to find the object when the object is dynamic in nature. It will check the presence of element in particular interval time and will handle exception by its own if the element is not currently visible.

We can use this Selenium Fluent Wait in the scenarios where we do not sure whether the element is visible or not. If the element is visible we will perform operation in it if not visible the fluent wait will handle the error by its own.

In this bellow example i have taken 2 second  for the presence of element and in each 250 millisecond it will check whether the  element is visible or not till end of 2 second by **Selenium Fluent Wait.**

Syntax-
Driver declaration
Waiting Time setting in driver
Function declaration and function definition(With driver and web element as parameter )
Function call

Example-

[codesyntax lang="java"]

```
FluentWait wait=new FluentWait(driver);
wait.poolingEvery(250,TimeUnit.MILISECONDS);
wait.withTimeout(2, TimeUnit.SECONDS);
wait.ignoring(TimeoutException.class);
Function<WebDriver, Boolean> function = new Function<WebDriver, Boolean>() {
public Boolean apply(WebDriver arg) {
WebElement element = arg
.findElement(By.xpath("//div[contains(text(),'You already have a Mailbox named')]"));
if (element.isDisplayed()) {
System.out.println("Found");
arg.findElement(By.xpath("//button[@class='btn pull-right create-toggle']")).click();
return true;
} else {
System.out.println("Not Found");
return false;
}
}
};
wait.until(function);
```

[/codesyntax]

**Thread.Sleep(Time)**

Thread.Sleep is the worst method for **"Selenium Wait"** so we do not advise to use this type of wait in the program unless until u need this. This Thread.Sleep() will pause your java program for an specific duration.

Code

```
Thread.Sleep(1000);
```

All the Selenium Wait methods we are discuses above are need for different time in Selenium WebDriver So please use the require Selenium Wait for your definite purpose.
