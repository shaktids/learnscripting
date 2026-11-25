---
title: "CSS Image Sprites"
description: "It is basically an image which is a collection of different images put together to form a single image. The use of image sprites is done for two main…"
lang: other
categories: ["CSS"]
author: "LearnScripting"
pubDate: 2021-06-15T09:31:58Z
legacy: true
wpId: 2799
---

It is basically an image which is a collection of different images put together to form a single image. The use of image sprites is done for two main reasons:

- For faster page loading since use only single image.
- It reduce the bandwidth used to load multiple images. This way less data is consume.

Image sprites are generally used for designing a graphic social media bar or a navigation bar to make it more attractive and efficient at the same time. It is just a method in HTML and CSS to implement more efficient way of putting images and designing web pages.

## Example:

```css
<!DOCTYPE html>
<html>
<head>
<style>
#navlist {
  position: relative;
}

#navlist li {
  margin: 0;
  padding: 0;
  list-style: none;
  position: absolute;
  top: 0;
}

#navlist li, #navlist a {
  height: 44px;
  display: block;
}

#home {
  left: 0px;
  width: 46px;
  background: url('img_navsprites_hover.gif') 0 0;
}

#prev {
  left: 63px;
  width: 43px;
  background: url('img_navsprites_hover.gif') -47px 0;
}

#next {
  left: 129px;
  width: 43px;
  background: url('img_navsprites_hover.gif') -91px 0;
}

#home a:hover {
  background: url('img_navsprites_hover.gif') 0 -45px;
}

#prev a:hover {
  background: url('img_navsprites_hover.gif') -47px -45px;
}

#next a:hover {
  background: url('img_navsprites_hover.gif') -91px -45px;
}
</style>
</head>
<body>

<ul id="navlist">
  <li id="home"><a href="default.asp"></a></li>
  <li id="prev"><a href="css_intro.asp"></a></li>
  <li id="next"><a href="css_syntax.asp"></a></li>
</ul>

</body>
</html>
```

## Output:
