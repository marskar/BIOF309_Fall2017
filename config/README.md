# Config

Here you will find config files for [Atom](https://atom.io/) and [Jupyter Notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/). There is also [conda environment file](https://conda.io/docs/using/envs.html).

## Atom

To run the command line commands below, you must first click "Install Shell Commands" in the "Atom" tab in Atom.

### Install packages

To install all of the packages in the `atom-packages.txt` file enter and run the following line into Terminal (Mac/Windows) or Command Prompt/Powershell (Windows):

`apm install --packages-file atom-packages.txt`

You can also install packages individually: `apm install packagename`

Or you can search for package(s) and install the ones you want in the "Install" section of the "Settings" menu.

I created the package list file with the following code:

`apm list --installed --bare > atom-packages.txt`

### Atom config file

The Atom config file (`config.cson`) contains all my preferred settings for Atom. If you want to edit your own Atom config file is in the `.atom` folder in your home directory.

### Enable/Disable packages

If you want Atom to open with optimal speed, you can disable all of the Community Packages and some of the builtin packages. Depending on what you plan to work on, you might (not) need/want some/all of the packages. Use the following command line commands: `apm enable packagename` `apm disable packagename` to disable/enable packages by name or do so in the "Packages" section of the "Settings" menu.

There is also a `atom-dev-package.txt` file which you can use to enable or disable all of the packages that slow down Atom during startup. To disable all of the packages:

```
apm disable `cat atom-dev-packages.txt`
```

and to enable:

```
apm enable `cat atom-dev-packages.txt`
```

## Conda

You can create a new conda environment using the `biof309_env.yml` file. To do this, enter

`conda env create --file biof309_env.yml`

into your Terminal (Mac/Windows) or Anaconda Prompt (Windows). You must have [Anaconda](https://www.anaconda.com/download/) (or Miniconda) installed for this to work.

I created the environment file with the following code:

`conda env export > biof309_env.yml`

## Jupyter Notebook - config.py

The following are instructions that will enable Jupyter Notebooks to

### 1\. Open markdown files as notebooks

You must have [notedown](https://github.com/aaren/notedown) installed for this to work!

### 2\. Export output files

<sup>*</sup>

 automatically

<sup>#</sup>

<sup>*</sup>

HTML, script (.py, .R, etc.), slides.html, markdown (.md), PDF, and TeX files<br>

<sup>#</sup>

whenever you create or save a .ipynb file.

This functionality requires [nbconvert](https://nbconvert.readthedocs.io/en/latest/install.html#installing-nbconvert), which comes with the [Anaconda Distribution](https://www.anaconda.com/download/) of Python.

You must have [LaTeX](https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex) installed to generate a PDF or tex files!

This method utilizes so-called 'save hooks' that are described in [nbcovert documentation](http://jupyter-notebook.readthedocs.io/en/latest/extending/savehooks.html). For more information, please consider taking a look at this [article](https://svds.com/jupyter-notebook-best-practices-for-data-science/). The original version of the code is from this [GitHub issue](https://github.com/ipython/ipython/issues/8009) and is hosted here in the this [repo](https://github.com/jbwhit/til/blob/master/jupyter/autosave_html_py.md) and this [gist](https://gist.github.com/jbwhit/881bdeeaae3e4128947c).

## Instructions

Append the text in the `jupyter_notebook_config.py` in this repo to your `jupyter_notebook_config.py` file in your `.jupyter` folder (you could also save over the file).

The file is hidden, so you will have to make it visible. To do this in Windows, follow [these instructions](https://www.howtogeek.com/howto/windows-vista/show-hidden-files-and-folders-in-windows-vista/).

On a Mac, you can press `Command+Shift+.` to reveal hidden files and folders.

If you do not have a `jupyter_notebook_config.py`, open a terminal window and run the following line:

`jupyter notebook --generate-config`

When you open your jupyter_notebook_config.py file, you will notice that all of the defaults are commented out.

## Jupyter Notebook - notebook.json

The notebook.json file is typically in `~/.jupyter/nbconfig/notebook.json`.

The `notebook.json` is able to set your keyboard shortcuts, turn on soft wrapping in code and markdown cells, and hide the toolbar and header.

The process for editing the json files to set keyboard shortcuts directly is **not** recommended, but described [here](http://jupyter-notebook.readthedocs.io/en/latest/extending/keymaps.html).

Instead, it is recommended to [make desired changes to keyboard shortcuts using Jupyter Notebook](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Custom%20Keyboard%20Shortcuts.html).

If you like soft wrapping, I believe making changes to my `notebook.json` is the only way to turn this option on.
