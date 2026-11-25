---
title: "Data Types in Postgres"
description: "Exploring the Multitude of Data Types in PostgreSQL In the realm of relational databases, PostgreSQL stands tall as a versatile and feature rich option…"
lang: other
categories: ["PostgreSQL"]
author: "Shakti Das"
pubDate: 2019-10-11T05:32:23Z
updatedDate: 2024-02-25T11:02:20Z
legacy: true
wpId: 1874
---

**Exploring the Multitude of Data Types in PostgreSQL**

In the realm of relational databases, PostgreSQL stands tall as a versatile and feature-rich option. One of its defining strengths lies in its extensive array of data types, providing developers and data architects with a wide spectrum of options to accurately model and store their data. From basic numeric types to specialized ones for geometries and JSON, PostgreSQL's diverse collection of data types caters to a myriad of use cases. Let's embark on a journey to explore the multitude of data types that PostgreSQL offers.

### 1. Numeric Data Types

PostgreSQL provides various numeric data types to handle different kinds of numerical values with precision:

- **Integer (`INT`)**: A standard whole number without a decimal point.
- **Decimal or Numeric (`NUMERIC`)**: Ideal for numbers requiring decimal points with precise storage for financial and scientific data.
- **Floating-Point (`FLOAT` and `REAL`)**: Approximate numeric values with a floating decimal point, with `FLOAT` providing more precision than `REAL`.

### 2. Character Data Types

For handling character and text data, PostgreSQL offers:

- **Character Varying (`VARCHAR`)**: Variable-length character strings.
- **Character (`CHAR`)**: Fixed-length character strings.
- **Text (`TEXT`)**: Non-specific character type for storing long strings of text.

### 3. Temporal Data Types

To deal with date and time values, PostgreSQL provides:

- **Date (`DATE`)**: Stores date values without time.
- **Time (`TIME`)**: Stores time values without a date.
- **Timestamp (`TIMESTAMP`)**: Stores both date and time.
- **Interval (`INTERVAL`)**: Represents a time interval.

### 4. Boolean Data Type

The `BOOL` type represents true or false values for logical operations.

### 5. Binary Data Types

For handling binary data, PostgreSQL offers:

- **Binary (`BYTEA`)**: Stores binary large objects (BLOBs) directly in the database.
- **UUID (`UUID`)**: Universally Unique Identifiers for generating unique identifiers.

### 6. Geometric Data Types

PostgreSQL includes specialized types for geometric shapes:

- **Point (`POINT`)**: Represents a point in a 2D plane.
- **Line (`LINE`)** and **Line Segment (`LSEG`)**: For lines and line segments.
- **Polygon (`POLYGON`)**: Represents a closed shape defined by points.

### 7. Array Data Types

The `ARRAY` type allows storing multiple values of the same data type in a single column.

### 8. JSON and JSONB Data Types

For handling JSON data, PostgreSQL offers:

- **JSON (`JSON`)**: Stores JSON data in its original form.
- **JSONB (`JSONB`)**: Binary representation of JSON data for faster indexing and querying.

### 9. Range Types

PostgreSQL also supports range types for representing a range of values of a particular data type, such as dates or integers.

### 10. Network Address Types

There are specialized data types for handling network addresses:

- **IP Address (`INET`)**: Stores IPv4 and IPv6 addresses.
- **MAC Address (`MACADDR`)**: Stores MAC addresses.

### 11. Enumerated Types

Developers can define their own enumerated types using the `CREATE TYPE` command, allowing for a finite set of values.

### 12. Composite Types

PostgreSQL supports composite types that allow grouping multiple fields together into a single type.

### 13. Custom Types

Users can create custom data types tailored to their specific needs, providing flexibility in data modeling.

### Why Data Types Matter

Choosing the right data type is crucial for efficient storage, retrieval, and query performance:

- **Data Integrity**: Ensures that the data stored matches the intended type, preventing errors.
- **Storage Efficiency**: Proper data types help optimize storage space, particularly important for large datasets.
- **Query Optimization**: Certain data types are better suited for specific types of queries, improving overall database performance.

### List of all the data types available in the postgres

