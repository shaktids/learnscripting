---
title: "Shell Environment & Environment Variables"
description: "In this post, we will discuss in detail about the Unix environment. An important Unix concept is the environment , which is defined by environment…"
lang: bash
categories: ["Linux", "Shell Scripting"]
author: "Shakti Das"
pubDate: 2022-12-19T17:26:58Z
updatedDate: 2023-09-30T06:48:39Z
legacy: true
wpId: 1713
---

In this post, we will discuss in detail about the Unix environment. An important Unix concept is the **environment**, which is defined by environment variables. Some are set by the system, others by user, yet others by the shell, or any program that loads another program.

A variable is a character string to which we assign a value. The value assigned could be a number, text, filename, device, or any other type of data.

For example, first we set a variable TEST and then we access its value using the **echo** command −

```
$VAR="Sample String"
$echo $VAR
```

It produces the following result.

```
 Sample String
```

Note that the environment variables are set without using the **$** sign but while accessing them we use the $ sign as prefix. These variables retain their values until we **come out of the shell.**

When you log in to the system, the shell undergoes a phase called **initialization** to set up the environment. This is usually a two-step process that involves the shell reading the following files −

- /etc/profile
- profile

The process is as follows −

- The shell checks to see whether the file **/etc/profile** exists.
- If it exists, the shell reads it. Otherwise, this file is skipped. No error message is displayed.
- The shell checks to see whether the file **.profile** exists in your home directory. Your home directory is the directory that you start out in after you log in.
- If it exists, the shell reads it; otherwise, the shell skips it. No error message is displayed.

As soon as both of these files have been read, the shell displays a prompt −

```
$
```

This is the prompt where you can enter commands in order to have them executed.

**Note** − The shell initialization process detailed here applies to all **Bourne** type shells, but some additional files are used by **bash** and **ksh**.

## The .profile File

The file **/etc/profile** is maintained by the system administrator of your Unix machine and contains shell initialization information required by all users on a system.

The file **.profile** is under your control. You can add as much shell customization information as you want to this file. The minimum set of information that you need to configure includes −

- The type of terminal you are using.
- A list of directories in which to locate the commands.
- A list of variables affecting the look and feel of your terminal.

You can check your **.profile** available in your home directory. Open it using the vi editor and check all the variables set for your environment.

## Setting the Terminal Type

Usually, the type of terminal you are using is automatically configured by either the **login** or **getty** programs. Sometimes, the auto-configuration process guesses your terminal incorrectly.

If your terminal is set incorrectly, the output of the commands might look strange, or you might not be able to interact with the shell properly.

To make sure that this is not the case, most users set their terminal to the lowest common denominator in the following way −

```
$TERM=vt100
$
```

## Setting the PATH

When you type any command on the command prompt, the shell has to locate the command before it can be executed.

The PATH variable specifies the locations in which the shell should look for commands. Usually the Path variable is set as follows −

```
$PATH=/bin:/usr/bin
$
```

Here, each of the individual entries separated by the colon character **(:)** are directories. If you request the shell to execute a command and it cannot find it in any of the directories given in the PATH variable, a message similar to the following appears −

```
$hello
hello: not found
$
```

There are variables like PS1 and PS2 which are discussed in the next section.

## PS1 and PS2 Variables

The characters that the shell displays as your command prompt are stored in the variable PS1. You can change this variable to be anything you want. As soon as you change it, it'll be used by the shell from that point on.

For example, if you issued the command −

```
$PS1='=>'
=>
=>
=>
```

Your prompt will become =>. To set the value of **PS1** so that it shows the working directory, issue the command −

```
=>PS1="[\u@\h \w]\$"
```

The result of this command is that the prompt displays the user's username, the machine's name (hostname), and the working directory.

There are quite a few **escape sequences** that can be used as value arguments for PS1; try to limit yourself to the most critical so that the prompt does not overwhelm you with information.

