---
title: What does chmod +x actually do?
description: Why your Bash script says "Permission denied", and the one-line fix.
lang: bash
pubDate: 2026-11-20
---

You wrote your first Bash script, typed `./hello.sh`, and got this:

```text
bash: ./hello.sh: Permission denied
```

Nothing is broken. Linux and macOS just don't let a file run as a program unless you say so.

## Permissions in one minute

Every file has three permissions: **read** (r), **write** (w) and **execute** (x). A new text file can be read and written, but not executed. You can see them with `ls -l`:

```text
-rw-r--r--  1 sam  staff  42 Nov 20 10:00 hello.sh
```

No `x` anywhere, so it can't run.

## The fix

```bash
chmod +x hello.sh
```

`chmod` means **ch**ange **mod**e, and `+x` means "add execute permission". Check again:

```text
-rwxr-xr-x  1 sam  staff  42 Nov 20 10:00 hello.sh
```

Now `./hello.sh` works.

## Don't forget the first line

For `./hello.sh` to work, the script should start with a **shebang** line that says which program runs it:

```bash
#!/usr/bin/env bash
echo "Hello from Bash!"
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

`#!/usr/bin/env bash` means "run this file with Bash". `chmod +x` means "this file is allowed to run". You need both.

</div>

You can always skip both and run `bash hello.sh` instead. That works without the execute permission.

<div class="callout try">
<p class="callout-title">Try it yourself</p>

Create `hello.sh` with the two lines above, try `./hello.sh`, see the error, fix it with `chmod +x`, and run it again.

</div>
