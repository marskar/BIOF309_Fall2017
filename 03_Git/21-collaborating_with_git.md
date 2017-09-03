---
title: Collaboration with Git and GitHub
teaching: 60
exercises: 0
questions:
- "How do I share my changes with others on the web?"
- "How can I use version control to collaborate with other people?"
- "What do I do when my changes conflict with someone else's?"
objectives:
- "Explain what remote repositories are and why they are useful."
- "Push to or pull from a remote repository."
- "Clone a remote repository."
- "Collaborate pushing to a common repository."
- "Explain what conflicts are and when they can occur."
- "Resolve conflicts resulting from a merge."
keypoints:
- "A local Git repository can be connected to one or more remote repositories."
- "Use the HTTPS protocol to connect to remote repositories until you have learned how to set up SSH."
- "`git push` copies changes from a local repository to a remote repository."
- "`git pull` copies changes from a remote repository to a local repository."
- "`git clone` copies a remote repository to create a local repository with a remote called `origin` automatically set up."
- "Conflicts occur when two or more people change the same file(s) at the same time."
- "The version control system does not allow people to overwrite each other's changes blindly, but highlights conflicts so that they can be resolved."
---

Version control really comes into its own when we begin to collaborate with
other people.  We already have most of the machinery we need to do this; the
only thing missing is to copy changes from one repository to another.

