# Introduction to the Command-line Interface (CLI)

## aka Introduction to Linux
Shell

---

### Getting into the Terminal (or something similar)

For Mac users:
-
Type "Command + Spacebar" or click on the Spotlight magnifying glass in the
upper right-hand corner.
- Type "Terminal"
- Hit "Return"

You should see
something like this:
![Mac
Terminal](https://www.imore.com/sites/imore.com/files/styles/larger/public/field/image/2016/03/13-add-
spacers-terminal.jpg?itok=tAISaSDn)

For Windows Users, there are many options.
I recommend either [git bash](https://git-scm.com/download/win) or, if you are
feeling adventurous, [Jupyter Lab](https://github.com/jupyterlab/jupyterlab).

## Finding out
where you are:

### Displays your location in the file system

```{.python .input  n=1}
pwd     # pwd (Linux)
```

```{.json .output n=1}
[
 {
  "data": {
   "text/plain": "'/Users/marskar/GitHub/BIOF309_Fall2017/02_UNIX'"
  },
  "execution_count": 1,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

###Creates a directory

```{.python .input}
mkdir   # mkdir directory
mkdir   # mkdir directory
```

###Changes directories with a specified path (absolute path)

```{.python .input}
cd pathname    # cd /directory/directory
cd pathname    # cd C:/directory/directory
```

###Changes directories with a relative path

```{.python .input}
cd ..
cd..
```

## Absolute Paths versus Relative Paths

* Absolute paths start at the root
directory in Linux and at the Hard drive Letter in Windows:

```{.python .input}
/Users/username/Document/BIOF309/file.txt
C:/Users/username/Documents/BIOF309/file.txt
```

* Relative paths are "relative" to the programs currently location.

```{.python .input}
.\file.txt    # Current directory
```

## Working with files

Lists files

```{.python .input}
    ls     # ls
    dir    # dir
```

Create a file

```{.python .input}
    nano   # nano hello.txt
    dir >     # dir > hello.txt
```

Copies files

```{.python .input}
    cp     # cp thisfile.txt /home/thisdirectory
    copy   # copy thisfile.txt
```

C:/Users/thisdirectory

Moves files

```{.python .input}
    mv    # mv thisfile.txt /home/thisdirectory
    move  # move thisfile.txt
```

C:/Users/thisdirectory

Deletes files

```{.python .input}
    rm    # rm thisfile.txt
    del   # rm thisfile.txt
```

Compares the contents of files

```{.python .input}
    diff  # diff file1 file2
    fc    # diff file1 file2
```

Finds a string of text in a file

```{.python .input}
    grep    # grep word or phrase thisfile.txt
    find    # grep word or phrase
```

thisfile.txt

Views contents of a file

```{.python .input}

    less    # less thisfile.txt
    more    # less thisfile.txt

```

Renames a file

```{.python .input}
    mv     # mv thisfile.txt thatfile.txt
    ren    # ren thisfile.txt
```

thatfile.txt
