---
title: "HTML Forms"
description: "HTML/Web form is an HTML element which takes the user input in text filed, textarea and other such input filelds. This data can be validated on the client…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-06-07T17:13:18Z
legacy: true
wpId: 2546
draft: true
---

HTML/Web form is an HTML element which takes the user input in text filed, textarea and other such input filelds. This data can be validated on the client browser using the JavaScript. After validation of data when user clicks on the "Submit" button form data is sent to the server for further processing.

HTML Form is used for development of dynamic web applications where user enters the input and based on the user input server sends response to the client. If you are learning web application development then you must learn to use HTML Form.

## HTML From Syntax:

```
<form action="server url" method="get|post">
  //input controls e.g. textfield, textarea, radiobutton, button
</form>
```

## HTML Form Tags:

| Tag | Description |
| --- | --- |
| &lt;form> | It defines an HTML form to enter inputs by the used side. |
| &lt;input> | It defines an input control. |
| &lt;textarea> | It defines a multi-line input control. |
| &lt;label> | It defines a label for an input element. |
| &lt;fieldset> | It groups the related element in a form. |
| &lt;legend> | It defines a caption for a &lt;fieldset> element. |
| &lt;select> | It defines a drop-down list. |
| &lt;optgroup> | It defines a group of related options in a drop-down list. |
| &lt;option> | It defines an option in a drop-down list. |
| &lt;button> | It defines a clickable button. |

## The &lt;form> Element:

The HTML `<form>` element is used to create an HTML form for user input:

## Syntax:

```
<form>
//Form elements
</form>
```

The `<form>` element is a container for different types of input elements, such as: text fields, checkboxes, radio buttons, submit buttons, etc.

## The HTML &lt;input> Element:

The HTML &lt;input> element is fundamental form element. It is used to create form fields, to take input from user.

The available types are as follows:

|  |  |
| --- | --- |
| **Type** | **Description** |
| button | A push button with no default behavior displaying the value of the value attribute, empty by default. |
| checkbox | A check box allowing single values to be selected/deselected. |
| color | A control for specifying a color; opening a color picker when active in supporting browsers. |
| date | A control for entering a date (year, month, and day, with no time). Opens a date picker or numeric wheels for year, month, day when active in supporting browsers. |
| datetime-local | A control for entering a date and time, with no time zone. Opens a date picker or numeric wheels for date- and time-components when active in supporting browsers. |
| file | A control that lets the user select a file. Use the accept attribute to define the types of files that the control can select. |
| email | A field for editing an email address. Looks like a text input, but has validation parameters and relevant keyboard in supporting browsers and devices with dynamic keyboards. |
| url | A field for entering a URL. Looks like a `text` input, but has validation parameters and relevant keyboard in supporting browsers and devices with dynamic keyboards. |
| hidden | A control that is not displayed but whose value is submitted to the server. There is an example in the next column, but it's hidden! |
| image | A graphical submit button. Displays an image defined by the src attribute. The alt attribute displays if the image srcis missing. |
| month | A control for entering a month and year, with no time zone. |
| number | A control for entering a number. Displays a spinner and adds default validation when supported. Displays a numeric keypad in some devices with dynamic keypads. |
| password | A single-line text field whose value is obscured. Will alert user if site is not secure. |
| radio | A radio button, allowing a single value to be selected out of multiple choices with the same name value. |
| range | A control for entering a number whose exact value is not important. Displays as a range widget defaulting to the middle value. Used in conjunction [min](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmin) and [max](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#htmlattrdefmax) to define the range of acceptable values. |
| reset | A button that resets the contents of the form to default values. Not recommended. |
| search | A single-line text field for entering search strings. Line-breaks are automatically removed from the input value. May include a delete icon in supporting browsers that can be used to clear the field. Displays a search icon instead of enter key on some devices with dynamic keypads. |
| submit | A button that submits the form. |
| text | The default value. A single-line text field. Line-breaks are automatically removed from the input value. |
| time | A control for entering a time value with no time zone. |

## HTML TextField Control:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Design</title>
</head>
<body>
    <form>
        First Name: <input type="text" name="fname"/> <br/>
        Last Name:  <input type="text" name="lname"/> <br/>
     </form>
</body>
</html>
```

## Output:

## TextField with labels:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Design</title>
</head>
<body>
    <form>
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname">
      </form>
</body>
</html>
```

## Output:

## The &lt;label> Element:

The &lt;label> tag defines a label for many form elements.

The &lt;label> element is useful for screen-reader users, because the screen-reader will read out loud the label when the user focus on the input element.

The &lt;label>element also help users who have difficulty clicking on very small regions (such as radio buttons or checkboxes) - because when the user clicks the text within the &lt;label> element, it toggles the radio button/checkbox.

The for attribute of the &lt;label> tag should be equal to the id  attribute of the &lt;input> element to bind them together.

## Input Type Submit:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Design</title>
</head>
<body>
    <form action="/action_page.php">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="James"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Bond"><br><br>
        <input type="submit" value="Submit">
      </form>
</body>
</html>
```

## Output:

## HTML Radio Button:

In HTML, a **radio button** is used to select one of many given choices. Radio buttons are shown in *radio groups* to show a set of related options, only one of which can be selected.

## Example of Radio button:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Radio Button</title>
</head>
<body>
    <form>
        <input type="radio" id="male" name="gender" value="male">
        <label for="male">Male</label><br>
        <input type="radio" id="female" name="gender" value="female">
        <label for="female">Female</label><br>
        <input type="radio" id="other" name="gender" value="other">
        <label for="other">Other</label>
      </form>

</body>
</html>
```

## Output:

## Checkboxes:

A Checkbox, selection box, or tick box is a small interactive box that can be toggled by the user to indicate an affirmative or negative choice. It is frequently found in HTML input forms, dialog boxes, and in the GUIs of applications and operating systems.

When clicked a checked mark (✓) appears inside the box, to indicate an affirmative choice (yes). When clicked again, the check mark disappears, indicating a negative choice (no).

Check boxes are used when more than one option may need to be checked or as an easy way to enable or disable a setting in a software program. Checking the box *enables* that setting, and unchecking *disables* it.

## Example of Checkboxes:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkboxes</title>
</head>

<body>
    <h2>Checkboxes</h2>
    <p>The <strong>input type="checkbox"</strong> defines a checkbox:</p>

    <form action="/action_page.php">
        <input type="checkbox" id="drinks1" name="drinks1" value="Tea">
        <label for="drinks1"> Tea</label><br>
        <input type="checkbox" id="drinks2" name="drinks2" value="Coffee">
        <label for="drinks2"> Coffee</label><br>
        <input type="checkbox" id="drinks3" name="drinks3" value="Cold Drinks">
        <label for="drinks3"> Cold Drinks</label><br><br>
        <input type="submit" value="Submit">
    </form>

</body>

</html>
```

## Output:

## Submit Button:

The &lt;input type="submit"> defines a button for submitting the form data to a form**-**handler. Theform-handler is typically a file on the server with a script for processing input data. The form-handler is specified in the form's action attribute.

## Example of Submit Button:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>submit Button</title>
</head>

<body>
    <form action="/action_page.php">
        <label for="username">user name:</label><br>
        <input type="text" id="username" name="username" value="James bond"><br>
        <label for="password">Password:</label><br>
        <input type="text" id="pass" name="pass" value="******"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>

</html>
```

## Output:

## The Method Attribute:

Themethod attribute specifies the HTTP method to be used when submitting the form data.

The form-data can be sent as URL variables (with `m="get"`) or as HTTP post transaction (with `method="post"`).

The default HTTP method when submitting form data is GET.

## GET Method Example:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Method</title>
</head>

<body>
    <p>This form will be submitted using the GET method:</p>

    <form action="/action_page.php" target="_blank" method="get">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="James"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Bond"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>

</html>
```

## Output:

## Post Method Example:

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Method</title>
</head>

<body>
    <h2>The method Attribute</h2>

    <p>This form will be submitted using the POST method:</p>

    <form action="/action_page.php" target="_blank" method="post">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="James"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Bond"><br><br>
        <input type="submit" value="Submit">
    </form>

</body>

</html>
```

## Output:

## HTML From Example:

```
<!DOCTYPE>
<html>

<body>
    <form action="***********">
        <table>
            <tr>
                <td class="tdLabel"><label for="register_name" class="label">Name:</label></td>
                <td><input type="text" name="name" value="" id="register_name" style="width:160px" /></td>
            </tr>
            <tr>
                <td class="tdLabel"><label for="register_password" class="label">Password:</label></td>
                <td><input type="password" name="password" id="register_password" style="width:160px" /></td>
            </tr>
            <tr>
                <td class="tdLabel"><label for="register_email" class="label">Email:</label></td>
                <td><input type="email" name="email" value="" id="register_email" style="width:160px" /></td>
            </tr>
            <tr>
                <td class="tdLabel"><label for="register_gender" class="label">Gender:</label></td>
                <td>
                    <input type="radio" name="gender" id="register_gendermale" value="male" />
                    <label for="register_gendermale">male</label>
                    <input type="radio" name="gender" id="register_genderfemale" value="female" />
                    <label for="register_genderfemale">female</label>
                </td>
            </tr>
            <tr>
                <td class="tdLabel"><label for="register_country" class="label">Select Country:</label></td>
                <td><select name="country" id="register_country" style="width:160px">
                        <option value="india">india</option>
                        <option value="pakistan">pakistan</option>
                        <option value="africa">africa</option>
                        <option value="china">china</option>
                        <option value="other">other</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div align="right"><input type="submit" id="register_0" value="register" />
                    </div>
                </td>
            </tr>
        </table>
    </form>
</body>

</html>
```

## Output:
