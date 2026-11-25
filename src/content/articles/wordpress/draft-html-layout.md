---
title: "HTML Layout"
description: "An HTML layout is a blueprint used to arrange web pages in a well defined manner. It is easy to navigate, simple to understand and uses HTML tags to…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-09T17:27:43
legacy: true
wpId: 2579
draft: true
---

An HTML layout is a blueprint used to arrange web pages in a well-defined manner. It is easy to navigate, simple to understand and uses HTML tags to customize web design elements. Crucial for any website, an HTML layout that uses the correct format will easily improve a website’s appearance. Additionally, because HTML layouts are typically responsive by default, they will also be properly formatted for mobile devices.

HTML contains different elements that define the structure of a web page:

- &lt;header>:This defines a header for a web page
- &lt;nav>: This defines a container for navigation links
- &lt;section>: This defines a section in a web page
- &lt;article>: This is the primary element that contains information about the web page
- &lt;aside>: The &lt;aside> content is often placed as a sidebar in a document
- &lt;footer>: This defines a footer for a document or a section
- &lt;details>: This is used to define additional details
- &lt;summary>: This defines a heading for the &lt;details> element

## HTML &lt;header>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webpage</title>
</head>

<body>
    <header style="background-color: #432567; height: 75px;width: 75%">
        <h1 style="font-size: 40px; color: rgb(255, 255, 255);text-align: center; padding-top: 15px;"> Welcome to LearnScripting Webpage</h1>
    </header>
</body>

</html>
```

Output:

## HTML &lt;navbar>:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML nav Ber</title>
    <style>
		li{  display: inline-block;
			padding: 25px}
	</style>
</head>
<body>
    <nav style="background-color:#b5b8af;">
		<h1 style="text-align: center;">Navgation Links</h1>
		<ul>
			<li><a href="#">Python</a></li>
			<li><a href="#">Java</a></li>
			<li><a href="#">Manual Testing</a></li>
			<li><a href="#">Selenium Testing</a></li>
		</ul>
	</nav>
</body>
</html>
```

## Output:

## HTML &lt;section>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Section Layout</title>
</head>

<body>
    <section style="background-color:#8d8684; width: 100%; border: 1px solid black;">
        <h2>Section Layout</h2>
        <p>>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolorem dolores error nihil fuga harum recusandae
            reprehenderit, dolore porro velit optio culpa aspernatur sunt suscipit nisi laborum, autem fugit ipsam
            blanditiis.</p>
    </section>

</body>

</html>
```

## Output:

## HTML &lt;article>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Article Layout</title>
</head>

<body>
    <article style="width: 100%; border:2px solid rgb(204, 82, 82); background-color: #fff0f5;">
        <h2>Article Layout</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsam ut, error distinctio blanditiis cupiditate
            itaque iste ab dolores debitis omnis vel dolor minus accusamus autem eum beatae aspernatur animi dolorum?
        </p>
    </article>

    <body>

    </body>

</html>
</body>

</html>
```

## Output:

## HTML &lt;aside>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aside Layout</title>
</head>

<body>
</body>
<aside style="background-color:#8888c2">
    <h2>Sidebar information</h2>
    <p>This conatins information which will represent like a side bar for a webpage</p>
</aside>
</body>

</html>
```

## Output:

## HTML &lt;footer>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Footer</title>
</head>

<body>
    <footer style="background-color:#f0f8ff; width: 100%; text-align: center;">
        <h3>Footer Example</h3>
        <p>© Copyright 20120-2021. </p>
    </footer>
</body>

</html>
```

## Output:

## HTML &lt;details>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detail Layout</title>
</head>

<body>
    <details style="background-color: #f5deb3">
        <summary>Algorithm</summary>
        <p>An algorithm is a specific procedure for solving a well-defined computational problem. ... It requires an
            understanding of the alternatives available for solving a computational problem, including the hardware,
            networking, programming language, and performance constraints that accompany any particular solution. </p>
    </details>
</body>

</html>
```

## Output:

## HTML &lt;summary>:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary Example</title>
</head>

<body>
    <details>
        <summary>TCP</summary>
        <p style="color: rgb(0, 255, 115); font-size: 20px;">Transmission Control Protocol</p>
    </details>
</body>

</html>
```

## Output:
