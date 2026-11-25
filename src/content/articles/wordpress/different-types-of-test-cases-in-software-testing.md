---
title: "Different Types of Test Cases in Software Testing"
description: "Their are Different Types of Test Cases in Software Testing but the mostly used test cases in software testing are 1.Functionality Test Cases 2.User…"
lang: other
categories: ["Jobs"]
author: "Shakti Das"
pubDate: 2017-08-20T05:56:19Z
legacy: true
wpId: 876
---

Their are **Different Types of Test Cases in Software Testing**  but the mostly used test cases in software testing are

1.Functionality Test Cases
2.User Interface Test Cases
3.Performance Test Cases
4.Integration Test Cases
5.Usability Test cases
6.Database Testing Test Cases
7.Security Test Cases
8.User Acceptance Test cases
9.Unit test cases

**1.Functionality Test Cases/Functional Test Case**

Functionality test cases are used to discover if an application’s interface works with the rest of the system and its users. The tests identify the success or failure of functions that the software is expected to perform.

The cases are a type of black-box testing that uses for its base the specifications or user stories of the software under test. This allows the tests to be performed without needing access to the workings or internal structures of the software being tested. The QA team are the usual writers of functionality test cases because they fall within normal QA processes. They can be written and run as soon as development makes a first function available for testing. To help steer development, they can be written in advance of the code, if all the tester has access to are the requirements.

As specified above, they can be written and run as soon as it is viable to do so and they should be repeated whenever updates are added, right through to when customers become a possibility.

*Example:* Confirming a user can successfully send an email.

**2.User Interface Test Cases**

User interface test cases are used to verify that specific pieces of the Graphical User Interface (GUI) look and work as expected. These types of test cases can be used to identify cosmetic inconsistencies, grammar and spelling errors, links, and any other elements the user interacts with or sees.

These cases are usually written by the testing team but the design team may also be involved as they are most familiar with the interface. User interface test cases are the types of test cases in software testing that usually drive cross-browser testing. Browsers tend to render things differently, and user interface test cases help ensure your application behaves consistently across multiple browsers.

These test cases will be run once the development phase is complete and the UI is hooked up to the database.

*Example:* What happens when the website is viewed on a small screen such as a mobile phone? Does the UI break?

**3.Performance Test Cases**

Performance test cases validate response times and overall effectiveness of an application. That is, after executing an action, how long does it take for the system to respond? Performance test cases should have a very clear set of success criteria.

The testing team typically writes these test cases and they are often automated. A large application can have hundreds or thousands of performance tests. Automating these tests and running them frequently helps expose scenarios where the application is not performing at the expected level.

Performance test cases help understand how the application will perform in the real world. These cases can be written once the testing team has performance requirements from the product team. However, many performance issues can be identified manually without having specified requirements.

*Example:* How long does it take for the system to authenticate a user and load the next page? When multiple people login at the same time, does the application remain stable?

**4.Integration Test Cases**

Integration test cases are meant to determine how different modules interact with each other. The main purpose with integration test cases are to ensure interfaces between the different modules are working properly.

The testing team identifies which areas should undergo integration testing, while the development team will have input on how those test cases should be written. Either of these two teams may work to write the cases.

They verify that modules that are already working individually are also able to work together.

*Example:* Checking the link between the home page and the “favorites” section. When you add an item as a “favorite”, from the homepage, does it appear in the “favorites” section?

**5.Usability Test cases**

Usability test cases can often be referred to as “tasks” or “scenarios”. Rather than providing detailed step-by-step instructions to execute the test, the tester is presented with a high level scenario or task to complete.

Usability test cases help identify how a user naturally approaches and uses the application. They help guide the tester through various situations and flows. No prior knowledge of the application is necessary.

These test cases are typically prepared by the design team alongside the testing team. Usability testing should be done prior to user acceptance testing.

*Example:* Can the user successfully add more than one item to their shopping cart? What is that experience like?

**6.Database Testing Test Cases**

Test cases for database testing examine what’s happening behind the scenes. The user interface is clean, and everything appears to be working… but where is all that data going?

In order to write these test cases, you need to have a strong understanding of the entire application, the database tables, and the the stored procedures. The testing team will often use SQL queries to develop database test cases.

Database tests are used to verify the developer has written the code in a way that stores and handles data in a consistent, safe manner.

*Example:* Let’s consider the creation of a user profile. When the user submits their profile, the following should be tested in regards to the database.

1. Did the application store the inputted data in the database?
2. Was any data lost in the process?
3. Partially performed data should not have been saved.
4. Unauthorized users should not be able to view or access the user’s information.

**7.Security Test Cases**

Security test cases help ensure the application restricts actions and permissions wherever necessary. These test cases are written to protect data when and where it needs to be safeguarded.

Security test cases are used to drive penetration testing and other types of security-based tests.

Authentication and encryption are often the main focus in security test cases. The security team (if one exists) is usually responsible for writing and conducting these tests.

*Example:* If a user reaches X number of failed login attempts, does the account become locked? Is a user able to upload data without being logged in?

**8.User Acceptance Test cases**

User acceptance test cases, or “UAT” test cases, help the team test the user acceptance testing environment. These test cases should be broad, covering all areas of the application.

The purpose of these test cases isn’t to find bugs (hopefully they’ve already been found and fixed in previous testing), but to verify the application is acceptable to the user. So, when they execute a test, are the results of that test, and the experience of that test acceptable?

Since many other types of testing have already been done by the time UAT starts, the focus is not so much on a granular level, but more so on the bigger picture. User acceptance test cases are used by the end-user or client and prepared by the testing team or product manager. This is perhaps the most important phase of testing as it is the last step before going into production.

*Example:* If testing for instance, a photo management application for a photography studio, the client (the user) should test that they are able to upload and manage their photos in a way that fits their business needs.