**1. [Numeric Types](https://www.postgresql.org/docs/9.5/datatype-numeric.html)**

**1.1. [Integer Types](https://www.postgresql.org/docs/9.5/datatype-numeric.html#DATATYPE-INT)**

**1.2. [Arbitrary Precision Numbers](https://www.postgresql.org/docs/9.5/datatype-numeric.html#DATATYPE-NUMERIC-DECIMAL)**

**1.3. [Floating-Point Types](https://www.postgresql.org/docs/9.5/datatype-numeric.html#DATATYPE-FLOAT)**

**1.4. [Serial Types](https://www.postgresql.org/docs/9.5/datatype-numeric.html#DATATYPE-SERIAL)**

**2. [Monetary Types](https://www.postgresql.org/docs/9.5/datatype-money.html)**

**3. [Character Types](https://www.postgresql.org/docs/9.5/datatype-character.html)**

**4. [Binary Data Types](https://www.postgresql.org/docs/9.5/datatype-binary.html)**

**4.1. [bytea Hex
Format](https://www.postgresql.org/docs/9.5/datatype-binary.html#AEN5777)**

**4.2. [bytea Escape
Format](https://www.postgresql.org/docs/9.5/datatype-binary.html#AEN5787)**

**5. [Date/Time Types](https://www.postgresql.org/docs/9.5/datatype-datetime.html)**

**5.1. [Date/Time Input](https://www.postgresql.org/docs/9.5/datatype-datetime.html#DATATYPE-DATETIME-INPUT)**

**5.2. [Date/Time Output](https://www.postgresql.org/docs/9.5/datatype-datetime.html#DATATYPE-DATETIME-OUTPUT)**

**5.3. [Time Zones](https://www.postgresql.org/docs/9.5/datatype-datetime.html#DATATYPE-TIMEZONES)**

**5.4. [Interval Input](https://www.postgresql.org/docs/9.5/datatype-datetime.html#DATATYPE-INTERVAL-INPUT)**

**5.5. [Interval Output](https://www.postgresql.org/docs/9.5/datatype-datetime.html#DATATYPE-INTERVAL-OUTPUT)**

**6. [Boolean Type](https://www.postgresql.org/docs/9.5/datatype-boolean.html)**

**7. [Enumerated Types](https://www.postgresql.org/docs/9.5/datatype-enum.html)**

**7.1. [Declaration of Enumerated Types](https://www.postgresql.org/docs/9.5/datatype-enum.html#AEN6927)**

**7.2. [Ordering](https://www.postgresql.org/docs/9.5/datatype-enum.html#AEN6933)**

**7.3. [Type Safety](https://www.postgresql.org/docs/9.5/datatype-enum.html#AEN6937)**

**7.4. [Implementation Details](https://www.postgresql.org/docs/9.5/datatype-enum.html#AEN6943)**

**[Geometric Types](https://www.postgresql.org/docs/9.5/datatype-geometric.html)**

**1. [Points](https://www.postgresql.org/docs/9.5/datatype-geometric.html#AEN7021)**

**2. [Lines](https://www.postgresql.org/docs/9.5/datatype-geometric.html#DATATYPE-LINE)**

**3. [Line Segments](https://www.postgresql.org/docs/9.5/datatype-geometric.html#DATATYPE-LSEG)**

**4. [Boxes](https://www.postgresql.org/docs/9.5/datatype-geometric.html#AEN7105)**

**5. [Paths](https://www.postgresql.org/docs/9.5/datatype-geometric.html#AEN7134)**

**6. [Polygons](https://www.postgresql.org/docs/9.5/datatype-geometric.html#DATATYPE-POLYGON)**

**7. [Circles](https://www.postgresql.org/docs/9.5/datatype-geometric.html#DATATYPE-CIRCLE)**

**9. [Network Address Types](https://www.postgresql.org/docs/9.5/datatype-net-types.html)**

**9.1. [inet](https://www.postgresql.org/docs/9.5/datatype-net-types.html#DATATYPE-INET)**

**9.2. [cidr](https://www.postgresql.org/docs/9.5/datatype-net-types.html#DATATYPE-CIDR)**

**9.3. [inet vs. cidr](https://www.postgresql.org/docs/9.5/datatype-net-types.html#DATATYPE-INET-VS-CIDR)**

**9.4. [macaddr](https://www.postgresql.org/docs/9.5/datatype-net-types.html#DATATYPE-MACADDR)**

**10. [Bit String Types](https://www.postgresql.org/docs/9.5/datatype-bit.html)**

**11. [Text Search Types](https://www.postgresql.org/docs/9.5/datatype-textsearch.html)**

**11.1. [tsvector](https://www.postgresql.org/docs/9.5/datatype-textsearch.html#DATATYPE-TSVECTOR)**

**11.2. [tsquery](https://www.postgresql.org/docs/9.5/datatype-textsearch.html#DATATYPE-TSQUERY)**

**12. [UUID Type](https://www.postgresql.org/docs/9.5/datatype-uuid.html)**

**13. [XML Type](https://www.postgresql.org/docs/9.5/datatype-xml.html)**

**13.1. [Creating XML Values](https://www.postgresql.org/docs/9.5/datatype-xml.html#AEN7560)**

**13.2. [Encoding Handling](https://www.postgresql.org/docs/9.5/datatype-xml.html#AEN7600)**

**13.3. [Accessing XML Values](https://www.postgresql.org/docs/9.5/datatype-xml.html#AEN7612)**

**14. [JSON Types](https://www.postgresql.org/docs/9.5/datatype-json.html)**

**14.1. [JSON Input and Output Syntax](https://www.postgresql.org/docs/9.5/datatype-json.html#JSON-KEYS-ELEMENTS)**

**14.2. [Designing JSON documents effectively](https://www.postgresql.org/docs/9.5/datatype-json.html#JSON-DOC-DESIGN)**

**14.3. [jsonb Containment
and Existence](https://www.postgresql.org/docs/9.5/datatype-json.html#JSON-CONTAINMENT)**

**14.4. [jsonb Indexing](https://www.postgresql.org/docs/9.5/datatype-json.html#JSON-INDEXING)**

**15. [Arrays](https://www.postgresql.org/docs/9.5/arrays.html)**

**15.1. [Declaration of Array Types](https://www.postgresql.org/docs/9.5/arrays.html#ARRAYS-DECLARATION)**

**15.2. [Array Value Input](https://www.postgresql.org/docs/9.5/arrays.html#ARRAYS-INPUT)**

**15.3. [Accessing Arrays](https://www.postgresql.org/docs/9.5/arrays.html#ARRAYS-ACCESSING)**

**15.4. [Modifying Arrays](https://www.postgresql.org/docs/9.5/arrays.html#ARRAYS-MODIFYING)**

**15.5. [Searching in Arrays](https://www.postgresql.org/docs/9.5/arrays.html#ARRAYS-SEARCHING)**

**15.6. [Array Input and Output Syntax](https://www.postgresql.org/docs/9.5/arrays.html#ARRAYS-IO)**

**16. [Composite Types](https://www.postgresql.org/docs/9.5/rowtypes.html)**

**16.1. [Declaration of Composite Types](https://www.postgresql.org/docs/9.5/rowtypes.html#ROWTYPES-DECLARING)**

**16.2. [Constructing Composite Values](https://www.postgresql.org/docs/9.5/rowtypes.html#AEN8114)**

**16.3. [Accessing Composite Types](https://www.postgresql.org/docs/9.5/rowtypes.html#ROWTYPES-ACCESSING)**

**16.4. [Modifying Composite Types](https://www.postgresql.org/docs/9.5/rowtypes.html#AEN8152)**

**16.5. [Using Composite Types in Queries](https://www.postgresql.org/docs/9.5/rowtypes.html#ROWTYPES-USAGE)**

**16.6. [Composite Type Input and Output Syntax](https://www.postgresql.org/docs/9.5/rowtypes.html#ROWTYPES-IO-SYNTAX)**

**17. [Range Types](https://www.postgresql.org/docs/9.5/rangetypes.html)**

**17.1. [Built-in Range Types](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-BUILTIN)**

**17.2. [Examples](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-EXAMPLES)**

**17.3. [Inclusive and Exclusive Bounds](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-INCLUSIVITY)**

**17.4. [Infinite (Unbounded) Ranges](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-INFINITE)**

**17.5. [Range Input/Output](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-IO)**

**17.6. [Constructing Ranges](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-CONSTRUCT)**

**17.7. [Discrete Range Types](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-DISCRETE)**

**17. [Defining New Range Types](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-DEFINING)**

**17.9. [Indexing](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-INDEXING)**

**17.10. [Constraints on Ranges](https://www.postgresql.org/docs/9.5/rangetypes.html#RANGETYPES-CONSTRAINT)**

**18 [Object Identifier Types](https://www.postgresql.org/docs/9.5/datatype-oid.html)**

**19. [pg\_lsn Type](https://www.postgresql.org/docs/9.5/datatype-pg-lsn.html)**

**20. [Pseudo-Types](https://www.postgresql.org/docs/9.5/datatype-pseudo.html)**

### Conclusion

PostgreSQL's rich assortment of data types empowers users to design robust and efficient databases tailored to their application's needs. Whether handling numeric values, textual data, dates, geometries, or JSON documents, PostgreSQL offers a comprehensive toolkit.

By understanding the nuances of these data types and choosing wisely, developers can craft databases that not only store data accurately but also perform optimally. So, the next time you're architecting a PostgreSQL database, remember the wealth of data types at your disposal, each designed to bring precision and efficiency to your data management endeavors.
