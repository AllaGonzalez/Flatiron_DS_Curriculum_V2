
# Bayesian Statistics - Recap

## Introduction

Well done! You covered a lot of ground in this section. From Bayes' theorem to some introductory NLP work, you now have the foundation to dive into the world of Bayesians!

## Objectives

You will be able to:

* Summarize Bayes' Theorem and potential applications
* Discuss various Naive Bayes algorithms
* Discuss the difference between Frequentists and Bayesian statistics


## Bayes' Theorem

To start, you investigated Bayes' theorem and some hypothetical examples.

$$ \large P(A|B) = \dfrac{P(B|A)P(A)}{P(B)}$$


## Bayesian Statistics


From there, you then went on to read more about some of the philosophical differences between Bayesians and Frequentists. Bayesians interpret probability as the level of confidence or belief in an event. In contrast, Frequentists view probability as the limit as the number of trials goes to infinity of successes versus trials. 

## MLE and MAP

In outlining the discussion of Bayesian techniques, you got an introduction to Maximum Likelihood Estimation and Maximum A Posteriori Estimation. In both, you saw methods for optimizing one's beliefs given certain information. This was used to estimate parameters for assumed distributions.

## Gaussian Naive Bayes

In moving to machine learning applications, you first investigated the Gaussian Naive Bayes classifier. This produced powerful results when applied to the two small datasets explored. To do this, you viewed each feature as a normal distribution using the mean and standard deviation for a particular subgroup. You then used these to find point estimates along the PDF and fed this through a multinomial Bayes setup.

## Document Classification with Naive Bayes

After exploring Bayes using normal distributions, you then investigated an offshoot to natural language processing. Due to insufficient preprocessing such as stop words, stemming and lemmatization, the performance of this algorithm was trivial. That said, the concepts should provide you with interesting questions as to other methods for adapting Naive Bayes algorithms to data of different forms.

## Summary

Again, quite a bit was covered in this section. There is certainly plenty of additional resources available if you wish to further dive into MLE, MAP or other Bayesian techniques. Bayesian inference can provide a powerful a powerful framework for quantifying and reasoning with uncertainty that has continued to gain popularity with additional computing resources. 
