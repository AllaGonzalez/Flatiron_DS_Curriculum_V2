
# Git Merge - Lab

## Introduction

It's time to continue to practice your git and bash skills! In this lab, you'll work primarily from the command line in order to create a git repository, create a development branch and practice merging updates into a master copy. Along the way, you'll see how python scripts can be run from the command line and continue to get more familiar with git and bash in general!

## Objectives

You will be able to:
    
* Initialize a git repository
* Add a branch to a git repository
* Merge updates from one branch into another

## Create a Local Folder to House the Git Repository

To start, create a folder from the command line. (Be sure to place this in a logical, organized location!)

## Initialize Git In Your New Folder

Still working from the command line, navigate into your folder and initialize git!

## Optional: Check What's Going On with `git status`

## Create a New Python File

From the command line type `nano numbers.py`.

Inside the file that opens write the following:

(use 4 spaces for the indentation on the second line)
```
for i in range(10):
    print(i**2)
```

Press Ctrl+X to exit and press Y to confirm that you wish to save your changes.

## Test Your Python File

Python files can be run from the command line with `python filename`.   
So in this case, let's practice running our super simple script with `python numbers.py`.
With luck, you should see the square numbers up through 81.

## Add and Commit Your Changes

Add and commit (with a comment) your new file.

## Create and Checkout a New Branch

Create a new branch called cubes and switch to it.

## Modify the Branch

Type `nano numbers.py` to open up the file again.

Change the file from

```
for i in range(10):
    print(i**2)
```

to

```
for i in range(10):
    print(i**3)
```

## Add and Commit the Changes to the Cubes Branch

Add and commit your changes to the cubes branch.

## Switch Back to the Master Branch

Now that we've made development changes in our new branch, we may wish to integrate them back into our master branch such as updating our production code. To do this, we'll switch back to the master branch and then merge the changes we made to our development branch.

## Merge the Changes from Cubes

Finally, let's merge the changes from the cubes branch into our master branch.

## Do a Couple Sanity Checks

Everything should have gone smoothly, but let's do a couple of checks to be sure. Try running the python file again and observe the output. Take a look a `git status` and see what the output is.

## Delete the Development Branch

While deleting branches should be cautionary, now that we've merged our changes into the master, we really don't need our development cubes branch anymore. To clean things up, delete the branch.

## Summary

Congratulations! In this lab, you practiced using multiple branches in git and merging your changes together. What's more, we also saw that you can use git locally with no remote connection to github if you wish!
