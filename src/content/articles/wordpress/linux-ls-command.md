---
title: "Linux ls command"
description: "ls syntax $ ls [ options ] [ file dir ] ls command options ls command main options: option description ls a list all files including hidden file starting…"
lang: bash
categories: ["Linux"]
author: "Shakti Das"
pubDate: 2020-04-11T05:02:18Z
legacy: true
wpId: 2054
---

## ls syntax

$ ls [*options*] [*file*|*dir*]

## ls command options

ls command main options:

| option | description |
| --- | --- |
| ls -a | list all files including hidden file starting with '.' |
| ls --color | colored list [=always/never/auto] |
| ls -d | list directories - with ' \*/' |
| ls -F | add one char of \*/=>@| to enteries |
| ls -i | list file's inode index number |
| ls -l | list with long format - show permissions |
| ls -la | list long format including hidden files |
| ls -lh | list long format with readable file size |
| ls -ls | list with long format with file size |
| ls -r | list in reverse order |
| ls -R | list recursively directory tree |
| ls -s | list file size |
| ls -S | sort by file size |
| ls -t | sort by time & date |
| ls -X | sort by extension name |

## ls command examples

You can press the *tab* button to auto complete the file or folder names.

List directory *Documents/Books* with *relative* path:

$ ls Documents/Books

List directory */home/user/Documents/Books* with *absolute* path.

$ ls /home/user/Documents/Books

List root directory:

$ ls /

List parent directory:

$ ls ..

List user's home directory (e.g: /home/user):

$ ls ~

List with long format:

$ ls -l

Show hidden files:

$ ls -a

List with long format and show hidden files:

$ ls -la

Sort by date/time:

$ ls -t

Sort by file size:

$ ls -S

List all subdirectories:

$ ls \*

Recursive directory tree list:

$ ls -R

List only text files with wildcard:

$ ls \*.txt

ls redirection to output file:

$ ls > out.txt

List directories only:

$ ls -d \*/

List files and directories with full path:

$ ls -d $PWD/\*