|  |  |  |
| --- | --- | --- |
| Sr.No. |  | Escape Sequence & Description |
| 1 | **\t** | Current time, expressed as HH:MM:SS |
| 2 | **\d** | Current date, expressed as Weekday Month Date |
| 3 | **\n** | Newline |
| 4 | **\s** | Current shell environment |
| 5 | **\W** | Working directory |
| 6 | **\w** | Full path of the working directory |
| 7 | **\u** | Current user’s username |
| 8 | **\h** | Hostname of the current machine |
| 9 | **\#** | Command number of the current command. Increases when a new command is entered |
| 10 | **\$** | If the effective UID is 0 (that is, if you are logged in as root), end the prompt with the # character; otherwise, use the $ sign |

You can make the change yourself every time you log in, or you can have the change made automatically in PS1 by adding it to your **.profile** file.

When you issue a command that is incomplete, the shell will display a secondary prompt and wait for you to complete the command and hit **Enter**again.

The default secondary prompt is **>** (the greater than sign), but can be changed by re-defining the **PS2** shell variable −

Following is the example which uses the default secondary prompt −

```
$ echo "this is a
> test"
this is a
test
$
```

The example given below re-defines PS2 with a customized prompt −

```
$ PS2="secondary prompt->"
$ echo "this is a
secondary prompt->test"
this is a
test
$
```

## Environment Variables

Following is the partial list of important environment variables. These variables are set and accessed as mentioned below −

Certainly, here's the data formatted into a three-column table with "Sr. No.," "Variable," and "Description" columns:

| Sr. No. | Variable | Description |
| --- | --- | --- |
| 1 | DISPLAY | Contains the identifier for the display that X11 programs should use by default. |
| 2 | HOME | Indicates the home directory of the current user: the default argument for the cd built-in command. |
| 3 | IFS | Indicates the Internal Field Separator that is used by the parser for word splitting after expansion. |
| 4 | LANG | LANG expands to the default system locale; LC\_ALL can be used to override this. For example, if its value is pt\_BR, then the language is set to (Brazilian) Portuguese and the locale to Brazil. |
| 5 | LD\_LIBRARY\_PATH | A Unix system with a dynamic linker, contains a colon-separated list of directories that the dynamic linker should search for shared objects when building a process image after exec, before searching in any other directories. |
| 6 | PATH | Indicates the search path for commands. It is a colon-separated list of directories in which the shell looks for commands. |
| 7 | PWD | Indicates the current working directory as set by the cd command. |
| 8 | RANDOM | Generates a random integer between 0 and 32,767 each time it is referenced. |
| 9 | SHLVL | Increments by one each time an instance of bash is started. This variable is useful for determining whether the built-in exit command ends the current session. |
| 10 | TERM | Refers to the display type. |
| 11 | TZ | Refers to Time zone. It can take values like GMT, AST, etc. |
| 12 | UID | Expands to the numeric user ID of the current user, initialized at the shell startup. |

Now, the data is organized into a three-column table with "Sr. No.," "Variable," and "Description" columns for better readability and understanding.

Following is the sample example showing a few environmental variables −

```
$ echo $HOME
/root
]$ echo $DISPLAY

$ echo $TERM
xterm
$ echo $PATH
/usr/local/bin:/bin:/usr/bin:/home/amrood/bin:/usr/local/bin
```

A shell maintains an environment that includes a set of variables defined by the `login` program, the system initialization file, and the user initialization files. In addition, some variables are defined by default.

A shell can have two types of variables:

- **Environment variables –** Variables that are exported to all processes spawned by the shell. Their settings can be seen with the `env` command. A subset of environment variables, such as PATH, affects the behavior of the shell itself.
- **Shell (local) variables –** Variables that affect only the current shell. In the C shell, a set of these shell variables have a special relationship to a corresponding set of environment variables. These shell variables are user, term, home, and path. The value of the environment variable counterpart is initially used to set the shell variable.

In the C shell, you use the lowercase names with the `set` command to set shell variables. You use uppercase names with the `setenv` command to set environment variables. If you set a shell variable, the shell sets the corresponding environment variable. Likewise, if you set an environment variable, the corresponding shell variable is also updated. For example, if you update the path shell variable with a new path, the shell also updates the PATH environment variable with the new path.

In the Bourne and Korn shells, you can use the uppercase variable name equal to some value to set both shell and environment variables. You also have to use the `export` command to activate the variables for any subsequently executed commands.

