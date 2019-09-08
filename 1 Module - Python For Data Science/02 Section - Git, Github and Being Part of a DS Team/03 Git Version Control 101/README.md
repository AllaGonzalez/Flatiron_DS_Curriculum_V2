
# Version Control 101

## Introduction

> “The past is never where you think you left it.” — [Katherine Anne Porter](http://en.wikipedia.org/wiki/Katherine_Anne_Porter)

Version Control is the process of storing multiple versions of a single project, allowing each version to be recalled at a later date.

There are a lot of different ways to do version control. You could save a new file every time you make a change, timestamp that file, and place all of those files into a timestamped folder. You could track all of your changes in a spreadsheet with copious notes. Or you could use dedicated version control software. Guess which method programmers use?


## Objectives

You will be able to:
* Understand the reason for using git

## Why Use Version Control?

Let's think about the future for a second. It's a year or two down the road, and you're working at your dream job (YAY!). You just deployed a new chat feature for the app you're working on. Suddenly, your boss runs over to your desk: "Wait! We can't deploy the chat yet! Revert! Revert!"

What do you do? You need to find all of the new code you pushed to the server and delete it. Then you need to find the old code, test it, and re-upload it. So much work to do. Well, since you used version control software, it's as easy as 1, 2, 3. Actually, it's as easy as `git reset --hard <commit id>`... but we'll get to that later. Using version control is useful because it allows you to easily rollback to a previous version of your application, saving you a ton of extra work and time.

There are a lot of advantages to version control. It's a great way to keep a backup of your work, it facilitates collaboration, and it gives you the freedom to experiment and try new things without messing up the code base.

## Local vs Remote Version Control

A local version control system stores all of the information on your computer, locally. This system works great while you work on a project by yourself. However, it becomes cumbersome when you attempt to collaborate.

Some organizations use a centralized repository on a company server. Think of a repository as a big folder that stores all of the files of a particular project. It is simply the location where a project's data is stored. Users pull only the files they need to work on from the server. The advantage is that multiple people can collaborate and work on the same project at once. The disadvantage of this process is that a user must be connected to the network in order to work on the project.

Which brings us to the third system, a distributed version control system. In a distributed system, all users have a complete copy of the entire repository. This means that you can work on the project independent of any network connection. Upon reconnecting, you can push your changes to the server and merge with the server's repository.

## Meet Git

Git is the distributed version control system we use here at The Flatiron School. Git began in 2005 and has quickly grown to be one of the most widely used version control systems in the industry. Because so many companies use Git, it's important that you get used to working with it. We also use GitHub, a popular remote repository hosting service built to integrate seamlessly with Git.

Check out some of the resources below to learn more about Git.

## Resources

* [Getting Started - About Version Control](http://git-scm.com/book/en/Getting-Started-About-Version-Control)
* [Git Basics - What is Git?](http://git-scm.com/video/what-is-git)

## Summary

In this lesson, you were introduced to version control and Git!
