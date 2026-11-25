---
title: "HTML5 DOM"
description: "DOM stands for Document Object Model. In the world of web, all HTML webpages are referred to as documents. The Document Object Model represents each of…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-10T18:57:46
legacy: true
wpId: 2631
draft: true
---

DOM stands for Document Object Model. In the world of web, all HTML webpages are referred to as documents. The Document Object Model represents each of these web pages in a tree-like structure to make it easier to access and manage the elements.

DOM contains a bunch of nodes where each node represents an HTML element. The &lt;HTML> tag always comes at the top and hence is called the “root node”. The rest of the nodes come under it and hence are called “children nodes”. The nodes present at the bottom are called “leaves” and are usually filled with elements’ attributes, values and events.

## Structure of DOM:

There are several ways to find HTML elements. such that

- Finding HTML elements by id
- Finding HTML elements by tag name
- Finding HTML elements by class name
- Finding HTML elements by CSS selectors
- Finding HTML elements by HTML object collections

## Finding HTML Element by Id:

## Syntax:

```
document.getElementsByTagName("id")
```

## Example:

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
    <script type="text/javascript">
        function cal(){
        var number=document.getElementById("number").value;
        alert(number*number*number*number);
        }
        </script>
        <form>
        Enter No:<input type="text" id="number" name="number"/><br/>
        <input type="button" value="result" onclick="cal()"/>
        </form>
</body>
</html>
```

## Output:

## Finding element by ClassName:

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
    <script type="text/javascript">
        function elements() {
            var allgenders = document.getElementsByName("gender");
            alert("Total Genders:" + allgenders.length);
        }
    </script>
    <form>
        First Name:<input type="text" name="fname" value="fname">
        Last Name:<input type="text" name="lname" value="lname">

        <input type="button" onclick="totalelements()" value="fullname">
    </form>
</body>

</html>
```

## Output:

## Finding Element By TagName:

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
    <script type="text/javascript">
        function counth2(){
        var totalh2=document.getElementsByTagName("h2");
        alert("total h2 tags are: "+totalh2.length);
        }
        function counth3(){
        var totalh3=document.getElementsByTagName("h3");
        alert("total h3 tags are: "+totalh3.length);
        }
        </script>
        <h2>This is h2 tag</h2>
        <h2>This is h2 tag</h2>
        <h3>This is h3 tag</h3>
        <h3>This is h3 tag</h3>
        <h3>This is h3 tag</h3>
        <button onclick="counth2()">count h2</button>
        <button onclick="counth3()">count h3</button>
</body>
</html>
```

## Output:
