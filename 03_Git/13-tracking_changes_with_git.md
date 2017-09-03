---
title:  Versioning edits with Git
teaching: 30
exercises: 0
questions:
- "How do I record changes in Git?"
- "How do I record notes about what changes I made and why?"
objectives:
- "Go through the modify-add-commit cycle for one or more files."
- "Explain where information is stored at each stage of Git commit workflow."
keypoints:
- "Files can be stored in a project's working directory (which users see), the staging area (where the next commit is being built up) and the local repository (where commits are permanently recorded)."
- "`git add` puts files in the staging area."
- "`git commit` saves the staged content as a new commit in the local repository."
- "Always write a log message when committing changes."
- "View previous commits using the `git log` command."
---

We can check the contents of the file that we previously saved in our project directory using the `%less` magic:
~~~
%less metasearch_analysis.py
~~~
{: .source}

~~~
# coding: utf-8
# get_ipython().system('git clone https://github.com/OpenNeuroLab/metasearch.git')
~~~
{: .output}


As we saw previously the status of our git repository shows us that we have
this untracked file along with our directory with data:
~~~
!git status
~~~
{: .source}

~~~
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        metasearch/
        metasearch_analysis.py

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

The first step in tracking a file in Git is to add it to the Git staging area.

![The file lifecycle in git](../fig/git_add.png)
Modified figure from git-scm.com


In order to add a file to the Git staging area we use "git add":

~~~
!git add metasearch_analysis.py
~~~
{: .source}

We check how this changed the way Git see our current project with the "git status" command once again:

~~~
!git status
~~~
{: .source}

~~~
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   metasearch_analysis.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        metasearch/

~~~
{: .output}

Git now knows that it's supposed to keep track of `metasearch_analysis.py`, but
it hasn't recorded these changes permanently in its repository yet. To
permanently store the current state of the metasearch_analysis.py file in the
Git repository we need to commit the changes that are staged. We use the `git
commit` command for this:

~~~
!git commit -m "add script for our analysis"
~~~
{: .source}

~~~
[master (root-commit) 0c89fa2] add script for our analysis
 1 file changed, 2 insertions(+)
 create mode 100644 metasearch_analysis.py
~~~
{: .output}

> ## The staging area helps to keep track of different changes
> 
> If you think of Git as taking snapshots of changes over the life of a
> project, "git add" specifies *what* will go in a snapshot (putting things in
> the staging area), and "git commit" then *actually takes* the snapshot, and
> makes a permanent record of it (as a commit). If you don't have anything
> staged when you type "git commit", Git will prompt you to use "git commit -a"
> or "git commit --all", which is kind of like gathering *everyone* for the
> picture! However, it's almost always better to explicitly add things to the
> staging area, because you might commit changes you forgot you made. Try to
> stage things manually, or you might find yourself searching for "git undo
> commit" more than you would like!
{: .callout}

