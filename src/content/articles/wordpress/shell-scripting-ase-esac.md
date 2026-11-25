---
title: "Shell scripting ase – esac"
description: "ase and esac are control structures in shell scripts that are used to define a case statement. Here's an example of how you can use a case statement in a…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2023-01-08T16:51:42Z
legacy: true
wpId: 3458
---

`ase` and `esac` are control structures in shell scripts that are used to define a `case` statement.

Here's an example of how you can use a `case` statement in a shell script:

```bash
case $VAR in
    value1)
        # do something
        ;;
    value2)
        # do something else
        ;;
    *)
        # do something else
        ;;
esac
```

In this example, the `case` statement checks the value of the variable `$VAR`. If the value is `value1`, the script will execute the commands in the first block. If the value is `value2`, the script will execute the commands in the second block. If the value is anything else, the script will execute the commands in the third block (the default case, indicated by the `*`).

The `;;` at the end of each block indicates the end of the case.

I hope this helps! Let me know if you have any questions.
