
# Section Recap

## Introduction

Congratulations, you just finished learning about and implementing recommendation systems! In this lesson, you'll get a brief recap of what you covered in the recommendation section. 

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

The key takeaways from this section include:

* Recommendation approaches can consist of simply recommending popular items (without personalization), or using algorithms which takes into account past customer behavior
* When using algorithms, the two main types are content-based algorithms (recommending new content based on similar _content_), or collaborative filtering based (recommending new content based on similar types of _users_)
* Collaborative Filtering (CF) is currently the most widely used approach to build recommendation systems
* The key idea behind CF is that similar users have similar interests and that a user generally likes items that are similar to other items they like
* CF is filling an "empty cell" in the utility matrix based on the similarity between users or item. Matrix Factorization or Decomposition can help us solve this problem  by determining what the overall "topics" are when a matrix is factored
* Matrix Decomposition can be reformulated as an optimization problem with loss functions and constraints
* Matrix Decomposition can be done using either Singular Value Decomposition (SVD) or Alternating Least Squares (ALS)
* Spark's ALS implementation can be used to build a scalable and efficient recommendation system

# Summary

You've really only scratched the surface of what it is possible to accomplish with recommendation systems, as there are more and more advanced recommendation systems coming out every day using hybrid and deep learning approaches. You can apply the skills you've learned related to recommendation systems to almost any industry.
