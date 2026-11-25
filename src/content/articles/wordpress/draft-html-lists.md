---
title: "HTML Lists"
description: "HTML lists are used to present list of information in well formed and semantic way. There are three different types of list in HTML and each one has a…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-05T11:44:17
legacy: true
wpId: 2530
draft: true
---

HTML lists are used to present list of information in well formed and semantic way. There are three different types of list in HTML and each one has a specific purpose and meaning.

1.**Unordered list** — Used to create a list of related items, in no particular order.

2. **Ordered list** — Used to create a list of related items, in a specific order.

3. **Description list** — Used to create a list of terms and their descriptions.

## Attributes of HTML Lists:

| Tag | Description |
| --- | --- |
| &lt;ul> | Unordered list |
| &lt;ol> | Ordered list |
| &lt;li> | List item |
| &lt;dl> | Description list |
| &lt;dt> | Defines a term in a description list |
| &lt;dd> | Describes the term in a description list |

## HTML Ordered List:

HTML Ordered list starts with &lt;ol> tag and end with&lt;/ol>.Every list start with&lt;li>tag and ends with&lt;/li> tag:

## Example of HTML Ordered List:

In Ordered HTML list, the items are marked by numbers.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ordered List</title>
</head>

<body>
    <ol>
        <li>Apple</li>
        <li>Mango</li>
        <li>Coconut</li>
        <li>Orange</li>
        <li>Grapes</li>
        <li>lemon</li>
        <li>Cucumber</li>
        <li>peanuts</li>
    </ol>
</body>

</html>
```

## Output:

## Example Of HTML unordered List:In

In HTML unordered list,the items are marked by bullets

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unordered List</title>
</head>

<body>
    <ul>
        <li>Apple</li>
        <li>Mango</li>
        <li>Coconut</li>
        <li>Orange</li>
        <li>Grapes</li>
        <li>lemon</li>
        <li>Cucumber</li>
        <li>peanuts</li>
    </ul>
</body>

</html>
```

## Output:

## Example of HTML Description List:

HTML description list contains with three tags:

1. dl: &lt;dl> tag defines the start of the list.
2. dt:&lt;dt> tag defines a item.
3. dd:&lt;dd> tag defines the item definition.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Description List</title>
</head>

<body>
    <dl>
        <dt>Mango</dt>
        <dd>This is a fruit</dd>
        <dt>sparrow</dt>
        <dd>This is a bird</dd>

    </dl>
</body>

</html>
```

## Output:
