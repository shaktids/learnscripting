---
title: "Understanding the \"case-esac\" Statement"
description: "In Bash scripting, the \"case esac\" statement is a powerful tool for handling multiple conditional scenarios. It allows you to compare a variable or…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2023-09-30T15:10:13Z
legacy: true
wpId: 3637
---

In Bash scripting, the "case-esac" statement is a powerful tool for handling multiple conditional scenarios. It allows you to compare a variable or expression against a list of patterns and execute code blocks based on the first matching pattern. This construct provides a cleaner and more efficient way to handle complex conditional logic compared to using a series of "if-elif-else" statements.

The syntax for the "case-esac" statement looks like this:

```bash
case expression in
    pattern1)
        # Code to execute when pattern1 matches
        ;;
    pattern2)
        # Code to execute when pattern2 matches
        ;;
    pattern3)
        # Code to execute when pattern3 matches
        ;;
    *)
        # Default code to execute if no patterns match
        ;;
esac
```

Here's a breakdown of the components:

- `expression`: This is the value or variable that you want to test against the patterns.
- `pattern1`, `pattern2`, `pattern3`, etc.: These are the patterns you want to match against the expression. Each pattern can include wildcards like `*` or `?` for pattern matching.
- `*)`: The asterisk `*` is used as a wildcard to match any value not covered by previous patterns. It acts as the default case when no other patterns match.
- `;;`: This double semicolon marks the end of each code block associated with a pattern.

### Practical Usage of "case-esac"

Now, let's look at some practical examples to understand how the "case-esac" statement can be used in real-world scenarios:

#### Example 1: Menu Selection

```bash
#!/bin/bash

echo "Select an option:"
echo "1. Start"
echo "2. Stop"
echo "3. Restart"

read choice

case $choice in
    1)
        echo "Starting the application..."
        ;;
    2)
        echo "Stopping the application..."
        ;;
    3)
        echo "Restarting the application..."
        ;;
    *)
        echo "Invalid option"
        ;;
esac
```

In this example, the user's choice is captured in the `choice` variable, and the "case-esac" statement is used to execute different actions based on the user's input.

#### Example 2: File Type Detection

```bash
#!/bin/bash

file="example.txt"

case $file in
    *.txt)
        echo "Text file"
        ;;
    *.jpg|*.jpeg|*.png)
        echo "Image file"
        ;;
    *.sh)
        echo "Shell script"
        ;;
    *)
        echo "Unknown file type"
        ;;
esac
```

In this example, the script determines the type of a file based on its extension.

### Conclusion

The "case-esac" statement is a versatile tool in Bash scripting, allowing you to simplify complex conditional logic by handling multiple cases efficiently. It offers a cleaner and more readable alternative to a series of "if-elif-else" statements, making your code more organized and easier to maintain. Whether you need to create a menu-driven script or perform file type detection, the "case-esac" statement is an essential construct for your Bash scripting toolbox.
