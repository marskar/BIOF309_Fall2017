---
title: Keeping track of changes with Git
teaching: 30
exercises: 0
questions:
- "How can I identify old versions of files?"
- "How do I review my changes?"
- "How can I recover old versions of files?"
objectives:
- "Explain what the HEAD of a repository is and how to use it."
- "Identify and use Git commit numbers."
- "Compare various versions of tracked files."
- "Restore old versions of files."
keypoints:
- "`git diff` displays differences between commits."
- "`git checkout` recovers old versions of files."
---

*   As we saw in the previous lesson, we can refer to commits by their
identifiers.
*  The most recent commit of the working directory can also be referred to by using the identifier
   `HEAD`.
* Every previous commit can in turn be referenced by adding the `~` symbol and incrementing the number
    * So the most recent commit is HEAD, the previous one is HEAD~1 (pronounced HEAD minus 1), and so on.
* The diff command allows us to observe differences between difference versions of our working directory

## View differences between files

To see the difference between our modified files and our last commit we can use

~~~
!git diff HEAD 
~~~
{: .bash}

~~~
output
~~~
{: .output}

We can specify a specific file for this:

~~~
!git diff HEAD metasearch_analysis.py
~~~
{: .python}

~~~
output
~~~
{: .output}

We can look for difference between to previous revisions too:

~~~
!git diff HEAD~3 HEAD~2 metasearch_analysis.py
~~~
{: .python}

~~~
output
~~~
{: .output}


We can also refer to commits using those long strings of digits and letters
that `git log` displays. These are unique IDs for the changes, and "unique"
really does mean unique: every change to any set of files on any computer has a
unique 40-character identifier. Our first commit was given the ID
XXX, so let's try this:

~~~
!git diff XXX 
~~~
{: .python}

~~~
output
~~~
{: .output}

That's the right answer, but typing out random 40-character strings is
annoying, so Git lets us use just the first few characters:

~~~
!git diff X
~~~
{: .bash}

~~~
output
~~~
{: .output}

Finally, a convenient way to search all versions of a file at once for a particular string is to use the `-p` flag for the `git log` command:

~~~
log = !git log -p
[x for x in log if 'clone' in x]
~~~
{: .python}

~~~
output
~~~
{: .output}


## Working with the history

All right! So we can save changes to files and see what we've changed—now how
can we restore older versions of things? Let's suppose we accidentally
delete our file:

~~~
%save metasearch_analysis 15 # Type Y to confirm
~~~
{: .python}

`git status` now tells us that the file has been changed,
but those changes haven't been staged:

~~~
!git status
~~~
{: .python}

~~~
output
~~~
{: .output}

We can put things back the way they were by using `git checkout`:

~~~
!git checkout HEAD metasearch_analysis.py
~~~
{: .python}

As you might guess from its name, `git checkout` checks out (i.e., restores) an
old version of a file. In this case, we're telling Git that we want to recover
the version of the file recorded in `HEAD`, which is the last saved commit. If
we want to go back even further, we can use a commit identifier instead:

~~~
$ git checkout HEAD~3 metasearch_analysis.py
~~~
{: .python}

> ## Don't Lose Your HEAD
> 
> Above we used
> 
> ~~~
> $ git checkout HEAD~3 metasearch_analysis.py
> ~~~
> {: .python}
> 
> to revert metasearch_analysis.py to its previous state. If you forget to
> specify the file in that command, Git will tell you that "You are in
> 'detached HEAD' state." In this state, you shouldn't make any changes. You
> can fix this by reattaching your head using ``git checkout master``
{: .callout}

It's important to remember that we must use the commit number that identifies
the state of the repository *before* the change we're trying to undo. A common
mistake is to use the number of the commit in which we made the change we're
trying to get rid of. Git messages written in the imperative help with this. 

If we want to go back to a version of our file before we started working on a
new feature that has not worked out and caused lots of bugs the commit message
"Start adding excellent new feature" is probably the first one to avoid and we
should jump one step further back in our history.


So, to put it all together, here's how Git works in cartoon form:

