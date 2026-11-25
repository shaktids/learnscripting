---
title: "JDBC MySql Connection in Ubuntu"
description: "Setting Up MySQL: Run the following command in the terminal: 123sudo apt get install mysql serversudo apt get install mysql clientsudo apt get install…"
lang: other
categories: ["Selenium"]
author: "Shakti Das"
pubDate: 2017-01-22T07:27:59Z
legacy: true
wpId: 1226
---

## Setting Up MySQL:

Run the following command in the terminal:

123sudo apt-get install mysql-serversudo apt-get install mysql-clientsudo apt-get install libmysql-java

This will install both in the most up to date version within your repositories. You will be prompted for a root password. You then need to login and setup the server. To do that, run the following command:

1mysql -u root -p

Password will be asked and after that you will be connected to the server. You have to create a database to work on. Run the following command to create one:

1CREATE [database\_name];

Replace [database\_name] with the name you want. Now, we have to switch database. Run following command in the terminal:

1>USE [database\_name];

Now, we have to set classpath. Enter this command at the end of you bashrc file:

1export CLASSPATH=$CLASSPATH:/usr/share/java/mysql-connector-java.jar

## Setting Up IDE:

In you favorite IDE, go to Project Properties tab, and click “Add External Jars”. Choose the jar file located at “/usr/share/java/” directory, in this case “mysql-connector-java.java”. Now test this connection using this program:

```
import java.sql.Connection;import java.sql.DriverManager; class JDBCTest {     String url = “jdbc:mysql://localhost”;     String user = “username”;     String password = “password”;     public static void main(String args[]) {         try {            Connection con;            con = DriverManager.getConnection(url, user, password);            System.out.println(“Success”);         } catch (Exception e) {            e.printStackTrace();         }    }}
```

After running this program, “Success” message will be shown if the connection is sucessful.
Got problems? Let me know in the comments.v
