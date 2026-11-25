---
title: "VBScript in Internet Explorer"
description: "VBScript in Internet Explorer Here are simple steps to turn on or turn off VBScript in your Internet Explorer:  Follow Tools Internet Options from the…"
lang: other
categories: ["VB Scripting"]
author: "Shakti Das"
pubDate: 2018-04-25T06:01:20Z
legacy: true
wpId: 76
---

VBScript in Internet Explorer
Here are simple steps to turn on or turn off VBScript in your Internet Explorer:
 Follow Tools -> Internet Options from the menu
 Select Security tab from the dialog box
 Click the Custom Level button
 Scroll down till you find Scripting option
 Select Enable radio button under Active scripting
 Finally click OK and come out
To disable VBScript support in your Internet Explorer, you need to select Disable radio button under Active scripting.
3. VBScript– Enabling in Browsers
VBScript
15
VBScript Placement in HTML File
There is a flexibility given to include VBScript code anywhere in an HTML document. But the most preferred way to include VBScript in your HTML file is as follows:
 Script in &lt;head>...&lt;/head> section.
 Script in &lt;body>...&lt;/body> section.
 Script in &lt;body>...&lt;/body> and &lt;head>...&lt;/head> sections.
 Script in an external file and then include in &lt;head>...&lt;/head> section.
In the following section, we will see how we can put VBScript in different ways:
VBScript in &lt;head>...&lt;/head> section
If you want to have a script run on some event, such as when a user clicks somewhere, then you will place that script in the head as follows:
&lt;html>
&lt;head>
&lt;script type="text/Vbscript">
&lt;!--
Function sayHello()
Msgbox("Hello World")
End Function
//-->
&lt;/script>
&lt;/head>
&lt;body>
&lt;input type="button" onclick="sayHello()" value="Say Hello" />
&lt;/body>
&lt;/html> 4. VBScript– Placements
VBScript
16
It will produce the following result: A button with the name SayHello. Upon clicking on the Button, the message box is displayed to the user with the message "Hello World".
VBScript in &lt;body>...&lt;/body> section
If you need a script to run as the page loads so that the script generates content in the page, the script goes in the &lt;body> portion of the document. In this case, you would not have any function defined using VBScript:
&lt;html>
&lt;head>
&lt;/head>
&lt;body>
&lt;script type="text/vbscript">
&lt;!--
document.write("Hello World")
//-->
&lt;/script>
&lt;p>This is web page body &lt;/p>
&lt;/body>
&lt;/html>
It will produce the following result:
Hello World
This is web page body
VBScript in &lt;body> and &lt;head> Sections
You can put your VBScript code in &lt;head> and &lt;body> section altogether as follows:
&lt;html>
&lt;head>
&lt;script type="text/vbscript">
&lt;!--
Function sayHello()
VBScript
17
msgbox("Hello World")
End Function
//-->
&lt;/script>
&lt;/head>
&lt;body>
&lt;script type="text/vbscript">
&lt;!--
document.write("Hello World")
//-->
&lt;/script>
&lt;input type="button" onclick="sayHello()" value="Say Hello" />
&lt;/body>
&lt;/html>
It will produce the following result: Hello World message with a 'Say Hello' button. Upon Clicking on the button a message box with a message "Hello World" is displayed to the user.
VBScript in External File
As you begin to work more extensively with VBScript, you will likely find that there are cases, where you are reusing identical VBScript code on multiple pages of a site. You are not restricted to be maintaining identical code in multiple HTML files.
The script tag provides a mechanism to allow you to store VBScript in an external file and then include it into your HTML files. Here is an example to show how you can include an external VBScript file in your HTML code using script tag and its src attribute:
&lt;html>
&lt;head>
&lt;script type="text/vbscript" src="filename.vbs" >&lt;/script>
&lt;/head>
&lt;body>
.......
&lt;/body>
VBScript
18
&lt;/html>
To use VBScript from an external file source, you need to write your all VBScript source code in a simple text file with extension ".vbs" and then include that file as shown above. For example, you can keep the following content in filename.vbs file and then you can use sayHello function in your HTML file after including filename.vbs file.
Function sayHello()
Msgbox "Hello World"
End Function
