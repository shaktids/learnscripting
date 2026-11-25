---
title: What is a script, anyway?
description: The idea in plain words. A script is a list of instructions you write once and let the computer follow for you.
lang: general
step: 1
pubDate: 2026-11-02
---

A **script** is a list of instructions written in a file. You write it once, and the computer follows it for you, step by step, as many times as you like.

That's really all it is. The rest of this site is about writing better lists.

## Think of a recipe

A recipe says: crack two eggs, whisk them, heat the pan, pour. You follow the steps from top to bottom. A script works the same way, except a computer is doing the cooking, and the computer is very literal. It does *exactly* what you wrote, nothing more and nothing less.

## Your very first one

Here is a complete Python script. It has two lines, and each line is one instruction.

```python
name = input("What is your name? ")
print("Hello,", name)
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

Line 1: ask the person for their name, and remember the answer as `name`.

Line 2: print "Hello," followed by that name.

</div>

When you run it, the computer stops and waits for you to type. If you type `Sam`, it prints `Hello, Sam`.

## Script or program?

You'll hear both words. A **program** is any set of instructions for a computer. A **script** is usually a small program that you run directly from a text file, without a separate "build" step. Every script is a program, but not every program is a script. Don't worry too much about the difference.

## Why bother?

- **Save time.** Do boring jobs in seconds, like renaming hundreds of photos.
- **No slips.** A script does a task the same way every time.
- **Understand computers.** Writing small scripts is the gentlest way into coding.

## Which language should I use?

This site covers four scripting languages:

| Language | Good for |
| --- | --- |
| Python | Almost anything: files, data, automation |
| Bash | The Linux and macOS terminal |
| PowerShell | Automating Windows |
| JavaScript | Web pages and the browser |

If you're not sure, **pick Python**. You can learn the others later, and most of the ideas carry over.

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Think of one boring, repetitive task you do on your computer every week. Write it down as a numbered list of steps. Congratulations: that list is the plan for your first real script.

</div>
