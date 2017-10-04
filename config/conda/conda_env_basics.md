
## Basic Conda Commands

Conda is the package and environment manager that comes with the [Anaconda distribution of Python](https://www.anaconda.com/download/).

Here we will learn how to use conda to create an environment that is separate from our main installation in which we can tightly control the version of each package that we install. 

There are many advantages to this including being able to
1. recreate the environment on different computer (e.g. one that belongs to a collaborator), 
2. set up a specific environment that contains only what is needed for a given project,
2. recover quickly and easily if anything breaks, and 
3. maintain a list of every version of every piece of software we used (e.g. to provide to reviewers of any articles we try to publish).

By the way, there is a great [cheatsheet for conda](https://conda.io/docs/_downloads/conda-cheatsheet.pdf) that I highly recommend.

Creating an environment and a GitHub repository are two fundamental steps to starting any project the right (i.e. reproducible) way and this approach is likely to save you plenty of frustration, pain and suffering in the future.

### Starting notes

The following commands **must** be run from the terminal (Mac/Linux) or anaconda prompt (Windows)!!!

Just like with `!cd`, any changes you make with `!conda` will not persist!

### Create an environment from an environment file

First try to create an environment from a `.yml` file using the `conda env create` command as below.

Note: You should first navigate to the location of your file.

`conda env create --file biof309_env.yml`

OR

`conda env create -f biof309_env.yml`

Note: You may call your `.yml` files whatever you want, but the `.yml` file above is called `biof309_env.yml`.

### Activate the newly created environment

To start your new environment, type 

`source activate biof309`

into your terminal (Mac/Linux)

OR

`activate biof309` 

into anaconda prompt (Windows).

If that works, you are all set!

To later deactivate the environment, type 

`source deactivate biof309`

into your terminal (Mac/Linux)

OR

`deactivate biof309`

into anaconda prompt (Windows).

### Export a new environment file

To save a **NEW** environment file, run the `conda env export` command and provide a **NEW** filename.

`conda env export --name my_env > my_env.yml`

Note: If you environment is activated you can skip the name option and argument.

If you want to **update** your environment file, instead of creating a new file as above, run the `conda env export` command in the directory where your environment file is located and use the **same** filename. The original environment file WILL BE OVERWRITTEN!

`conda env export --name biof309 > biof309_env.yml`

OR

`conda env export --n biof309 > biof309_env.yml`

Note: If you environment is activated you can skip the name option and argument.

### Update your environment based on an environment file

Let's say you made some changes to your environment file (e.g. using Atom) and want to apply those changes to your environment.

To update your environment from an environment file, use the `conda env update` command as below.

`conda env update --name=biof309 --file=biof309_env.yml`

Note: The equal signs are optional!

### More conda commands

If you want to create and modify your own environment from scratch, you can use the commands below.

`conda create --yes --name my_env python=3.6.2` #create a new env with a specific version of python

Note: `conda create`, not `conda env create`.

`conda env list` #confirm environment was created

Now activate your environment as described above!

`conda install ipython jupyter notebook pandas numpy scipy matplotlib pandas seaborn bokeh scikit-learn altair biopython`

Note: You can specify the versions of each package as with the `conda create` command above.

`conda list` #confirm all packages installed correctly

`conda list > conda_list.txt` #save a nice list of packages

`conda list --explicit > conda_list_explicit.txt` #save a detailed list of packages
