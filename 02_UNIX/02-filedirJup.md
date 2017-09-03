
## Navigating Files and Directories
Teaching: 15 minute
Exercises: 0 minute

Questions:
- "How can I move around on my computer?"
- "How can I see what files and directories I have?"
- "How can I specify the location of a file or directory on my computer?"

Objectives:
- "Explain the similarities and differences between a file and a directory."
- "Translate an absolute path into a relative path and vice versa."
- "Construct absolute and relative paths that identify specific files and directories."
- "Explain the steps in the shell's read-run-print cycle."
- "Identify the actual command, flags, and filenames in a command-line call."
- "Demonstrate the use of tab completion, and explain its advantages."

Key Points:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- "Directories can also store other directories, which forms a directory tree."
- "`cd path` changes the current working directory."
- "`ls path` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- "`pwd` prints the user's current working directory."
- "`whoami` shows the user's current identity."
- "`/` on its own is the root directory of the whole file system."
- "A relative path specifies a location starting from the current location."
- "An absolute path specifies a location from the root of the file system."
- "Directory names in a path are separated with '/' on Unix, but '\\\\' on Windows."
- "'..' means 'the directory above the current one'; '.' on its own means 'the current directory'."
- "Most files' names are `something.extension`. The extension isn't required, and doesn't guarantee anything, but is normally used to indicate the type of data in the file."
- "Most commands take options (flags) which begin with a '-'."
---

The part of the operating system responsible for managing files and directories
is called the **file system**.
It organizes our data into files,
which hold information,
and directories (also called "folders"),
which hold files or other directories.

Several commands are frequently used to create, inspect, rename, and delete files and directories.
Now we will start exploring them, using Jupyter Notebook.

## Jupyter Notebook

"The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text." The main advantage of Jupyter Notebook is interactivity.

## Using UNIX-style shell commands in Jupyter QtConsole and Notebook

You should use all of the commands in this lesson without any modification except whoami. For whoami, add an exclamation point (!) in front of this command i.e. !whoami. We will go over the difference between including and not including the exclamation point (!) later.

The dollar sign is a **prompt**, which shows us that the shell is waiting for input;
your shell may use a different character as a prompt and may add information before
the prompt. When typing commands, either from these lessons or from other sources,
do not type the prompt, only the commands that follow it.

Type the command `whoami`,
then press the Enter key (sometimes marked Return) to send the command to the shell.
The command's output is the ID of the current user,
i.e.,
it shows us who the shell thinks we are:


```python
!whoami
```

    skarzynskimw
    

More specifically, when we type `whoami` the shell:

1.  finds a program called `whoami`,
2.  runs that program,
3.  displays that program's output, then
4.  displays a new prompt to tell us that it's ready for more commands.


> ## Username Variation
>
> In this lesson, we have used the username `nelle` (associated
> with our hypothetical scientist Nelle) in example input and output throughout.  
> However, when
> you type this lesson's commands on your computer,
> you should see and use something different,
> namely, the username associated with the user account on your computer.  This
> username will be the output from `whoami`.  In
> what follows, `nelle` should always be replaced by that username.  

Next,
let's find out where we are by running a command called `pwd`
(which stands for "print working directory").
At any moment,
our **current working directory**
is our current default directory,
i.e.,
the directory that the computer assumes we want to run commands in
unless we explicitly specify something else.
Here,
the computer's response is `/Users/nelle`,
which is Nelle's **home directory**:


```python
pwd
```




    'C:\\Users\\skarzynskimw'



> ## Home Directory Variation
>
> The home directory path will look different on different operating systems.
> On Linux it may look like `/home/nelle`,
> and on Windows it will be similar to `C:\Documents and Settings\nelle` or
> `C:\Users\nelle`.  
> (Note that it may look slightly different for different versions of Windows.)
> In future examples, we've used Mac output as the default - Linux and Windows
> output may differ slightly, but should be generally similar.  

To understand what a "home directory" is,
let's have a look at how the file system as a whole is organized.  For the
sake of example, we'll be
illustrating the filesystem on our scientist Nelle's computer.  After this
illustration, you'll be learning commands to explore your own filesystem,
which will be constructed in a similar way, but not be exactly identical.  

On Nelle's computer, the filesystem looks like this:

