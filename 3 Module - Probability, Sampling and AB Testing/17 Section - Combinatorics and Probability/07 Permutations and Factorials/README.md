
# Permutations and Factorials



## Introduction

In the previous lab, you defined at a few sample spaces by counting the total number of possible outcomes. This is not very practical when sample spaces grow. In this lab, you'll be introduced to *permutations*, which will provide a structured way to help you define sample space sizes!

## Objectives

You will be able to: 
- Understand how to count permutations, and how factorials are the building blocks of permutations
- Understand how to mathematically derive how many permutations there are for big sets
- Understand how to compute permutations of a subset
- Learn about permutations with replacement and repetition

## Defining the Sample Space by Counting

Let's consider the following example.

The Beyonce tribute band "The Single Ladies" is playing a free mini gig in your local park next week. They have selected three all-time classics: "Drunk in Love", "Crazy in Love" and "Formation", but still have to decide the order they will play the songs in. Knowing this, how many playlists are possible?

It is easy and fairly quick to write down possible orders here:

"Drunk in Love", "Crazy in Love", "Formation"

"Drunk in Love", "Formation", "Crazy in Love"

"Crazy in Love", "Drunk in Love", "Formation"

"Crazy in Love", "Formation", "Drunk in Love" 

"Formation", "Drunk in Love", "Crazy in Love"

"Formation", "Crazy in Love", "Drunk in Love"

That's it! When we count the possible outcomes, we get to 6 elements in the sample set. Now what if "The Single Ladies" plays a setlist of 4 songs? or 5? That's where the notion of *permutations* comes in handy.


## Permutations

The problem setting in general is that, there are $n$ objects, and we want to know how many *permutations* are possible.

This is a way how you can tackle this. You're the front singer and have to decide which song to play first. You have 3 songs to choose from, so 3 ways of choosing a first song. Then, you move on to the second song. You've chosen the first one, so you have 2 songs to choose from now. Etcetera. Mathematically, this boils down to:

 $ \text{# Beyonce permutations} = 3*2*1 = 3 ! = 6$

Generalizing this to $n$, this means that the number of permutations with $n$ distinct objects is $n!$, or the factorial of $n$.

## Permutations of a Subset

Now, lets consider another example. "The Single Ladies" is still playing a concert at central park, but the disagree on the final three songs that they will play. They only get a 12min gig slot, so they really can't play more than 3, yet they have a shortlist of 8 they need to pick from. How many final song selections are possible given this info? As for the first example, the order of the songs played is still important.

When the band members decide on the first song, they have 8 possible songs to choose from. When choosing the second song, they have 7 to choose from. Then for the third song, they have 6 left.

 $ \text{# Beyonce k-permutations} = 8*7*6 = 336$

formalizing this, the question is how many ways we can select $k$ elements out of a pool of $n$ objects. The answer is 

$n*(n-1)*...*(n-k+1)$ or in other words, $P_{k}^{n}= \dfrac{n!}{(n-k)!}$

This is known as a $k$-permutation of $n$.

The idea is here that we only "care" about the order of the first $k$ objects. The order of the other $(n-k)$ objects doesn't matter, hence they're left out of the equation.

## Permutations with Replacement

When talking about setlists, it makes total sense to assume that songs will not be played twice. This is not always how it works though. Imagine a bag with three marbles in it: a green one, a red one, and a blue one. Now we'll draw marbles three times in a row, but each time, we'll write down the marble color and *put it back in the bag* before drawing again.

Now the number of possible outcomes is $3 * 3 * 3$.

Generalizing this to $n$, this means that the number of permutations with replacement when having $n$ distinct objects is equal to $n^j$ where $j$ is the number of "draws".

## Permutations with Repetition

When using permutations, some elements may be *repeated*.

A classic example is using permutations on words. Let's say you have the letters of the word "TENNESSEE". How many different words can you create using these letters?

Simply saying that there are 9 letters so the answer is $9!$ does not give you the correct answer. Looking at the word TENNESSEE by itself, you can swap the 3rd and the 4th letter and have the same word. So the total number is less than $9!$.

The solution is to divide $9!$ by the factorials for each letter that is repeated!

The answer here is then (9 letters, 4 x E, 2 x N, 2 x S)

$\dfrac{9!}{4!2!2!} = 3780$

The general formula can be written as:

$\dfrac{n!}{n_1!n_2!\ldots n_k!}$

where $n_j$ stands for identical objects of type $j$ (the distinct letters in our TENNESSEE example). 

## Summary

Now you're well on your way to calculate all sorts of permutations using factorials - both for understanding the sample space, subsets, etc! Let's move on for some practice!
