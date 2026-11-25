---
title: "🐼 Pandas Syllabus (Beginner to Advanced)"
description: "1. Introduction to Pandas What is Pandas? Installing Pandas Importing the library Data structures in Pandas: Series DataFrame Comparison with NumPy 2…"
pubDate: 2025-07-04T02:27:02Z
legacy: true
wpId: 5255
---

---

### 1. Introduction to Pandas
- What is Pandas?
- Installing Pandas
- Importing the library
- Data structures in Pandas:
  - Series
  - DataFrame
- Comparison with NumPy

---

### 2. Series
- Creating a Series from:
  - List
  - Dictionary
  - NumPy array
- Accessing and indexing
- Operations on Series (arithmetic, aggregation)
- Handling missing values in Series

---

### 3. DataFrame Basics
- Creating DataFrame from:
  - Lists of dictionaries
  - Dictionary of lists
  - NumPy arrays
  - CSV/Excel/SQL/JSON
- Accessing columns and rows:
  - `df['col']`, `df.col`
  - `.loc[]`, `.iloc[]`
- DataFrame attributes:
  - `shape`, `columns`, `index`, `dtypes`, `ndim`, etc.

---

### 4. Data Selection and Filtering
- Boolean indexing
- Conditional filtering
- Using `isin()`, `between()`
- `query()` method

---

### 5. Data Manipulation
- Adding/removing columns and rows
- Renaming columns: `df.rename()`
- Sorting: `sort_values()`, `sort_index()`
- Resetting index: `reset_index()`, `set_index()`
- Changing data types: `astype()`

---

### 6. Handling Missing Data
- `isnull()`, `notnull()`
- Filling missing data: `fillna()`
- Dropping missing data: `dropna()`
- Forward and backward fill

---

### 7. Aggregation and Grouping
- Using `groupby()`
- Aggregation functions: `sum()`, `mean()`, `count()`, `agg()`
- Multiple aggregations
- Grouping by multiple columns

---

### 8. Merging, Joining, and Concatenation
- `merge()` (SQL-like joins)
- `concat()` (along rows or columns)
- `join()` for index-based joins

---

### 9. Working with Time Series
- Converting to datetime: `pd.to_datetime()`
- Extracting date parts: year, month, weekday
- Resampling (`resample()`), rolling averages (`rolling()`)

---

### 10. Input and Output Operations
- Reading data from:
  - CSV: `read_csv()`
  - Excel: `read_excel()`
  - SQL: `read_sql()`
  - JSON: `read_json()`
- Writing data: `to_csv()`, `to_excel()`, etc.

---

### 11. Advanced Operations
- `apply()`, `map()`, `applymap()`
- Lambda functions with Pandas
- Pivot tables: `pivot_table()`
- Multi-indexing and hierarchical indexing
- Window functions (rolling, expanding)

---

### 12. Visualization (with Matplotlib/Seaborn)
- Plotting with Pandas: `df.plot()`
- Line, bar, histogram, boxplot, scatter
- Correlation matrix and heatmaps

---

### 13. Optimization & Performance
- Working with large datasets
- Using `categorical` types
- Memory usage analysis
- Vectorized operations

---

### 14. Real-world Case Studies & Projects
- Stock market analysis
- Sales data insights
- Web scraping + Pandas
- Cleaning messy datasets (nulls, duplicates)

---

### ✅ **Bonus Topics**

- Integration with NumPy, Matplotlib, Seaborn
- Pandas + SQL (via SQLAlchemy)
- Pandas Profiling for EDA
- Using Pandas in Jupyter Notebook
- Interview questions & exercises

---
