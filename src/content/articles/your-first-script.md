---
title: Your first script
description: Write, save and run a file that says hello. You'll go from an empty file to a working script.
lang: general
step: 3
pubDate: 2026-11-06
---

Time to write a real script, save it, and run it. We'll use Python, but the steps are the same in every language.

## 1. Make a folder

Create a folder for your scripts somewhere easy to find, such as `Documents/scripts`. Keeping them together saves a lot of hunting later.

## 2. Create the file

Open your text editor and create a new file called `hello.py` inside that folder. The `.py` ending tells everyone (including your computer) that this is a Python file.

Type this in:

```python
print("Hello, world!")
print("I wrote this script myself.")
```

Save the file.

## 3. Run it

Open a terminal and move into your folder with `cd` (short for "change directory"):

```bash
cd Documents/scripts
```

Then run the script:

```bash
python hello.py
```

You should see:

```text
Hello, world!
I wrote this script myself.
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

`print(...)` means "show this on the screen". The text inside the quotes is shown exactly as written. The computer runs line 1, then line 2, top to bottom.

</div>

## When it goes wrong

Errors are normal. Every programmer sees dozens a day. Read the last line of the error message first; it usually says what's wrong.

- **`No such file or directory`:** you're in the wrong folder. Run `cd` again, or check the file name.
- **`SyntaxError`:** there's a typo. Check for a missing quote or bracket.
- **`python` is not recognized:** see [Set up your computer](/articles/set-up-your-computer/).

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Add a third line that prints your favourite food. Save, then run the script again.

</div>
