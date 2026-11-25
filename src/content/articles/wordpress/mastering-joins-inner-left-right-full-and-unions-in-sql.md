---
title: "Mastering Joins (INNER, LEFT, RIGHT, FULL) and Unions in SQL"
description: "Joins and unions are fundamental concepts in SQL that allow you to combine data from multiple tables or queries into a single result set. Whether you're…"
lang: other
categories: ["PostgreSQL"]
author: "Shakti Das"
pubDate: 2024-02-25T12:30:49Z
legacy: true
wpId: 4697
---

Joins and unions are fundamental concepts in SQL that allow you to combine data from multiple tables or queries into a single result set. Whether you're retrieving related data from different tables or combining results from separate queries, understanding joins and unions is crucial for effective data retrieval and manipulation. In this blog post, we'll delve into the world of joins (INNER, LEFT, RIGHT, FULL) and unions, exploring their syntax, purposes, and practical examples.

## Understanding Joins

Joins are used to combine rows from two or more tables based on a related column between them. Each type of join serves a different purpose, allowing you to retrieve data in various ways:

### 1. INNER JOIN

The INNER JOIN returns rows when there is at least one match in both tables based on the join condition.

#### Syntax:

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

#### Example:

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;
```

### 2. LEFT JOIN (or LEFT OUTER JOIN)

The LEFT JOIN returns all rows from the left table (table1), along with matching rows from the right table (table2). If there is no match, NULL values are returned for the right table columns.

#### Syntax:

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

#### Example:

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
LEFT JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;
```

### 3. RIGHT JOIN (or RIGHT OUTER JOIN)

The RIGHT JOIN returns all rows from the right table (table2), along with matching rows from the left table (table1). If there is no match, NULL values are returned for the left table columns.

#### Syntax:

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

#### Example:

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
RIGHT JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;
```

### 4. FULL JOIN (or FULL OUTER JOIN)

The FULL JOIN returns all rows when there is a match in either the left table (table1) or the right table (table2). If there is no match, NULL values are returned for the unmatched side.

#### Syntax:

```sql
SELECT columns
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

#### Example:

```sql
SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
FULL JOIN Customers
ON Orders.CustomerID = Customers.CustomerID;
```

## Understanding Unions

Unions are used to combine the result sets of two or more SELECT statements into a single result set. The number of columns and their data types must match in the SELECT statements.

### Syntax:

```sql
SELECT columns
FROM table1
UNION
SELECT columns
FROM table2;
```

### Example:

```sql
SELECT ProductID, ProductName
FROM Products
WHERE CategoryID = 1
UNION
SELECT ProductID, ProductName
FROM Products
WHERE CategoryID = 2;
```

## Practical Examples

### 1. Combining Data from Two Tables (INNER JOIN)

Suppose we have two tables: `Employees` and `Departments`. We want to retrieve the names of employees along with their department names.

#### Example:

```sql
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

### 2. Combining Data from Two Tables (LEFT JOIN)

Now, we want to retrieve all employees, including those without assigned departments.

#### Example:

```sql
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
LEFT JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

### 3. Combining Data from Two Tables (UNION)

Suppose we want to retrieve a list of products from two categories.

#### Example:

```sql
SELECT ProductID, ProductName, CategoryID
FROM Products
WHERE CategoryID = 1
UNION
SELECT ProductID, ProductName, CategoryID
FROM Products
WHERE CategoryID = 2;
```

### 4. Combining Data from Two Tables (FULL JOIN)

We want to retrieve all employees and their assigned departments, including employees without departments and departments without employees.

#### Example:

```sql
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
FULL JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

## Conclusion

Joins (INNER, LEFT, RIGHT, FULL) and unions are powerful tools in SQL for combining data from multiple tables or queries into a single result set. Whether you need to retrieve related data from different tables or merge results from separate queries, understanding how to use joins and unions effectively is essential for database querying and analysis.

In this blog post, we've explored the syntax and purposes of INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, and UNION in SQL. By mastering these concepts and their practical applications, you can efficiently retrieve, combine, and analyze data from diverse sources, unlocking valuable insights for your applications and reporting needs. Whether you're a developer, data analyst, or database administrator, the ability to wield joins and unions effectively will elevate your SQL skills and empower you to work with complex datasets with ease.
