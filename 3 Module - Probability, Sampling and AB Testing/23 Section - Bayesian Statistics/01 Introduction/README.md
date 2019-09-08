
# Bayesian Statistics - Introduction

## Introduction

In this section, you'll investigate the Bayesian statistical framework. Bayesian statistics are an alternative perspective to classical Frequentist approaches which you've seen thus far. Bayesian statistics applies reasoning to unknown probabilities in a manner which the frequentist approach does not allow. 

## Objectives

You will be able to:

- Discuss the concept of Bayesian statistics
 
## Thomas Bayes
 
Bayesian statistics owes its name to the famous mathematician Thomas Bayes. Born (sometime) in the early 1700s, he bucked many academic traditions of his time due to his families religious beliefs. Cambridge and Oxford were known for the most prestigious mathematics of the time, but Bayes was a Presbytarien barring him from these universities which had ties to the Church of England. 

## Bayes Theorem

Bayes Theorem is a method for rewriting conditional probabilities. The formula is:

### $$ P(A|B) = \dfrac{P(B|A)P(A)}{P(B)}$$

In the following lessons, you'll learn more about 2 traditional interpretations of this formula. The first provides an intuitive understanding, viewing the numerator as the probability of both A and B occuring:  

### $$ P(A|B) = \dfrac{P(A \cap B)}{P(B)}$$

This should make perfect sense: the probability that A is true, given B is true, is the probability that A and B are both true, divided by the probability that B was true in the first place. 

The second interpretation of Bayes theorem leads straight into the Bayesian statistical framework itself, bringing about discussions of priors, likelihoods and posterior probabilities.

## Naive Bayes

After setting the ground for Bayesian statistics with plenty of theory and practice of Bayes' theorem itself, you'll take a look at using Bayes' theorem to perform some classification tasks. Here, you'll see that Bayes' theorem can be applied to multiple variables simultaneously. While multinomial bayes has assumptions such as linear independence, which may not be met, (hence its naivety) it can nonetheless provide strong results in scenarios with clean and well normalized datasets.

## Summary

Get ready to jump in! This section provides an exciting introduction to Bayes theorem and Bayesian statistics, further rounding out your statistical toolbox!
