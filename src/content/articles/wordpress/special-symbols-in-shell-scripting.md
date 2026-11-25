---
title: "Special Symbols or Operators in Shell Scripting"
description: "In this post, we will learn how to use inbuild special symbols in the shell to make our code simple. Let's assume we have a file in the temp directory and…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2022-01-31T17:46:59Z
legacy: true
wpId: 3023
---

In this post, we will learn how to use inbuild special symbols in the shell to make our code simple.
Let's assume we have a file in the temp directory and we will use the inbuilt keyword to test the functionality.

We have 2 files in the Desktop

The **ls** command shows all the files in the current directory.

> root@vps43086554:~/Desktop# ls
> sample.sh sample.txt
> root@vps43086554:~/Desktop#

Now will make a simple shell script **sample.sh** where we will write an if condition where the condition will check with the help of existing keywords.

> if [ -e sample.txt ];
> then echo "Inside if ture part"
> fi

In the above the if condition we have written an if the condition where we have written -e and a file name.

## File Operators

## -e

Ture if file exists.
Menas it will check if the file exists in the directory then it will return true.

Prerequisite -Create 2 files sample.sh sample.txt

> if [ -e sample.txt ];
> then echo "Inside if ture part"
> fi

Output-
root@vps43086554:~/Desktop# sh sample.sh
Inside if ture part
root@vps43086554:~/Desktop#

## -d

True if the file is a directory.

Prerequisite- Create a folder named a folder.

Code to create a folder named as folder.

> root@vps43086554:~/Desktop# mkdir folder
> root@vps43086554:~/Desktop# ls
> folder sample.sh sample.txt

Code to check the folder is exists or not.

> if [ -e folder ];
> then echo "Inside if ture part"
> fi

Output

root@vps43086554:~/Desktop# sh sample.sh
Inside if ture part

## -f

True if the file exists and the file is a regular file.

Prerequisite- Create an invalid file named non\_normarl.gfd.

Code-

> if [ -f non\_normal.gfd ];
> then echo "Inside if ture part"
> fi
> if [ -f sample.txt ];
> then echo "Inside if ture part of valid file"
> fi

root@vps43086554:~/Desktop# sh sample.sh
Inside if ture part of valid file

## -r

True if the file is readable by you

## -s

True if the file exists and is not empty.

## -w

True if the file is writable by you.

## -x

True if the file is executable by you.

## String Operators

## -z "String"

True if the string is empty

## -n "String"

True if the file is not empty.

## STRING1=STRING2

True id the strings are equal.

## STRING1!=STRING2

True if the strings are not equal.

## agr1 -eq arg2

True if arg1 is equal to arg2

## agr1 -nq arg2

True if arg1 is not equal to arg2

## arg1 -lt arg2

True if the arg1 is less than arg2

## arg1 -le arg2

True if arg1 is less than or equal to arg2

## arg1 -gt arg2

True if the arg1 is greater than arg2

## arg1 -ge arg2

True if the arg1 is greater than or equal to arg2
