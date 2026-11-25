---
title: "HTML Quick List"
description: "The basic HTML document: Basic Tags: Text Formatting (Formatting): HTML Links: HTML Images: HTML Styles: Ordered List: <ol <li Apple</li <li Mango</li <li…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-09T10:14:34
legacy: true
wpId: 2577
draft: true
---

## The basic HTML document:

```
<! DOCTYPE   html>
 <Html>
 <Head>
 <Title> Document Title </ title>
 </ Head>
 <Body> visible text ... </ body>
 </ Html>
```

## Basic Tags:

```
<H1> the biggest title </ h1>
 <H2>... </ H2>
 <H3>... </ H3>
 <H4>... </ H4>
 <H5>... </ H5>
 <H6> smallest heading </ h6>

 <P> This is a paragraph. </ P>
 <Br> (line feed) <hr> (horizontal) <! - This is a comment ->
```

## Text Formatting (Formatting):

```
<b> bold text </ b>
 <Code> computer code </ code>
 <em> emphasized text </ em>
 <I> italic text </ i>
 <Kbd> keyboard </ kbd>
 <Pre> preformatted text </ pre>
 <Small> smaller text </ small>
 <Strong> important text </ strong>

 <Abbr> (acronym) <address> (contact information) <bdo> (text direction) <blockquote> (from another source reference section) <cite> (working name) <del> (deleted text) <ins > (insert text) <sub> (subscript text) <sup> (superscript text)
```

## HTML Links:

```
<a href="https://www.google.com.com">Go to the website </a>
<a href="path\file_name.html">Go to next Page</a>
```

## HTML Images:

```
<img src="https://images.pexels.com/photos/3876407/pexels-photo-3876407.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" height="180" width="300" alt="nature image">
```

## HTML Styles:

```
style= "property:value"
```

## Ordered List:

&lt;ol>
&lt;li>Apple&lt;/li>
&lt;li>Mango&lt;/li>
&lt;li>Coconut&lt;/li>
&lt;li>Orange&lt;/li>
&lt;li>Grapes&lt;/li>
&lt;li>lemon&lt;/li>
&lt;li>Cucumber&lt;/li>
&lt;li>peanuts&lt;/li>
&lt;/ol>

## Undered List:

&lt;ul>
&lt;li>Apple&lt;/li>
&lt;li>Mango&lt;/li>
&lt;li>Coconut&lt;/li>
&lt;li>Orange&lt;/li>
&lt;li>Grapes&lt;/li>
&lt;li>lemon&lt;/li>
&lt;li>Cucumber&lt;/li>
&lt;li>peanuts&lt;/li>
&lt;/ul>

## Definition List:

```
 <dl>
        <dt>Mango</dt>
        <dd>This is a fruit</dd>
        <dt>sparrow</dt>
        <dd>This is a bird</dd>

    </dl>
```

## Tables (Tables):

```
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
```

## Frames:

```
<frameset cols="25%,50%,25%">
    <frame src="frame1.html">
        <frame src="frame2.html">
            <frame src="frame3.html">
</frameset>
```

Forms:

```
<form action="/action_page.php" method="get">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>
```
