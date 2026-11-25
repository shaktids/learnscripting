---
title: "Cracking the top Amazon coding interview questions"
description: "Landing a job at Amazon is a dream for many developers around the globe. Amazon is one of the largest companies in the world, with a workforce of over…"
lang: other
categories: []
author: "Shakti Das"
pubDate: 2021-01-19T12:42:37
legacy: true
wpId: 2197
draft: true
---

Landing a job at Amazon is a dream for many developers around the globe. Amazon is one of the largest companies in the world, with a workforce of over half a million strong.

For you to join them, you’ll need to complete their unique interview that combines technical and leadership knowledge.

Today, I’ll walk you through everything you need to crack the **Amazon interview**, including coding questions and a step-by-step preparation guide.

**Today we will go over the following:**

- 45 common Amazon coding interview questions
- Overview of Amazon coding interviews
- How to prepare for a coding interview
- Wrapping up and resources

### Succeed in your Amazon interview.**Strategically prepare for Amazon interviews by learning the patterns behind common questions**[Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview)
![](/images/wp/5337062296256512-4be42bb3.jpg)

## 45 common Amazon coding interview questions

### 1. Find the missing number in the array

You are given an array of positive numbers from `1` to `n`, such that all numbers from `1` to `n` are present except one number `x`. You have to find `x`. The input array is not sorted. Look at the below array and give it a try before checking the solution.3712845n = 8 missing number = 6

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def find\_missing(input): #TODO: Write - Your - Code  return -1TestShow Solution

