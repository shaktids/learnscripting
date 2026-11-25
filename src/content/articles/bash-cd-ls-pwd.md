---
title: Finding your way around with cd, ls and pwd
description: The three Bash commands you will type more than any others, and how to stop feeling lost in the terminal.
lang: bash
pubDate: 2026-11-14
---

When you open a terminal, you're always standing *inside* some folder. These three commands tell you where you are, what's around you, and how to move.

## pwd: where am I?

`pwd` stands for **p**rint **w**orking **d**irectory.

```bash
pwd
```

```text
/home/sam
```

That's your current folder. On macOS it might look like `/Users/sam`.

## ls: what's here?

`ls` **l**i**s**ts what's in the current folder.

```bash
ls
```

Two useful extras:

```bash
ls -l    # long format: sizes, dates, permissions
ls -a    # also show hidden files (names starting with a dot)
```

## cd: move somewhere

`cd` **c**hanges **d**irectory.

```bash
cd Documents      # go into the Documents folder
cd ..             # go up one level
cd ~              # go back to your home folder
cd -              # jump back to where you just were
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

`..` always means "the folder above this one", and `~` always means "my home folder". Anything after `#` is a comment, so Bash ignores it.

</div>

## A tip that saves hours

Press **Tab** while typing a folder or file name and Bash finishes it for you. Press Tab twice to see all the options. It's faster, and it stops typos.

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Open a terminal, `cd` into your Documents folder, list everything with `ls -l`, then return home with `cd ~` and check with `pwd`.

</div>
