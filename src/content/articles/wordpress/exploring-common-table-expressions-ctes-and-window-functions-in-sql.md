---
title: "Exploring Common Table Expressions (CTEs) and Window Functions in SQL"
description: "Common Table Expressions (CTEs) and Window Functions are advanced features in SQL that offer powerful capabilities for querying and analyzing data. CTEs…"
lang: other
categories: ["PostgreSQL"]
author: "Shakti Das"
pubDate: 2024-02-25T12:32:08Z
legacy: true
wpId: 4699
---

Common Table Expressions (CTEs) and Window Functions are advanced features in SQL that offer powerful capabilities for querying and analyzing data. CTEs provide a way to create temporary result sets that can be referenced within a query, while Window Functions enable calculations across a set of rows related to the current row. In this blog post, we'll dive into the world of CTEs and Window Functions, exploring their syntax, applications, and examples.

## Common Table Expressions (CTEs)

### What are CTEs?

CTEs are temporary result sets that exist only for the duration of a query. They allow you to define a query and then reference it within another query, making complex queries more readable and manageable.

### Syntax:

```sql
WITH cte_name AS (
    -- CTE query here
)
SELECT columns
FROM cte_name
WHERE conditions;
```

### Example:

Suppose we want to find the average salary of employees in each department:

```sql
WITH DepartmentAverage AS (
    SELECT DepartmentID, AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY DepartmentID
)
SELECT Departments.DepartmentName, DepartmentAverage.AvgSalary
FROM Departments
LEFT JOIN DepartmentAverage
ON Departments.DepartmentID = DepartmentAverage.DepartmentID;
```

In this example, we create a CTE called `DepartmentAverage` that calculates the average salary for each department. We then join this CTE with the `Departments` table to display the department names along with their average salaries.

## Window Functions

### What are Window Functions?

Window Functions allow you to perform calculations across a set of rows related to the current row. They provide a way to perform advanced analytics without the need for self-joins or subqueries.

### Syntax:

```sql
SELECT columns,
       window_function(column) OVER (PARTITION BY partition_column ORDER BY order_column)
FROM table_name;
```

### Example:

Suppose we want to rank employees based on their salaries within each department:

```sql
SELECT EmployeeID, FirstName, LastName, DepartmentID, Salary,
       RANK() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS SalaryRank
FROM Employees;
```

In this example, the `RANK()` function is a Window Function that calculates the rank of each employee's salary within their department. The `PARTITION BY` clause divides the result set into partitions based on the `DepartmentID`, and the `ORDER BY` clause orders the rows within each partition by `Salary`.

## Practical Examples

### 1. Calculating Running Total with Window Functions

Suppose we want to calculate the running total of sales amounts:

```sql
SELECT OrderID, OrderDate, Amount,
       SUM(Amount) OVER (ORDER BY OrderDate) AS RunningTotal
FROM Orders;
```

### 2. Finding Top N Rows within Each Group with Window Functions

Suppose we want to find the top 3 highest paid employees in each department:

```sql
WITH RankedEmployees AS (
    SELECT EmployeeID, FirstName, LastName, DepartmentID, Salary,
           RANK() OVER (PARTITION BY DepartmentID ORDER BY Salary DESC) AS SalaryRank
    FROM Employees
)
SELECT EmployeeID, FirstName, LastName, DepartmentID, Salary
FROM RankedEmployees
WHERE SalaryRank <= 3;
```

### 3. Recursive CTE for Hierarchical Data

CTEs can be used recursively to query hierarchical data, such as organizational charts:

```sql
WITH RecursiveCTE AS (
    SELECT EmployeeID, FirstName, LastName, ManagerID, 1 AS Level
    FROM Employees
    WHERE ManagerID IS NULL
    UNION ALL
    SELECT e.EmployeeID, e.FirstName, e.LastName, e.ManagerID, rc.Level + 1
    FROM Employees e
    INNER JOIN RecursiveCTE rc ON e.ManagerID = rc.EmployeeID
)
SELECT EmployeeID, FirstName, LastName, ManagerID, Level
FROM RecursiveCTE;
```

## Conclusion

Common Table Expressions (CTEs) and Window Functions are powerful tools in SQL for handling complex querying and analytical tasks. CTEs provide a way to create temporary result sets that can be referenced within a query, improving readability and maintainability. Window Functions allow for advanced calculations across rows, making it easier to perform analytics without the need for complex joins or subqueries.

In this blog post, we've explored the syntax and applications of CTEs and Window Functions in SQL, including practical examples. By mastering these advanced features, you can enhance your SQL skills and tackle a wide range of data querying and analysis challenges with ease. Whether you're working with hierarchical data, calculating running totals, or ranking rows within groups, CTEs and Window Functions provide valuable tools for efficiently working with complex datasets.