> *Click [here](https://www.educative.io/m/find-the-missing-number) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Constant, O(1)*O*(1)

A naive solution is to simply search for every integer between `1` and `n` in the input array, stopping the search as soon as there is a missing number. But we can do better. Here is a linear, O(n)*O*(*n*), solution that uses the arithmetic series sum formula.​​ Here are the steps to find the missing number:

- Find the sum `sum_of_elements` of all the numbers in the array. This would require a linear scan, O(n)*O*(*n*).
- Then find the sum `expected_sum` of first `n` numbers using the arithmetic series sum formula
- The difference between these i.e. `expected_sum - sum_of_elements`, is the missing number in the array.

### 2. Determine if the sum of two integers is equal to the given value

Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not. Consider this array and the target sums:5712843Target Sum107+3=10, 2+8=10Target Sum19No 2 values sum up to 19

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def find\_sum\_of\_two(A, val): #TODO: Write - Your - Code  return;TestShow Solution

> *Click [here](https://www.educative.io/m/sum-of-two-values) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Linear, O(n)*O*(*n*)

You can use the following algorithm to find a pair that add up to the target (say `val`).

- Scan the whole array once and store visited elements in a hash set.
- During `scan`, for every element `e` in the array, we check if `val - e` is present in the hash set i.e. `val - e` is already visited.
- If `val - e` is found in the hash set, it means there is a pair (`e`, `val - e`) in array whose sum is equal to the given `val`.
- If we have exhausted all elements in the array and didn’t find any such pair, the function will return `false`

### 3. Merge two sorted linked lists

Given two sorted linked lists, merge them so that the resulting linked list is also sorted. Consider two sorted linked lists and the merged list below them as an example.head1481519NULLhead2791016NULLhead1478910151619NULL

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def merge\_sorted(head1, head2):  #TODO: Write - Your - Code  return head1TestShow Solution

> *Click [here](https://www.educative.io/m/merge-two-sorted-linked-lists) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(m + n)*O*(*m*+*n*) where m and n are lengths of both linked lists

**Memory Complexity:** Constant, O(1)*O*(1)

Maintain a head and a tail pointer on the merged linked list. Then choose the head of the merged linked list by comparing the first node of both linked lists. For all subsequent nodes in both lists, you choose the smaller current node and link it to the tail of the merged list, and moving the current pointer of that list one step forward.

Continue this while there are some remaining elements in both the lists. If there are still some elements in only one of the lists, you link this remaining list to the tail of the merged list. Initially, the merged linked list is `NULL`.

Compare the value of the first two nodes and make the node with the smaller value the head node of the merged linked list. In this example, it is `4` from `head1`. Since it’s the first and only node in the merged list, it will also be the tail. Then move one step forward.

### 4. Copy linked list with arbitrary pointer

You are given a linked list where the node has two pointers. The first is the regular pointer. The second pointer is called and it can point to any node in the linked list. Your job is to write code to make a deep copy of the given linked list. Here, deep copy means that any operations on the original list should not affect the copied list.

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def deep\_copy\_arbitrary\_pointer(head):   #TODO: Write - Your - Code  return NoneTestShow Solution

> *Click [here](https://www.educative.io/m/copy-linked-list-with-arbitrary-pointer) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Linear, O(n)*O*(*n*)

This approach uses a map to track arbitrary nodes pointed by the original list. You will create a deep copy of the original linked list (say `list_orig`) in two passes.

- In the first pass, create a copy of the original linked list. While creating this copy, use the same values for data and `arbitrary_pointer` in the new list. Also, keep updating the map with entries where the key is the address to the old node and the value is the address of the new node.
- Once the copy has been created, do another pass on the copied linked list and update arbitrary pointers to the new address using the map created in the first pass.

### 5. Level Order Traversal of Binary Tree

Given the root of a binary tree, display the node values at each level. Node values for all levels should be displayed on separate lines. Let’s take a look at the below binary tree.100502002575350Level order traversal for this tree should look like: 100; 50, 200; 25, 75, 350

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

1234def level\_order\_traversal(root):  result = ""  #TODO: Write - Your - Code  return resultTestShow Solution

> *Click [here](https://www.educative.io/m/level-order-traversal-binary-tree) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Linear, O(n)*O*(*n*)

Here, you are using two queues: `current_queue` and `next_queue`. You push the nodes in both queues alternately based on the current level number.

You’ll dequeue nodes from the `current_queue`print the node’s data, and enqueue the node’s children to the next\_queue. Once the current\_queue becomes empty, you have processed all nodes for the current level\_number. To indicate the, print a line break (\n), swap the two queues, and continue with the above-mentioned logic.

After printing the leaf nodes from the `current_queue`swap `current_queue` and `next_queue`. Since the current\_queue would be empty, you can terminate the loop.

### 6. Determine if a binary tree is a binary search tree

Given a Binary Tree, figure out whether it’s a [Binary Search Tree](https://www.educative.io/blog/data-structures-trees-java#types). In a binary search tree, each node’s key value is smaller than the key value of all nodes in the right subtree and is greater than the key values of all nodes in the left subtree. Below is an example of a binary tree that is a valid BST.100502002575125350

Below is an example of a binary tree that is not a BST.10050200257590350

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def is\_bst(root):  #TODO: Write - Your - Code  returnTestShow Solution

> *Click [here](https://www.educative.io/m/is-binary-tree-a-binary-search-tree) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Linear, O(n)*O*(*n*)

There are several ways of solving this problem. A basic algorithm would be to check on each node where the maximum value of its left sub-tree is less than the node’s data and the minimum value of its right sub-tree is greater than the node’s data. This is highly inefficient as for each node, both of its left and right sub-trees are explored.

Another approach would be to do a regular in-order traversal and in each recursive call, pass maximum and minimum bounds to check whether the current node’s value is within the given bounds.

### 7. String segmentation

You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.

Given a dictionary of words.appleapplepearpie

Input string of “applepie” can be segmented into dictionary words.applepie

Input string “applepeer” cannot be segmented into dictionary words.applepeer

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

```
def can_segment_string(s, dictionary):
  #TODO: Write - Your - Code
  return
```

TestShow Solution

> *Click [here](https://www.educative.io/m/string-segmentation) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Exponential, O(2^n)*O*(2​*n*​​)

**Memory Complexity:** Polynomial, O(n^2)*O*(*n*​2​​)

You can solve this problem by segmenting the large string at each possible position to see if the string can be completely segmented into words in the dictionary. If you write the algorithm in steps it will be as follows:

```
n = length of input stringfor i = 0 to n - 1  first_word = substring (input string from index [0, i] )  second_word = substring (input string from index [i + 1, n - 1] )  if dictionary has first_word    if second_word is in dictionary OR second_word is of zero length, then return true    recursively call this method with second_word as input and return true if it can be segmented
```

The algorithm will compute two strings from scratch in each iteration of the loop. Worst case scenario, there would be a recursive call of each time. This shoots the time complexity up to 2^n2​*n*​​.

You can see that you may be computing the same substring multiple times, even if it doesn’t exist in the dictionary. This redundancy can be fixed by memoization, where you remember which substrings have already been solved.

To achieve memoization, you can store the string in a new set each time. This will reduce both time and memory complexities.

### 8. Reverse Words in a Sentence

Reverse the order of words in a given sentence (an array of characters)."Hello World""World Hello"

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def reverse\_words(sentence):    # sentence here is an array of characters  #TODO: Write - Your - Code  return sentenceTestShow Solution

> *Click [here](https://www.educative.io/m/reverse-words-in-a-sentence) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Constant, O(1)*O*(1)

The steps to solve this problem are simpler than they seem:

- Reverse the string.
- Traverse the string and reverse each word in place.

### 9. How many ways can you make change with coins and a total amount

Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. We can make changes in the following 6 ways:

![](/images/wp/6472580916576256-6db71977.jpg)

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def solve\_coin\_change(denominations, amount):  # TODO: Write - Your - Code  return -1TestShow Solution

> *Click [here](https://www.educative.io/m/coin-changing-problem) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Quadratic, O(m\*n)*O*(*m*∗*n*)

**Memory Complexity:** Linear, O(n)*O*(*n*)

To solve this problem, we’ll keep an array of size `amount + 1`. One additional space is reserved because we also want to store the solution for the `0` amount.

There is only one way you can make a change of `0`, i.e., select no coin so we’ll initialize `solution[0] = 1`. We’ll solve the problem for each amount, denomination to amount, using coins up to a denomination, `den`.

The results of different denominations should be stored in the array solution. The solution for amount `x` using a denomination `den` will then be:

```
solution[x] = solution[x] + solution[x - den]
```

We’ll repeat this process for all the denominations, and at the last element of the `solution` array, we will have the solution.

> ***Enjoying the article?** Scroll down to [sign up](https://www.educative.io/blog/blog-newsletter-annoucement) for our free, bi-monthly newsletter.*

### 10. Find Kth permutation

Given a set of ‘n’ elements, find their Kth permutation. Consider the following set of elements:123

All permutations of the above elements are (with ordering):

![](/images/wp/4505554614484992-cd216bdd.jpg)

Here we need to find the Kth permutation.

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def find\_kth\_permutation(v, k, result):  #TODO: Write - Your - Code  return resultTestShow Solution

> *Click [here](https://www.educative.io/m/find-permutation) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Linear, O(n)*O*(*n*)

Here is the algorithm that we will follow:

```
If input vector is empty return result vector block_size = (n-1)! ['n' is the size of vector]Figure out which block k will lie in and select the first element of that block(this can be done by doing (k-1)/block_size) Append selected element to result vector and remove it from original input vector Deduce from k the blocks that are skipped i.e k = k - selected*block_size and goto step 1
```

## Succeed in your Amazon interview.

Avoid waiting another 6 months to apply by taking our coding interview prep course. Educative’s text-based courses are easy to skim and feature live coding environments - making learning quick and efficient.

**[Grokking the Coding Interview: Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview)**

### 11. Find all subsets of a given set of integers

We are given a set of integers and we have to find all the possible subsets of this set of integers. The following example elaborates on this further.

**Given set of integers:**234

**All possile subsets for the given set of integers:**232, 342, 43, 42, 3, 4

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def get\_all\_subsets(v, sets):  #TODO: Write - Your - Code  return setsTestShow Solution

> *Click [here](https://www.educative.io/m/find-all-subsets) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Exponential, O(2^n\*n)*O*(2​*n*​​∗*n*)

**Memory Complexity:** Exponential, O(2^n\*n)*O*(2​*n*​​∗*n*)

There are several ways to solve this problem. We will discuss the one that is neat and easier to understand. We know that for a set of `n` elements there are 2^n2​*n*​​ subsets. For example, a set with 3 elements will have 8 subsets. Here is the algorithm we will use:

```
n = size of given integer setsubsets_count = 2^nfor i = 0 to subsets_count    form a subset using the value of 'i' as following:        bits in number 'i' represent index of elements to choose from original set,        if a specific bit is 1 choose that number from original set and add it to current subset,        e.g. if i = 6 i.e 110 in binary means that 1st and 2nd elements in original array need to be picked.    add current subset to list of all subsets
```

### 12. Print balanced brace combinations

Print all braces combinations for a given value n so that they are balanced. For this solution, we will be using recursion.

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

1234def print\_all\_braces(n):  #TODO: Write - Your - Code  result = []  return resultTestShow Solution

> *Click [here](https://www.educative.io/m/all-possible-braces) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Exponential, 2^n2​*n*​​

**Memory Complexity:** Linear, O(n)*O*(*n*)

The solution is to maintain counts of `left_braces` and `right_braces`. The basic algorithm is as follows:​

```
left_braces count: 0right_braces count: 0 if left_braces count is less than n:  add left_braces and recurse furtherif right_braces count is less than left_braces count:  add right_braces and recurse furtherstop recursing when left_braces and right_braces counts are both equal to n
```

### 13. Clone a Directed Graph

Given the root node of a directed graph, clone this graph by creating its deep copy so that the cloned graph has the same vertices and edges as the original graph.

Let’s look at the below graphs as an example. If the input graph is G = (V, E)*G*=(*V*,*E*) where V is set of vertices and E is set of edges, then the output graph (cloned graph) G’ = (V’, E’) such that V = V’ and E = E’. We are assuming that all vertices are reachable from the root vertex, i.e. we have a connected graph.

![](/images/wp/6619415429775360-4cb1162c.jpg)

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

1234567class Node:  def \_\_init\_\_(self, d):    self.data = d    self.neighbors = []def clone(root):  return None    # return rootTestShow Solution

> *Click [here](https://www.educative.io/m/clone-directed-graph) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Linear, O(n)*O*(*n*)

**Memory Complexity:** Logarithmic, O(logn)*O*(*l**o**g**n*)

We use depth-first traversal and create a copy of each node while traversing the graph. To avoid getting stuck in cycles, we’ll use a hashtable to store each completed node and will not revisit nodes that exist in the hashtable. The hashtable key will be a node in the original graph, and its value will be the corresponding node in the cloned graph.

### 14. Find Low/High Index

Given a sorted array of integers, return the low and high index of the given key. You must return `-1` if the indexes are not found. The array length can be in the millions with many duplicates.

In the following example, according to the `key`, the `low` and `high` indices would be:

- `key`: 1, `low` = 0 and `high` = 0
- `key`: 2, `low` = 1 and `high` = 1
- `ke`y: 5, `low` = 2 and `high` = 9
- `key`: 20, `low` = 10 and `high` = 10

![](/images/wp/5097413187469312-1c455b10.jpg)

For the testing of your code, the input array will be:

```
1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6
```

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

1234567def find\_low\_index(arr, key): #TODO: Write - Your - Code  return -2def find\_high\_index(arr, key):  #TODO: Write - Your - Code  return -2TestShow Solution

> *Click [here](https://www.educative.io/m/find-low-high-index) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Logarithmic, O(logn)*O*(*l**o**g**n*)

**Memory Complexity:** Constant, O(1)*O*(1)

Linearly scanning the sorted array for `low` and `high` indices are highly inefficient since our array size can be in millions. Instead, we will use a slightly modified binary search to find the `low` and `high` indices of a given key. We need to do binary search twice: once for finding the `low` index, once for finding the `high` index.

Let’s look at the algorithm for finding the `low` index. At every step, consider the array between `low` and `high` indices and calculate the `mid` index.

- If the element at `mid` index is less than the `key`, `low` becomes `mid + 1` (to move towards the start of range).
- If the element at `mid` is greater or equal to the `key`, the `high` becomes `mid - 1`. Index at `low` remains the same.
- When `low` is greater than `high`, `low` would be pointing to the first occurrence of the `key`.
- If the element at `low` does not match the `key`, `return -1`.

Similarly, we can find the `high` index by slightly modifying the above condition:

- Switch the `low` index to `mid + 1` when element at mid index is less than or equal to the `key`.
- Switch the `high` index to `mid - 1` when the element at `mid` is greater than the `key`.

### 15. Search Rotated Array

Search for a given number in a sorted array, with unique elements, that has been rotated by some arbitrary number. Return `-1` if the number does not exist. Assume that the array does not contain duplicates.

![](/images/wp/4862830865022976-0d648633.jpg)

- [Practice](https://www.educative.io/blog/crack-amazon-coding-interview-questions#)

123def binary\_search\_rotated(arr, key):  #TODO: Write - Your - Code  return -1TestShow Solution

> *Click [here](https://www.educative.io/m/search-rotated-array) to view the solution in C++, Java, JavaScript, and Ruby.*

**Runtime Complexity:** Logarithmic, O(logn)*O*(*l**o**g**n*)

**Memory Complexity:** Logarithmic, O(logn)*O*(*l**o**g**n*)

The solution is essentially a binary search but with some modifications. If we look at the array in the example closely, we notice that at least one half of the array is always sorted. We can use this property to our advantage. If the number `n` lies within the sorted half of the array, then our problem is a basic binary search. Otherwise, discard the sorted half and keep examining the unsorted half. Since we are partitioning the array in half at each step, this gives us O(log n)*O*(*l**o**g**n*) runtime complexity.

### More common Amazon coding interview questions

16. K largest elements from an array
17. Convert a Binary tree to DLL
18. Given a binary tree T, find the maximum path sum. The path may start and end at any node in the tree.
19. Rotate a matrix by 90 degrees
20. Assembly line scheduling with dynamic programming
21. Implement a stack with `push()`, `min()`, and `pop()` in O(1)*O*(1) time
22. How do you rotate an array by K?
23. Design Snake Game using Object Oriented analysis and design technique.
24. Print all permutations of a given string using recursion
25. Implement a queue using a linked list
26. Find the longest increasing subsequence of an array.
27. Lowest common ancestor in a Binary Search Tree and Binary Tree
28. Rotate a given list to the right by `k` places, which is non-negative.
29. Write a function that counts the total of set bits in a 32-bit integer.

31. How do you detect a loop in a singly linked list?
32. Reverse an array in groups
33. Given a binary tree, check if it’s a mirror of itself
34. Josephus problem for recursion
35. Zero Sum Subarrays
36. Huffman Decoding for greedy algorithms
37. Egg Dropping Puzzle for dynamic programming
38. N-Queen Problem
39. Check if strings are rotations of each other
40. 0-1 Knapsack Problem
41. Unbounded knapsack problem
42. Longest palindromic subsequence
43. Print `nth` number in the Fibonacci series
44. Longest common substring
45. Longest common subsequence

*For answers to questions on dynamic programming, check out [6 Dynamic Programming problems for coding interviews](https://www.educative.io/blog/6-dp-problems-to-solve-for-your-next-coding-interview)*

## Overview of Amazon coding interview

To land a software engineering job at Amazon, you need to know what lies ahead. The more prepared you are, the more confident you will be. So, let’s break it down.

- **Interview Timeline:** The whole interview process takes 6 to 8 weeks to complete.
- **Types of Interviews:** Amazon coding interviews consist of 5 to 7 interviews. This includes 1 assessment for fit and aptitude, 1-2 online tests, and 4-6 on-site interviews, also known as *The Loop.*
- **The Loop:** The onsite interviews include 1 to 3 interviews with hiring managers and 1 bar raiser interview to evaluate Amazon’s 14 leadership principles.
- **Coding Questions:** Amazon programming questions focus on algorithms, data structures, puzzles, and more.
- **Hiring Levels:** Amazon usually hires at entry-level 4 (out of 12 total), and the average salary for that level ranges from $106,000 to $114,000 yearly.
- **Hiring Teams:** Amazon hires based on teams. The most common hiring teams are Alexa and AWS.
- **Programming Languages:** Amazon prefers the following programming languages for coding questions: Java, C++, Python, Ruby, and Perl.

### Amazon’s 14 leadership principles

Though coding interviews at Amazon are similar to other big tech companies, there are a few differences in their process, in particular, the **Bar Raiser**. Amazon brings in an objective third-party interviewer called a Bar Raiser, who evaluates candidates on Amazon’s 14 Leadership Principles. The Bar Raiser has complete veto power over whether or not you will be hired. Bar Raisers ensure that Amazon hires someone at the top 50th percentile of candidates for that level.

It is unlikely that you will know which of your interviewers is the Barn Raiser. The key is to take every part of the interview seriously and always assume you’re being evaluated for cultural fit as well as technical competency. Below are the 14 values that you be evaluated on. Customer Obsession: Leaders start with the customer and work backward. They work vigorously to earn and keep customer trust. Ownership: Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company. They never say “that’s not my job."Invent and Simplify: Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here."Are Right, A Lot: Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs. Learn and Be Curious: Leaders are never done learning and always seek to improve themselves. Hire and Develop the Best: Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent and willingly move them throughout the organization. Insist on the Highest Standards: Leaders have relentlessly high standards — many people may think these standards are unreasonably high. Leaders are continually raising the bar. Think Big: Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. Bias for Action: Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk-taking. Frugality: Accomplish more with less. Constraints breed resourcefulness, self-sufficiency, and invention. Earn Trust: Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Dive Deep: Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics differ. No task is beneath them. Have Backbone; Disagree and Commit: Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. **Deliver Results:** Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle.

## How to prepare for an Amazon coding interview

Now that you have a sense of what to expect from an interview and know what kinds of questions to expect, let’s learn some preparation strategies based on Amazon’s unique [interview process](https://www.codinginterview.com/amazon).

### Updating your resume

Make sure you’ve updated your resume and LinkedIn profile. Always use deliverables and metrics when you can as they are concrete examples of what you’ve accomplished. Typically recruiters will browse LinkedIn for candidates.

If an Amazon recruiter believes that you are a good match they will reach out to you (via email or LinkedIn) to set up a time to chat. For tips on how to network and update your resume, check out our [career advice for recent college graduates.](https://www.educative.io/blog/land-tech-job-advice)

### Prepare for coding assessment

It’s up to you to come to a coding interview fully prepared for technical assessment. I recommend at least **three months** of self-study to be successful. This includes choosing a programming language, reviewing the basics, and studying algorithms, data structures, [system design](https://www.educative.io/blog/top-10-system-design-interview-questions), object-oriented programming, OS, and concurrency concepts.

You’ll also want to prepare for [behavioral interviews](https://www.educative.io/blog/behavioral-interviews-how-to-prepare-and-ace-interview-questions).

> *For a robust, 12-week interview guide, check out the [Definitive Interview Prep Roadmap](https://www.codinginterview.com/interview-roadmap)*

### Prescreen with a recruiter

Expect a light 15-30 minute call where the recruiter will gauge your interest level and determine if you’re a good fit. The recruiter may touch on a few technical aspects. They just want to get an idea of your skills. Typical questions might include your past work experiences, your knowledge of the company/position, salary, and other logistical questions.

It’s important to have around 7-10 of your own questions ready to ask the interviewer. Asking questions at an early stage shows investment and interest in the role.

### Online Assessment

Once you complete the call with the recruiter, they’ll administer an online coding test, a debugging test, and an aptitude test. The debugging section will have around 6-7 questions, which you have 30 minutes to solve. The aptitude section will have around 14 multiple-choice questions, dealing with concepts like basic permutation combination and probabilities.

The coding test consists of two questions. You’ll have about 1.5 hours to complete it. Expect the test to be conducted through Codility, HackerRank, or another site. Expect some easy to medium questions that are typically algorithm related. Examples include:​

- Reverse the second half of a linked list​
- Find all anagrams in a string​
- Merge overlapping intervals

### Phone Interviews

Once you’ve made it past the prescreen and online assessment, the recruiter will schedule your next round, likely with a hiring manager or a manager from the team you’re looking to join. At this stage in the process, there will be one to three more interviews.

This is where they’ll ask you questions directly related to your resume, as well as data structures, algorithms, and other various coding questions that apply to the position. You can expect to write code, review code, and demonstrate your technical knowledge.

*For tips on video and phone interviews, check out my article [Video Interviews: a comprehensive guide for software developers](https://www.educative.io/blog/video-interviews-a-comprensive-guide-for-software-developers)*

### On-Site Interviews: The Loop

If you have successfully made it through the series of phone interviews, you’ll be invited for an on-site visit. This full day of on-site interviews is referred to as the “The Loop”. Throughout the day, you’ll meet with 4-6 people. Expect half of these interviews to be technical and the other half to assess soft skills. Be prepared to work through questions on a whiteboard and discuss your thought process.

Concepts that Amazon loves to test on are [data structures](https://www.educative.io/blog/data-structures-algorithms) and [algorithms](https://www.educative.io/blog/data-structures-algorithms). It’s important to know the runtimes, theoretical limitations, and basic implementation strategies of different classes of algorithms.

- **Data structures you should know:** Arrays, Stacks, Queues, Linked lists, Trees, Graphs, Hash tables
- **Algorithms you should know:** Breadth First Search, Depth First Search, Binary Search, Quicksort, Mergesort, Dynamic programming, Divide and Conquer

### The Offer / No Offer

Generally, you’ll hear back from a recruiter within a week after your interviews. If you didn’t get an offer, Amazon will give you a call. You’ll likely have to wait another six months to re-apply. Judging that your on-site interviews went well, they’ll reach out to you, at which point they’ll make you an offer, send you documents to sign, and discuss any further questions you have.

## Wrapping up and resources

Cracking the Amazon coding interview comes down to the time you spend preparing, such as practicing coding questions, studying behavioral interviews, and understanding Amazon’s company culture. There is no golden ticket, but more preparation will surely make you a more confident and desirable candidate.

Learning how to articulate your problem-solving process comes with practice and interview experience. And remember: if you don’t get an offer right away, be patient. It’s okay to reapply or apply to different positions/teams. The willingness to persevere makes a difference.

The essential resources below will help you prepare and build confidence for Amazon interviews. Keep learning and studying!
