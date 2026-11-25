---
title: "How to Read From xlsx file In Maven Project By Apache Plugin and Dependency"
description: "For reading files from the .xlsx file we need the following .jar files to be imported to the Build Path.Downloads the followings and import the version…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T07:37:23Z
legacy: true
wpId: 68
---

For reading files from the .xlsx file we need the following .jar files to be imported to the Build Path.Downloads the followings and import the version.

poi-ooxml-3.11-beta2.jar
poi-ooxml-schemas-3.11-beta2.jar
xmlbeans-2.6.0.jar
stax-api-1.0.1.jar

If you are not using Maven then add following JAR files in your
**poi-3.11-beta2.jar**
**commons-codec-1.9.jar**
**poi-ooxml-3.11-beta2.jar**
**poi-ooxml-schemas-3.11-beta2.jar**
**xmlbeans-2.6.0.jar**
**stax-api-1.0.1.jar**

Along with the **[l2wish.xlsx file.](http://learntowish.com/wp-content/uploads/2017/01/l2wish.xlsx)**

Set the location of file in accordance to your system.

Along with the following dependency as in my pom.xml .This pom.xml files i was created for my project i am posting my code bellow.

Main program file contains the following code

```
package test3;
import java.io.FileInputStream;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import test1.ExcelHelper;

public class MyClass {
    Object[][] obb;
    ExcelHelper Excelelperpag = new ExcelHelper();
    @Test(dataProvider = "getexcel")
    public void pro(String uname, String pwd) {
        System.out.println(uname);
        System.out.println(pwd);
    }

    @DataProvider()
    public Object[][] getexcel() {
        FileInputStream fis;
        try {
            fis = new FileInputStream("D:\\l2wish.xlsx");
           XSSFWorkbook wb = new XSSFWorkbook(fis);
            Sheet sh = wb.getSheet("Sheet1");
            int count = sh.getLastRowNum();
            System.out.println("Count=" + count);
            obb = new Object[count][2];
            for (int i = 0; i < count; i++) {
                Row rw = sh.getRow(i);
                obb[i][0] = rw.getCell(0).getStringCellValue();
              obb[i][1] = rw.getCell(1).getStringCellValue();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return obb;
    }
}
```

POM.XML

```
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>test2</groupId>
    <artifactId>test3</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>3.0.1</version>
        </dependency>
        <dependency>
            <groupId>org.testng</groupId>
            <artifactId>testng</artifactId>
            <version>6.8</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi</artifactId>
            <version>3.11-beta2</version>
        </dependency>
            <dependency>
            <groupId>org.apache.poi</groupId>
            <artifactId>poi-ooxml</artifactId>
            <version>3.9</version>
        </dependency>
         <dependency>
              <groupId>org.apache.maven.surefire</groupId>
              <artifactId>surefire</artifactId>
              <version>2.19.1</version>
              <type>pom</type>
        </dependency>
        <dependency>
            <groupId>log4j</groupId>
            <artifactId>log4j</artifactId>
            <version>1.2.17</version>
        </dependency>
    </dependencies>
    <build>
        <plugins>
             <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>2.19.1</version>
                <configuration>
                  <suiteXmlFiles>
                            <suiteXmlFile>testng.xml</suiteXmlFile>
                  </suiteXmlFiles>
                </configuration>
              </plugin>
        </plugins>
    </build>
</project>
```
