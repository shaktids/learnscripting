---
title: "V-Model"
description: "[if gte vml 1] <v:shapetype id=\" x0000 t75\" coordsize=\"21600,21600\" o:spt=\"75\" o:preferrelative=\"t\" path=\"m@4@5l@4@11@9@11@9@5xe\" filled=\"f\" stroked=\"f\"…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2017-01-22T02:20:52Z
legacy: true
wpId: 35
---

[if gte vml 1]>&lt;v:shapetype id="\_x0000\_t75" coordsize="21600,21600" o:spt="75" o:preferrelative="t" path="m@4@5l@4@11@9@11@9@5xe" filled="f" stroked="f">&lt;br />
&lt;v:stroke joinstyle="miter"/>&lt;br />
&lt;v:formulas>&lt;br />
&lt;v:f eqn="if lineDrawn pixelLineWidth 0"/>&lt;br />
&lt;v:f eqn="sum @0 1 0"/>&lt;br />
&lt;v:f eqn="sum 0 0 @1"/>&lt;br />
&lt;v:f eqn="prod @2 1 2"/>&lt;br />
&lt;v:f eqn="prod @3 21600 pixelWidth"/>&lt;br />
&lt;v:f eqn="prod @3 21600 pixelHeight"/>&lt;br />
&lt;v:f eqn="sum @0 0 1"/>&lt;br />
&lt;v:f eqn="prod @6 1 2"/>&lt;br />
&lt;v:f eqn="prod @7 21600 pixelWidth"/>&lt;br />
&lt;v:f eqn="sum @8 21600 0"/>&lt;br />
&lt;v:f eqn="prod @7 21600 pixelHeight"/>&lt;br />
&lt;v:f eqn="sum @10 21600 0"/>&lt;br />
&lt;/v:formulas>&lt;br />
&lt;v:path o:extrusionok="f" gradientshapeok="t" o:connecttype="rect"/>&lt;br />
&lt;o:lock v:ext="edit" aspectratio="t"/>&lt;br />
&lt;/v:shapetype>&lt;v:shape id="\_x0000\_i1025" type="#\_x0000\_t75" alt="Untitled Diagram(1)" style='width:600pt;height:387pt'>&lt;br />
&lt;v:imagedata src="file:///D:\Users\Auro\AppData\Local\Temp\msohtmlclip1\01\clip\_image001.jpg" o:href="https://i2.wp.com/www.learntowish.com/wp-content/uploads/2016/04/Untitled-Diagram1.jpg?resize=860%2C555"/>&lt;br />
&lt;/v:shape>&lt;![endif]

In order to overcome the drawbacks of waterfall model,Spiral Model,Prototype Model also if the requirements are not verified then we go V-Model

Note-This model is best suitable for verification and validation

Unit Testing-Testing each and every lines in the source code.

Functional Testing-Testing the entire functionality of an application against the requirement specification.

Integration testing – Testing the data flow between  two module.

System testings – End to end testing done by the test engineer.

Acceptance testings – End to end testing done by customer.

As soon as customer  gives a requirement to the business analyst the requirement will be re-viewed by customer at the very initial stage to avoid Conflict requirement,Wrong requirement,Missing requirement

Conflict Requirement  -In the CRS their should be a unique requirement for every component if  their are duplicate requirement for each component it is called as conflict requirement.
Example-In the documentation in  page -10  customer has specified the amount test field should be consists of only integer where as in that same document customer has again specified  that the amount field should consist of  alphanumeric this type of mistake are called as conflict requirement.

Wrong Rquirments-The requirement are incorrect is called wrong requirement.
Example-In the requirement specification customer specified for the mobile text field it should contain integer and decimal.This type of requirement are called as wrong requirement.

Missing Requirment-A customer has hot specified requirement for the component then it is missing requirement.
Example-For the component user name the customer could have not specified requirement.

Once a review of CRS is done it will be given for the next stage is SRS meanwhile the acceptance testing team starts write acceptance test plan and test case.

Once the SRS is done it will will be given to the system testing team where they review SRS against CRS.
Later system testing team start writing system test plan and system test case, This continue till coding.

Verification-It is a process of checking are we building the product right.
Static Testing-Testing without execution of the source code is called as static testing.Activities which are involved in this testing are-Review requirement(SRS & CRS)
-Review Design(HLD & LLD)
-Review of source code.
Once a developer writes the source code they do the unit testing.
Unit Testing-Testing each and every lines of the source code is working or not.
Once a unit testing is done functional testing and system testing will be done.
Once system testing is done the application will be tested by the end users before the product is release to the market.
Validation-Process of checking are we building the right product.

Dynamic Testing-Testing with the execution of the source code is called as dynamic testing.Here we do the actual testing of application by giving the valid inputs.

Advantages of V Model- Requirement at the very inital stage.
-By modifying the requirement at very inital stage we can avoid the downward flow of defect.
-Each and every  stages of test testing starts at very initial stage.
-By testing wach and every stages the customer can expect a very high quality of product.
-The work is done simultaneously in each and every stages.

Drawbacks
Documentation work is more.
Investment should be high.

Q-Why do we will go for V Model?
A-Customer is expecting very high quality of the software we go for the V model.

Q-For what short of application we go for the V model?
A-For long term project.
-For complex application.
it is all above the prevention of the defect.

Static Testing-This testing can be performed before the execution.
-Static testing is done before the code is deployed.

