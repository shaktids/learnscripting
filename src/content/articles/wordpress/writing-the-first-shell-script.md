---
title: "Writing the first Shell Script"
description: "To write your first shell script, you will need to use a text editor to create a new file. You can use any text editor that you like, such as vi , nano …"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2022-12-27T09:08:41Z
legacy: true
wpId: 3371
---

To write your first shell script, you will need to use a text editor to create a new file. You can use any text editor that you like, such as `vi`, `nano`, or `gedit`.

Here is an example of a simple shell script that displays the message "Hello, World!" on the screen:

```bash
#!/bin/bash

echo "Hello, World!"
```

To make the script executable, you will need to give it execute permissions using the `chmod` command:

```bash
chmod +x myscript.sh
```

You can then run the script by typing its name:

```bash
./myscript.sh
```

This will execute the commands in the script and display the message "Hello, World!" on the screen.

Here is a brief explanation of the lines in the script:

- The first line, `#!/bin/bash`, is called the shebang line. It tells the system which interpreter to use to execute the script. In this case, it is telling the system to use the `bash` shell to execute the script.
- The second line, `echo "Hello, World!"`, is a command that displays the message "Hello, World!" on the screen. The `echo` command is a built-in command in the bash shell that prints its arguments to the standard output.

I hope this helps! Let me know if you have any questions.
