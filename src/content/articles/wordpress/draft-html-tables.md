---
title: "HTML Tables"
description: "The <table tag is in HTML is a block element which is used to create a table. It is useful when we want to represent data using rows and columns. The…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-05T11:40:15
legacy: true
wpId: 2517
draft: true
---

The **&lt;table> tag** is in HTML is a [block](https://www.computerhope.com/jargon/b/block-level-element.htm) element which is used to create a [table](https://www.computerhope.com/jargon/t/table.htm). It is useful when we want to represent data using rows and columns. The basic elements that make up a table include [&lt;th>](https://www.computerhope.com/jargon/h/html-th-tag.htm), [&lt;td>](https://www.computerhope.com/jargon/h/html-td-tag.htm), and [&lt;tr>](https://www.computerhope.com/jargon/h/html-tr-tag.htm).

## The attributes of HTML table tag is:

|  |  |
| --- | --- |
| **Tag** | **Description** |
| &lt;table> | It defines a table. |
| &lt;tr> | It defines a row in a table. |
| &lt;th> | It defines a header cell in a table. |
| &lt;td> | It defines a cell in a table. |
| &lt;caption> | It defines the table caption. |
| &lt;colgroup> | It specifies a group of one or more columns in a table for formatting. |
| &lt;col> | It is used with &lt;colgroup> element to specify column properties for each column. |
| &lt;tbody> | It is used to group the body content in a table. |
| &lt;thead> | It is used to group the header content in a table. |
| &lt;tfooter> | It is used to group the footer content in a table. |

## Example of HTML Table tag:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

</head>

<body>
    <table>
        <tr>
            <th>No</th>
            <th>Full_Nmae</th>
            <th>Position</th>
            <th>Salary</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>James</td>
            <td>Manager</td>
            <td>50000</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Lyra</td>
            <td>Ass.Manager</td>
            <td>50000</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Harry</td>
            <td>Developer</td>
            <td>45000</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Navin</td>
            <td>Tester</td>
            <td>40000</td>
        </tr>
    </table>
</body>

</html>
```

## Output:

## How to add Border in HTML Table tag(With CSS):

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table,
        th,
        td {
            border: 1px solid black;
            border-collapse: collapse;
        }
    </style>
</head>

<body>
    <table>
        <tr>
            <th>No</th>
            <th>Full_Nmae</th>
            <th>Position</th>
            <th>Salary</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>James</td>
            <td>Manager</td>
            <td>50000</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Lyra</td>
            <td>Ass.Manager</td>
            <td>50000</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Harry</td>
            <td>Developer</td>
            <td>45000</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Navin</td>
            <td>Tester</td>
            <td>40000</td>
        </tr>
    </table>
</body>

</html>
```

## Output:

## HTML Table with Colspan(with CSS):

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table,
        th,
        td {
            border: 1px solid black;
        }
    </style>
</head>

<body>
    <h2>Cell that span two columns</h2>
    <table>
        <tr>
            <th>No</th>
            <th>Full_Name</th>
            <th>Position</th>
            <th>Salary</th>
            <th colspan="2">Phone No.</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>James</td>
            <td>Manager</td>
            <td>50000</td>
            <td>657890</td>
            <td>127655</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Lyra</td>
            <td>Ass.Manager</td>
            <td>50000</td>
            <td>128765</td>
            <td>127675</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Harry</td>
            <td>Developer</td>
            <td>45000</td>
            <td>128768</td>
            <td>127679</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Navin</td>
            <td>Tester</td>
            <td>40000</td>
            <td>128769</td>
            <td>127676</td>
        </tr>
    </table>
</body>

</html>
```

## Output:

## HTML table with rowspan(with CSS):

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table,
        th,
        td {
            border: 1px solid black;
        }
    </style>
</head>

<body>
    <h2>Cell that span two rows</h2>
    <table>
        <tr>
            <th>Name</th>
            <td>james</td>
        </tr>
        <tr>
            <th>Position</th>
            <td>Manager</td>
        </tr>
        <tr>
            <th rowspan="2">Phone No.</th>
            <td>654789</td>
            <td>567843</td>
        </tr>

    </table>
</body>

</html>
```

Output:
