---
title: Make a button do something with JavaScript
description: Your first taste of making a web page react when you click. No installs needed, just a browser.
lang: javascript
pubDate: 2026-11-18
---

JavaScript runs in every web browser, so you can start without installing anything. In this article you'll make a button that counts your clicks.

## Step 1: make a web page

Create a file called `clicker.html` and paste this in:

```html
<!doctype html>
<html>
  <body>
    <button id="btn">Click me</button>
    <p id="count">You clicked 0 times.</p>

    <script>
      let clicks = 0;
      const button = document.getElementById("btn");
      const text = document.getElementById("count");

      button.addEventListener("click", () => {
        clicks = clicks + 1;
        text.textContent = "You clicked " + clicks + " times.";
      });
    </script>
  </body>
</html>
```

Save it, then double-click the file to open it in your browser. Click the button and watch the number go up.

## What's going on?

<div class="callout plain">
<p class="callout-title">In plain English</p>

Make a variable `clicks` that starts at 0. Find the button and the paragraph on the page by their `id`. When the button is clicked, add 1 to `clicks` and change the paragraph's text to show the new number.

</div>

- `let` makes a variable that can change. `const` makes one that stays the same.
- `document.getElementById(...)` finds an element on the page.
- `addEventListener("click", ...)` means "when this is clicked, run this code".

## The browser console

Every browser has a hidden JavaScript playground. Press **F12** (or Cmd + Option + J on a Mac) and open the **Console** tab. Type this and press Enter:

```javascript
console.log("Hello from the console!");
```

It's the quickest place to try out small bits of JavaScript.

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Add a second button called "Reset" that sets the count back to 0.

</div>
