---
title: "CSS Navigation Bar"
description: "A navigation bar is a user interface element within a webpage that contains links to other sections of the website. In most cases, the navigation bar is…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-15T07:36:48Z
legacy: true
wpId: 2774
---

A navigation bar is a user interface element within a webpage that contains links to other sections of the website. In most cases, the navigation bar is part of the main website template, which means it is displayed on most, if not all, pages within the website. This means that no matter what page you are viewing, you can use the navigation bar to visit other sections of the website.

A website navigation bar is most commonly displayed as horizontal list of links at the top of each page. It may be below the header or logo, but it is always placed before the main content of the page. In some cases, it may make sense to place the navigation bar vertically on the left side of each page. This type of navigation bar is also called a sidebar, since it appears to the side of the primary content. Some websites have both a horizontal navigation bar at the top and a vertical navigation bar on the left side of each page.

The navigation bar is an important element of a website's design since it allows users to quickly visit any section within the site. If we've ever visited a website without a navigation bar, we may have found it is difficult to locate the page you need. We may have also had to click "Back" several times in order to find a link to the next section we wanted to visit. Thankfully, web design has become more standardized in recent years and nearly every website now includes a navigation bar.

## Horizontal Navigation Bar:

The horizontal navigation bar is the horizontal list of links, which is generally on the top of the page.

## Example:

```css
<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0px;
  overflow: hidden;
  background-color: lightgray;
}

li {
  float: left;
}

li a {
  display: block;
  color: blue;
 font-size:20px;
  text-align: center;
  padding: 10px 20px;
  text-decoration: none;
}
.active{
background-color: gray;
color: white;
}
li a:hover {
  background-color: orange;
  color: white;
}
</style>
</head>
<body>

<ul>
  <li><a class="active" href="#home">Home</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">HTML</a></li>
  <li><a href="#">CSS</a></li>
</ul>

</body>
</html>

```

## Output:

## Vertical Navigation Bar:

```css
<!DOCTYPE html>
<html>

<head>
    <style>
        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }

        li a {
            display: block;
            width: 60px;
            background-color: #dddddd;
        }
    </style>
</head>

<body>

    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#news">News</a></li>
        <li><a href="#contact us">Contact us</a></li>
        <li><a href="#about">About</a></li>
    </ul>

    <p>A background color is added to the links to show the link area.</p>
    <p>Notice that the whole link area is clickable, not just the text.</p>

</body>

</html>
```

## Output:
