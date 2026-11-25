---
title: "Selenium WebDriver"
description: "WebDriver is an interface present in selenium jar file which consists of some browser specific method to perform operation on browser. Advantages Supports…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T02:14:03Z
legacy: true
wpId: 23
---

WebDriver is an interface present in selenium jar file which consists of some browser specific method to perform  operation on browser.

**Advantages**

Supports multiple browser
Support secure network
Supports secure network
Supports multiple OS.
Supports http protocol.

**Disadvantages**

Does not supports windows application.
Selenium web driver consists of jar files jar files consists of core java classes and interface.

Following are the methods are available in the webdriver

**1.get()**

driver.get() method is used to open an website in the webdriver.It takes argument as string in website link format.

**2.findelement()**

driver.findelement() method used to find the location of an element in side the webpage.

**3.findelements()**

driver.findelements() method used t used to get all the elements ts present in the webpage.

**4.navigate().to()**
driver.navigate().to()  Takes webpage  as string and open through the driver.

driver.navigate().back() Click the back button of the browser.

driver.navigate().forward() Click the forward button of the browser.

driver.navigate().refresh() Cllick the refresh page of the browser.

5.getcurrenturl()

Returns current url as a string.

6.getpagesource()

7.switchto
window()
frame()
8.windows maximize()
9,manage
maximize()
delete cookies()
10.getwindowhandles()
11.close()
12.quit()
13.gettitle()

1.get()

Get method is used to pass the url in the browser.

2.findelemnet()

Used to identify the single element present in the UI.

3.navigate.to()

It is used to pass the url

4.gettitle()

Method is used to capture the title of the current web page.

5.getCurretnUrl()

It is used to capture th current url.

6.getPageSource()

Method is used to get the html source code of current web page.

7.Manage()

When webdriver open an webpage sometimes it open in minimize mode.This method is used to maximize the windows lunch by selenium webdriver.

8.manage().DeleteCookies()

To delete all cookies present in browser.

9.driver.close()

It will close the current driver windows lunch by selenium webdriver.

10.Quit()

It will close all the windows by selenium driver.

To run selenium in firefox browser check the following post.
**[1.Selenium gecko driver setup to run Firefox in Ubuntu or Windows](http://learntowish.com/selenium-gecko-driver-setup-to-run-firefox-in-ubuntu-or-windows/)**