![http://figshare.com/articles/How_Git_works_a_cartoon/1328266](../fig/fig/git_staging.svg)

## Other useful points to note

* Remember to keep building up history's with the git lifecycle. When you
  finally decide you really need to use git to recover some code of many months
  ago you'll be grateful for your diligence then.
* [Learngitbranching](http://learngitbranching.js.org) is a great place to learn more advanced manipulation in git.
* Many editors have plugins to extend the functionality. Once you are
  comfortable with the basics of Git, they can really improve the experience of
  using git. Frequently the best way to use the more obscure commands is to go
  back to the command line though. Many times the only straight-forward
  solution is to a problem you are having is to type an incantation to Git at
  the command line.



> ## Simplifying the Common Case
>
> If you read the output of `git status` carefully,
> you'll see that it includes this hint:
>
> ~~~
> (use "git checkout -- <file>..." to discard changes in working directory)
> ~~~
> {: .bash}
>
> As it says,
> `git checkout` without a version identifier restores files to the state saved in `HEAD`.
> The double dash `--` is needed to separate the names of the files being recovered
> from the command itself:
> without it,
> Git would try to use the name of the file as the commit identifier.
{: .callout}

The fact that files can be reverted one by one
tends to change the way people organize their work.
If everything is in one large document,
it's hard (but not impossible) to undo changes to the introduction
without also undoing changes made later to the conclusion.
If the introduction and conclusion are stored in separate files,
on the other hand,
moving backward and forward in time becomes much easier.

> ## Recovering Older Versions of a File
>
> Jennifer has made changes to the Python script that she has been working on for weeks, and the
> modifications she made this morning "broke" the script and it no longer runs. She has spent
> ~ 1hr trying to fix it, with no luck...
>
> Luckily, she has been keeping track of her project's versions using Git! Which commands below will
> let her recover the last committed version of her Python script called
> `data_cruncher.py`?
>
> 1. `$ git checkout HEAD`
>
> 2. `$ git checkout HEAD data_cruncher.py`
>
> 3. `$ git checkout HEAD~1 data_cruncher.py`
>
> 4. `$ git checkout <unique ID of last commit> data_cruncher.py`
>
> 5. Both 2 and 4
{: .challenge}

> ## Reverting a Commit
>
> Jennifer is collaborating on her Python script with her colleagues and
> realises her last commit to the group repository is wrong and wants to
> undo it.  Jennifer needs to undo correctly so everyone in the group
> repository gets the correct change.  `git revert [wrong commit ID]`
> will make a new commit that undoes Jennifer's previous wrong
> commit. Therefore `git revert` is different than `git checkout [commit
> ID]` because `checkout` is for local changes not committed to the
> group repository.  Below are the right steps and explanations for
> Jennifer to use `git revert`, what is the missing command?
>
> 1. ________ # Look at the git history of the project to find the commit ID
>
> 2. Copy the ID (the first few characters of the ID, e.g. 0b1d055).
>
> 3. `git revert [commit ID]`
>
> 4. Type in the new commit message.
>
> 5. Save and close
{: .challenge}

> ## Understanding Workflow and History
>
> What is the output of cat venus.txt at the end of this set of commands?
>
> ~~~
> $ cd planets
> $ nano venus.txt #input the following text: Venus is beautiful and full of love
> $ git add venus.txt
> $ nano venus.txt #add the following text: Venus is too hot to be suitable as a base
> $ git commit -m "comments on Venus as an unsuitable base"
> $ git checkout HEAD venus.txt
> $ cat venus.txt #this will print the contents of venus.txt to the screen
> ~~~
> {: .bash}
>
> 1.
>
> ~~~
> Venus is too hot to be suitable as a base
> ~~~
> {: .output}
>
> 2.
>
> ~~~
> Venus is beautiful and full of love
> ~~~
> {: .output}
>
> 3.
>
> ~~~
> Venus is beautiful and full of love
> Venus is too hot to be suitable as a base
> ~~~
> {: .output}
>
> 4.
>
> ~~~
> Error because you have changed venus.txt without committing the changes
> ~~~
> {: .output}
{: .challenge}

> ## Checking Understanding of `git diff`
>
> Consider this command: `git diff HEAD~3 mars.txt`. What do you predict this command
> will do if you execute it? What happens when you do execute it? Why?
>
> Try another command, `git diff [ID] mars.txt`, where [ID] is replaced with
> the unique identifier for your most recent commit. What do you think will happen,
> and what does happen?
{: .challenge}

> ## Getting Rid of Staged Changes
>
> `git checkout` can be used to restore a previous commit when unstaged changes have
> been made, but will it also work for changes that have been staged but not committed?
> Make a change to `mars.txt`, add that change, and use `git checkout` to see if
> you can remove your change.
{: .challenge}

> ## Explore and Summarize Histories
>
> Exploring history is an important part of git, often it is a challenge to find
> the right commit ID, especially if the commit is from several months ago.
>
> Imaging the `planets` project has more than 50 files.
> You would like to find a commit with specific text in `mars.txt` is modified.
> When you type `git log`, a very long list appeared,
> How can you narrow down the search?
>
> Recorded that the `git diff` command allow us to explore one specific file,
> e.g. `git diff mars.txt`. We can apply the similar idea here.
>
> ~~~
> $ git log mars.txt
> ~~~
> {: .bash}
>
> Unfortunately some of these commit messages are very ambiguous e.g. `update files`.
> How can you search through these files?
>
> Both `git diff` and `git log` are very useful and they summarize different part of the history for you.
> Is that possible to combine both? Let's try the following:
>
> ~~~
> $ git log --patch mars.txt
> ~~~
> {: .bash}
>
> You should get a long list of output, and you should be able to see both commit messages and the difference between each commit.
>
> Question: What does the following command do?
>
> ~~~
> $ git log --patch HEAD~3 HEAD~1 *.txt
> ~~~
> {: .bash}
{: .challenge}
