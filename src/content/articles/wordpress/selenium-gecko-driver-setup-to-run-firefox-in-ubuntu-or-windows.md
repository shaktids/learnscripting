---
title: "Selenium gecko driver setup to run Firefox in Ubuntu or Windows"
description: "As Selenium is cross platform supported we can use it for the different environment as per our need .In this tutorial we will explain how to run the…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T01:01:42Z
legacy: true
wpId: 2890
---

As Selenium is cross platform supported we can use it for the different environment as per our need .In this tutorial we will explain how to run the Firefox Browser Using Selenium.

Step:1

Download the gicko driver from the below linnk for your system environment.
Download the gecko driver from the [following link.](https://github.com/mozilla/geckodriver/releases)

Step:2

Extract the geckodriver from the zip and place in your local directory.
After placing the gickodriver everything is ready.Only we need to write the code in the editor to open the browser.

**For Java**

Copy and paste the code after importing  the external jar files of java selenium web driver.

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
public class MyClass {
public static void main(String[] args) {
//Create a new instance of Firefox Browser
System.setProperty("webdriver.gecko.driver","/home/shakti/Downloads/geckodriver");

WebDriver driver = new FirefoxDriver();

}
}
