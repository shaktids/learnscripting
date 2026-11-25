---
title: Set up your computer
description: Install Python and find your terminal on Windows, macOS or Linux, in about ten minutes.
lang: general
step: 2
pubDate: 2026-11-04
---

Before you can run a script you need two things: a **terminal** (a window where you type commands) and the **language** installed. Here's how to get both.

## Find your terminal

The terminal looks scary at first: a plain window with a blinking cursor. It's just a place to type instructions instead of clicking.

- **Windows:** press the Windows key, type `Terminal`, and press Enter. (On older Windows, search for `PowerShell` instead.)
- **macOS:** press Cmd + Space, type `Terminal`, and press Enter.
- **Linux:** press Ctrl + Alt + T on most distributions.

## Install Python

### Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest version.
2. Run the installer. **Tick "Add python.exe to PATH"** at the bottom of the first screen. This matters!
3. Click *Install Now*.

### macOS

Download the installer from [python.org/downloads](https://www.python.org/downloads/) and run it. On macOS the command is usually `python3`, not `python`.

### Linux

Python is almost always installed already. Check with the command below.

## Check it worked

Open a **new** terminal window and type:

```bash
python --version
```

You should see something like `Python 3.13.0`. On macOS or Linux, try `python3 --version` if `python` isn't found.

<div class="callout warn">
<p class="callout-title">"python is not recognized"?</p>

On Windows, this nearly always means the PATH box wasn't ticked. Run the installer again, choose *Modify*, and turn on "Add Python to environment variables".

</div>

## Get a text editor

Scripts are plain text files. You *can* write them in Notepad, but a code editor helps a lot: it colours your code and spots typos. [Visual Studio Code](https://code.visualstudio.com/) is free and works everywhere. PyCharm Community is a great choice for Python too.

## What about the other languages?

- **Bash** is built into macOS and Linux. On Windows, install [Git for Windows](https://git-scm.com/download/win), which includes Git Bash.
- **PowerShell** is built into Windows. It also runs on macOS and Linux.
- **JavaScript** runs in every web browser. For running `.js` files in the terminal, install [Node.js](https://nodejs.org/).

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Open your terminal and run `python --version`. If you see a version number, you're ready for step 3.

</div>
