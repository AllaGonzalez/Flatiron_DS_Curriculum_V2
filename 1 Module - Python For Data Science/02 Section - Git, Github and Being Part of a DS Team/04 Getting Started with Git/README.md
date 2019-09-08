
# Getting Started with Git

## Introduction 
As you now know, git is a version control system. The Learn platform at Flatiron school has a deep integration with Git and GitHub. GitHub is an online hosting platform that uses git. We need to teach you just enough git to interact with GitHub like a real developer. While you can run python notebooks on the Learn platform itself, you'll also want to be able to download material to your local computer so you can work on it there.

## Objectives

You will be able to:

* Fork a repository from GitHub to create your own local copy.
* Use `git clone` to clone a repository to your local computer.
* Use `git status` to see the status of your locally cloned git repository.
* Use `git add .` to add your local changes to be committed.
* Use `git commit -am "Commit Message"` to commit changes that have been added with a message.
* Use `git push` to upload your local changes to GitHub.


## Some terminology and concepts

As you can see from the objectives above, we're going to dive in and use several git commands in this lesson. 

The first that we'll use is `forking`, a concept from the github platform.

Forking is the process of making a personal copy of the Learn lab on GitHub. It's basically how you tell Learn that you have started working on a lab.

![What's a Fork](http://ironboard-curriculum-content.s3.amazonaws.com/front-end/lab-assets/git-workflow-1.png)
  
Afterward, we'll then use `git clone` from a bash shell like terminal or git bash in order to copy the material from the web to our local computer.

From there, git will allow us to continue to track and incorporate changes that we make to our work. 

`git status` allows us to see if we have made any changes.

If we have made changes that we would like to save to our version control history, we can then use `git add` to add the changed files to the version history and `git commit` to finalize the process. As a final process, we can then use `git push` to push our changes to the web so that we or collaborators can access them from anywhere. 

Now that you have a brief overview of what we're about to dive into, let's go through the process step by step.

## Open up a Bash Shell and Create a Course Folder / Subfolder

To use git, we're going back to the bash shell (mac: terminal, windows: git bash) once again!
To start:

* Create a folder on your computer for your course materials and navigate into it. (mkdir and cd) 
* Then create a subfolder titled "Section1", "Bash_and_Git" (or whatever you find to be an appropriate title) and navigate into that.

* Return to your web browser and navigate to the lesson you want to download.
* Click the github icon

<img src="images/learn_github_logo.png">


You'll be redirected to the associated github repository like this.  
<img src="images/github_fork_button.png">

* **Click the fork button**, as shown above in order to create a copy to your personal account which you can edit and update.

After a moment of this:

<img src="images/github_forking_in_progress.png" width="650">


You'll be redirected to your new personal copy of the repository:

<img src="images/forked_github_page.png" width="850">

## `git clone`

Now that you have your own copy (by forking), we're going to download a copy to your local computer using git clone.

* Copy the URL. 
    * Mac: Press **cmd+L** to highlight the url bar and **cmd+c** to copy the url
    * Windows: Press **Ctrl+L** to highlight the url bar and **Ctrl+c** to copy the url

* Return to your bash shell

* Type: **git clone** and paste your repo url (**cmd + v** or **Ctrl+V**)

** Voila!  **

The repository and all of its contents will be downloaded locally to your computer!

You should be able to see the new folder by listing the files in the current directory with `ls`.  
You can then navigate into the git directory with `cd directory_name`.

Now that you have a local copy, we can further investigate some more git commands for version control. **Note that for these to work you must be in the git folder (the one we just cloned above). Make sure to navigate into the folder using the `cd` command.**

## `git status`

Once you have a git repository locally, git will keep track of every change you make to the code in that folder. You can ask git what the differences or changes you've made since the last commit by typing `git status` into your terminal.

It's really helpful to constantly get the status from git to see what changes you need to stage, add, commit, or push.

## `git add`

Adding changes with the `git add` command is a way to stage any changes and get them ready to become a permanent record in your git log via a commit. The workflow worth memorizing right now is to simply add all your changes via `git add .`.

## `git commit`

A commit is a permanent moment in time in your git history. A commit creates a new version of your code. To commit, memorize this command. `git commit -am "Your commit message"`. You are using the `git commit` command with the flags `-am`, which tell git to commit all the changes and to include a commit message. You supply the commit message in `""` directly in the command, `"Your commit message".


## `git push`

Pushing is the process of taking your local code and commits and syncing them, or uploading them, to GitHub. You're updating the GitHub remote (remotes are just fancy names for copies of the repository), generally your fork, represented by a remote named `origin`, by pushing your code to the remote. The git command to do this is simply `git push`. When you `git push` from within a git repository, it will take all the commits that you have locally and push them to the online remote.


## Additional Resources

[GIT Cheatsheet](http://www.git-tower.com/blog/content/posts/54-git-cheat-sheet/git-cheat-sheet-large01.png)

[GIT Best Practices](http://www.git-tower.com/blog/content/posts/54-git-cheat-sheet/git-cheat-sheet-large02.png)

[Understanding the GitHub Flow](https://guides.github.com/introduction/flow)

[Hello World GitHub](https://guides.github.com/activities/hello-world)

[Forking on GitHub](https://guides.github.com/activities/forking)

[Git - The Simple Guide](http://rogerdudler.github.io/git-guide/)

[Git Immersion](http://gitimmersion.com/)

[Try Git](http://try.github.com/)
<p data-visibility='hidden'>View <a href='https://learn.co/lessons/enough-git-for-learn-co' title='Enough Git for Learn'>Enough Git for Learn</a> on Learn.co and start learning to code for free.</p>

## Summary

In this lesson, we took an introductory look at git and github. First, we saw how to fork and clone repositories from Learn ot your local machine. From there, we then further discussed how to add changes to git, commit them, and push them online.


