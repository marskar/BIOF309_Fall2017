---
start: true
title: "The layers of computing"
teaching: 30
exercises: 0
questions:
- "Where, exactly, is my data? Where should it be?"
- "Where is the computer analyzing my data? Can I make it go faster?"
- "How do all of these places relate to each other?"
- "What is the shell and why do I care?"
- "What is python? What is IPython? What is Juypter?"
- "What are the tools we'll be using in the course?"
objectives:
- "Understand how the components in your computing stack relate to one another"
- "Understand the different ways of interacting with your computer and what the pros and cons are"
- "Explain when and why command-line interfaces should be used instead of graphical interfaces."
- "Explain the advantages of remote computing including cloud and high performance computing."
- "Explain how to access the NIMH dedicated computing resources in the most convenient manner."
- "Get exposed to IPython and learn it's strengths."
- "Learn shortcuts and hotkeys to make command line computing fast and efficient"
keypoints:
- "A shell is a program whose primary purpose is to read commands and run other
programs."
- "The shell’s main advantages are its high action-to-keystroke ratio, its
support for automating repetitive tasks, and that it can be used to access
networked machines."
- "The shell’s main disadvantages are its primarily textual nature and how
cryptic its commands and operation can be."
- "We will work on a remote instance of the linux operating system"
- "Although there are many ways to work remotely, we will use a graphical
interface using NoMachine."
- "We will use an IPython console to interact with the Python interpretter"
- "We will learn basic commands for working with the computer file system:
`pwd`, `ls`, `mkdir` and `cd`."
-  "Understand the difference between alias, system commands, and IPython magics"
- "Show how `cd` behaves differently because each system call is a subprocess"
---

## Getting started