When we run "git commit", Git takes everything we have told it to save by using
"git add" and stores a copy permanently inside the special `.git` directory.
This permanent copy is called a [commit]({{ page.root }}/reference/#commit) (or
[revision]({{ page.root }}/reference/#revision)) and its short identifier is
`0c89fa2` (Your commit may have another identifier.)

We use the `-m` flag (for "message") to record a short, descriptive, and
specific comment that will help us remember later on what we did and why. If we
just run "git commit" without the `-m` option, Git will launch `atom` (or
whatever other editor we configured as `core.editor`) so that we can write a
longer message.

[Good commit messages][commit-messages] start with a brief (<50 characters) summary of
changes made in the commit.  If you want to go into more detail, add
a blank line between the summary line and your additional notes.

Now when we run "git status" we see:

~~~
!git status
~~~
{: .source}

~~~
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        metasearch/

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

Not only is the metasearch_analysis.py file now tracked but it is also
no longer part of the output of  "git status". It is now in the unmodified
state. When we look at our repository's history we can observe our commit. For
this, we use "git log":

~~~
!git log
~~~
{: .source}

~~~
commit 0c89fa2638154272519761de68189f8bb0d0b789
Author: XXX <XXX@hotmail.com>
Date:   Mon Feb 27 16:12:08 2012 -0500

    add script for our analysis
~~~
{: .output}

"git log" lists all commits  made to a repository in reverse chronological
order. The listing for each commit includes the commit's full identifier (which
starts with the same characters as the short identifier printed by the `git
commit` command earlier), the commit's author, when it was created, and the log
message Git was given when the commit was created.

## Where Are My Changes?
If we run `%ls` at this point, we will see that there has been no obvious change
to the filesystem:

~~~
%ls
~~~
{: .source}

~~~
metasearch/ metasearch_analysis.py
~~~
{: .output}

There are no obvious changes observed in the project directory because Git
saves information about files' history in the special `.git` directory
mentioned earlier so that our filesystem doesn't become cluttered (and so that
we can't accidentally edit or delete an old version).
  
## The Git Lifecycle

We have now seen the different states that files typically inhabit as Git
tracks them. The default file state is unmodified. Any time we make a change to
any of our files tracked by Git we will observe that they are listed as
modified. We must stage and then commit such changes to return the files to
their unmodified state.

The cycle of making changes to files, staging these changes, and then
committing them is continually repeated and our project continues to develop
with each file being represented in the Git repository as a combination of
committed changes. We will start working through such a cycle now by making
another edit to our analysis script. For now we'll just add a comment to
document the fact that we are using data from the the Open Neuroimaging
Laboratory at http://openneu.ro.

![The file lifecycle in git](../fig/git_workflow.png)
Figure from git-scm.com


>## Editing our script file
> If not already open in our text editor atom, we should now open it using the IPython `%edit` magic:
> ~~~
> %edit metasearch_analysis.py
> ~~~
> {: .source}
{: .callout}

Once we have finished editing our script we should observe something like the following:

~~~
%less metasearch_analysis.py
~~~
{: .source}

~~~
# coding: utf-8
# Download the data from the Open Neuroimaging Labaroatory, see http://openneu.ro
# get_ipython().system('git clone https://github.com/OpenNeuroLab/metasearch.git')
~~~
{: .output}

At this point we will see that Git now views this as a modified file:

~~~
!git status
~~~
{: .source}

~~~
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   metasearch_analysis.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        metasearch/

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

We previously used "git add" to add an untracked file to the staging area. This
time we will use it to add a modified file to the staging area.

~~~
!git add metasearch_analysis.py
~~~
{: .source}

Finally to complete the Git life-cycle for this current change-set we will commit our staged changes:

~~~
!git commit -m "add comment about Open Neuroimaging Laboratory"
~~~
{: .source}

~~~
[master b7dfff7] add comment about Open Neuroimaging Laboratory
 1 file changed, 2 insertions(+), 1 deletion(-)
~~~
{: .output}

We can use the "git status" and "git log" commands to confirm that an
additional commit is stored in the Git repository and no staged or unstaged
changes exist for the file metasearch_analysis.py.





## What if I don't want Git to track some of my changes?
There are many reasons we might want git to overlook certain files or sub-
directories in our project.

 One such case is if our data contains Personally identifiable information
(PII). While Git helps us to share our code but we can't do this if we have
added PII to the Git repository. To help with this we can explicitly include a
directory in which we will add such data or perhaps even code so that we
prevent accidentally tracking such content. Let's create such a directory and
add our dataset to it so that we don't accidentally include things we don't
want to.


~~~
Path('data_not_in_repo').mkdir()
~~~
{: .python}

The metasearch directory is itself a git repository. We definitely don't want to track this. While this is sometimes something we might want to do, in our case it would be best to make sure that the metasearch directory remains untracked. To move this directory using the pathlib library is  a little cumbersome so we shall use the ipython `%mv` magic to do this:

~~~
 %mv metasearch data_not_in_repo
~~~
{: .python}

Now to make sure that git does not track this directory we add its name to a
file called .gitignore in our current directory:
 
~~~
Path('.gitignore').write_text('data_not_in_repo')
~~~
{: .source}

Now when we check the status we no longer see the metasearch directory as
untracked by the repository. Furthermore, we will not be able to add any of the
files in this directory into the git repository.


  
> ## Editing and Staging
> 
> We have made a data_not_in_repo directory and we have moved the metasearch
> directory into it. We want to stage these commands for subsequent commit
> Fill in the blank spaces in the code below to achieve this:
> 
> ~~~
> %hist -n g data_not_in_repo
> %hist -n g metasearch
> %save -a metasearch_analysis.py ____
> !git add ____
> ~~~
> {: .python}
{: .challenge}

> ##  Committing
> 
>  What commit message should we use for the changes we staged in the last
>  question? Have a think about and then choose one of the following for a subsequent commit:
>  
> 1. "Using pathlib"
> 2. "Create a data_not_in_repo directory to avoid tracking some files and move the metasearch directory here"
> 3. "Make and add to data_not_in_repo"
> 4. "Change metasearch.py"
> 
> 
> > ## Solution
> > 
> > Answer 1 is not descriptive enough. Answer 2 is too long and this wasn't a
> > particularly extensive change. While answer 4 could be considered useful in
> > some contexts it is answer 3 that strikes the balance well between being
> > concise and descriptive
> > 
> {: .solution}
{: .challenge}


[commit-messages]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
