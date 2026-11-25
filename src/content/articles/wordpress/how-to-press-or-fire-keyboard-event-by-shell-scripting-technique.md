---
title: "How to Press or Fire Keyboard Event by Shell Scripting Technique"
description: "In most of the programming language the key press events are not comes as inbuilt feathers.At that point of time we need support of the shell scripting…"
lang: bash
categories: ["Shell Scripting", "VB Scripting"]
author: "Shakti Das"
pubDate: 2018-09-25T03:50:49Z
legacy: true
wpId: 151
---

In most of the programming language the key press events are not comes as inbuilt feathers.At that point of time we need support of the shell scripting technique.In this post you will find the use and the different shortcut key available for this .

**For VB Shell Scripting Scripting we need to create the code using set command as below**

'Set WshShell = WScript.CreateObject("WScript.Shell")
'WshShell.Run "%windir%\notepad"
set objSendKey=CreateObject("WScript.shell")
set objSetFocus = Window("nativeclass:=Notepad","index:=0")
SystemUtil.Run "notepad.exe", "", "", "
wait 2
objSetFocus.Move 10,10
wait 1
objSetFocus.Click
[smartads]

#### 1. How do I send an enter keystroke using QTP?

You could use the ASCII character for a carriage return Chr(13)

objSendKey.SendKeys(Chr(13))

(For more ASCII codes to use in QTP check out :QTP ASCII CHR() CODE CHART )

or use the Tilde character:
objSendKey.SendKeys(“~”)

Both will emulate an ‘Enter’ key.

#### 2. How do I send a space?
To send a space, send the string ” “

3. How do I to send multiple keystrokes at one time using QTP’s VBscript?

To send multiple keys you can create compound string arguments. For example the following will hold down the Ctrl key, press the H key for the ‘Replace’ and type joe into the Replace window’s find textbox:
objSendKey.SendKeys("^(h)joe"

)

#### 4. How do I send a SHIFT, CTRL or Alt keystroke?

The special character for the Shift key in vbscript is the + sign.
For example to hold down the shift key and type a string all in capital letters try this:
objSendKey.SendKeys("+(joecolantonio)")

The special character for the Ctrl key in vbscript is the ^ sign and the character for the Alt key in vbscript is the % sign
Keystroke Equivalent
Alt %
Ctrl ^
Shift +

#### 5. How do a send a right mouse click?

Try sending a a shift F10:
objSendKey.

SendKeys(“+{F10}”);

#### 6. Are there any Sendkeys best practices?

There are a few I can think of :

Always move the application to a known start position.
Always set focus to the object you want to interact with before using SendKeys.
For synchronization issues use the .exist or wait functionality often in your script.

For Example:
objSetFocus.Move 10,10
wait 1
objSetFocus.Click

#### 7. How do I send parenthesis using SendKeys?

Parenthesis are special characters in QTP so one way to do this is to use a combination of the shift key with the numeric nine and zero keys:
objSendKey.SendKeys("+9")
objSendKey.SendKeys("joe colantonio")
objSendKey.SendKeys("+0")

#### 8. My SendKeys is not working when I try to send a multiple values.What should I do?

If QTP’s SendKeys is not performing as expected try sending each keystroke a separate line.

#### 9. What is the QTPs equivalent for shell available in the market?

In QTP you can use the Run Method which can be used to run a file or an application. For example to start notepad:
SystemUtil.Run "notepad.exe", "", "", ""

#### 10. How to do a select a checkbox or a row in an object?

If the object like a checkbox has focus sending a blank space should select it:
objSendKey.SendKeys(" ")

#### 11. How do I repeat a keystroke multiple times?

This only works for singe keystrokes but if you wanted to type a letter five times you could use this shortcut:
objSendKey.SendKeys("{J 5}")

#### 12. What is VBScript’s equivalent for keystroke :

These are the short code for the equivalent keystroke available for the particular key.
Keystroke Equivalent
Alt %
Backspace {BACKSPACE}
Break {BREAK}
Caps Lock {CAPSLOCK}
Ctrl ^
Delete {DELETE}
Down Arrow {DOWN}
End {END}
Esc {ESC}
Help {HELP}
Home {HOME}
Insert {INSERT}
Left Arrow {LEFT}
Num Lock {NUMLOCK}
Page Down {PGDN}
Page Up {PGUP}
Print Screen {PRTSC}
Right Arrow {RIGHT}
Scroll Lock {SCROLLOCK}
Shift +
Tab {TAB}
UP Arrow {UP}
F1 {F1}
F2 {F2}
F3 {F3}
F4 {F4}
F5 {F5}
F6 {F6}
F7 {F7}
F8 {F8}
F9 {F9}
F10 {F10}
F11 {F11}
F12 {F12}

#### 13. What are the QTP VBScript’s string constants for non-visible characters in strings?

Constant Value Description
VbCr Chr(13) Carriage return
VbCrLf Chr(13) & Chr(10) Carriage return and a Linefeed
VbLf Chr(10) Line Feed
VbNewLine Chr(13) & Chr(10) New Line
VbTab Chr(9) Horizontal tab

#### 14. I don’t see the action I need to perform in the chart above – what should I do?

Try the Device Replay method instead – check out the Device Replay chart (QTP DEVICE REAPLY CODE CHART )

#### 15. I’m using C# not QTP how do I start an application

Use Process() for example:
using System;
using System.Diagnostics;
using System.Windows.Forms;
Process myProcess = new Process():
myProcess.StartInfo.FileName = "cmd";
myProcess.Start();

#### 16. In CSharp what are the SendKeys methods?

Flush() – processes all Window messages in the queue

Send() – this sends keystrokes to an app

SendWait() – Sends keystrokes to an app and waits for the keystrokes to complete.

More Info:

If you found this helpful you might want to also check out my post 3 ways to use keyboard input in QuickTest Professional: Type, SendKeys and Device Replay.

Bibliomaniacs:

And as always for my fellow bibliomaniacs who may want to dive deeper into SendKeys , I would also recommend these two books:

1. VBScript Programmer’s Reference. (Sendkey info starts on page 338)

2. A Tester’s Guide to .NET Programming (Expert’s Voice) – This book is for the automation imagineer who may want to create a simple custom GUI sendkeys app (check out page 173 of this book)
