---
title: "How do I copy data from one table to another in Postgres using the copy command"
description: "In PostgreSQL, you can copy data from one table to another using the COPY command in combination with a query to select the data you want to copy. Here's…"
lang: other
categories: ["PostgreSQL"]
author: "Shakti Das"
pubDate: 2024-02-25T10:57:38Z
legacy: true
wpId: 2264
---

In PostgreSQL, you can copy data from one table to another using the `COPY` command in combination with a query to select the data you want to copy. Here's a step-by-step guide on how to do this:

### Syntax:

```sql
COPY destination_table_name [ ( column_name [, ...] ) ]
    FROM { 'filename' | PROGRAM 'command' | STDIN }
    [ [ WITH ] ( option [, ...] ) ]
```

### Steps:

#### 1. Ensure the Destination Table Exists

Make sure the table you want to copy the data into already exists. If it doesn't, create it with the necessary structure (columns, data types, etc.).

#### 2. Write a SELECT Query

Craft a `SELECT` query that retrieves the data you want to copy. This query will define what data gets transferred from one table to another.

For example:

```sql
SELECT column1, column2, ...
FROM source_table
WHERE conditions; -- You can add WHERE clauses to filter specific rows if needed
```

#### 3. Use the COPY Command

Use the `COPY` command to copy the data from the result of your `SELECT` query into the destination table.

Here's an example:

```sql
COPY destination_table (column1, column2, ...)
FROM (
    SELECT column1, column2, ...
    FROM source_table
    WHERE conditions
) AS subquery;
```

Let's break down this example:

- `COPY destination_table (column1, column2, ...)` specifies the target table and columns where the data will be copied.
- `FROM (... AS subquery)` is where you put your `SELECT` query as a subquery.

### Example:

Let's say we have two tables, `employees` and `new_employees`, and we want to copy data from `employees` to `new_employees`.

#### Existing Tables:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    position VARCHAR(100)
);

CREATE TABLE new_employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    position VARCHAR(100)
);
```

#### Data in `employees`:

```sql
INSERT INTO employees (name, age, position) VALUES
    ('Alice', 30, 'Manager'),
    ('Bob', 25, 'Developer'),
    ('Charlie', 28, 'Designer');
```

#### Copy Command:

```sql
COPY new_employees (name, age, position)
FROM (
    SELECT name, age, position
    FROM employees
    WHERE age > 25
) AS subquery;
```

In this example:

- We are copying `name`, `age`, and `position` columns from `employees` to `new_employees`.
- We're only copying employees where the age is greater than 25, as specified in the `WHERE` clause.

After executing this `COPY` command, the `new_employees` table will have the following data:

```sql
id |  name   | age |  position
----+---------+-----+-----------
  1 | Alice   |  30 | Manager
  2 | Charlie |  28 | Designer
```

### Important Notes:

- The `COPY` command is a powerful tool, but it requires appropriate permissions. Ensure you have the necessary permissions to copy data from one table to another.
- Be cautious when using `COPY`, especially with large datasets. It's a direct data manipulation command and can't be undone with a simple rollback.
- Always double-check your query and destination table to avoid unintentional data overwrites or errors.

This method is efficient for copying large amounts of data between tables and is commonly used in PostgreSQL for data migration tasks.
