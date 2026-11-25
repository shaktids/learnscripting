---
title: "Writing the first script"
description: "For our first shell script, we'll just write a script which says \"Hello World\". We will then try to get more out of a Hello World program than any other…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-04-20T02:53:49
legacy: true
wpId: 2292
draft: true
---

For our first shell script, we'll just write a script which says "Hello World". We will then try to get more out of a Hello World program than any other tutorial you've ever read :-)
Create a file (first.sh) as follows:

---

first.sh

```
#!/bin/sh
# This is a comment!
echo Hello World        # This is a comment, too!
```

---

The first line tells Unix that the file is to be executed by /bin/sh. This is the standard location of the Bourne shell on just about every Unix system. If you're using GNU/Linux, /bin/sh is normally a symbolic link to bash (or, more recently, dash).

The second line begins with a special symbol: `#`. This marks the line as a comment, and it is ignored completely by the shell.
The only exception is when the *very first* line of the file starts with `#!` - as ours does. This is a special directive which Unix treats specially. It means that even if you are using csh, ksh, or anything else as your interactive shell, that what follows should be interpreted by the Bourne shell.
Similarly, a Perl script may start with the line `#!/usr/bin/perl`to tell your interactive shell that the program which follows should be executed by perl. For Bourne shell programming, we shall stick to `#!/bin/sh.`

The third line runs a command: `echo`, with two parameters, or arguments - the first is `"Hello"`; the second is `"World"`.
Note that `echo` will automatically put a single space between its parameters.
The `#` symbol still marks a comment; the # and anything following it is ignored by the shell.

now run `chmod 755 first.sh` to make the text file executable, and run `./first.sh`.
Your screen should then look like this:

```
$ chmod 755 first.sh
$ ./first.sh
Hello World
$
```

You will probably have expected that! You could even just run:

```
$ echo Hello World
Hello World
$
```

Now let's make a few changes.
First, note that `echo` puts ONE space between its parameters. Put a few spaces between "Hello" and "World". What do you expect the output to be? What about putting a TAB character between them?
As always with shell programming, try it and see.
The output is exactly the same! We are calling the `echo` program with two arguments; it doesn't care any more than `cp` does about the gaps in between them. Now modify the code again:

```
#!/bin/sh
# This is a comment!
echo "Hello      World"       # This is a comment, too!
```

This time it works. You probably expected that, too, if you have experience of other programming languages. But the key to understanding what is going on with more complex command and shell script, is to understand and be able to explain: WHY?
`echo` has now been called with just ONE argument - the string "Hello    World". It prints this out exactly.
The point to understand here is that the shell parses the arguments BEFORE passing them on to the program being called. In this case, it strips the quotes but passes the string as one argument.
As a final example, type in the following script. Try to predict the outcome before you run it:

---

first2.sh

```
#!/bin/sh
# This is a comment!
echo "Hello      World"       # This is a comment, too!
echo "Hello World"
echo "Hello * World"
echo Hello * World
echo Hello      World
echo "Hello" World
echo Hello "     " World
echo "Hello "*" World"
echo `hello` world
echo 'hello' world
```