For all shells, you generally refer to shell and environment variables by their uppercase names.

In a user initialization file, you can customize a user's shell environment by changing the values of the predefined variables or by specifying additional variables. The following table shows how to set environment variables in a user initialization file.Table 4–18 Setting Environment Variables in a User Initialization File

| Shell Type | Line to Add to the User Initialization File |
| --- | --- |
| C shell | `setenv` VARIABLE valueExample:`setenv MAIL /var/mail/ripley` |
| Bourne or Korn shell | VARIABLE`=`value`; export` VARIABLEExample: `MAIL=/var/mail/ripley;export MAIL` |

The following table describes environment variables and shell variables that you might want to customize in a user initialization file. For more information about variables that are used by the different shells, see the [sh(1)](https://docs.oracle.com/docs/cd/E19082-01/819-2239/sh-1/index.html), [ksh(1)](https://docs.oracle.com/docs/cd/E19082-01/819-2239/ksh-1/index.html), or [csh(1)](https://docs.oracle.com/docs/cd/E19082-01/819-2239/csh-1/index.html) man pages.Table 4–19 Shell and Environment Variable Descriptions

| Variable | Description |
| --- | --- |
| CDPATH, or cdpath in the C shell | Sets a variable used by the `cd` command. If the target directory of the `cd` command is specified as a relative path name, the `cd` command first looks for the target directory in the current directory (“.”). If the target is not found, the path names listed in the CDPATH variable are searched consecutively until the target directory is found and the directory change is completed. If the target directory is not found, the current working directory is left unmodified. For example, the CDPATH variable is set to `/home/jean`, and two directories exist under `/home/jean`, `bin`, and `rje`. If you are in the `/home/jean/bin` directory and type `cd rje`, you change directories to `/home/jean/rje`, even though you do not specify a full path. |
| history | Sets the history for the C shell. |
| HOME, or home in the C shell | Sets the path to the user's home directory. |
| LANG | Sets the locale. |
| LOGNAME | Defines the name of the user currently logged in. The default value of LOGNAME is set automatically by the login program to the user name specified in the `passwd` file. You should only need to refer to, not reset, this variable. |
| LPDEST | Sets the user's default printer. |
| MAIL | Sets the path to the user's mailbox. |
| MANPATH | Sets the hierarchies of man pages that are available. |
| PATH, or path in the C shell | Specifies, in order, the directories that the shell searches to find the program to run when the user types a command. If the directory is not in the search path, users must type the complete path name of a command.  As part of the login process, the default PATH is automatically defined and set as specified in `.profile` (Bourne or Korn shell) or `.cshrc` (C shell).The order of the search path is important. When identical commands exist in different locations, the first command found with that name is used. For example, suppose that PATH is defined in Bourne and Korn shell syntax as PATH=/bin:/usr/bin:/usr/sbin:$HOME/bin and a file named `sample` resides in both `/usr/bin` and `/home/jean/bin`. If the user types the command `sample` without specifying its full path name, the version found in `/usr/bin` is used. |
| prompt | Defines the shell prompt for the C shell. |
| PS1 | Defines the shell prompt for the Bourne or Korn shell. |
| SHELL, or shell in the C shell | Sets the default shell used by `make`, `vi`, and other tools. |
| TERMINFO | Specifies the path name for an unsupported terminal that has been added to the `terminfo` file. Use the TERMINFO variable in either the `/etc/profile` or `/etc/.login` file. When the TERMINFO environment variable is set, the system first checks the TERMINFO path defined by the user. If the system does not find a definition for a terminal in the TERMINFO directory defined by the user, it searches the default directory, `/usr/share/lib/terminfo`, for a definition. If the system does not find a definition in either location, the terminal is identified as “dumb.” |
| TERM, or term in the C shell | Defines the terminal. This variable should be reset in either the `/etc/profile` or `/etc/.login` file. When the user invokes an editor, the system looks for a file with the same name that is defined in this environment variable. The system searches the directory referenced by TERMINFO to determine the terminal characteristics. |
| TZ | Sets the time zone. The time zone is used to display dates, for example, in the `ls -l` command. If TZ is not set in the user's environment, the system setting is used. Otherwise, Greenwich Mean Time is used. |
