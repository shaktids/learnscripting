---
title: "My SQL Alter Command"
description: "Alter Table Drop A Column Syntax To DROP A COLUMN in an existing table, the Oracle ALTER TABLE syntax is: ALTER TABLE table name DROP COLUMN column name…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2017-01-22T07:18:44Z
legacy: true
wpId: 49
---

# Alter Table Drop A Column

### Syntax

To DROP A COLUMN in an existing table, the Oracle ALTER TABLE syntax is:

ALTER TABLE table\_name  DROP COLUMN column\_name;

### Example

Let’s look at an example that shows how to drop a column in an Oracle table using the ALTER TABLE statement.

For example:

ALTER TABLE customers  DROP COLUMN customer\_name;

This Oracle ALTER TABLE example will drop the column called *customer\_name* from the table called *customers*.

CategoriesMySql, Oracle

# Alter table Modify

This command is used to alter table existing data type.By giving this command we can change the parameter of  an  table.

ALTER TABLE table\_name  MODIFY column\_name column\_type;

alter table emp modify id number(20);

# Alter Command For Add Renaming Column

Alter table command is used to modify the table structure we can add a column or modify column.

Syntax
ALTER TABLE table\_name
ADD column\_name datatype

eg-alter table test add mobile number(10);

Modifying a column

**Syntax**

**ALTER TABLE “table\_name”
RENAME COLUMN “column 1” TO “column 2”;**
