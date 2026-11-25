---
title: "PowerShell for Windows users: your first five commands"
description: Open the terminal without fear and get useful answers from Windows in seconds.
lang: powershell
pubDate: 2026-11-16
---

PowerShell is built into Windows. Press the Windows key, type `PowerShell` (or `Terminal`), and press Enter. Here are five commands to start with.

PowerShell commands follow a **Verb-Noun** pattern: `Get-Something`, `Set-Something`. Once you notice that, you can often guess a command's name.

## 1. Get-Location: where am I?

```powershell
Get-Location
```

This shows the folder you're in, for example `C:\Users\Sam`.

## 2. Get-ChildItem: what's here?

```powershell
Get-ChildItem
```

This lists the files and folders where you are. The short form `ls` works too.

## 3. Set-Location: move around

```powershell
Set-Location Documents
Set-Location ..
```

The first line moves into Documents, and the second moves back up one level. The short form is `cd`.

## 4. Get-Help: ask PowerShell

```powershell
Get-Help Get-ChildItem -Examples
```

This shows real examples for any command. It's your built-in teacher.

## 5. Get-Process: what's running?

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

<div class="callout plain">
<p class="callout-title">In plain English</p>

Get every running program, sort them by how much CPU they've used (biggest first), and show only the top five. The `|` symbol, called a pipe, passes the results of one command into the next.

</div>

The pipe is PowerShell's superpower. Small commands snap together like LEGO.

<div class="callout warn">
<p class="callout-title">"Running scripts is disabled on this system"?</p>

Windows blocks `.ps1` script files by default. To allow scripts that you wrote yourself, run this once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

</div>

<div class="callout try">
<p class="callout-title">Try it yourself</p>

List only the `.txt` files in your Documents folder with `Get-ChildItem ~\Documents -Filter *.txt`.

</div>
