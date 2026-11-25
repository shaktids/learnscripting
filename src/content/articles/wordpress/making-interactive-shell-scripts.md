---
title: "Making Interactive Shell Scripts"
description: "An interactive shell script is a script that prompts the user for input, rather than just running automatically. There are several ways to create an…"
lang: bash
categories: ["Shell Scripting"]
author: "Shakti Das"
pubDate: 2023-01-15T06:01:45Z
legacy: true
wpId: 3478
---

An interactive shell script is a script that prompts the user for input, rather than just running automatically. There are several ways to create an interactive shell script, depending on the type of input you are looking for. Here are a few common methods:

1. **read command:** The `read` command is used to read input from the user and store it in a variable. For example:

```bash
read -p "Enter your name: " name
echo "Hello, $name!"
```

2. **select command:** The `select` command allows the user to select an option from a list of options. For example:

```bash
PS3="Select an option: "
options=("Option 1" "Option 2" "Option 3")
select opt in "${options[@]}"
do
    case $opt in
        "Option 1")
            echo "You selected option 1."
            ;;
        "Option 2")
            echo "You selected option 2."
            ;;
        "Option 3")
            echo "You selected option 3."
            ;;
        *) echo "Invalid option.";;
    esac
done
```

3. **if statement**: You can use the `if` statement to check the user's input and perform different actions based on that input. For example:

```bash
echo "Do you want to continue? (y/n)"
read answer
if [ "$answer" = "y" ]; then
    echo "Continuing..."
else
    echo "Exiting..."
fi
```

4. **while loop**: You can use the `while` loop to repeatedly prompt the user for input until they provide the correct input. For example:

```bash
while true; do
    read -p "Enter a number between 1 and 10: " num
    if [[ $num =~ ^[1-9]$|^10$ ]]; then
        echo "Thank you for entering $num."
        break
    else
        echo "Invalid input. Please try again."
    fi
done
```

These are just a few examples of how you can create interactive shell scripts. Depending on the complexity of your script, you may need to use a combination of these methods. It's also good practice to add a help option or instruction to make the script more user-friendly.
