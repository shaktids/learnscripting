---
title: "What is .gz file in Linux and how to compress & decompress .gz file"
description: "Gzip or .gz is used to compress a file in order to reduce disk space, it is quite popular in Linux and UNIX operating systems for this reason. Gzip has…"
lang: bash
categories: ["Linux"]
author: "Shakti Das"
pubDate: 2019-01-09T06:47:31Z
legacy: true
wpId: 1303
---

Gzip or .gz is used to compress a file in order to reduce disk space, it is quite popular in Linux and UNIX operating systems for this reason. Gzip has been around since [May 1996](https://www.ietf.org/rfc/rfc1952.txt) and is still widely used today.

The below examples showing the process of compressing gzip and unzipping .The compression technique can help you save a lot of memory by compressing .

## Prerequisite

- Any Linux environment should be installed in your system.
- System should have the gzip package installed, this is usually already installed by default, however you can install it now if required.
- Find the correct Linux version installed in your system.The command are below mentioned for Red hot Linux or Debian.

**RHEL**:

```
yum install gzip
```

**Debian:**

```
apt-get install gzip
```

## Example Gzip Commands

**1. Compress a single file**

```
gzip file.txt
```

This will compress file.txt and create file.txt.gz, note that this will remove the original file.txt file.gzip file.txt

**2. Compress multiple files at once**

```
gzip file1.txt file2.txt file3.txt
```

This will compress all files specified in the command, note again that this will remove the original files specified by turning file1.txt, file2.txt and file3.txt into file1.txt.gz, file2.txt.gz and file3.txt.gzgzip file1.txt file2.txt file3.txt To instead compress all files within a directory, see example 8 below.

**3. Compress a single file and keep the original**

```
gzip -c file.txt > file.txt.gz
```

You can instead keep the original file and create a compressed copy.gzip -c file.txt > file.txt.gz The -c flag outputs the compressed copy of file.txt to stdout, this is then sent to file.txt.gz, keeping the original file.txt file in place. Newer versions of gzip may also have -k or –keep available, which could be used instead with “gzip -k file.txt”.

**4. Compress all files recursively**

All files within the directory and all sub directories can be compressed recursively with the -r flag

```
[root@centos test]# ls -laR
 .:
 drwxr-xr-x.  2 root root   24 Jul 28 18:05 example
 -rw-r--r--.  1 root root    8 Jul 28 17:09 file1.txt
 -rw-r--r--.  1 root root    3 Jul 28 17:54 file2.txt
 -rw-r--r--.  1 root root    5 Jul 28 17:54 file3.txt
 ./example:
 -rw-r--r--. 1 root root  5 Jul 28 18:00 example.txt
 [root@centos test]# gzip -r *
 [root@centos test]# ls -laR
 .:
 drwxr-xr-x.  2 root root   27 Jul 28 18:07 example
 -rw-r--r--.  1 root root   38 Jul 28 17:09 file1.txt.gz
 -rw-r--r--.  1 root root   33 Jul 28 17:54 file2.txt.gz
 -rw-r--r--.  1 root root   35 Jul 28 17:54 file3.txt.gz
 ./example:
 -rw-r--r--. 1 root root 37 Jul 28 18:00 example.txt.gz
```

In the above example there are 3 .txt files in the test directory which is our current working directory, there is also an example sub directory which contains example.txt. Upon running gzip with the -r flag over everything, all files were recursively compressed. This can be reversed by running “gzip -dr \*”, where -d is used to decompress and -r performs this on all of the files recursively.

**5. Decompress a gzip compressed file**
To reverse the compression process and get the original file back that you have compressed, you can use the gzip command itself or gunzip which is also part of the gzip package.

```

gzip -d file.txt.gz

OR

gunzip file.txt.gz
```

Both of these commands will produce the same result, decompressing file.txt.gz to file.txt, removing the compressed file.txt.gz file.

Similar to example 3, it is possible to decompress a file and keep the original .gz file as below.

```

gunzip -c file.txt.gz > file.txt
```

As mentioned in step 4, -d can be combined with -r to decompress all files recursively.

**6. List compression information**
With the -l or --list flag we can see useful information regarding a compressed .gz file such as the compressed and uncompressed size of the file as well as the compression ratio, which shows us how much space our compression is saving.

```
[root@centos ~]# gzip -l linux-3.18.19.tar.gz          compressed        uncompressed  ratio uncompressed_name           126117045           580761600  78.3% linux-3.18.19.tar

[root@centos ~]
```

# ls -lah -rw-r--r--. 1 root root 554M Jul 28 17:24 linux-3.18.19.tar -rw-r--r--. 1 root root 121M Jul 28 17:25 linux-3.18.19.tar.gz . In this example, a gzipped copy of the Linux kernel has compressed to 78.3% of its original size, taking up 121MB of space rather than 554MB.

**7. Adjust compression level**
The level of compression applied to a file using gzip can be specified as a value between 1 (less compression) and 9 (best compression). Using option 1 will complete faster, but space saved from the compression will not be optimal. Using option 9 will take longer to complete, however you will have the largest amount of space saved.

The below example compares the differences between -1 and -9, as shown while -1 finishes much faster it compresses around 5% less (approximately 30mb more space required).

```
[root@centos ~]# time gzip -1 linux-3.18.19.tar real    0m13.602s user    0m12.908s sys     0m0.662s

[root@mirror1 ~]
```

# gzip -l linux-3.18.19.tar.gz compressed uncompressed ratio uncompressed\_name 156001021 580761600 73.1% linux-3.18.19.tar

[root@centos ~]

# time gzip -9 linux-3.18.19.tar
real 0m58.129s
user 0m57.193s
sys 0m0.735s

# gzip -l linux-3.18.19.tar.gz
compressed uncompressed ratio uncompressed\_name
125064095 580761600 78.5% linux-3.18.19.tar

-1 can also be specified with the flag --fast, while option -9 can also be specified with the flag --best. By default gzip uses a compression level of -6, which is slightly biased towards higher compression at the expense of speed. When selecting a value between 1 and 9 it is important to consider what is more important to you, the amount of space saved or the amount of time spent compressing, the default -6 option provides a fair trade off.
**8. Compress a directory**
With the help of the tar command, we can create a tar file of a whole directory and gzip the result. We can perform the whole lot in one step, as the tar command allows us to specify a compression method to use. This example creates a compressed etc.tar.gz file of the entire /etc/ directory. The tar flags are as follows, ‘c’ creates a new tar archive, ‘z’ specifies that we want to compress with gzip, ‘v’ provides verbose information, and ‘f’ specifies the file to create. The resulting etc.tar.gz file contains all files within /etc/ compressed using gzip.

```
tar czvf etc.tar.gz /etc/
```

**9. Integrity test**
The -t or --test flag can be used to check the integrity of a compressed file.

On a normal file, the result will be listed as OK, shown below.

```
[root@centos test]# gzip -tv file1.txt.gz
file1.txt.gz:    OK
```

I have now manually modified this file with a text editor and added a random value, essentially introducing corruption and it is now no longer valid.

```
[root@centos test]# gzip -tv file1.txt.gz
file1.txt.gz:
gzip: file1.txt.gz: invalid compressed data--crc error
gzip: file1.txt.gz: invalid compressed data--length error
```

The compressed .gz file makes use of cyclic redundancy check (CRC) in order to detect errors. The CRC value can be viewed by running gzip with the -l and -v flags, as shown below.

```
[root@centos test]# gzip -lv file1.txt.gz
method  crc     date  time           compressed        uncompressed  ratio uncompressed_name
defla 08db5c50 Jul 28 18:15                  40           167772160 100.0% file1.txt
```

**10. Concatenate multiple files**
Multiple files can be concatenated into a single .gz file.

```
gzip -c file1.txt > files.gz
gzip -c file2.txt >> files.gz
```

The files.gz now contains the contents of both file1.txt and file2.txt, if you decompress files.gz you will get a file named ‘files’ which contains the content of both .txt files. The output is similar to running ‘cat file1.txt file2.txt’. If instead you want to create a single file that contains multiple files you can use the tar command which supports gzip compression, as covered above in example 8.
**11. Additional commands included with gzip**
The gzip package provides some very useful commands for working with compressed files, such as zcat, zgrep and zless/zmore.

As you can probably tell by the names of the commands, these are essentially the cat, grep, and less/more commands, however they work directly on compressed data. This means that you can easily view or search the contents of a compressed file without having to decompress it and then view or search it in a second step.

```
[root@centos test]# zcat test.txt.gz
test
example
text
```

[root@centos test]

# zgrep exa test.txt.gz
example

This is especially useful when searching through or reviewing log files which have been compressed during log rotation.
