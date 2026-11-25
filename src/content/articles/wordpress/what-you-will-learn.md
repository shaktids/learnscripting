---
title: "What you will Learn"
description: "This Blog will give you a broad overview of the types of learning algorithms that are currently used in the diverse fields of machine learning and what to…"
lang: other
categories: ["Machine Learning"]
author: "Shakti Das"
pubDate: 2018-05-06T03:05:08Z
legacy: true
wpId: 106
---

This Blog will give you a broad overview of the types of learning algorithms that
are currently used in the diverse fields of machine learning and what to watch out
for when applying them. From our own experience, however, we know that doing
the "cool" stuff—using and tweaking machine learning algorithms such as support
vector machines (SVM), nearest neighbor search (NNS), or ensembles thereof—will
only consume a tiny fraction of the overall time of a good machine learning expert.
Looking at the following typical workﬂow, we see that most of our time will be spent
in rather mundane tasks:
1. Reading the data and cleaning it.
2. Exploring and understanding the input data.
3. Analyzing how best to present the data to the learning algorithm.
4. Choosing the right model and learning algorithm.
5. Measuring the performance correctly.
When talking about exploring and understanding the input data, we will need a
bit of statistics and basic math. But while doing this, you will see that those topics,
which seemed so dry in your math class, can actually be really exciting when you
use them to look at interesting data.
The journey begins when you read in the data. When you have to face issues such as
invalid or missing values, you will see that this is more an art than a precise science.
And a very rewarding one, as doing this part right will open your data to more
machine learning algorithms, and thus increase the likelihood of success.
With the data being ready in your program's data structures, you will want to get a
real feeling of what kind of animal you are working with. Do you have enough data
to answer your questions? If not, you might want to think about additional ways to
get more of it. Do you maybe even have too much data? Then you probably want to
think about how best to extract a sample of it.Often you will not feed the data directly into your machine learning algorithm.Instead, you will find that you can refine parts of the data before training. Many
times, the machine learning algorithm will reward you with increased performance.You will even find that a simple algorithm with refined data generally outperforms a very sophisticated algorithm with raw data. This part of the machine learning workﬂow is called feature engineering, and it is generally a very exciting and
rewarding challenge. Creative and intelligent that you are, you will immediately see the results.

Choosing the right learning algorithm is not simply a shootout of the three or four that are in your toolbox (there will be more algorithms in your toolbox that you will see). It is more of a thoughtful process of weighing different performance and functional requirements. Do you need fast results and are willing to sacrifice quality? Or would you rather spend more time to get the best possible result? Do you have a
clear idea of the future data or should you be a bit more conservative on that side? Finally, measuring the performance is the part where most mistakes are waiting for the aspiring ML learner. There are easy ones, such as testing your approach with the  same data on which you have trained. But there are more difficult ones; for example, when you have imbalanced training data. Again, data is the part that determines
whether your undertaking will fail or succeed.

We see that only the fourth point is dealing with the fancy algorithms. Nevertheless,we hope that this book will convince you that the other four tasks are not simply chores, but can be equally important if not more exciting. Our hope is that by the end of the book you will have truly fallen in love with data instead of learned algorithms.To that end, we will not overwhelm you with the theoretical aspects of the diverse ML
algorithms, as there are already excellent books in that area (you will fnd pointers in Appendix, Where to Learn More about Machine Learning). Instead, we will try to provide an intuition of the underlying approaches in the individual chapters—just enough for you to get the idea and be able to undertake your first steps. Hence, this book is by no means "the definitive guide" to machine learning. It is more a kind of starter kit. We hope that it ignites your curiosity enough to keep you eager in trying to learn more
and more about this interesting field.

In the rest of this chapter, we will set up and get to know the basic Python libraries,**NumPy** and **SciPy**, and then train our first machine learning using scikit-learn. During this endeavor, we will introduce basic ML concepts that will later be used throughout the book. The rest of the chapters will then go into more detail through the five steps described earlier, highlighting different aspects of machine learning in Python using
diverse application scenarios.
