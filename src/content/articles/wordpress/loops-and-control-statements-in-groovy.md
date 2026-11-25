---
title: "Loops and Control Statements in Groovy"
description: "While Loop The syntax of the while statement is shown below − The while statement is executed by first evaluating the condition expression (a Boolean…"
lang: other
categories: ["Groovy"]
author: "Shakti Das"
pubDate: 2020-03-27T03:50:12Z
legacy: true
wpId: 1989
---

## While Loop

The syntax of the while statement is shown below −

```
while(condition) {
   statement #1
   statement #2
   ...
}
```

The **while** statement is executed by first evaluating the condition expression (a Boolean value), and if the result is true, then the statements in the while loop are executed. The process is repeated starting from the evaluation of the condition in the while statement. This loop continues until the condition evaluates to false. When the condition becomes false, the loop terminates. The program logic then continues with the statement immediately following the while statement. The following diagram shows the diagrammatic explanation of this loop.

Following is an example of a while loop statement

```
class Example {
   static void main(String[] args) {
      int count = 0;

      while(count<5) {
         println(count);
         count++;
      }
   }
}
```

In the above example, we are first initializing the value of a count integer variable to 0. Then our condition in the while loop is that we are evaluating the condition of the expression to be that count should be less than 5. Till the value of count is less than 5, we will print the value of count and then increment the value of count. The output of the above code would be −

```
0
1
2
3
4
```

## For Loop

Following is an example of a while loop statement

```
class Example {
   static void main(String[] args) {
      int count = 0;

      while(count<5) {
         println(count);
         count++;
      }
   }
}
```

In the above example, we are first initializing the value of a count integer variable to 0. Then our condition in the while loop is that we are evaluating the condition of the expression to be that count should be less than 5. Till the value of count is less than 5, we will print the value of count and then increment the value of count. The output of the above code would be −

```
0
1
2
3
4
```

## for-in statement

The **for-in** statement is used to iterate through a set of values. The **for-in** statement is generally used in the following way.

```
for(variable in range) {
   statement #1
   statement #2
   …
}
```

The following diagram shows the diagrammatic explanation of this loop.

Following is an example of a for-in statement −

```
class Example {
   static void main(String[] args) {
      int[] array = [0,1,2,3];

      for(int i in array) {
         println(i);
      }
   }
}
```

In the above example, we are first initializing an array of integers with 4 values of 0,1,2 and 3. We are then using our for loop statement to first define a variable i which then iterates through all of the integers in the array and prints the values accordingly. The output of the above code would be −

```
0
1
2
3
```

The **for-in** statement can also be used to loop through ranges. The following example shows how this can be accomplished.

```
class Example {
   static void main(String[] args) {

      for(int i in 1..5) {
         println(i);
      }

   }
}
```

In the above example, we are actually looping through a range which is defined from 1 to 5 and printing the each value in the range. The output of the above code would be −

```
1
2
3
4
5
```

The **for-in** statement can also be used to loop through Map’s. The following example shows how this can be accomplished.

```
class Example {
   static void main(String[] args) {
      def employee = ["Ken" : 21, "John" : 25, "Sally" : 22];

      for(emp in employee) {
         println(emp);
      }
   }
}
```

In the above example, we are actually looping through a map that has a defined set of key-value entries. The output of the above code would be −

```
Ken = 21
John = 25
Sally = 22
```

## Break Statement

The **break** statement is used to alter the flow of control inside loops and switch statements. We have already seen the break statement in action in conjunction with the switch statement. The break statement can also be used with a while and for statements. Executing a **break** statement with any of these looping constructs causes immediate termination of the innermost enclosing loop.

The following diagram shows the diagrammatic explanation of the **break** statement.

Following is an example of the break statement

```
class Example {
   static void main(String[] args) {
      int[] array = [0,1,2,3];

      for(int i in array) {
         println(i);
         if(i == 2)
         break;
      }
   }
}
```

The output of the above code would be −

```
0
1
2
```

As expected since there is a condition put saying that if the value of **i** is 2 then break from the loop that is why the last element of the array which is 3 is not printed.

## Continue Statement

The continue statement complements the break statement. Its use is restricted to while and for loops. When a continue statement is executed, control is immediately passed to the test condition of the nearest enclosing loop to determine whether the loop should continue. All subsequent statements in the body of the loop are ignored for that particular loop iteration.

The following diagram shows the diagrammatic explanation of the continue statement −

Following is an example of the **continue** statement

```
class Example {
   static void main(String[] args) {
      int[] array = [0,1,2,3];

      for(int i in array) {
         println(i);
         if(i == 2)
         continue;
      }
   }
}
```

The output of the above code would be −

```
0
1
2
3
```
