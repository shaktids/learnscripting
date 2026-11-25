---
title: Automate a real task - rename a folder of files
description: Turn a boring ten-minute chore into a two-second script that renames every file in a folder.
lang: python
step: 5
pubDate: 2026-11-12
---

You've learned variables, ifs and loops. Now let's use them on a real chore: giving a messy folder of photos tidy, numbered names like `holiday-001.jpg`, `holiday-002.jpg` and so on.

<div class="callout warn">
<p class="callout-title">Practise on a copy</p>

Scripts are fast, including when they're wrong. Copy a few files into a new test folder and run the script there first.

</div>

## Step 1: list the files

```python
from pathlib import Path

folder = Path("test-photos")

for file in folder.iterdir():
    print(file.name)
```

`Path` is Python's built-in helper for files and folders. `iterdir()` gives you every item in the folder, one at a time. Run this first to check it finds your files.

## Step 2: do a dry run

Before renaming anything, print what you *would* do:

```python
from pathlib import Path

folder = Path("test-photos")
files = sorted(f for f in folder.iterdir() if f.suffix.lower() == ".jpg")

for number, file in enumerate(files, start=1):
    new_name = f"holiday-{number:03}{file.suffix.lower()}"
    print(file.name, "->", new_name)
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

Collect only the `.jpg` files and sort them by name. Then go through them, counting from 1. For each one, build a new name: `{number:03}` pads the number to three digits, so 7 becomes `007`.

</div>

## Step 3: rename for real

When the dry run looks right, swap the `print` for `rename`:

```python
    file.rename(folder / new_name)
```

Run it, and every photo gets its new name in an instant.

## What you just did

You used a **variable** (`folder`), a **loop** (`for ... in`), a **decision** (only `.jpg` files) and a built-in **library** (`pathlib`). That's real automation, and it's the same pattern behind scripts that sort downloads, back up files or clean up old logs.

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Change the script so it also handles `.png` files. Then make it ask for the name prefix with `input()` instead of always using "holiday".

</div>
