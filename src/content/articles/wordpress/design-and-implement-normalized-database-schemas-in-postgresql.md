---
title: "Design and Implement Normalized Database Schemas in PostgreSQL"
description: "Database design is a crucial aspect of building efficient and scalable applications. A well designed database schema not only ensures data integrity but…"
lang: other
categories: ["PostgreSQL"]
author: "Shakti Das"
pubDate: 2024-02-25T11:28:50Z
legacy: true
wpId: 4658
---

Database design is a crucial aspect of building efficient and scalable applications. A well-designed database schema not only ensures data integrity but also improves performance and simplifies maintenance. In this blog post, we'll explore the importance of normalized database schemas and how to design and implement them in PostgreSQL.

## Understanding Normalization

Normalization is the process of organizing data in a database to reduce redundancy and dependency by dividing large tables into smaller, related tables. The goal is to minimize data redundancy and improve data integrity. There are several normal forms, but we'll focus on the first three, which are the most commonly used:

### First Normal Form (1NF)

- Eliminates duplicate columns from the same table.
- Creates a separate table for each group of related data and identifies each row with a unique column or set of columns (primary key).

### Second Normal Form (2NF)

- Meets the requirements of 1NF.
- Removes partial dependencies, meaning no column should be dependent on only a portion of a multi-column primary key.

### Third Normal Form (3NF)

- Meets the requirements of 2NF.
- Eliminates columns not dependent on the primary key, avoiding transitive dependencies.

## Designing a Normalized Database Schema

Let's walk through an example of designing a normalized database schema for a simple e-commerce application that tracks customers, orders, and products. We'll start with an unnormalized schema and gradually normalize it.

### Unnormalized Schema

First, let's consider an unnormalized schema:

```sql
Table: Orders
- OrderID (Primary Key)
- CustomerName
- ProductName
- Price
```

This table violates 1NF because it contains repeating groups (ProductName and Price). To normalize it, we create separate tables for Customers and Products:

### First Normal Form (1NF)

```sql
Table: Customers
- CustomerID (Primary Key)
- CustomerName

Table: Products
- ProductID (Primary Key)
- ProductName
- Price
```

Now, each table contains atomic values, and there are no repeating groups. However, we still have redundant data in the Orders table:

### Second Normal Form (2NF)

```sql
Table: Orders
- OrderID (Primary Key)
- CustomerID (Foreign Key)
- ProductID (Foreign Key)
- Quantity
- OrderDate
```

By introducing CustomerID and ProductID as foreign keys, we remove partial dependencies. However, the Price column in the Orders table is dependent on the ProductID, violating 2NF.

### Third Normal Form (3NF)

```sql
Table: Orders
- OrderID (Primary Key)
- CustomerID (Foreign Key)
- ProductID (Foreign Key)
- Quantity
- OrderDate

Table: Customers
- CustomerID (Primary Key)
- CustomerName

Table: Products
- ProductID (Primary Key)
- ProductName
- Price
```

Now, the schema is in 3NF. The Orders table contains only columns directly related to orders, and Price is stored in the Products table, removing transitive dependencies.

## Implementing in PostgreSQL

Let's implement our normalized schema in PostgreSQL. We'll create the necessary tables and establish the foreign key relationships:

```sql
-- Create Customers table
CREATE TABLE Customers (
    CustomerID SERIAL PRIMARY KEY,
    CustomerName VARCHAR(100)
);

-- Create Products table
CREATE TABLE Products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2)
);

-- Create Orders table
CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,
    CustomerID INT REFERENCES Customers(CustomerID),
    ProductID INT REFERENCES Products(ProductID),
    Quantity INT,
    OrderDate DATE
);
```

With these SQL commands, we've created normalized tables in PostgreSQL. Now, when inserting data into the Orders table, we need to ensure the CustomerID and ProductID exist in the Customers and Products tables, respectively, maintaining referential integrity.

## Conclusion

Designing and implementing normalized database schemas is a fundamental aspect of database development. It helps ensure data integrity, reduces redundancy, and simplifies queries. In this post, we've walked through the process of normalization from 1NF to 3NF, using a simple e-commerce example. We then implemented the normalized schema in PostgreSQL, demonstrating how to create tables and establish foreign key relationships.

Understanding and applying normalization principles will not only lead to better database performance but also make database maintenance and expansion easier as your application grows. Whether you're building a small application or a large-scale system, a well-designed normalized schema is a solid foundation for efficient data management.