Dynamic Testing-This testing can be performed after after the execution.
-This testing is done after the code is deployed.

# [Prototype Model](http://learntowish.com/prototype-model/)

When the customer is new to the domain or he has a requirement but he does not have a clear picture of requirement in such case we go for prototype model.

[if gte vml 1]>&lt;v:shape id="\_x0000\_i1026" type="#\_x0000\_t75" alt="PROTOTYPE MODEL" style='width:197.25pt;height:390pt'>&lt;br />
&lt;v:imagedata src="file:///D:\Users\Auro\AppData\Local\Temp\msohtmlclip1\01\clip\_image003.jpg" o:href="https://i0.wp.com/www.learntowish.com/wp-content/uploads/2016/04/PROTOTYPE-MODEL-1.jpg?resize=263%2C520"/>&lt;br />
&lt;/v:shape>&lt;![endif]

Assuming the customer is new to domain or he has a requirement but not clear about the requirement.
The requirement will given Business Analyst(BA) in Coustomer Requiremet Specification(CRS) where later converted to Software Requirement Specification(SRS).
Once the SRS is completed design and develop prototype is done that is web designers they starts writing the dummy implementation using some of the scripting languages like HTML,CSS& AJAX.
Once a design of prototype is done the prototype testing will be done to ensure that the components are existing or not.
Once a prototype testing is done a dummy implementation will be sent to the customer for the review if the customer approves it will be driven by next activities.
NOTE In case if the customer modifies then the requirement need to be updated design and also prototype testing that is a lot of rework and time-consuming.
Once a designing is done developer starts writing source code by using programming language that is java,.NET etc..
Once a coding is done testing will be done on the application by giving valid or invalid inputs.
Once the application is tested the application will be installed in the customer place or on the customer  server by build engineer or release engineer or installation engineer or developer.

**Advantages of Prototype Model**
Frequent communication between customer ,developer and the tester.
Beginning we set the expectation for the client.
Customer gets a opportunities in the beginning it self to ask for the requirement changes that is very easy to do before coding or testing.
Customer can get fair accurate product even he new to the domain.
We set the expectation of the client

**Drawbacks of Prototype Model**
There is a delay in starting the real-time project.
Investment should be high for the project.
In case if requirement changes then lots of rework need to be done time-consuming.
Testing is carried out after the coding.

**Q-When do we go for prototype model?**
A-Customer is new to the domain,
-Customer have requirement but he does not have clear picture of requirement.
-Testing is carried out after the coding.

# [Spiral Model](http://learntowish.com/spiral-model/)

Whenever their is a dependency in application or fetcher or module we follow spiral mode

Example-To develop an application in 3D we first need to develop in 2d.

[if gte vml 1]>&lt;v:shape id="\_x0000\_i1027" type="#\_x0000\_t75" alt="psiral" style='width:459.75pt;height:348.75pt'>&lt;br />
&lt;v:imagedata src="file:///D:\Users\Auro\AppData\Local\Temp\msohtmlclip1\01\clip\_image004.png" o:href="https://i0.wp.com/www.learntowish.com/wp-content/uploads/2016/04/psiral.png?resize=613%2C465"/>&lt;br />
&lt;/v:shape>&lt;![endif] [if gte vml 1]>&lt;v:shape id="\_x0000\_i1028" type="#\_x0000\_t75" alt="SPIRAL MODEL 1" style='width:225pt;height:132pt'>&lt;br />
&lt;v:imagedata src="file:///D:\Users\Auro\AppData\Local\Temp\msohtmlclip1\01\clip\_image005.png" o:href="https://i0.wp.com/www.learntowish.com/wp-content/uploads/2016/04/SPIRAL-MODEL-1.png?resize=300%2C176"/>&lt;br />
&lt;/v:shape>&lt;![endif]

The requirement are gathered for A where as later the crs will converted to SRS by the business analyst once the SRS complied the design(HLD & LLD) will be done.

Once the design is done the coding is done by the programmer or the developer using the programming language.

Once the coding is done the testing will be done.And once the complete A module is developed and tested the end user will starts testing the application before installing in customer place.And in case they identify the defect the defect will communicated to the developer where they fixed the defect.

Once the customer are time then only the requirement will be given for the next module that is B and this continues till n number of module with same activities.

**Fetcher**-It follows a spiral

**Advantages**-The requirement changes are allowed after develop one fetcher or one module then we can go and develop the next module of the project.At each Stage or release customer can sea the software.

**Drawbacks**-It is traditional model,
Developers are involved in testing,
Requirements are not verified,
Testing is the phase which will carried out after coding,If any major changes are done then lots of rework will happen that is time consuming.

**Q-When do we go for spiral model?**
A-When their is a dependency in application or fetcher or or module we go for spiral model
When the customer give requirements in stages we go for spiral model.

**Q-If you have 2 module A and B, If you have identified a major** defect in module B what will be your testing approach?
A-If a major defect is identified in module B then the defect will send to the developers for fixing.Once the defect is fixed i am going to retest the  defect first and later i am going to test module A.Because in fixing the major defect it should not impact the related fetcher of the application.

**Q-If you have two module A and B and their is a minor change in module A what will be the test approach?**
A-First i am going to test the newly added requirement in module A where as i am not going to test the module B because as it is a minor it will not impact on the other related fetchers.
