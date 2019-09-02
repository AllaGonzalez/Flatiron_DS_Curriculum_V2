
# Setting up a Professional Data Science Environment

## Introduction
If you might want to become a professional data scientist, it’s important to take a little time to “set yourself up for success” by installing and learning to use the right tools on your computer. If you already have Git and Anaconda installed, feel free to jump down to the cloning, virtual environment setup and testing towards the bottom of the page.

## Objectives
You will be able to:
* Install a professional data science environment

## What Tools do Professional Data Scientists Use?
* **Python** - There are many languages that can be used for data science, but these days most data scientists are using Python to write their code.
* **Jupyter Notebook** - Most of those data scientists use Jupyter Notebook for writing their Python. Jupyter Notebook is a tool that allows you to mix comments in-between your code snippets so you can document and share your thinking process and make it easier for others to review, replicate and expand on your work. It's also what we're using for almost all of our lessons in this course!
* **Anaconda** - Anaconda is one of the most popular ways for data scientists to install Python and Jupyter Notebook on their computers. It also provides package management and virtual environments so you can get all the latest data science tools running like NumPy, SciPy, and Tensorflow, and so you can use different versions of Python and your packages for different projects without them conflicting with each other.
* **Git** - Git is a version control system. It’s a way of keeping track of all the changes made across your project. Think of it like “track changes” in Word - but with the ability to track changes across multiple documents. At Flatiron School, we use Git to keep track of all of the lessons we create and all the changes we make to them.
* **GitHub** - GitHub is a website where data scientists (and programmers) can save their work in case their computer breaks, and share it with their team or the world! At Flatiron School, we store all of our lessons on GitHub.

It’s going to take us a few minutes to get this all installed, but once we do, not only will you be set-up for working through the course, but you’ll also have a professional data science setup on your computer for any future courses or projects you want to work on!

## Computer Prerequisites
There are many amazing computing devices available these days, but not all of them will allow you to do data science. We love smartphones, flip phones, Chromebooks, tablets (including iPads), game boys, Nintendo switches, roku’s and arduino’s. You’re not going to be able to complete this course on any of those devices - sorry.

