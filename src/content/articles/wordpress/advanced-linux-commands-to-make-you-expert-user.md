---
title: "Advanced Linux Commands to Make You  Expert User"
description: "Linux commands and their optional parameter are very useful for the user who wants to take advance of the full feature of Linux CLI. In this post, we have…"
lang: bash
categories: ["Linux", "Shell Scripting"]
author: "Shakti Das"
pubDate: 2019-04-01T09:46:37Z
legacy: true
wpId: 1523
---

Linux commands and their optional parameter are very useful for the user who wants to take advance of the full feature of Linux CLI. In this post, we have discussed the most featured commands are being used extensively in day-to-day activities.

To explore more about commands you can explore all the commands available in using the **Linux Inbuild self-help commands (help or man or info)** available, Which will give the briefing about the options and uses by precise examples.

## A

### alias
The alias command is a way to keep your command /commands in a temporary variable. Unix commands using a shorter name than those that are usually associated with such commands.

```
Syntax:
alias shortName="your custom command here"

Example:
alias wr=”cd /var/www/html”
```

### apt-get
[APT](https://wiki.debian.org/Apt) (Advanced Package Tool) is the command line tool to interact with this packaging system. There is already dpkg commands to manage it. But apt is more friendly way to handle packaging. You can use it to find and install new packages, upgrade packages, clean the packages etc.

```bash
Syntax:
sudo apt-get install <package_name>
sudo apt-get remove <package_name>
sudo apt-get purge <package_name>
sudo apt-get clean
sudo apt-get autoclean
sudo apt-get autoremove

Example:
sudo apt-get install pinta
```

### AWK, Gawk
awk command searches files for text containing a pattern. When a line or text matches, awk performs a specific action on that line/text. The Program statement tells awk what operation to do; Program statement consists of a series of "rules" where each rule specifies one pattern to search for, and one action to perform when a particular pattern is found. A regular expression enclosed in slashes (/) is an awk pattern to match every input record whose text belongs to that set.

```
Syntax:
awk 'pattern {action}' input-file > output-file

Example:
awk '{ print $5 }' table1.txt > output1.txt
```

Awk is a scripting language used for manipulating data and generating reports.The awk command programming language requires no compiling, and allows the user to use variables, numeric functions, string functions, and logical operators.

Awk is a utility that enables a programmer to write tiny but effective programs in the form of statements that define text patterns that are to be searched for in each line of a document and the action that is to be taken when a match is found within a line. Awk is mostly used for pattern scanning and processing. It searches one or more files to see if they contain lines that matches with the specified patterns and then performs the associated actions.

Awk is abbreviated from the names of the developers – Aho, Weinberger, and Kernighan.

**WHAT CAN WE DO WITH AWK ?**

**1. AWK Operations:**
(a) Scans a file line by line
(b) Splits each input line into fields
(c) Compares input line/fields to pattern
(d) Performs action(s) on matched lines

**2. Useful For:**
(a) Transform data files
(b) Produce formatted reports

**3. Programming Constructs:**
(a) Format output lines
(b) Arithmetic and string operations
(c) Conditionals and loops

**Syntax:**

```
awk options 'selection _criteria {action }' input-file > output-file
```

**Options:**

```
-f program-file : Reads the AWK program source from the file
                  program-file, instead of from the
                  first command line argument.
-F fs            : Use fs for the input field separator
```

**Sample Commands**

**Example:**
Consider the following text file as the input file for all cases below.

```
$cat > employee.txt
```

```
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
```

**1. Default behavior of Awk :**By default Awk prints every line of data from the specified file.

```
$ awk '{print}' employee.txt
```

**Output:**

```
ajay manager account 45000
sunil clerk account 25000
varun manager sales 50000
amit manager account 47000
tarun peon sales 15000
deepak clerk sales 23000
sunil peon sales 13000
satvik director purchase 80000
```

In the above example, no pattern is given. So the actions are applicable to all the lines. Action print without any argument prints the whole line by default, so it prints all the lines of the file without failure.

**2. Print the lines which matches with the given pattern.**

```
$ awk '/manager/ {print}' employee.txt
```

**Output:**

```
ajay manager account 45000
varun manager sales 50000
amit manager account 47000
```

In the above example, the awk command prints all the line which matches with the ‘manager’.

**3. Splitting a Line Into Fields :**For each record i.e line, the awk command splits the record delimited by whitespace character by default and stores it in the $n variables. If the line has 4 words, it will be stored in $1, $2, $3 and $4 respectively. Also, $0 represents the whole line.

```
$ awk '{print $1,$4}' employee.txt
```

**Output:**

```
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

In the above example, $1 and $4 represents Name and Salary fields respectively.

**Built In Variables In Awk**

Awk’s built-in variables include the field variables—$1, $2, $3, and so on ($0 is the entire line) — that break a line of text into individual words or pieces called fields.

**NR:** NR command keeps a current count of the number of input records. Remember that records are usually lines. Awk command performs the pattern/action statements once for each record in a file.

**NF:** NF command keeps a count of the number of fields within the current input record.

**FS:** FS command contains the field separator character which is used to divide fields on the input line. The default is “white space”, meaning space and tab characters. FS can be reassigned to another character (typically in BEGIN) to change the field separator.

**RS:** RS command stores the current record separator character. Since, by default, an input line is the input record, the default record separator character is a newline.

**OFS:** OFS command stores the output field separator, which separates the fields when Awk prints them. The default is a blank space. Whenever print has several parameters separated with commas, it will print the value of OFS in between each parameter.

**ORS:** ORS command stores the output record separator, which separates the output lines when Awk prints them. The default is a newline character. print automatically outputs the contents of ORS at the end of whatever it is given to print.

**Examples:**

**Use of NR built-in variables (Display Line Number)**

```
$ awk '{print NR,$0}' employee.txt
```

**Output:**

```
1 ajay manager account 45000
2 sunil clerk account 25000
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
7 sunil peon sales 13000
8 satvik director purchase 80000
```

In the above example, the awk command with NR prints all the lines along with the line number.

**Use of NF built-in variables (Display Last Field)**

```
$ awk '{print $1,$NF}' employee.txt
```

**Output:**

```
ajay 45000
sunil 25000
varun 50000
amit 47000
tarun 15000
deepak 23000
sunil 13000
satvik 80000
```

In the above example $1 represents Name and $NF represents Salary. We can get the Salary using $NF , where $NF represents last field.

**Another use of NR built-in variables (Display Line From 3 to 6)**

```
$ awk 'NR==3, NR==6 {print NR,$0}' employee.txt
```

**Output:**

```
3 varun manager sales 50000
4 amit manager account 47000
5 tarun peon sales 15000
6 deepak clerk sales 23000
```

**More Examples**

**For the given text file:**

```
$cat > geeksforgeeks.txt

A    B    C
Tarun    A12    1
Man    B6    2
Praveen    M42    3
```

**1) To print the first item along with the row number(NR) separated with ” – “ from each line in geeksforgeeks.txt:**

```
$ awk '{print NR "- " $1 }' geeksforgeeks.txt
```

```
1 - Tarun
2 – Manav
3 - Praveen
```

**2) To return the second row/item from geeksforgeeks.txt:**

```
$ awk '{print $2}' geeksforgeeks.txt
```

```
A12
B6
M42
```

**3) To print any non empty line if present**

```
$ awk 'NF > 0' geeksforgeeks.txt
```

```
0
```

**4) To find the length of the longest line present in the file:**

```
$ awk '{ if (length($0) > max) max = length($0) } END { print max }' geeksforgeeks.txt
```

```
13
```

**5) To count the lines in a file:**

```
$ awk 'END { print NR }' geeksforgeeks.txt
```

```
3
```

**6) Printing lines with more than 10 characters:**

```
$ awk 'length($0) > 10' geeksforgeeks.txt
```

```
Tarun    A12    1
Praveen    M42    3
```

**7) To find/check for any string in any column:**

```
$ awk '{ if($3 == "B6") print $0;}' geeksforgeeks.txt
```

**8) To print the squares of first numbers from 1 to n say 6:**

```
$ awk 'BEGIN { for(i=1;i<=6;i++) print "square of", i, "is",i*i; }'
```

```
square of 1 is 1
square of 2 is 4
square of 3 is 9
square of 4 is 16
square of 5 is 25
square of 6 is 36
```

## B

### bzip2
A portable, fast, open source program that compresses and decompresses files at a high rate, but that does not archive them.

```
Syntax:
bzip2 option(s) filenames

Example:
bzip2 -z backup.tar
```

## C

### cat
A Unix/Linux command that can read, modify or concatenate text files. The [cat command](https://searchdatacenter.techtarget.com/answer/What-can-you-do-with-the-cat-command) also displays file contents.

```
Syntax:
cat [OPTION] [FILE]...

Example:
cat /etc/passwd
cat test test1
```

### cd
The cd command changes the current directory in Linux and can conveniently toggle between directories. The Linux cd command is similar to the CD and CHDIR commands in MS-DOS.

```
Syntax:
cd [-L | -P [-e]] directory

Example:
cd documents/work/accounting

Options
L
Force symbolic links to be followed. In other words, if you tell cd to move into a "directory", which is actually a symbolic link to a directory, it moves into the directory the symbolic link points to.
This option is the default behavior of cd; normally, it will always act as if -L has been specified.
-P
Use the physical directory structure without following symbolic links. In other words, only change into the specified directory if it actually exists as named; symbolic links will not be followed. This option is the opposite of the -L option, and if they are both specified, this option will be ignored.
-e
If the -P option is specified, and the current working directory cannot be determined, this option tells cd to exit with an error. If -P is not specified along with this option, this option has no function.
```

### chmod
The [chmod command](https://searchdatacenter.techtarget.com/definition/chmod-change-mode?int=off) changes the permissions of one or more files. Only the file owner or a privileged user can change the access mode.

```
Syntax:
chmod [OPTION]... MODE[,MODE]... FILE...
chmod [OPTION]... OCTAL-MODE FILE...
chmod [OPTION]... --reference=RFILE FILE...

[reference]
Reference   Class     Description
u          owner      file's owner
g          group      users who are members of the file's group
o          others     users who are neither the file's owner nor members of the file's group
a          all       All three of the above, same as ugo

[operator]
Operator  Description
+         Adds the specified modes to the specified classes
-         Removes the specified modes from the specified classes
=         The modes specified are to be made the exact modes for the specified classes

[mode]
Mode    Permission
r       Permission to read the file.
w       Permission to write (or delete) the file.
x       Permission to execute the file, or, in the case of a directory, search it.

[mode]
4       Permission to read the file.
2       Permission to write (or delete) the file.
1       Permission to execute the file, or, in the case of a directory, search it.
0       No Permission

So 7 is the combination of permissions 4+2+1 (read, write, and execute), 5 is 4+0+1(read, no write, and execute), and 4 is 4+0+0 (read, no write, and no execute).

Example:

chmod u=rwx,g=rx,o=r myfile
chmod 754 myfile
```

### chown
The chown prompt changes file or group ownership. It gives admins the option to change ownership of all the objects within a directory tree, as well as the ability to view information on the objects processed.

```
Syntax:
chown [-c|--changes] [-v|--verbose] [-f|--silent|--quiet] [--dereference] [-h|--no-dereference] [--preserve-root] [--from=currentowner:currentgroup] [--no-preserve-root] [-R|--recursive] [--preserve-root] [-H] [-L] [-P] {new-owner|--reference=ref-file} file ...
```

| *new-owner* form | Description |
| --- | --- |
| *user* | The name of the user to own the file. In this form, the colon ("**:**") and the *group* is omitted. The owning group is not altered. |
| *user***:***group* | The *user* and *group* to own the file, separated by a colon, with no spaces in between. |
| **:***group* | The group to own the file. In this form, *user* is omitted, and the *group* must be preceded by a colon. |
| *user***:** | If *group* is omitted, but a colon follows *user*, the owner is changed to *user*, and the owning group is changed to the login group of *user*. |
| **:** | Specifying a colon with no *user* or *group* is accepted, but ownership will not be changed. This form does not cause an error, but changes nothing. |

###### Options

| Option | Description |
| --- | --- |
| **-c**, **--changes** | Similar to **--verbose** mode, but only displays information about files that are actually changed. For example:  changed ownership of 'dir/dir1/file1' from hope:neil to hope:hope |
| **-v**, **--verbose** | Display [verbose](https://www.computerhope.com/jargon/v/verbose.htm) information for every file processed. For example:  changed ownership of 'dir/dir1/file1' from hope:neil to hope:hope ownership of 'dir/dir1' retained as hope:hope |
| **-f**, **--silent**, **--quiet** | Quiet mode. Do not display output. |
| **--dereference** | [Dereference](https://www.computerhope.com/jargon/d/dereference-operator.htm) all [symbolic links](https://www.computerhope.com/jargon/s/symblink.htm). If *file* is a symlink, change the owner of the referenced file, not the symlink itself. This is the default behavior. |
| **-h**, **--no-dereference** | Never dereference symbolic links. If *file* is a symlink, change the owner of the symlink rather than the referenced file. |
| **--from=***currentowner***:***currentgroup* | Change the owner or group of each file only if its current owner or group match *currentowner* and/or *currentgroup*. Either may be omitted, in which case a match is not required for the other attribute. |
| **--no-preserve-root** | Do not treat **/** (the root directory) in any special way. This is the default behavior. If the **--preserve-root** option is previously specified in the command, this option will cancel it. |
| **--reference=***ref-file* | Use the owner and group of file *ref-file*, rather than specifying ownership with *new-owner*. |
| **-R**, **--recursive** | Operate on files and directories [recursively](https://www.computerhope.com/jargon/r/recursive.htm). Enter each matching directory, and operate on all its contents. |

Recursive options

The following options modify how a [hierarchy](https://www.computerhope.com/jargon/h/hierfile.htm) is traversed when the **-R** or **--recursive**option is specified.

| Option | Description |
| --- | --- |
| **--preserve-root** | Never operate recursively on the root directory **/**.  If **--recursive** is not specified, this option has no effect. |
| **-H** | If a file specified on the command line is a symbolic link to a directory, traverse it and operate on those files and directories as well. |
| **-L** | Traverse all symbolic links to a directories. |
| **-P** | Do not traverse any symbolic links; operate on the symlinks themselves. This is the default behavior. |

If more than one of **-H**, **-L**, or **-P** is specified, only the final option takes effect.

Other options

These options display information about the program, and cannot be used with other options or arguments.

| Option | Description |
| --- | --- |
| **--help** | Display a brief help message and exit. |
| **--version** | Display [version](https://www.computerhope.com/jargon/v/version.htm) information and exit. |

Exit status

**chown** exits with a status of **0** for success. Any other number indicates failed operation.

```
Example:
sudo chown myuser myfile.txt
sudo chown notme:notmygroup myfile.txt
sudo chown -R myuser:mygroup otherfiles

```

### cmp
The cmp utility compares two files of any type and writes the results to the standard output. By default, cmp is silent if the files are the same. If they differ, cmp reports the byte and line number where the first difference occurred.

```
Syntax:
cmp [OPTION]... FILE1 [FILE2 [SKIP1 [SKIP2]]]

[OPTION]
-b --print-bytes
Print differing bytes.
-i SKIP --ignore-initial=SKIP
Skip the first SKIP bytes of input.
-i SKIP1:SKIP2 --ignore-initial=SKIP1:SKIP2
Skip the first SKIP1 bytes of FILE1 and the first SKIP2 bytes of FILE2.
-l --verbose
Output byte numbers and values of all differing bytes.
-n LIMIT --bytes=LIMIT
Compare at most LIMIT bytes.
-s --quiet --silent
Output nothing; yield exit status only.
-v --version
Output version info.
--help
Output this help.
SKIP1 and SKIP2 are the number of bytes to skip in each file. SKIP values may be followed by the following multiplicative suffixes: kB 1000, K 1024, MB 1,000,000, M 1,048,576, GB 1,000,000,000, G 1,073,741,824, and so on for T, P, E, Z, Y.
If a FILE is '-' or missing, read standard input.

Example:

cmp -b file1.txt file2.txt
cmp -i 10 file1.txt file2.txt
```

### comm
Admins use comm to compare lines common to file1 and file2. The output is in three columns; from left to right: lines unique to file1, lines unique to file2 and lines common in both files.

```
Syntax:
comm [OPTION]... FILE1 FILE2

Example:
comm file1.txt file2.txt
```

### cp
The [cp command](http://www.labtestproject.com/linuxcmd/cp.html) copies files and directories. Copies can be made simultaneously to another directory even if the copy is under a different name.

```
Syntax:
cp [OPTION] Source Destination
cp [OPTION] Source Directory
cp [OPTION] Source-1 Source-2 Source-3 Source-n Directory

Example:
cp Src_file1 Src_file2 Src_file3 Dest_directory
```

### cpio
The [cpio command](https://searchdatacenter.techtarget.com/tip/Moving-files-in-a-Unix-to-Linux-port) copies files into or out of a cpio or tar archive. A tar archive is a file that contains other files, plus information about them, such as their file name, owner, timestamps and access permissions. The archive can be another file on the disk, a magnetic tape or a pipe. It also has three operating modes: copy-out, copy-in and copy-pass. It is also­ a more efficient alternative to tar.

[GNU](https://www.computerhope.com/jargon/g/gnu.htm) **cpio** is a tool for creating and extracting archives, or copying files from one place to another. It handles a number of cpio formats as well as reading and writing [tar](https://www.computerhope.com/unix/utar.htm) files.

The following archive formats are supported: [binary](https://www.computerhope.com/jargon/b/binary.htm), old [ASCII](https://www.computerhope.com/jargon/a/ascii.htm), new ASCII, [CRC](https://www.computerhope.com/jargon/c/crc.htm), [HPUX](https://www.computerhope.com/jargon/h/hp-ux.htm)binary, HPUX old ASCII, old tar, and [POSIX](https://www.computerhope.com/jargon/p/posix.htm).1 tar. The tar format is provided for compatibility with the **tar** program. By default, **cpio** creates binary format archives, for compatibility with older cpio programs. When extracting from archives, cpio automatically recognizes which kind of archive it is reading and can read archives created on machines with a different byte-order.

Copy-Out Mode Syntax:

In copy-out mode, **cpio** copies files into an archive. It reads a list of [filenames](https://www.computerhope.com/jargon/f/filename.htm), one per line, on the [standard input](https://www.computerhope.com/jargon/s/stdin.htm) and writes the archive onto the standard output. A typical way to generate the list of filenames is with the [find](https://www.computerhope.com/unix/ufind.htm) command; you should give **find** the **-depth** option to minimize problems with [permissions](https://www.computerhope.com/jargon/p/permissi.htm) on [directories](https://www.computerhope.com/jargon/d/director.htm) that are unreadable. Copy-Out mode syntax:

```
cpio {-o|--create} [-0acvABLV] [-C bytes] [-H format] [-M message]
     [-O [[user@]host:]archive] [-F [[user@]host:]archive]
     [--file=[[user@]host:]archive] [--format=format]
     [--message=message][--null] [--reset-access-time] [--verbose] [--dot]
     [--append] [--block-size=blocks] [--dereference] [--io-size=bytes]
     [--rsh-command=command] [--help] [--version] < name-list [> archive]
```

Copy-In Mode Syntax:

In copy-in mode, **cpio** copies files out of an archive or lists the archive contents. It reads the archive from the standard input. Any non-option [command line](https://www.computerhope.com/jargon/c/commandi.htm) [arguments](https://www.computerhope.com/jargon/a/argument.htm)are [shell](https://www.computerhope.com/jargon/s/shell.htm) [globbing](https://www.computerhope.com/jargon/g/glob.htm) patterns; only files in the archive whose names match one or more of those patterns are copied from the archive. Unlike in the shell, an initial '**.**' in a filename does match a [wildcard](https://www.computerhope.com/jargon/w/wildcard.htm) at the start of a pattern, and a '**/**' in a filename can match wildcards. If no patterns are given, all files are extracted. Copy-In mode syntax:

```
cpio {-i|--extract} [-bcdfmnrtsuvBSV] [-C bytes] [-E file] [-H format]
     [-M message] [-R [user][:.][group]]
     [-I [[user@]host:]archive] [-F [[user@]host:]archive]
     [--file=[[user@]host:]archive] [--make-directories] [--nonmatching]
     [--preserve-modification-time] [--numeric-uid-gid] [--rename] [-t|--list]
     [--swap-bytes] [--swap] [--dot] [--unconditional] [--verbose]
     [--block-size=blocks] [--swap-halfwords] [--io-size=bytes]
     [--pattern-file=file] [--format=format] [--owner=[user][:.][group]]
     [--no-preserve-owner] [--message=message] [--force-local]
     [--no-absolute-filenames] [--absolute-filenames] [--sparse]
     [--only-verify-crc] [--to-stdout] [--quiet] [--rsh-command=command]
     [--help] [--version] [pattern...] [< archive]
```

Copy-Pass Mode Syntax:

In copy-pass mode, **cpio** copies files from one directory tree to another, combining the copy-out and copy-in steps without actually using an archive. It reads the list of files to copy from the standard input; the directory into which it will copy them is given as a non-option argument. Copy-Pass mode syntax:

```
cpio {-p|--pass-through} [-0adlmuvLV] [-R [user][:.][group]] [--null]
     [--reset-access-time] [--make-directories] [--link] [--quiet]
     [--preserve-modification-time] [--unconditional] [--verbose] [--dot]
     [--dereference] [--owner=[user][:.][group]] [--no-preserve-owner]
     [--sparse] [--help] [--version] destination-directory < name-list
```

CPIO Options

|  |  |
| --- | --- |
| **-0**, **--null** | Read a list of filenames terminated by a [null](https://www.computerhope.com/jargon/n/null.htm) character, instead of a [newline](https://www.computerhope.com/jargon/n/newline.htm), so that files whose names contain newlines can be archived. GNU **find** is one way to produce a list of null-terminated filenames. This option may be used in copy-out and copy-pass modes. |
| **-a**, **--reset-access-time** | Reset the access times of files after reading them, so that it does not look like they have just been read. |
| **-A**, **--append** | Append to an existing archive. Only works in copy-out mode. The archive must be a disk file specified with the **-O** or **-F** (**-file**) option. |
| **-b**, **--swap** | Swap both halfwords of words and [bytes](https://www.computerhope.com/jargon/b/byte.htm) of halfwords in the data. Equivalent to **-sS**. This option may be used in copy-in mode. Use this option to convert [32-bit](https://www.computerhope.com/jargon/num/32bit.htm) [integers](https://www.computerhope.com/jargon/i/integer.htm) between big-[endian](https://www.computerhope.com/jargon/e/endian.htm) and little-endian machines. |
| **-B** | Set the [I/O](https://www.computerhope.com/jargon/i/io.htm) [block](https://www.computerhope.com/jargon/b/block.htm) size to 5120 bytes. Initially the block size is 512 bytes. |
| **--block-size=***BLOCK-SIZE* | Set the I/O block size to **BLOCK-SIZE \* 512** bytes. |
| **-c** | Identical to '**-H newc**'; uses the new (SVR4) portable format. If you want the old portable (ASCII) archive format, use '**-H odc**' instead. |
| **-C** *IO-SIZE*, **--io-size=***IO-SIZE* | Set the I/O block size to *IO-SIZE* bytes. |
| **-d**, **--make-directories** | Create leading directories where needed. |
| **-E** *FILE*, **--pattern-file=***FILE* | Read additional patterns specifying filenames to extract or list from *FILE*. The lines of *FILE* are treated as if they had been non-option arguments to **cpio**. This option is used in copy-in mode. |
| **-f**, **--nonmatching** | Only copy files that do not match any of the given patterns. |
| **-F**, **--file=***archive* | Archive filename to use instead of standard input or output. To use a tape drive on another machine as the archive, use a filename that starts with '**HOSTNAME:**'. The [hostname](https://www.computerhope.com/jargon/h/hostname.htm) can be preceded by a [username](https://www.computerhope.com/jargon/u/username.htm) and an '**@**' to access the remote tape drive as that user, if you have [permission](https://www.computerhope.com/jargon/p/permissi.htm) to do so (typically an entry in that user's '**~/.rhosts**' file). |
| **--force-local** | With **-F**, **-I**, or **-O**, take the archive file name to be a local file even if it contains a colon, which would ordinarily indicate a remote host name. |
| **-H** *FORMAT*, **--format=***FORMAT* | Use archive format *FORMAT*. The valid formats are listed below; the same names are also recognized in all-[caps](https://www.computerhope.com/jargon/u/uppercase.htm). The default in copy-in mode is to automatically detect the archive format, and in copy-out mode is '**bin**'.  **bin**: The obsolete binary format.  **odc**: The old (POSIX .1) portable format.  **newc**: The new (SVR4) portable format, which supports file systems having more than 65536 [inodes](https://www.computerhope.com/jargon/i/inode.htm).  **crc**: The new (SVR4) portable format with a [checksum](https://www.computerhope.com/jargon/c/checksum.htm) added.  **tar**: The old tar format.  **ustar**: The POSIX .1 tar format. Also, recognizes GNU tar archives, which are similar but not identical.  **hpbin**: The obsolete binary format used by HPUX's cpio (which stores device files differently).  **hpodc**: The portable format used by HPUX's cpio (which stores device files differently). |
| **-i**, **--extract** | Run in copy-in mode. (see '[Copy-in mode](https://www.computerhope.com/unix/ucpio.htm#Copy-In-Mode)'). |
| **-I** *archive* | Archive filename to use instead of standard input. To use a tape drive on another machine as the archive, use a filename that starts with '**HOSTNAME:**'. The hostname can be preceded by a username and an '**@**' to access the remote tape drive as that user, if you have permission to do so (typically an entry in that user's '**~/.rhosts**' file). |
| **-k** | Ignored; for compatibility with other versions of cpio. |
| **-l**, **--link** | Link files instead of copying them, when possible. |
| **-L**, **--dereference** | Copy the file that a symbolic link points to, rather than the symbolic link itself. |
| **-m**, **--preserve-modification-time** | Retain previous file modification times when creating files. |
| **-M** *MESSAGE*, **--message=***MESSAGE* | Print *MESSAGE* when the end of a volume of the backup media (such as a tape or a [floppy disk](https://www.computerhope.com/jargon/f/floppydi.htm)) is reached, to prompt the user to insert a new volume. If *MESSAGE* contains the string '**%d**', it is replaced by the current volume number (starting at 1). |
| **-n**, **--numeric-uid-gid** | Show numeric UID and GID instead of translating them into names when using the '**--verbose**' option. |
| **--no-absolute-filenames** | Create all files relative to the current directory in copy-in mode, even if they have an absolute file name in the archive. |
| **--absolute-filenames** | This is the default: tell **cpio** not to strip leading file name components that contain '**..**' and leading slashes from file names in copy-in mode. |
| **--no-preserve-owner** | Do not change the ownership of the files; leave them owned by the user extracting them. This is the default for non-root users, so that users on [System V](https://www.computerhope.com/jargon/s/system-v.htm) don't inadvertently give away files. This option can be used in copy-in mode and copy-pass mode. |
| **-o**, **--create** | Run in copy-out mode. (see '[Copy-out mode](https://www.computerhope.com/unix/ucpio.htm#Copy-Out-Mode)'). |
| **-O** *archive* | Archive filename to use instead of standard output. To use a tape drive on another machine as the archive, use a filename that starts with '**HOSTNAME:**'. The hostname can be preceded by a username and an '**@**' to access the remote tape drive as that user, if you have permission to do so (typically an entry in that user's '**~/.rhosts**' file). |
| **--only-verify-crc** | Verify the CRC of each file in the archive, when reading a CRC format archive. Do not actually extract the files. |
| **-p**, **--pass-through** | Run in copy-pass mode. (see '[Copy-pass mode](https://www.computerhope.com/unix/ucpio.htm#Copy-Pass-Mode)'). |
| **--quiet** | Do not print the number of blocks copied. |
| **-r**, **--rename** | Interactively rename files. |
| **-R** [*user*][**:.**][*group*], **--owner** [*user*][**:.**][*group*] | Set the ownership of all files created to the specified user and/or group in copy-out and copy-pass modes. Either the user, the group, or both, must be present. If the group is omitted but the '**:**' or '**.**' separator is given, use the given user's login group. Only the [super-user](https://www.computerhope.com/jargon/r/root.htm) can change files' ownership. |
| **--rsh-command=***COMMAND* | Notifies **cpio** that is should use *COMMAND* to communicate with remote devices. |
| **-s**, **--swap-bytes** | Swap the bytes of each halfword (pair of bytes) in the files. This option can be used in copy-in mode. |
| **-S**, **--swap-halfwords** | Swap the halfwords of each word (4 bytes) in the files. This option may be used in copy-in mode. |
| **--sparse** | Write files with large blocks of zeros as sparse files. This option is used in copy-in and copy-pass modes. |
| **-t**, **--list** | Print a table of contents of the input. |
| **--to-stdout** | Extract files to standard output. This option may be used in copy-in mode. |
| **-u**, **--unconditional** | Replace all files, without asking whether to replace existing newer files with older files. |
| **-v**, **--verbose** | List the files processed, or with '**-t**', give an '**ls -l**' style table of contents listing. In a verbose table of contents of a **ustar**archive, user and group names in the archive that do not exist on the local system are replaced by the names that correspond locally to the numeric UID and GID stored in the archive. |
| **-V**, **--dot** | Print a '**.**' for each file processed. |
| **--version** | Print the cpio program version number and exit. |

cpio examples

When creating an archive, **cpio** takes the list of files to be processed from the standard input, and then sends the archive to the standard output, or to the device defined by the '**-F**' option. Usually **find** or [**ls**](https://www.computerhope.com/jargon/l/ls.htm) is used to provide this list to the standard input. In the following example you can see the possibilities for archiving the contents of a single directory:

```
% ls | cpio -ov > directory.cpio
```

The '**-o**' option creates the archive, and the '**-v**' option prints the names of the files archived as they are added. Notice that the options can be put together after a single '**-**' or can be placed separately on the command line. The '**>**' redirects the **cpio** output to the file '**directory.cpio**'.

If you wanted to archive an entire directory tree, the **find** command can provide the file list to **cpio**:

```
% find . -print -depth | cpio -ov > tree.cpio
```

This will take all the files in the current directory, the directories below and place them in the archive **tree.cpio**. Again the '**-o**' creates an archive, and the '**-v**' option shows you the name of the files as they are archived (see '[Copy-out mode](https://www.computerhope.com/unix/ucpio.htm#Copy-Out-Mode)'). Using the '**.**' in the find statement will give you more flexibility when doing restores, as it will save file names with a relative path via a hard-wired, [absolute path](https://www.computerhope.com/jargon/a/absopath.htm). The '**-depth**' option forces '**find**' to print of the entries in a directory before printing the directory itself. This limits the effects of restrictive directory permissions by printing the directory entries in a directory before the directory name itself.

Extracting an archive requires a bit more thought because **cpio** will not create directories by default. Another characteristic, is it will not overwrite existing files unless specified.

```
% cpio -iv < directory.cpio
```

This will retrieve the files archived in the file **directory.cpio** and place them in the present directory. The '**-i**' option extracts the archive and the '**-v**' shows the file names as they are extracted. If you are dealing with an archived directory tree, you need to use the '**-d**' option to create directories as necessary, something like:

```
% cpio -idv < tree.cpio
```

This will take the contents of the archive **tree.cpio** and extract it to the current directory. If you try to extract the files on top of files of the same name that already exist (and have the same or later modification time) **cpio** will not extract the file unless told to do so by the **-u** option (see '[Copy-in mode](https://www.computerhope.com/unix/ucpio.htm#Copy-In-Mode)').

In copy-pass mode, **cpio** copies files from one directory tree to another, combining the copy-out and copy-in steps without actually using an archive. It reads the list of files to copy from the standard input; the directory into which it will copy them is given as a non-option argument (see '[Copy-pass mode](https://www.computerhope.com/unix/ucpio.htm#Copy-Pass-Mode)').

```
% find . -depth -print0 | cpio --null -pvd new-dir
```

The example shows copying the files of the present directory, and sub-directories to a new directory called **new-dir**. Some new options are the '**-print0**' available with GNU find, combined with the '**--null**' option of **cpio**. These two options act together to send file names between **find** and **cpio**, even if special characters are embedded in the file names. Another is '**-p**', which tells **cpio** to pass the files it finds to the directory '**new-dir**'.

```
find . -print | cpio -ocv > /dev/fd0
```

Above, using the **find** command would list all files and directories and using the **cpio**command copy those files listed to the floppy drive.

```
find . -print | cpio -dumpv /home/users/hope
```

In the above example, the **find** command would list all files and subdirectories of the current directory, and [pipe](https://www.computerhope.com/jargon/p/pipe.htm) them to the **cpio** command, which copies those files to the **hope** user account.

```
cpio -icuvd < /dev/fd0
```

The above command would restore the files back from the floppy.

```
Syntax:

Example:
```

### CRON
CRON is a Linux system process that executes a program at a preset time. To use a [CRON script](https://searchdatacenter.techtarget.com/definition/CRON-script?int=off), admins must prepare a text file that describes the program and when they want CRON to execute it. Then, the crontab program loads the text file and executes the program at the specified time.

System Cron jobs exist as entries in the `/etc/crontab` file. Each job is described on a single line by defining a time interval, a user to run the command as, and the command to run. Cron can run any kind of script, command, or executable.

```bash
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /        cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /        cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
```

Below is the default system `crontab` file from Debian 9:

The first job in the Cron table is:

```bash
`17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly`.
```

This means at 17 minutes past each hour, change directory to `/`, the root of the filesystem. Then, as the `root` user, run the `run-parts` binary to execute all jobs in `/etc/cron.hourly`.

Time intervals are denoted by numbers and operators filled in place of each asterisk in a Cron job’s `crontab` line. From left to right, the asterisks represent:

- **Minutes** specified as a number from 0 to 59.
- **Hours** specified as numbers from 0 to 23.
- **Days of the month**, specified as numbers from 1 to 31.
- **Months** specified as numbers from 1 to 12.
- **Days of the week**, specified as numbers from 0 to 7, with Sunday represented as either/both 0 and 7.

### cURL
Admins use [cURL](https://www.rosehosting.com/blog/curl-command-examples/) to transfer a URL. It is useful for determining if an application can reach another service and how healthy the service is.

```
Syntax:

Example:
```

## D

### declare
The [declare command](https://www.tutorialspoint.com/unix_commands/declare.htm) states variables, gives them attributes or modifies the properties of variables.

### df
This command displays the amount of disk space available on the file system containing each file name argument. With no file name, the [df command](https://searchnetworking.techtarget.com/answer/What-Linux-command-is-used-to-display-hard-disk-space) shows the available space on all the currently mounted file systems.

his command displays the amount of disk space available on the file system containing each file name argument. With no file name, the [df command](https://searchnetworking.techtarget.com/answer/What-Linux-command-is-used-to-display-hard-disk-space) shows the available space on all the currently mounted file systems.

## E

### echo
Use echo to repeat a string variable to standard output.

### enable
The enable command stops or starts printers and classes.

### env
The env command runs a program in a modified environment or displays the current environment and its variables.

### eval
The eval command analyzes several arguments, concatenates them into a single command and reports on that argument's status.

### exec
This function replaces the parent process with any subsequently typed command. The [exec command](https://www.tldp.org/LDP/abs/html/x17974.html) treats its arguments as the specification of one or more subprocesses to execute.

### exit
The exit command terminates a script and returns a value to the parent script.

### expect
The [expect](https://askubuntu.com/questions/703754/how-to-do-more-with-an-expect-script-than-just-a-log-in) command talks to other interactive programs via a script and waits for a response, often from any string that matches a given pattern.

### export
The [export command](https://whatis.techtarget.com/definition/export) converts a file into a different format than its current format. Once a file is exported, it can be accessed by any application that uses the new format.

## F

**find**
The [find command](https://www.if-not-true-then-false.com/2010/linux-locate-command-find-files-and-directories-quickly-and-efficiently/) searches the directory tree to locate particular groups of files that meet specified conditions, including -name, -type, -exec, -size, -mtime and -user.

### for**, **while
The [for](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html) and [while](https://www.linuxtopia.org/online_books/bash_guide_for_beginners/sect_09_02.html) commands execute or loop items repeatedly as long as certain conditions are met.

### free
With the free command, admins can see the total amount of free and used physical memory and swap space in the system, as well as the buffers and cache used by the kernel.

## G

### **gawk** See AWK.

### grep
The [grep command](https://searchmicroservices.techtarget.com/definition/grep?int=off) searches files for a given character string or pattern and can replace the string with another. This is one method of searching for files within Linux.

### gzip
This is the [GNU Project's](https://www.gnu.org/software/gzip/) open source program for file compression that compresses webpages on the server end for decompression in the browser. This is popular for streaming media compression and can simultaneously concatenate and compress several streams.

## H

### history
The [history function](https://searchdatacenter.techtarget.com/tip/Mastering-the-Linux-history-command) shows all the commands used since the start of the current session.

### I

### ifconfig
The [iconfig](https://searchnetworking.techtarget.com/tip/Troubleshooting-with-the-ifconfig-command) command configures kernel-resident network interfaces at boot time. It is usually only needed when debugging or during system tuning.

### ifup
With [ifup](http://www.linux-tutorial.info/modules.php?name=ManPage&sec=8&manpage=ifup), admins can configure a network interface and enable a network connection.

### ifdown
The ifdown command shuts down a network interface and disables a network connection.

**iptables**The [iptables command](https://whatis.techtarget.com/definition/iptables) allows or blocks traffic on a Linux host and can prevent certain applications from receiving or transmitting a request.

### K

### kill

With [kill signals](https://searchdatacenter.techtarget.com/tip/The-civilized-way-to-use-Linux-kill-signals-to-shut-down-processes), admins can send a specific signal to a process. It is most often used to safely shut down processes or applications.

### L

### less
The less command lets an admin scroll through configuration and error log files, displaying text files one screen at a time with backward or forward navigation available.

### locate
The locate command reads one or more databases and writes file names to match certain output patterns.

### lft
The lft command determines connection routes and provides information to debug connections or find a box/system location. It also displays route packets and file types.

### ln
The [ln command](https://lowfatlinux.com/linux-link-files-ln.html) creates a new name for a file using hard linking, which allows multiple users to share one file.

### ls
The [ls command](https://searchdatacenter.techtarget.com/tip/Put-these-troubleshooting-tools-in-your-toolbox) lists files and directories within the current working directory, which allows admins to see when configuration files were last edited.

### lsof
Admins use lsof to list all the open files. They can add -u to find the number of open files by username.

### lsmod
The [lsmod command](https://linux.101hacks.com/unix/lsmod/) displays a module's status within the kernel, which helps troubleshoot server function issues.

### M

### man
The man command allows admins to format and display the user manual that's built into Linux distributions, which documents commands and other system aspects.

The man command allows admins to format and display the user manual that's built into Linux distributions, which documents commands and other system aspects.

### more
Similar to less, [more](https://www.lifewire.com/more-command-4041467) pages through text one screen at a time, but has limitations on file navigation.

### mount
This command [mounts file systems](https://whatis.techtarget.com/definition/mount) on servers. It also lists the current file systems and their mount locations, which is useful to locate a defunct drive or install a new one.

### mkdir
Linux mkdir generates a new directory with a name path.

### N

### neat
A [Gnome GUI tool](https://searchdatacenter.techtarget.com/tip/Unix-to-Linux-migration-Setting-up-a-network) that allows admins to specify the information needed to set up a network card.

### netconfig/netcfg
Admins can [use netconfig](https://docs.oracle.com/cd/E26502_01/html/E28988/gmglb.html) to configure a network, enable network products and display a series of screens that ask for configuration information.

### netstat
This command provides information and statistics about protocols in use and current TCP/IP network connections. It is a helpful forensic tool for figuring out which processes and programs are active on a computer and are involved in [network communications](http://www.faqs.org/docs/linux_network/x-087-2-iface.netstat.html).

### nslookup
A user can enter a host name and find the corresponding IP address with [nslookup](https://searchnetworking.techtarget.com/definition/nslookup?int=off). It can also help find the host name.

### O

### od
The od command dumps binary files in octal -- or hex/binary -- format to standard output.

### P

**passwd**
Admins use passwd to update a user's current password.

### ping
The ping command verifies that a particular IP address exists and can accept requests. It can test connectivity and determine response time, as well as ensure an operating user's host computer is working.

### ps
Admins [use ps](https://linoxide.com/how-tos/linux-ps-command-examples/) to report the statuses of current processes in a system.

### pwd
The [print working directory (pwd)](https://searchdatacenter.techtarget.com/answer/PATH-vs-pwd) command displays the name of the current working directory.

### R

### read
The read command interprets lines of text from standard input and assigns values of each field in the input line to shell variables for further processing.

### rsync
This [command syncs](https://searchdatacenter.techtarget.com/tip/Rsync-and-Amanda-Keeping-your-data-safe-with-open-source-backup) data from one disk or file to another across a network connection. It is similar to rcp, but has more options.

### S

### screen
The GNU [screen utility](https://searchdatacenter.techtarget.com/tip/Screen-The-terminal-baby-sitter-in-the-sysadmins-toolbox) is a terminal multiplexor where a user can use a single terminal window to run multiple terminal applications or windows.

### sdiff
Admins [use sdiff](https://www.howtoforge.com/linux-sdiff-command/) to compare two files and produce a side-by-side listing indicating lines that are dissimilar. The command then merges the files and outputs the results to the outfile.

### sed
The [sed utility](https://searchdatacenter.techtarget.com/tip/Search-and-replace-on-steroids-Do-more-with-these-sed-commands) is a stream editor that filters text in a pipeline, distinguishing it from other editors. It takes text input, performs operations on it and outputs the modified text. This command is typically used to extract part of a file using pattern matching or to substitute multiple occurrences of a string within a file.

### service
This command is the quickest way to start or [stop a service](https://searchdatacenter.techtarget.com/tip/Master-Linux-service-management-on-System-V-and-systemd), such as networking.

### shutdown
The [shutdown command](https://www.cyberciti.biz/tips/linux-shutdown-command-and-logfile.html) turns off the computer and can be combined with variables such as -h for halt after shutdown or -r for reboot after shutdown.

### slocate
Like locate, slocate, or secure locate, provides a way to index and quickly search for files, but it can also securely store file permissions and ownership to hide information from unauthorized users.

### Snort
Snort is an [open source network intrusion detection system](https://searchdatacenter.techtarget.com/news/919324/Nab-hackers-with-Snort-on-Linux) and packet sniffer that monitors network traffic. It looks at each packet to detect dangerous payloads or suspicious anomalies. Snort is based on libpcap.

### sort
This command sorts lines of text alphabetically or numerically according to the fields. Users can input multiple sort keys.

### sudo
The [sudo command](https://searchsecurity.techtarget.com/definition/sudo-superuser-do?int=off) lets a system admin give certain users the ability to run some -- or all -- commands at the root level and logs all the commands and arguments.

### SSH
SSH is a command interface for secure remote computer access and is used by network admins to remotely control servers.

## T

### tar
The [tar command](https://whatis.techtarget.com/definition/tar-Tape-ARchive?int=off) lets users create archives from a number of specified files or to extract files from a specific archive.

### tail
The [tail command](https://searchdatacenter.techtarget.com/tip/Easily-read-a-log-file-in-Linux-with-command-line-tools) displays the last few lines of the file. This is particularly helpful for troubleshooting code because admins don't often need all the possible logs to determine code errors.

### TOP
TOP is a [set of protocols](https://searchnetworking.techtarget.com/definition/Technical-Office-Protocol?int=off) for networks that performs distributed information processing and displays the tasks on the system that take up the most memory. TOP can sort tasks by CPU usage, memory usage and runtime.

### touch
Admins can create a blank file within Linux with the touch command.

### tr
This command translates or deletes characters from a text stream. It writes to a standard output, but it does not accept file names as arguments -- it only accepts input from standard input.

### traceroute
The [traceroute function](https://whatis.techtarget.com/definition/traceroute?int=off) determines and records a route through the internet between two computers and is useful for troubleshooting network/router issues. If the domain does not work or is not available, admins can use traceroute to track the IP.

## U

### uname
This function displays the current [operating system name](http://www.basicconfig.com/linux/uname_command) and can print system information.

### uniq
With uniq, admins can compare adjacent lines in a file and remove or identify any duplicate lines.

## V

### vi
The [vi environment](https://www.howtogeek.com/102468/a-beginners-guide-to-editing-text-files-with-vi/) is a text editor that allows a user to control the system with just the keyboard instead of both mouse selections and keystrokes.

**vmstat**
The [vmstat command](https://searchdatacenter.techtarget.com/tip/How-to-keep-an-eye-on-Linux-performance) snapshots everything in a system and reports information on such items as processes, memory, paging and CPU activity. This is a good method for admins to use to determine where issues/slowdown may occur in a system.

## W

### wget
This is a network utility that retrieves web files that support HTTP, HTTPS and FTP protocols. The [wget command](http://www.editcorp.com/Personal/Lars_Appel/wget/v1/wget_7.html) works non-interactively in the background when a user is logged off. It can create local versions of remote websites and recreate original site directories.

### while
See for.

### whoami
The whoami command prints or writes the user login associated with the current user ID to the standard output.

## X

### xargs
Admins [use xargs](https://shapeshed.com/unix-xargs/#what-is-the-xargs-command-in-unix) to read, build and execute arguments from standard input. Each input is separated by blanks.

- [1](https://searchdatacenter.techtarget.com/tutorial/77-Linux-commands-and-utilities-youll-actually-use#1)
- [Jessica Lulka](https://www.techtarget.com/contributor/Jessica-Lulka) asks:What Linux prompts do you use the most?[Join the Discussion](https://searchdatacenter.techtarget.com/tutorial/77-Linux-commands-and-utilities-youll-actually-use#commenting)
- [1](https://searchdatacenter.techtarget.com/tutorial/77-Linux-commands-and-utilities-youll-actually-use#1)
- [Jessica Lulka](https://www.techtarget.com/contributor/Jessica-Lulka) asks:What Linux prompts do you use the most?[Join the Discussion](https://searchdatacenter.techtarget.com/tutorial/77-Linux-commands-and-utilities-youll-actually-use#commenting)
- 1
- 2