![The File System](../fig/filesystem.svg)

At the top is the **root directory**
that holds everything else.
We refer to it using a slash character `/` on its own;
this is the leading slash in `/Users/nelle`.

Inside that directory are several other directories:
`bin` (which is where some built-in programs are stored),
`data` (for miscellaneous data files),
`Users` (where users' personal directories are located),
`tmp` (for temporary files that don't need to be stored long-term),
and so on.  

We know that our current working directory `/Users/nelle` is stored inside `/Users`
because `/Users` is the first part of its name.
Similarly,
we know that `/Users` is stored inside the root directory `/`
because its name begins with `/`.

> ## Slashes
>
> Notice that there are two meanings for the `/` character.
> When it appears at the front of a file or directory name,
> it refers to the root directory. When it appears *inside* a name,
> it's just a separator.

Underneath `/Users`,
we find one directory for each user with an account on Nelle's machine,
her colleagues the Mummy and Wolfman.  

![Home Directories](../fig/home-directories.svg)

The Mummy's files are stored in `/Users/imhotep`,
Wolfman's in `/Users/larry`,
and Nelle's in `/Users/nelle`.  Because Nelle is the user in our
examples here, this is why we get `/Users/nelle` as our home directory.  
Typically, when you open a new command prompt you will be in
your home directory to start.  

Now let's learn the command that will let us see the contents of our
own filesystem.  We can see what's in our home directory by running `ls`,
which stands for "listing":

(Again, your results may be slightly different depending on your operating
system and how you have customized your filesystem.)

`ls` prints the names of the files and directories in the current directory in
alphabetical order,
arranged neatly into columns.

Many bash commands, and programs that people have written that can be
run from within bash, support a `--help` flag to display more
information on how to use the commands or programs.

For more information on how to use `ls` we can type `man ls`.
`man` is the Unix "manual" command:
it prints a description of a command and its options,
and (if you're lucky) provides a few examples of how to use it.

> ## `man` and Git for Windows
>
> The bash shell provided by Git for Windows does not
> support the `man` command. Doing a web search for
> `unix man page COMMAND` (e.g. `unix man page grep`)
> provides links to numerous copies of the Unix manual
> pages online.
> For example, GNU provides links to its
> [manuals](http://www.gnu.org/manual/manual.html):
> these include [grep](http://www.gnu.org/software/grep/manual/),
> and the
> [core GNU utilities](http://www.gnu.org/software/coreutils/manual/coreutils.html),
> which covers many commands introduced within this lesson.

To navigate through the `man` pages,
you may use the up and down arrow keys to move line-by-line,
or try the "b" and spacebar keys to skip up and down by full page.
Quit the `man` pages by typing "q".

Here,
we can see that our home directory contains mostly **sub-directories**.
Any names in your output that don't have trailing slashes,
are plain old **files**.

We can also use `ls` to see the contents of a different directory.  Let's take a
look at our `Desktop` directory by running `ls Desktop`.


```python
ls Desktop
```

     Volume in drive C is OSDisk
     Volume Serial Number is B4A0-C61A
    
     Directory of C:\Users\skarzynskimw\Desktop
    
    03/16/2017  04:57 PM    <DIR>          .
    03/16/2017  04:57 PM    <DIR>          ..
    02/19/2016  12:27 PM                 0 .open
    05/18/2016  03:07 PM        12,782,002 16-May-2016 all ADCC experiments.wsp
    05/16/2016  12:09 PM        10,818,256 16-May-2016.wsp
    04/06/2016  12:13 PM    <DIR>          20160406
    11/03/2016  01:23 PM           204,325 20161103 Workspace.wsp
    10/01/2012  04:08 PM            66,438 600_118541752.jpeg
    07/17/2016  03:23 PM    <DIR>          Adrian NEW.Data
    07/16/2016  05:39 PM        14,539,382 Adrian NEW.enl
    04/18/2016  09:21 PM    <DIR>          Amnis ImageStream Data
    05/18/2016  03:09 PM               783 Anti-C3d.lnk
    03/09/2017  04:35 PM             2,171 Atom.lnk
    03/07/2017  10:33 AM             2,064 Blue Jeans.lnk
    05/06/2016  12:23 PM            22,282 Boost Figure Legends 20160505.docx
    05/18/2016  03:07 PM        13,914,053 Boost Figures DRAFT 20160518.pptx
    07/05/2016  10:28 PM         6,273,393 Boost Figures DRAFT 20160705.pptx
    08/17/2016  01:35 PM         8,605,691 Boost Figures DRAFT 20160817.pptx
    03/25/2016  10:51 PM         9,422,202 Boost Figures DRAFT.pptx
    03/25/2016  09:06 PM         9,718,167 Boost Figures DRAFT2.pptx
    05/06/2016  11:50 AM        10,062,424 Boost Figures DRAFT20160505.pptx
    08/17/2016  01:29 PM           101,184 Boost Manuscript 20160817.docx
    07/17/2016  11:35 AM    <DIR>          Boostuximab POP.Data
    09/12/2016  07:32 AM           119,746 Boostuximab POP.enl
    03/23/2016  11:11 AM         1,025,024 BRD4 CoIP JQ1 dose response blot - Full.ppt
    03/06/2017  11:13 AM           242,111 choosing_a_good_chart2.jpg
    03/06/2017  11:12 AM            46,219 choosing_a_good_chart2.pdf
    04/17/2016  12:39 PM    <DIR>          cohort III 8063
    04/17/2016  02:03 PM    <DIR>          cohort IV 7900 7960
    04/17/2016  12:41 PM    <DIR>          cohort V 8145 7865
    03/15/2017  11:54 PM           858,447 ColloquiumAgenda2017.pdf
    03/10/2017  07:54 PM             7,695 CPFP1stYearPlans.png
    11/22/2015  08:39 PM    <DIR>          data-shell
    02/18/2016  12:34 PM                 0 draft.txt
    10/01/2012  04:08 PM            65,441 event_105065492.jpeg
    02/07/2017  10:33 AM            40,233 Geneious.PNG
    02/08/2017  06:17 PM             2,177 Git Shell.lnk
    01/08/2017  12:14 AM               308 GitHub.appref-ms
    02/17/2016  09:14 AM    <DIR>          inflamData
    02/12/2016  05:07 PM         1,072,925 Lab meetingMWS.pptx
    04/27/2016  11:50 AM    <DIR>          MartinSkarzynski 20160408 BiAb
    04/27/2016  11:50 AM    <DIR>          MartinSkarzynski 20160408 BiAb_001
    04/27/2016  11:50 AM    <DIR>          MartinSkarzynski 20160408 BiAb_002
    03/11/2017  07:16 PM             7,232 MartinSkarzynskiPhoto.jpg
    10/01/2012  04:08 PM            29,961 member_8747578.jpeg
    02/15/2016  12:07 PM               997 MTPuTTY.lnk
    10/09/2014  11:42 AM            70,934 Orloff award.jpeg
    02/19/2016  12:59 PM               737 out.csv
    04/12/2016  12:50 PM               524 Plans&2do
    01/19/2016  10:51 AM    <DIR>          Programs to install
    01/01/2017  08:47 PM             1,061 R i386 3.3.2.lnk
    01/01/2017  08:47 PM             1,054 R x64 3.3.2.lnk
    02/08/2017  06:56 PM             2,161 Rodeo.lnk
    03/16/2017  02:58 PM           168,355 shell-novice-data.zip
    03/08/2017  12:30 PM           168,355 shell-novice-data2.zip
    02/15/2016  12:24 PM             3,185 Shortcut to SecureDownloadManager.exe.lnk
    02/19/2016  09:40 AM    <DIR>          sql-novice-survey
    02/19/2016  09:20 AM    <DIR>          sql-survey-data
    02/19/2016  12:31 PM             3,072 surver-demo.db
    02/19/2016  12:44 PM                 0 survery.db
    02/19/2016  12:58 PM                 0 survey
    02/19/2016  09:19 AM            20,480 survey.db
    02/19/2016  12:56 PM               470 test.sql
    04/18/2016  09:21 PM    <DIR>          Trogo
    07/15/2016  05:07 PM         3,262,751 Trogo Figure 20160715.pptx
    07/05/2016  10:30 PM            29,184 TrogoFigureLegendsMethodsResults.doc
                  48 File(s)    103,785,656 bytes
                  18 Dir(s)  223,941,660,672 bytes free
    

Your output should be a list of all the files and sub-directories on your
Desktop, including the `data-shell` directory you downloaded at
the start of the lesson.  Take a look at your Desktop to confirm that
your output is accurate.  

As you may now see, using a bash shell is strongly dependent on the idea that
your files are organized in an hierarchical file system.  
Organizing things hierarchically in this way helps us keep track of our work:
it's possible to put hundreds of files in our home directory,
just as it's possible to pile hundreds of printed papers on our desk,
but it's a self-defeating strategy.

Now that we know the `data-shell` directory is located on our Desktop, we
can change our location to a different directory, so we are no longer located in
our home directory.  

The command to change locations is `cd` followed by a
directory name to change our working directory.
`cd` stands for "change directory",
which is a bit misleading:
the command doesn't change the directory,
it changes the shell's idea of what directory we are in.

Let's say we want to move to the `data` directory we saw above.  We can
use the following series of commands to get there:


```python
cd Desktop
```

    C:\Users\skarzynskimw\Desktop
    


```python
cd data-shell
```

    C:\Users\skarzynskimw\Desktop\data-shell
    


```python
cd data
```

    C:\Users\skarzynskimw\Desktop\data-shell\data
    

These commands will move us from our home directory onto our Desktop, then into
the `data-shell` directory, then into the `data` directory.  `cd` doesn't print anything,
but if we run `pwd` after it, we can see that we are now
in `/Users/nelle/Desktop/data-shell/data`.
If we run `ls` without arguments now,
it lists the contents of `/Users/nelle/Desktop/data-shell/data`,
because that's where we now are:


```python
pwd
```




    'C:\\Users\\skarzynskimw\\Desktop\\data-shell\\data'



We now know how to go down the directory tree, but
how do we go up?  We might try the following:


```python
cd data-shell
```

    [WinError 2] The system cannot find the file specified: 'data-shell'
    C:\Users\skarzynskimw\Desktop\data-shell\data
    

But we get an error!  Why is this?  

With our methods so far,
`cd` can only see sub-directories inside your current directory.  There are
different ways to see directories above your current location; we'll start
with the simplest.  

There is a shortcut in the shell to move up one directory level
that looks like this:


```python
cd ..
```

    C:\Users\skarzynskimw\Desktop\data-shell
    

`..` is a special directory name meaning
"the directory containing this one",
or more succinctly,
the **parent** of the current directory.
Sure enough,
if we run `pwd` after running `cd ..`, we confirm that we're back in `/Users/nelle/Desktop/data-shell`:


```python
pwd
```




    'C:\\Users\\skarzynskimw\\Desktop\\data-shell'



These then, are the basic commands for navigating the filesystem on your computer:
`pwd`, `ls` and `cd`.  Let's explore some variations on those commands.  What happens
if you type `cd` on its own, without giving
a directory?


```python
cd
```

    C:\Users\skarzynskimw
    

How can you check what happened?  `pwd` gives us the answer!


```python
pwd
```




    'C:\\Users\\skarzynskimw'



It turns out that `cd` without an argument will return you to your home directory,
which is great if you've gotten lost in your own filesystem.  

> ## Hidden Files and Directories
>
> ls shows hidden directories `..` and `.`, you may also see a hidden file
> such as `.bash_profile`. This file usually contains shell configuration
> settings. You may also see other files and directories beginning
> with `.`. These are usually files and directories that are used to configure
> different programs on your computer. The prefix `.` is used to prevent these
> configuration files from cluttering the terminal when a standard `ls` command
> is used.

Let's try returning to the `data` directory from before.  Last time, we used
three commands, but we can actually string together the list of directories
to move to `data` in one step:


```python
cd Desktop/data-shell/data/
```

    C:\Users\skarzynskimw\Desktop\data-shell\data
    

Check that we've moved to the right place by running `pwd` and `ls`  

If we want to move up one level from the data directory, we could use `cd ..`.  But
there is another way to move to any directory, regardless of your
current location.  

So far, when specifying directory names, or even a directory path (as above),
we have been using **relative paths**.  When you use a relative path with a command
like `ls` or `cd`, it tries to find that location  from where we are,
rather than from the root of the file system.  

However, it is possible to specify the **absolute path** to a directory by
including its entire path from the root directory, which is indicated by a
leading slash.  The leading `/` tells the computer to follow the path from
the root of the file system, so it always refers to exactly one directory,
no matter where we are when we run the command.

This allows us to move to our `data-shell` directory from anywhere on
the filesystem (including from inside `data`).  To find the absolute path
we're looking for, we can use `pwd` and then extract the piece we need
to move to `data-shell`.


```python
pwd
```




    'C:\\Users\\skarzynskimw\\Desktop\\data-shell\\data'



> ## Two More Shortcuts
>
> The shell interprets the character `~` (tilde) at the start of a path to
> mean "the current user's home directory". For example, if Nelle's home
> directory is `/Users/nelle`, then `~/data` is equivalent to
> `/Users/nelle/data`. This only works if it is the first character in the
> path: `here/there/~/elsewhere` is *not* `here/there/Users/nelle/elsewhere`.
>
> Another shortcut is the `-` (dash) character.  `cd` will translate `-` into
> *the previous directory I was in*, which is faster than having to remember,
> then type, the full path.  This is a *very* efficient way of moving back
> and forth between directories. The difference between `cd ..` and `cd -` is
> that the former brings you *up*, while the latter brings you *back*. You can
> think of it as the *Last Channel* button on a TV remote.


```python
cd ~
```

    C:\Users\skarzynskimw
    


```python
cd ..
```

    C:\Users
    


```python
cd -
```

    C:\Users\skarzynskimw
    

### Nelle's Pipeline: Organizing Files

Knowing just this much about files and directories,
Nelle is ready to organize the files that the protein assay machine will create.
First,
she creates a directory called `north-pacific-gyre`
(to remind herself where the data came from).
Inside that,
she creates a directory called `2012-07-03`,
which is the date she started processing the samples.
She used to use names like `conference-paper` and `revised-results`,
but she found them hard to understand after a couple of years.
(The final straw was when she found herself creating
a directory called `revised-revised-results-3`.)

> ## Sorting Output
>
> Nelle names her directories "year-month-day",
> with leading zeroes for months and days,
> because the shell displays file and directory names in alphabetical order.
> If she used month names,
> December would come before July;
> if she didn't use leading zeroes,
> November ('11') would come before July ('7'). Similarly, putting the year first
> means that June 2012 will come before June 2013.

## Tab completion 
Now let's take Nelle to the north-pacific-gyre subdirectory of the `data-shell` directory ,
using the cd command and tab completion:
type De, press tab, type da, press tab, type no, press tab, type 20, press tab


```python
cd Desktop/data-shell/north-pacific-gyre/2012-07-03/
```

    C:\Users\skarzynskimw\Desktop\data-shell\north-pacific-gyre\2012-07-03
    

You can see that whenever you press tab,
the shell automatically completes the directory name for us.
Try using the cd command to return to the data-shell directory. Then go to the writing subdirectory of data-shell. Next, type the letter t, followed by tab.
Pressing tab when there is more than one choice, brings up a list of choices, in this case the Desktop and data directories.


```python

```


```python

```

# Exercizes 

> ## Absolute vs Relative Paths
>
> Starting from `/Users/amanda/data/`,
> which of the following commands could Amanda use to navigate to her home directory,
> which is `/Users/amanda`?
>
> 1. `cd .`
> 2. `cd /`
> 3. `cd /home/amanda`
> 4. `cd ../..`
> 5. `cd ~`
> 6. `cd home`
> 7. `cd ~/data/..`
> 8. `cd`
> 9. `cd ..`
>
> > ## Solution
> > 1. No: `.` stands for the current directory.
> > 2. No: `/` stands for the root directory.
> > 3. No: Amanda's home directory is `/Users/amanda`.
> > 4. No: this goes up two levels, i.e. ends in `/Users`.
> > 5. Yes: `~` stands for the user's home directory, in this case `/Users/amanda`.
> > 6. No: this would navigate into a directory `home` in the current directory if it exists.
> > 7. Yes: unnecessarily complicated, but correct.
> > 8. Yes: shortcut to go back to the user's home directory.
> > 9. Yes: goes up one level.
