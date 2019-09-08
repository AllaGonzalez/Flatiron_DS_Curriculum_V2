
# Git, Github and Being Part of a Data Science Team - Section Recap

## Introduction

In this section you took a look at how git is used for collaboration as part of a development team. This started by practicing navigating directories using the command line and continued by further investigating git commands. You practiced creating and maintaining git repositories including adding, committing and pushing changes. You saw how to make multiple branches and then merge changes back into the master branch. You also saw how to navigate merge conflicts when the same line of the same file has been edited in both branches trying to be merged. Be sure to continue to head back to the PEP8 and git documentation for clarification, review and learning more commands and arguments or style suggestions. 

On top of all that, you then did a data analysis project using word frequency! Nice work! To wrap it all up, here's a review of some concepts and some tips for how to continue to pull up documentation and find help on the fly!

## Objectives

* Understand the purpose of git
* Review the `cd`, `ls`, `pwd`, `mkdir` and `nano` commands
* Be able to retrieve git documentation
* Interpret and implement git documentation
* Review `git add` command arguments 
* Revieiw `git stash`
* Review git merge conflicts


## Bash and the Command Line

Recall some of our primary tools for navigating the command line: `cd`, `ls`, `pwd`, `mkdir` and `nano`. You can use `cd ..` to move up a directory level and `cd ~/Documents` for folders starting at the user's home directory. You can use `ls -a` to view hidden files and `ls -la` for a long listing of all files. (Again the `l` argument is for long form and the `a` in both cases for all files, including those beginning with `.` indicating that they are hidden.) You can also make directories with the `mkdir` command. You saw how to use `nano` to make and edit files from the command line. Other editors such as emacs and vim can be worthwhile if you are doing more substantial command line editing. 

## Git Background

Remember that git was not only designed as a version control system, but a means for collaborative development. It was originally released in 2005 by Linus Torvalds, to help facilitate development of the Linux kernel. While there is still much to learn about git, you saw some of the primary concepts all developers interact with when using git to collaborate on projects. 

## Git Commands

You've seen a decent amount of `git commands` including `git add`, `git commit`, `git branch`, `git checkout` and `git merge`. Also very important is to know how to access documentation so that you can both review and extend your knowledge. For example, to see a list of git commands in general, start with `git --help`. 

<img src="images/git_help.png" width="700">

You can then also review individual commands with 'git help <command>' such as `git help add` (Afterwards press `q` to quit the commands documentation.)

<img src="images/git_help_add.png" width="1200">

In the synopsis, you can see optional parameters such as in `git add --all` which you previously used before. 

Similarly, for the commit documentation, take a look at `git help commit` (and subsequently use `q` to quit.)

<img src="images/git_help_commit.png" width="1000">

Here, you might notice additional arguments that you can begin to use, such as `a`, which you see listed in the synopsis.  Then, if you look under the options header, you will see a full description.

<img src="images/git_help_commit_options.png" width="900">

So for example, you could combine this with the `m` option as `git commit -am "your commit message"`. (Indeed this is a useful shortcut; by doing this you can bypass the `git add` command in your workflow in updating files being tracked by git.)

At some point, you will also run into some trouble with git and have merge conflicts or other idiosyncracies between versions of your code. You have seen how git annotates merge conflicts, and can also use git stash to temporarily store changes.

## Summary

Once again, preliminary tools such as the command line and git are foundational to managing projects and maintaining code. Similarly, knowing how to access further information quickly is also an indispensable soft skill. Be sure to continue to organize work, modularize, and use version control. Also, keep in mind PEP8 and be thoughtful of how you organize, comment and structure your code. All of these will make you a stronger programmer and data scientist.
