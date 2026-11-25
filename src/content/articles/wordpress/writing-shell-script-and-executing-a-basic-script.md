---
title: "Writing Shell Script and Executing a Basic Script"
description: "You can use a text editor such as Notepad or Sublime Text to write a shell script. The script should be saved with a file extension such as .sh. Once you…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2023-01-15T05:54:06Z
legacy: true
wpId: 3468
---

You can use a text editor such as Notepad or Sublime Text to write a shell script. The script should be saved with a file extension such as .sh.

Once you have written your script, you need to make the script executable by using the command `chmod +x scriptname.sh` and then you can execute the script by running `./scriptname.sh` in the command line interface.

A basic shell script can be as simple as printing a message to the console, for example:

```bash
#!/bin/bash
echo "Hello, World!"
```

You can also include shell commands and logic in your script, like performing tasks such as reading and writing files, connecting to databases, and so on.

For example, you can create a script that will check if a file exists and if it does, it will print the contents of that file.

```bash
#!/bin/bash
if [ -f "/path/to/file.txt" ]; then
    cat /path/to/file.txt
else
    echo "File not found."
fi
```

You can also include loops, variables, and conditional statements to make the script more powerful.

Keep in mind that shell scripts are platform dependent. The shell commands and syntax may be different on other operating systems.