Systems like Git allow us to move work between any two repositories.  In
practice, though, it's easiest to use one copy as a central hub, and to keep it
on the web rather than on someone's laptop.  Most programmers use hosting
services like [GitHub](http://github.com), [BitBucket](http://bitbucket.org) or
[GitLab](http://gitlab.com/) to hold those master copies; we'll explore the pros
and cons of this in the final section of this lesson.

Let's start by sharing the changes we've made to our current project with the
world.  Log in to GitHub, then click on the icon in the top right corner to
create a new repository called `repro_course`:


* Name your repository "repro_course" and then click "Create Repository":

* This effectively makes a directory with a `.git` repository in it.

* As soon as the repository is created, GitHub displays a page with a URL and some
information on how to configure your local repository:


Our local repository still contains our earlier work on `metasearch_analysis.py`, but the
remote repository on GitHub doesn't contain any files yet:

The next step is to connect the two repositories.  We do this by making the
GitHub repository a [remote]({{ page.root }}/reference/#remote) for the local repository.
The home page of the repository on GitHub includes the string we need to
identify it.






Click on the 'HTTPS' link to change the [protocol]({{ page.root }}/reference/#protocol) from
SSH to HTTPS.

> ## HTTPS vs. SSH
> 
> We use HTTPS here because it does not require additional configuration.  After
> the workshop you may want to set up SSH access, which is a bit more secure, by
> following one of the great tutorials from
> [GitHub](https://help.github.com/articles/generating-ssh-keys),
> [Atlassian/BitBucket](https://confluence.atlassian.com/display/BITBUCKET/Set+up+SSH+for+Git)
> and [GitLab](https://about.gitlab.com/2014/03/04/add-ssh-key-screencast/)
> (this one has a screencast).
{: .callout}


Copy that URL from the browser, go into the local `repro_course` repository, and run
this command:

~~~
!git remote add origin https://github.com/github-name/repro_course.git
~~~
{: .python}

Make sure to use the URL for your repository i.e. the only
difference should be your username instead of `github-name`.

We can check that the command has worked by running `git remote -v`:

~~~
!git remote -v
~~~
{: .python}

~~~
origin   https://github.com/github-name/repro_course.git (push)
origin   https://github.com/github-name/repro_course.git (fetch)
~~~
{: .output}

The name `origin` is a local nickname for your remote repository: we could use
something else if we wanted to, but `origin` is by far the most common choice.

Once the nickname `origin` is set up, this command will push the changes from
our local repository to the repository on GitHub:

~~~
!git push origin master
~~~
{: .python}

~~~
Counting objects: 9, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (9/9), 821 bytes, done.
Total 9 (delta 2), reused 0 (delta 0)
To https://github.com/github-name/repro_course.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
~~~
{: .output}

> ## Proxy
> 
> If the network you are connected to uses a proxy there is an chance that your
> last command failed with "Could not resolve hostname" as the error message. To
> solve this issue you need to tell Git about the proxy:
> 
> ~~~
> !git config --global http.proxy http://user:password@proxy.url
> !git config --global https.proxy http://user:password@proxy.url
> ~~~
> {: .python}
> 
> When you connect to another network that doesn't use a proxy you will need to
> tell Git to disable the proxy using:
> 
> ~~~
> !git config --global --unset http.proxy
> !git config --global --unset https.proxy
> ~~~
> {: .python}
{: .callout}

> ## Password Managers
> 
> If your operating system has a password manager configured, `git push` will
> try to use it when it needs your username and password.  For example, this
> is the default behavior for Git Bash on Windows. If you want to type your
> username and password at the terminal instead of using a password manager,
> type:
> 
> ~~~
> !unset SSH_ASKPASS
> ~~~
> {: .python}
> 
> in the terminal, before you run `git push`.  Despite the name, [git uses
> `SSH_ASKPASS` for all credential
> entry](http://git-scm.com/docs/gitcredentials#_requesting_credentials), so
> you may want to unset `SSH_ASKPASS` whether you are using git via SSH or
> https.
> 
> You may also want to add `unset SSH_ASKPASS` at the end of your `~/.bashrc`
> to make git default to using the terminal for usernames and passwords.
{: .callout}


> ## The '-u' Flag
> 
> You may see a `-u` option used with `git push` in some documentation.  It is
> related to concepts we cover in our intermediate lesson, and can safely be
> ignored for now.
{: .callout}

We can pull changes from the remote repository to the local one as well:

~~~
!git pull origin master
~~~
{: .python}

~~~
From https://github.com/username/repro_course
 * branch            master     -> FETCH_HEAD
Already up-to-date.
~~~
{: .output}

Pulling has no effect in this case because the two repositories are already
synchronized.  If someone else had pushed some changes to the repository on
GitHub, though, this command would download them to our local repository.


## Collaboration with git

For the next step, get into pairs.  One person will be the "Owner" and the other
will be the "Collaborator". The goal is that the Collaborator add changes into
the Owner's repository. We will switch roles at the end, so both persons will
play Owner and Collaborator.

> ## Practicing By Yourself
> 
> If you're working through this lesson on your own, you can carry on by opening
> a second terminal window.
> This window will represent your partner, working on another computer. You
> won't need to give anyone access on GitHub, because both 'partners' are you.
{: .callout}

The Owner needs to give the Collaborator access.
On GitHub, click the settings button on the right,
then select Collaborators, and enter your partner's username.

![Adding Collaborators on GitHub](../fig/fig/github-add-collaborators.png)

To accept access to the Owner's repo, the Collaborator
needs to go to [https://github.com/notifications](https://github.com/notifications).
Once there she can accept access to the Owner's repo.

Next, the Collaborator needs to download a copy of the Owner's repository to
 her machine. This is called "cloning a repo". We'll clone it to a directory
 called github_collaboration in our home directory (replacing 'username' with
 the Owner's username):

~~~
%cd
%mkdir github_collaboration
!git clone https://github.com/username/repro_course.git ~/github_collaboration
%cd github_collaboration
~~~
{: .python}

Open metasearch_analysis.py in an editor and add a comment. Stage and commit
the comment.


~~~
!git add metasearch_analysis.py
!git commit -m "test the powers of collaboration"
~~~
{: .python}

Then push the change to the *Owner's repository* on GitHub:

~~~
!git push origin master
~~~
{: .python}

~~~
Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 306 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/username/repro_course.git
   9272da5..29aba7c  master -> master
~~~
{: .output}

Note that we didn't have to create a remote called `origin`: Git uses this
name by default when we clone a repository.  (This is why `origin` was a
sensible choice earlier when we were setting up remotes by hand.)

Take a look to the Owner's repository on its GitHub website now (maybe you need
to refresh your browser.) You should be able to see the new commit made by the
Collaborator.

To download the Collaborator's changes from GitHub, the Owner now enters:

~~~
!git pull origin master
~~~
{: .python}

~~~
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
From https://github.com/username/repro_course
 * branch            master     -> FETCH_HEAD
Updating 9272da5..29aba7c
Fast-forward
 pluto.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 pluto.txt
~~~
{: .output}

Now the three repositories (Owner's local, Collaborator's local, and Owner's on
GitHub) are back in sync.

> ## A Basic Collaborative Workflow
> 
> In practice, it is good to be sure that you have an updated version of the
> repository you are collaborating on, so you should `git pull` before making
> our changes. The basic collaborative workflow would be:
> 
> * update your local repo with `git pull origin master`,
> * make your changes and stage them with `git add`,
> * commit your changes with `git commit -m`, and
> * upload the changes to GitHub with `git push origin master`
> 
> It is better to make many commits with smaller changes rather than
> of one commit with massive changes: small commits are easier to
> read and review.
{: .callout}


## Dealing with conflict

As soon as people can work in parallel, it's likely someone's going to step on someone
else's toes.  This will even happen with a single person: if we are working on
a piece of software on both our laptop and a server in the lab, we could make
different changes to each copy.  Version control helps us manage these
[conflicts]({{ page.root }}/reference/#conflicts) by giving us tools to
[resolve]({{ page.root }}/reference/#resolve) overlapping changes.

To see how we can resolve conflicts, we must first create one.  The file
`metasearch_analysis.py` currently looks like this in both partners' copies of our `repro_course`
repository:

~~~
%less metasearch_analysis.py
~~~
{: .python}


* Let's add a line to one partner's copy only:

~~~
%edit metasearch_analysis.py
%less metasearch_analysis.py
~~~
{: .python}

and then push the change to GitHub:

~~~
!git add metasearch_analysis.py
!git commit -m "Adding a line in our home copy"
~~~
{: .python}

~~~
[master 5ae9631] Adding a line in our home copy
 1 file changed, 1 insertion(+)
~~~
{: .output}

~~~
!git push origin master
~~~
{: .python}

~~~
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 352 bytes, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/username/repro_course
   29aba7c..dabb4c8  master -> master
~~~
{: .output}

Now let's have the other partner
make a different change to their copy
*without* updating from GitHub:

~~~
%edit metasearch_analysis.py
%less metasearch_analysis.py
~~~
{: .python}

We can commit the change locally:

~~~
!git add metasearch_analysis.py
!git commit -m "Adding a line in the second local copy"
~~~
{: .python}

~~~
[master 07ebc69] Adding a line in my copy
 1 file changed, 1 insertion(+)
~~~
{: .output}

but Git won't let us push it to GitHub:

~~~
!git push origin master
~~~
{: .python}

~~~
To https://github.com/username/repro_course.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/username/repro_course.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
~~~
{: .output}

![The Conflicting Changes](../fig/fig/conflict.svg)

Git detects that the changes made in one copy overlap with those made in the
other and stops us from trampling on our previous work. What we have to do is
pull the changes from GitHub, [merge]({{ page.root }}/reference/#merge) them
into the copy we're currently working in, and then push that. Let's start by
pulling:

~~~
!git pull origin master
~~~
{: .python}

~~~
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1)
Unpacking objects: 100% (3/3), done.
From https://github.com/username/repro_course
 * branch            master     -> FETCH_HEAD
Auto-merging metasearch_analysis.py
CONFLICT (content): Merge conflict in metasearch_analysis.py
Automatic merge failed; fix conflicts and then commit the result.
~~~
{: .output}

`git pull` tells us there's a conflict, and marks that conflict in the affected
file.

Our change—the one in `HEAD`—is preceded by `<<<<<<<`. Git has then inserted
`=======` as a separator between the conflicting changes and marked the end of
the content downloaded from GitHub with `>>>>>>>`. (The string of letters and
digits after that marker identifies the commit we've just downloaded.)

It is now up to us to edit this file to remove these markers and reconcile the
changes. We can do anything we want: keep the change made in the local
repository, keep the change made in the remote repository, write something new
to replace both, or get rid of the change entirely. Let's replace both with a
comment stating that we resolved our first of many git conflicts.

~~~
%less metasearch_analysis.py
~~~
{: .python}


To finish merging, we add `metasearch_analysis.py` to the changes being made by
the merge and then commit:

~~~
!git add metasearch_analysis.py
!git status
~~~
{: .python}

~~~
On branch master
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:

    modified:   metasearch_analysis.py

~~~
{: .output}

~~~
!git commit -m "Merging changes from GitHub"
~~~
{: .python}

~~~
[master 2abf2b1] Merging changes from GitHub
~~~
{: .output}

Now we can push our changes to GitHub:

~~~
!git push origin master
~~~
{: .python}

~~~
Counting objects: 10, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 697 bytes, done.
Total 6 (delta 2), reused 0 (delta 0)
To https://github.com/username/repro_course.git
   dabb4c8..2abf2b1  master -> master
~~~
{: .output}

Git keeps track of what we've merged with what, so we don't have to fix things
by hand again when the collaborator who made the first change pulls again:

~~~
!git pull origin master
~~~
{: .python}

~~~
remote: Counting objects: 10, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 2), reused 6 (delta 2)
Unpacking objects: 100% (6/6), done.
From https://github.com/username/repro_course
 * branch            master     -> FETCH_HEAD
Updating dabb4c8..2abf2b1
Fast-forward
 metasearch_analysis.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
~~~
{: .output}

We get the merged file:

~~~
%less metasearch_analysis.py
~~~
{: .python}

We don't need to merge again because Git knows someone has already done that.

Version control's ability to merge conflicting changes is another reason users
tend to divide their programs and papers into multiple files instead of storing
everything in one large file. There's another benefit too: whenever there are
repeated conflicts in a particular file, the version control system is
essentially trying to tell its users that they ought to clarify who's
responsible for what, or find a way to divide the work up differently.


> ## GitHub GUI
> 
> Browse to your `repro_course` repository on GitHub.
> Under the Code tab, find and click on the text that says "XX commits" (where "XX" is some number).
> Hover over, and click on, the three buttons to the right of each commit.
> What information can you gather/explore from these buttons?
> How would you get that same information in the shell?
{: .challenge}

> ## GitHub Timestamp
> 
> Create a remote repository on GitHub.  Push the contents of your local
> repository to the remote.  Make changes to your local repository and push
> these changes.  Go to the repo you just created on Github and check the
> [timestamps]({{ page.root }}/reference/#timestamp) of the files.  How does GitHub record
> times, and why?
{: .challenge}

> ## Push vs. Commit
> 
> In this lesson, we introduced the "git push" command.
> How is "git push" different from "git commit"?
{: .challenge}

> ## Fixing Remote Settings
> 
> It happens quite often in practice that you made a typo in the
> remote URL. This exercice is about how to fix this kind of issues.
> First start by adding a remote with an invalid URL:
> 
> ~~~
> git remote add broken https://github.com/this/url/is/invalid
> ~~~
> {: .python}
> 
> Do you get an error when adding the remote? Can you think of a
> command that would make it obvious that your remote URL was not
> valid? Can you figure out how to fix the URL (tip: use `git remote
> -h`)? Don't forget to clean up and remove this remote once you are
> done with this exercise.
{: .challenge}

> ## GitHub License and README files
> 
> In this section we learned about creating a remote repository on GitHub, but when you initialized your
> GitHub repo, you didn't add a README.md or a license file. If you had, what do you think would have happened when
> you tried to link your local and remote repositories?
{: .challenge}

> ## Switch Roles and Repeat
> 
> Switch roles and repeat the whole process.
{: .challenge}

> ## Review Changes
> 
> The Owner push commits to the repository without giving any information
> to the Collaborator. How can the Collaborator find out what has changed with
> command line? And on GitHub?
{: .challenge}

> ## Comment Changes in GitHub
> 
> The Collaborator has some questions about one line change made by the Owner and
> has some suggestions to propose.
> 
> With GitHub, it is possible to comment the diff of a commit. Over the line of
> code to comment, a blue comment icon appears to open a comment window.
> 
> The Collaborator posts its comments and suggestions using GitHub interface.
{: .challenge}

> ## Version History, Backup, and Version Control
> 
> Some backup software can keep a history of the versions of your files. They also
> allows you to recover specific versions. How is this functionality different from version control?
> What are some of the benifits of using version control, Git and Github?
{: .challenge}


> ## Solving Conflicts that You Create
> 
> Clone the repository created by your instructor.
> Add a new file to it,
> and modify an existing file (your instructor will tell you which one).
> When asked by your instructor,
> pull her changes from the repository to create a conflict,
> then resolve it.
{: .challenge}

> ## Conflicts on Non-textual files
> 
> What does Git do
> when there is a conflict in an image or some other non-textual file
> that is stored in version control?
{: .challenge}

> ## A Typical Work Session
> 
> You sit down at your computer to work on a shared project that is tracked in a
> remote Git repository. During your work session, you take the following
> actions, but not in this order:
> 
> - *Make changes* by appending the number `100` to a text file `numbers.txt`
> - *Update remote* repository to match the local repository
> - *Celebrate* your success with beer(s)
> - *Update local* repository to match the remote repository
> - *Stage changes* to be committed
> - *Commit changes* to the local repository
> 
> In what order should you perform these actions to minimize the chances of
> conflicts? Put the commands above in order in the *action* column of the table
> below. When you have the order right, see if you can write the corresponding
> commands in the *command* column. A few steps are populated to get you
> started.
> 
> |order|action . . . . . . . . . . |command . . . . . . . . . . |
> |-----|---------------------------|----------------------------|
> |1    |                           |                            |
> |2    |                           | `echo 100 >> numbers.txt`  |
> |3    |                           |                            |
> |4    |                           |                            |
> |5    |                           |                            |
> |6    | Celebrate!                | `AFK`                      |
{: .challenge}