* Connect to felix or helix using NoMachine
We'll be conducting this course using a remote desktop utility called
[NoMachine](http://www.nomachine.com). You should have already met with the DSST
staff to configure and test it. Open the NoMachine App and connect to
felix.nimh.nih.gov if you are an NIMH employee or have a temporary course account. If you work for
another institute you can use helix.nih.gov.
* Open Terminal from the Application-> System Tools menu
* We've setup a short script to get you started quickly in the NIH HPC (felix or helix). To run it, type:

~~~
source /data/DSST/scripts/repro_env_setup.sh
~~~
{: .bash}

* Start up an IPython window

~~~
jupyter qtconsole &
~~~
{: .bash}

Your screen should now look something like this:

![image_of_shell](../fig/HPC_desktop.png)

Before we do anything we should all type the following command. For now we
don't need to know what it does but it will help to avoid confusion as we learn
about our command line interface:


~~~
%automagic
~~~
{: .python}

~~~
Automagic is OFF, % prefix IS needed for line magics.
~~~
{: .output}


## Know who (or what) you're talking to

It's easy and common to click on an icon, open and window and typing, clicking,
and analyzing in that window without much thought about how or where those
commands are being executed and where the data is being stored. It's worth the
effort to take some time and understand exactly what your computing (stack)[https://en.wikipedia.org/wiki/Solution_stack]
looks like and exactly where everything is happening. Understanding this stack
can help you make your analysis more efficient and secure.

## Where am I?

The desktop you're looking at inside the NoMachine window is from a computer
that lives over in building 12B at NIH's high performance computing (HPC)
center. This computer (helix or felix) is separate from but closely affiliated
with the large cluster of computers known as the (Biowulf)[https://hpc.nih.gov/systems/].

NoMachine is a remote desktop program. It allows your to interact with the
remote computer (helix/felix) almost as if you were sitting right in front of
it. ((VNC)[https://en.wikipedia.org/wiki/Virtual_Network_Computing] is another common remote desktop program).

The window on the left of your NX desktop is running an IPython shell. On the
right side, there is a window running a (Bash) shell. A (shell)[https://en.wikipedia.org/wiki/Shell_(computing)] refer to a user interface. It is designed to allow the user, you, to interact with the computer in an efficient and convenient way. It's named a shell because it stands between the user and the "guts" of the computer system, which is called the kernel.

<img src="../fig/layers_of_computing.png" alt="The shell kernel metaphor" style="width: 600px;"/>


> ## Bash and tcsh shell vs. IPython 
> 
>_This is the first of many expandable boxes you'll see in these lesson. They provide a bit more 
> info that are not essential to the flow of the course. Only read them if you're interested._
> 
> We'll be working almost exclusively in the IPython shell in this course.
> IPython provides an easy way to explore and interact with your data that
> leverages the power of the Python programming language. The Bash shell is an
> extremely versatile tool designed to allow you to control and interact with
> files and your computer more generally. You've likely had exposure to Bash (or
> it's close cousin, tcsh) if you've used analysis packages like AFNI, FSL, and
> FreeSurfer. The Bash shell is a [great thing to
> learn](https://swcarpentry.github.io/shell-novice/), but we want to focus on
> teaching you reproducible computing concepts without getting bogged down in the
> syntax of too many different languages.
{: .solution}


> ## Challenge: Draw your stack
> 
> _Expandable orange boxes like this one contain challenges for you to try._
> 
> Draw a diagram to illustrate how the programs and computers listed below relate to one another.
> 
> * Your laptop
> * Helix & Felix
> * The Biowulf cluster
> * NoMachine Remote Desktop
> * IPython Shell
> * Angry Birds on your phone
> 
> Now get with your partner and compare your drawings. Discuss the difference and edit as needed.
{: .challenge}


## The Jupyter qtconsole

> ## A note on the IPython prompt
>
> ~~~
>  In [1]
> ~~~
> {: .source}
> The IPython prompt, as depicted above, sits before our blinking cursor. It
> consists of the word "In" followed by a number. It informs us that we are
> currently entering input. In this case the first input of the IPython kernel
> session. Every time we execute a command this number will increment by one.
 {: .callout}

The [Jupyter qtconsole](https://jupyter.readthedocs.io/en/latest/index.html) is
a developing environment that is optimized for interactive computing typical of
scientific analyses. It provides lots of convenient commands and shortcuts for
this. Different languages can be used with this interface. In our case we will be
using IPython. It provides us with a convenient interface to the system shell
and the Python interpreter. We will start by typing in the IPython command:

~~~
%pwd
~~~
{: .source}
~~~
/Users/this_user
~~~
{: .output}

This returns the present working directory, the file-system-context
for the commands that we execute. We can refer to these files by simply typing
their names. We can list these files by using the next command:
~~~
%ls
~~~
{: .source}

The `%ls` command returns all the files in the present working directory. When
we wish to perform actions on these files we can refer to them directly by
their names and the shell will understand which files we are referring to.
Later we will talk about how to add new files to the current directory but for
now we will use the `%mkdir` command to add a directory into our present
working directory:

~~~
%mkdir repro_course
~~~
{: .source}

## IPython magics and system commands

The above commands can be entered into the IPython in slightly different ways.
Instead of using the "%" sign we can instead use the "!" sign and we will still
get the same results (although we will not be able to make the same directory
again).

~~~
!pwd
!ls
!mkdir repro_course
~~~
{: .source}
~~~
/Users/this_user
... A list of files in the current directory...
mkdir: cannot create directory `repro_course': File exists
~~~
{: .output}

When we use the "%" sign it denotes that the command is an "IPython magic". These
are special commands available in IPython that make doing some common tasks
easier on the command line. The "!" instead evalutate the command with the system
shell. On a Linux or Mac OSX operating system this will likely be the Bash
shell. All of these commands exist in Bash; however, on a Windows operating
system the pwd system command does not exist. You can see we have to be careful
about using system commands. Some will be operating system dependent. Since the
IPython magics will work regardless of the operating system used, we shall
instead use those when we can.

## System commands start a new sub-process
Apart from the different system commands across platforms there is another
reason we might have a preference for IPython magics. Each system command starts
up a sub-process, executes the commands, and then closes. The effect of this can
be seen very easily when we use the "!cd" system command to change directories.

~~~
%pwd
!cd repro_course
%pwd
~~~
{: .source}
~~~
/Users/this_user
/Users/this_user
~~~
{: .output}

This would not be the behavior we would wish from a command that changes our
present working directory. This occurs because the changes made to the
environment in the sub-process are not propagated back to the IPython shell. If
we use the IPython magic `%cd` we get the behavior we want.

~~~
%pwd
%cd repro_course
%pwd
~~~
{: .source}

~~~
/Users/this_user
/Users/this_user/repro_course
/Users/this_user/repro_course
~~~
{: .output}

*  As we work through the course we will continue to learn some convenient
shortcuts available to use in the IPython shell; however, most of the time we
will be writing commands that are in the Python language.

> ##  Understanding the file folder metaphor
> 
> Working on the command line requires a fluid understanding of how a file system is organized. 
> Most file systems use the [file folder metaphor](https://en.wikipedia.org/wiki/Directory_(computing)#Folder_metaphor) to provide a system that would be familar to most computer users. 
> This is also sometimes referred to an (inverted) directory "tree". When someone asks you 
> to "change up one directory" they are referencing this metaphor.
> 
> If you'd like a bit more practice understanding and navigating a directory tree, check out [this lesson](http://swcarpentry.github.io/shell-novice/02-filedir/) at Software Carpentry. There are also some exercises available at [Code Academy](https://www.codecademy.com/learn/learn-the-command-line).
> 
> 
{: .solution}

## Convenient commands to remember

*   Use tab completion when possible. The computer is more precise than we are.
*   We can cycle through previous commands using up and down arrows.
*   We can cycle through previous commands starting with the current text using
Ctl + n/p.
*   Enter,  Ctl + Enter / Shift + Enter allow us to run commands in different
ways.
