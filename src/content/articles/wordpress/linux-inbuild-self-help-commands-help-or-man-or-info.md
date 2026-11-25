---
title: "Linux  Inbuild self-help commands  (help or man or info)"
description: "Linux has many commands available which can be very useful. Even it is very powerful when it gets all the available parameters along with the commands…"
lang: bash
categories: ["Linux", "Shell Scripting"]
author: "Shakti Das"
pubDate: 2020-04-05T03:43:30Z
legacy: true
wpId: 2027
---

Linux has many commands available which can be very useful. Even it is very powerful when it gets all the available parameters along with the commands. Due to the varsity of the commands available in the Linux, it's difficult to remember all the commands.

## How to use –h or –help?
Launch the terminal by pressing Ctrl+ Alt+ T or just click on the terminal icon in the taskbar. Simply type your command whose usage you to know in the terminal with –h or –help after space and press enter. And you’ll get the complete usage of that command as shown below.

## Description

**help** displays brief summaries of shell builtin commands. If *PATTERN* is specified, gives detailed help on all commands matching *PATTERN*, otherwise the list of help topics is printed.

## Syntax

```
help [-dms] [PATTERN ...]
```

## Options

|  |  |
| --- | --- |
| **-d** | Output short description for each topic. |
| **-m** | Display usage in pseudo-manpage format. |
| **-s** | Output only a short usage synopsis for each topic matching. |

## Examples

```
help echo
```

Display a brief description of the builtin shell command echo.

## Linux man command

The "man" is a short term for manual page. In unix like operating systems such as linux, man is an interface to view the system's reference manual.

A user can request to display a man page by simply typing man followed by a space and then argument. Here its argument can be a command, utility or function. A manual page associated with each of these arguments is displayed.

If you will provide a section number in the command, then man will be directed to look into that section number of the manual and that section page will be displayed. And if not, then by default it will display the first page and you have to go through the entire sections in a pre-defined manner.

We'll read about section number in this tutorial.

**Syntax of man:**

1. man [option(s)] keyword(s)

But generally [option(s)] are not used. Only keyword is written as an argument.

For example,

1. man ls

This command will display all the information about **'ls'** command as shown in the screenshot.

## info command in Linux with Examples

**info**command reads documentation in the *info*format. It will give detailed information for a command when compared with the man page. The pages are made using the *texinfo*tools because of which it can link with other pages, create menus and easy navigation.

**Syntax:**

```
info [OPTION]... [MENU-ITEM...]
```

**Options:**

- **-a, –all:** It use all matching manuals.
- **-k, –apropos=STRING:** It look up STRING in all indices of all manuals.
- **-d, –directory=DIR:** It add DIR to INFOPATH.
- **-f, –file=MANUAL:** It specify Info manual to visit.
- **-h, –help:** It display this help and exit.
- **-n, –node=NODENAME:** It specify nodes in first visited Info file.
- **-o, –output=FILE:** It output selected nodes to FILE.
- **-O, –show-options, –usage:** It go to command-line options node.
- **-v, –variable VAR=VALUE:** It assign VALUE to Info variable VAR.
- **–version:** It display version information and exit.
- **-w, –where, –location:** It print physical location of Info file.

**Examples:**

- **-a :** It use all matching manuals and displays them for a particular command. info -a cvs
