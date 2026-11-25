---
title: "Root Login in Ubuntu Desktop 16.04"
description: "The root Account in Ubuntu is disabled by default because his password is not set. But if you’d like to use root Account by some reason, it’s possible to…"
lang: bash
categories: ["Linux"]
author: "Shakti Das"
pubDate: 2017-01-22T07:30:21Z
legacy: true
wpId: 61
---

|  |  |
| --- | --- |
|  | The root Account in Ubuntu is disabled by default because his password is not set. But if you’d like to use root Account by some reason, it’s possible to use like follows. |
| [1] | The user account added during installation is set an administrative account with Sudo, so it’s easy to get root account’s shell like follows. |

|  |
| --- |
| xerus@dlp:~$ [sudo](https://www.server-world.info/en/command/html/sudo.html) -s  [sudo] password for xerus:  # own password  root@dlp:~#  # switched |

|
 [2] |
 Or it’s possible to switch to root account with su command to set root account’s password. |

|
 xerus@dlp:~$ [sudo](https://www.server-world.info/en/command/html/sudo.html) [passwd](https://www.server-world.info/en/command/html/passwd.html) root  [sudo] password for xerus:  # own password  Enter new UNIX password:  # set root password  Retype new UNIX password:  # confirm  passwd: password updated successfully  xerus@dlp:~$  [su](https://www.server-world.info/en/command/html/su.html) –  Password:  # input root password  root@dlp:~#  # switched |

|
 \* |
 The examples on this site shows as a root account. If you use Sudo, add “sudo” on the head of commands. It had better to limit user if you enable root account.  For using by Sudo, it’s possible to limit to prohibit shells in sudoers config, [refer to details about Sudo Settings](https://www.server-world.info/en/note?os=Ubuntu_16.04&p=initial_conf&f=7). |

|
 [3] |
 For limit to do su command, set like follows. |

|
 root@dlp:~# [vi](https://www.server-world.info/en/command/html/vi.html) /etc/pam.d/su  # line 15: uncomment and add a group which is allow to do su command  auth   required   pam\_wheel.so  group=adm |
