---
title: "SQL Insert Command Different Types"
description: "SQL Insert Command Different Types Different type of SQL command are used to perform same operation need to use at different time as per our…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2017-01-22T07:47:44Z
legacy: true
wpId: 1227
---

**SQL Insert Command Different Types**Different type of SQL command are used to perform same operation  need to use at different time as per our requirement.We can use them in the next example  we are going to create a table name as TEST and heaving the following command.

Create Table command

CREATE TABLE TEST(ID NUMBER(10),NAME VARCHAR2(30));

Type-1

INSERT INTO TABLENAME(COLUMN1,COLUMN2) VALUES (VALUES1,VALUES2);

eg-insert into test(id,name) values(1,’shak’);

Type-2

eg-insert into test values(2,’data1′);

Type-3

eg-insert into test(‘&id’,’&name’);
