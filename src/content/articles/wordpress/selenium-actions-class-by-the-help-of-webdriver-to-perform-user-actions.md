---
title: "Selenium Actions class By the help of Webdriver to Perform User Actions"
description: "Selenium Actions present in Selenium WebDriver class which is used to perform user interaction operations.Like mouse mouse click ,double click drag and…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T01:10:36Z
legacy: true
wpId: 15
---

**Selenium Actions** present in **Selenium WebDriver class** which is used to perform  user interaction operations.Like mouse mouse click ,double click drag and drop.Many a time we found that these operation are needed by **Selenium WebDriver.**To use this action class first we need to transfer the driver control to this class and then to perform action operation.

To create an object of action class we need to create an object of action class for creating an object the following code be written

```
Actions act=new Actions(driver);
```

To perform operation on an Web Element we needs to do user defined operations

```
    public static void main(String ar[]) {
        System.setProperty("webdriver.gecko.driver", "D:\\geckodriver.exe");
        WebDriver driver = new FirefoxDriver();
        driver.get("http://google.co.in");
        Actions act = new Actions(driver);
        WebElement we = driver.findElement(By.xpath(".//*[@id='hplogo']"));
        act.moveToElement(we).perform();
        act.contextClick(we).perform();
    }
```

**NOTE-**It will show the exception in Selenium 3 instead you can use **Java Robot Class.**

|
 **Modifier and Type** |
 **Method and Description** |

|
 Action |
 build() |

Generates a composite action containing all actions so far, ready to be performed (and resets the internal builder state, so subsequent calls to build() will contain fresh sequences).

|
 Actions |
 click() |

Clicks at the current mouse location.

|
 Actions |
 click(WebElement onElement) |

Clicks in the middle of the given element.

|
 Actions |
 clickAndHold() |

Clicks (without releasing) at the current mouse location.

|
 Actions |
 clickAndHold(WebElement onElement) |

Clicks (without releasing) in the middle of the given element.

|
 Actions |
 contextClick() |

Performs a context-click at the current mouse location.

|
 Actions |
 contextClick(WebElement onElement) |

Performs a context-click at middle of the given element.

|
 Actions |
 doubleClick() |

Performs a double-click at the current mouse location.

|
 Actions |
 doubleClick(WebElement onElement) |

Performs a double-click at middle of the given element.

|
 Actions |
 dragAndDrop(WebElement source, WebElement target) |

A convenience method that performs click-and-hold at the location of the source element, moves to the location of the target element, then releases the mouse.

|
 Actions |
 dragAndDropBy(WebElement source, int xOffset, int yOffset) |

A convenience method that performs click-and-hold at the location of the source element, moves by a given offset, then releases the mouse.

|
 Actions |
 keyDown(Keys theKey) |

Performs a modifier key press.

|
 Actions |
 keyDown(WebElement element, Keys theKey) |

Performs a modifier key press after focusing on an element.

|
 Actions |
 keyUp(Keys theKey) |

Performs a modifier key release.

|
 Actions |
 keyUp(WebElement element, Keys theKey) |

Performs a modifier key release after focusing on an element.

|
 Actions |
 moveByOffset(int xOffset, int yOffset) |

Moves the mouse from its current position (or 0,0) by the given offset.

|
 Actions |
 moveToElement(WebElement toElement) |

Moves the mouse to the middle of the element.

|
 Actions |
 moveToElement(WebElement toElement, int xOffset, int yOffset) |

Moves the mouse to an offset from the top-left corner of the element.

|
 Actions |
 pause(long pause) |

Deprecated.

‘Pause’ is considered to be a bad design practice.

|
 void |
 perform() |

A convenience method for performing the actions without calling build() first.

|
 Actions |
 release() |

Releases the depressed left mouse button at the current mouse location.

|
 Actions |
 release(WebElement onElement) |

Releases the depressed left mouse button, in the middle of the given element.

|
 Actions |
 sendKeys(java.lang.CharSequence... keysToSend) |

Sends keys to the active element.

|
 Actions |
 sendKeys(WebElement element, java.lang.CharSequence... keysToSend) |

Equivalent to calling: *Actions.click(element).sendKeys(keysToSend).* This method is different from WebElement.sendKeys(CharSequence...) – see sendKeys(CharSequence...) for details how.

dsdsd