You’re going to need a computer (laptop or desktop). It should be running a recent (last 3-4 years) version of MacOS, Windows or Linux, and ideally, it should have 8Gb of RAM and at least 20Gb free hard drive space. More information [here](https://flatironschool.com/wp-content/uploads/Student-Facing-Computer-Requirements.pdf):

Assuming you have a computer that meets the requirements, let’s start by getting git Installed.

## Installing Git
For each tool, we’ll provide installation instructions for the two most common operating systems - Windows and MacOS.


## Windows
Go [here](https://git-scm.com/download/win). Then double click on the downloaded exe file. It may open a window asking if you want to allow this application to make changes to your device. Just click “yes”. It will then open the installer. Click “next” to accept the license, and when you “select components” on the next screen make sure to keep the “Windows explorer integration” options checked.

Note - if there are any differences in the options provided in the installer you download, just accept the defaults - they’ll probably be fine!

![screen-1](http://curriculum-content.s3.amazonaws.com/data-science/screen-1.png)

When asked to select an editor, if you’re familiar with vi/vim feel free to use that, otherwise you should probably select an easier to use text editor such as nano.

![screen-2](http://curriculum-content.s3.amazonaws.com/data-science/screen-2.png)

When asked to adjust your PATH environment, either of the first two options is fine as you’ll mainly be using Git from the new “Git Bash” program that is being installed. You’re probably best to select “use Git from the Windows Command Prompt” as it’ll give you the option of using it there in the future if you wish.

![screen-0](http://curriculum-content.s3.amazonaws.com/data-science/screen-0.png)

For https, you should select the “use the OpenSSL library” option.

![screen-3](http://curriculum-content.s3.amazonaws.com/data-science/screen-3.png)


Select the default option for handling line endings

![screen-4](http://curriculum-content.s3.amazonaws.com/data-science/screen-4.png)

And use MinTTY as the default terminal emulator

![screen-5](http://curriculum-content.s3.amazonaws.com/data-science/screen-5.png)

For extra options, enable the file system caching and the git credential manager.

![screen-6](http://curriculum-content.s3.amazonaws.com/data-science/screen-6.png)

And then wait while Git is installed onto your computer.

![screen-7](http://curriculum-content.s3.amazonaws.com/data-science/screen-7.png)

Finally, click finish to complete setup

![screen-8](http://curriculum-content.s3.amazonaws.com/data-science/screen-8.png)

#### MacOS
If you are comfortable with the command line and have installed [homebrew](https://brew.sh/), you should install Git by running the command `brew install git` in a terminal window.  

If you have no idea what the last paragraph meant, just go [here](https://git-scm.com/download/mac). Then double click on the downloaded dmg file and it will open a small finder window looking something like this (the exact name and version will change over time):


<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-10.png' width="750">

Double click on the .pkg file to run it. When you try to do that you might get a security warning pop up that looks something like this:


<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-11.png' width="550">

If that happens, just click on the apple at the top left of the screen, select “system preferences” from the drop-down menu. Then select “Security and Privacy”, select the “General” tag, click on the lock to make changes at the bottom of the window (you’ll have to enter your password). Below the “Allow apps downloaded from” option, you should see a message stating that an app was blocked from opening. (If you don’t see this message, double click on the .pkg file again and then look back at the Security & Privacy screen and it should pop up).  Click the “open anyway” button.

You should then see a message confirming whether you really want to open the app.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-12.png' width="550">

Click on the “open” button. You should then see an installer screen.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-13.png' width="650">

Click “continue”, then “install”, enter your password when prompted, and when the installation is complete, click the “close” button.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-14.png' width="650">


## Confirming your git installation (all OS’s)

To confirm you have installed Git successfully, open a terminal window (in Windows, using the start menu, open the “Git Bash” program to get a terminal, on a mac, just open the “Terminal” app in the “Utilities” folder within your “Applications” folder). Type `git --version`. It should return the version of git you are running.

While you’re in the terminal, you should also set up your name and email address.

Type `git config --global user.name`

If it returns your name, you’re set! If it returns nothing or displays an error message, type `git config --global user.name “Your Name”` - replacing Your Name with your name.

Type `git config --global user.email`

If it returns your email address, you’re set! If it returns nothing or displays an error message, type `git config --global user.email your@email.com` - replacing your@email.com with your email address.

## Installing Python and Jupyter Notebook via Anaconda

The easiest way to get set up with Python and Jupyter Notebook so you can start coding is to install the Anaconda distribution. Let’s go through the install instructions  for the two most common operating systems - Windows and MacOS.

#### Windows
Go [here](https://www.anaconda.com/download/#windows) and click on the “download” button for the Python 3.x (currently 3.6) version of Anaconda.

![screen-15](http://curriculum-content.s3.amazonaws.com/data-science/screen-15.png)

A window may pop up asking if you want to give Anaconda your information in return for a cheat sheet - you do not need to do so unless you want to.

You should see in the bottom of your browser window that a .exe file is being downloaded. When it finishes downloading, click on the arrow to the right of the name of the file in the bottom left corner of your browser, and select “open”.

![screen-16](http://curriculum-content.s3.amazonaws.com/data-science/screen-16.png)

If you don’t see the file in your browser, you can also just open up Windows Explorer, navigate to the “Downloads” directory and double click on the Anaconda file in the list to open it.

![screen-17](http://curriculum-content.s3.amazonaws.com/data-science/screen-17.png)

That will open the Anaconda installer which will install the software for you on your computer.

![screen-18](http://curriculum-content.s3.amazonaws.com/data-science/screen-18.png)

Click “next”, then “I agree” to accept the license, and you can install for “just me”, clicking next. Then select the destination folder (the default should work for most people).

![screen-19](http://curriculum-content.s3.amazonaws.com/data-science/screen-19.png)

On the next screen, make sure to check the "Add Anaconda to my PATH environment" checkbox. It will inform you that it's not recommended, but this is required to be able to access Anaconda from the command line and the final instructions in this guide won't work unless you check this box. Then click “install”.

![screen-20](http://curriculum-content.s3.amazonaws.com/data-science/screen-00.png)

This step may take a few minutes.

![screen-21](http://curriculum-content.s3.amazonaws.com/data-science/screen-21.png)

Once the installation is complete,

![screen-22](http://curriculum-content.s3.amazonaws.com/data-science/screen-22.png)

Hit “next”. You can skip the Visual Code Studio installation

![screen-23](http://curriculum-content.s3.amazonaws.com/data-science/screen-23.png)

And then finally click “finish”.

![screen-24](http://curriculum-content.s3.amazonaws.com/data-science/screen-24.png)

It’ll open up a browser window which you can just close down.

![screen-25](http://curriculum-content.s3.amazonaws.com/data-science/screen-25.png)

And that’s the process of installing Anaconda. The next step is to test your installation.

#### Mac
Go [here](https://www.anaconda.com/download/#macos) and click on the “download” button for the Python 3.x (currently 3.6) version of Anaconda.

![screen-26](http://curriculum-content.s3.amazonaws.com/data-science/screen-26.png)

You should see in the bottom of your browser window that a .pkg file is being downloaded. When it finishes downloading, click on the arrow to the right of the name of the file in the bottom left corner of your browser, and select “open”.

![screen-27](http://curriculum-content.s3.amazonaws.com/data-science/screen-27.png)

If you don’t see the file in your browser, you can also just open up the finder, navigate to the “Downloads” directory and double click on the Anaconda file in the list to open it.

![screen-28](http://curriculum-content.s3.amazonaws.com/data-science/screen-28.png)

You’ll be informed that the package will run a program to see whether the software can be installed. Click “continue”.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-29.png' width="600">

You’ll then see a wizard that will run you through the installation process. Click continue on the first screen.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-30.png' width="600">

Then look at the read me, and click “continue” again.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-31.png' width="600">

You’ll then need to accept the license. Start by clicking “continue”

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-32.png' width="600">

And then click on “agree” in the dialog that comes up and asks you to accept the license.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-33.png' width="600">

Then click on “install” to install the software.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-34.png' width="600">

And you’ll have to enter an administrative username and password for your computer to finally install the software.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-35.png' width="600">

The wizard will let you know next that it’s preparing the install, and then it’ll take a couple of minutes to install all of the necessary software.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-36.png' width="600">

You’ll be given the option to install Microsoft VSCode. For now, you can skip that option by clicking “continue”.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-37.png' width="600">

You should then see a final window informing you that the software was installed successfully. Click close to finish the installation.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-38.png' width="600">

If you’re asked whether you’d like to move the installer to trash, click the “Move to trash” button.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-39.png' width="600">


## Testing your installation

To test your installation, on Windows, click on Start and then Anaconda Navigator in the program list (or search for Anaconda in the search bar and select Anaconda Navigator). On a Mac, open up the finder, and in the Applications folder, double click on Anaconda-Navigator.

From now on, screenshots will be from a Mac, but we’ll highlight any material differences in the experience between the OS’s.

The Anaconda Navigator is one of the ways you’ll be able to run Jupyter Notebooks. Click on the “launch” button in the Jupyter notebook tile.

![screen-40](http://curriculum-content.s3.amazonaws.com/data-science/screen-40.png)

On a Mac, you’ll see a terminal window pop up.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-41.png' width="600">

On both Windows and a Mac, you’ll see a window in your web browser that allows you to open existing Jupyter notebooks or create a new one.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-42.png' width="1000">

Click on the “New” button in the top right corner.

![screen-43](http://curriculum-content.s3.amazonaws.com/data-science/screen-44.png)

And select “Python 3” from the drop-down list.

When you do, you’ll see a new notebook in your browser window that looks something like this:

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-43.png' width="650">

To make sure it’s working, click in the cell and type the following:

```
import sys
print(sys.version)
```

Then hold down the shift key and hit enter to run the code in the cell. You should see an output something like this.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-45.png' width="600">

Don’t worry if the version number or date is slightly different. If you get a similar output (something that isn’t an error message), congratulations! You’ve got Anaconda, Python and the Jupyter notebook installed successfully!

To shut down Jupyter notebook, just close the tabs in your browser containing the notebook and the list of notebooks. On a Mac, you should also click on the terminal window and hit “ctrl-C” to close the notebook.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-46.png' width="600">


You’ll then have to hit “y” and return to confirm that you want to close down Jupyter notebook.

## Cloning this Repository

To finish this setup process, you’re going to need to download a copy of the files in this repository. To do that, you need to start by opening a terminal window.

If you’re on a windows machine, select “git bash” from either the start menu or the search bar and it’ll open up a terminal (don’t use the default Windows terminal - it will not work for this). If you’re working on a mac, open the “Terminal” app in the “Utilities” folder within your “Applications” folder.

Let’s type `pwd` to “print the working directory. It should be somewhere you are OK downloading files to. If not, feel free to use the “cd” command to change directory to one you’d like to work from.

Then type (or better still, cut and paste) `git clone https://github.com/learn-co-curriculum/dsc-1-01-05-setting-up-environment`

*In Windows, in git bash, to paste from the clipboard the shortcut should be `ctrl-shift-insert`*

This will create a new subdirectory called dsc-1-01-05-setting-up-environment which will contain a copy of all of the files from this repository. Go into that directory by typing `cd dsc-1-01-05-setting-up-environment` (after typing `cd dsc` you should be able to hit the tab key to "tab complete" so you don't need to type the whole directory name. That should work on both Windows and Macs.

## Setting Up Virtual Environments

As you do data science projects, you will spend a lot of your time using pre-written libraries to speed up your development. Examples include NumPy, Pandas and scikit-learn. As you work on different projects, you may also find that you end up using different versions of different libraries for different projects. The most common versioning issue is that some projects will run in Python 2 whereas others will run in Python 3, but you may also find that different projects depend on different versions of libraries like Tensorflow.

Occasionally, code that works in an old version of a library won’t work in a newer version. So if you open up a new project and install the dependencies, it’s possible that your old project won’t work anymore.

To avoid that problem, a best practice is to use “virtual environments”. Virtual environments allow you to have different versions of Python and different versions of the various libraries you use, so you can install a new version of a library for one project but still use the old version for another project. It’s almost as if you have multiple computers that you can swap between, each having a different setup and configuration, just by running a couple of commands.

There is a build in virtual environment feature in Python, but we’re going to use the more flexible virtual environments provided by Conda as part of the Anaconda distribution you installed.

To use a new virtual environment, there are two steps you need to complete. The first step is to create the virtual environment. That may take a couple of minutes as your computer has to download the necessary version of Python and all of the libraries that you want to be able to use in that environment. The next step then is to “use” the virtual environment by activating it.

If you want to learn more about Conda environments, have a look at the [documentation](https://conda.io/docs/user-guide/tasks/manage-environments.html), otherwise, let’s give this a try.

You need to start by navigating into the root of this project folder, so you’re going to want to type `cd  dsc-1-01-05-setting-up-environment` in your terminal if you didn't already.

Then to create the environment, on a mac, type `conda env create -f environment.yml`. On windows, type `conda env create -f windows.yml`. Depending on the speed of your computer and your internet connection it may take up to five minutes for this to complete. While it does you should see output similar to that displayed below start to appear in your terminal.

<img src='http://curriculum-content.s3.amazonaws.com/data-science/screen-47.png' width="750">

If you see a message that states “WARNING: A newer version of Conda exists”, run `conda update -n base conda` and then try again to create the environment using `conda env create -f environment.yml`.

Next, try activating the environment. Whether you're on a Mac or using git bash on a windows machine, type `source activate learn-env` (if you have an issue with running git bash, the command to activate Conda within the Conda shell on windows is `activate learn-env`).

To confirm that it worked, type `conda info --envs` and confirm that the output in the terminal ends with /learn-env - e.g. *  /Users/peterbell/anaconda3/envs/learn-env


## Updating your Virtual Environment

Every so often we create new versions of the virtual environment and we'll ask you to update your virtual environment. To do that, download the latest version of this repository with the latest changes. Then go into a terminal window and:
```
source activate base # To make sure you're not in the learn-env environment
conda remove -n learn-env --all # To get rid of the environment
conda env list # Make sure it doesn't list learn-env - if it does, try the last step again
# Then to re-create the environment from the latest environment file
# On a Mac
conda env create -f environment.yml
# Or in Windows a Mac
conda env create -f windows.yml

```

## Configuring your Kernel

Jupyter Notebooks run "kernels" - the computational engine used for executing your code. It's important to be running the right kernel within your notebook, otherwise you may get errors stating that you don't have a particular package or have the wrong version of it or even complaints about the version of Python you're running (some packages that work with Python 3.6.6 don't currently support Python 3.7, for example).

It is essential to run `source activate learn-env` (if you have an issue with running git bash, the command to activate Conda within the Conda shell on windows is `activate learn-env`) every time you start a new terminal window that you are going to use to either run a Jupyter Notebook or your tests. If you don't do this you **will** get errors, so please check this first. If you are not sure whether you have activated the environment, in the terminal type `conda list -f obscure` and it should show you that you have v1.0.1 of the "obscure" package. If it doesn't show that, (re)run (`source`) `activate learn-env`.

However, there is one more step you need to perform. Firstly you need to ensure your terminal is running the learn-env virtual environment so you have the necessary packages. Then you need to go into your Jupyter Notebook and when viewing a notebook, click on "Kernel" in the top bar, then "Change Kernel" and then pick the learn-env kernel. You must make sure you're running the learn-env kernel whenever you're working in a Jupyter Notebook.

If for any reason you don't see the learn-env option in the drop-down list of kernels, exit the notebook in the browser, close down the notebook server, and in the terminal type `python -m ipykernel install --user --name=learn-env` - that will add the learn-env to your list of kernels and when you restart the Jupyter Notebook server and then open a notebook, you'll be able to select the learn-env option from the list of kernels.

## Summary

Congratulations! If you've gotten this far and everything has worked, you have a great baseline setup for working as a professional data scientist!


