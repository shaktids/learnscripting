---
title: "Adding SSH Keys to the Linux Host"
description: "Resolving the warning message There are three methods to remove this error. Please keep in mind that the modification to fix this needs to be performed on…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-05-11T15:51:22
legacy: true
wpId: 2300
draft: true
---

## Resolving the warning message

There are three methods to remove this error. Please keep in mind that the modification to fix this needs to be performed on the client side, so if you are getting this connecting from home/work you must update that specific computer.

### Method One — Generate a new host key (MAC or Linux)

If you have connected to a host in the past, the old host key is stored in your computer's /user/.ssh/known\_hosts file. If the key has been updated on the server, you must now delete the old key on your computer.

Change HOSTNAME to the host you're connecting to, such as **example.com**

```
[local]$ ssh-keygen -R HOSTNAME
```

The -R option removes the old key related to a specific hostname.

- <https://linux.die.net/man/1/ssh-keygen>

You can now connect via SSH to store a new key.

### Method Two — Deleting your known\_hosts file

If you log in to other servers, do not delete the known\_hosts file, or you’ll have no way of knowing if your SSH keys have changed.

Delete your entire known\_hosts file (on your local computer) if you have several hosts that need to be updated. On first log in, it confirms the new key.

- **On a Mac or Linux machine** – the known\_hosts file is located in the .ssh/known\_hosts directory. You can simply run this command in a terminal to delete the known\_host file:

```
[local]$ rm .ssh/known_hosts
```

- **On a Windows machine using [PuTTY](https://help.dreamhost.com/hc/en-us/articles/215464538-How-do-I-configure-PuTTY-)** – you must access the registry to remove the known\_hosts:

1. Open up ‘regedit.exe’ by doing a search.
2. Navigate to HKEY\_CURRENT\_USER\Software\SimonTatham\PuTTY\SshHostKeys
3. Delete all keys in there or delete the individual host key.

### Method Three — Edit the known\_hosts file

Edit the known\_hosts file. In the above case, open the file /home/username/.ssh/known\_hosts in the preferred text editor, and then remove the problem line. Make sure to change username to your Shell user.

- This is similar to method two but rather than deleting the entire known\_hosts file, you delete the specific host line in the file instead.
- The warning message lists the line number; it can be found after the file name in the error. In the above error message, the line number is 10,278. If you are on a Mac or Linux machine and if you are [using the "vi" editor](https://help.dreamhost.com/hc/en-us/articles/115006413028-Creating-and-editing-a-file-via-SSH), you can simply type the following command to jump to that line:

```
[local]$ vim +10278
```

The editor opens to that specific line. Click the ‘d’ key twice to delete that line, and then enter the following to save:

```
[local]$ :x
```

View the following article for further details on how to use vim.

- [Creating and editing a file via SSH](https://help.dreamhost.com/hc/en-us/articles/115006413028-Creating-and-editing-a-file-via-SSH)

On a Windows machine using [PuTTY](https://help.dreamhost.com/hc/en-us/articles/215464538-How-do-I-configure-PuTTY-), navigate to the Registry folder as shown in method two above. In that directory, a list of hostnames appears. Right click on the one you need to remove, and then select ‘Delete’.
