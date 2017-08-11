# Introduction to the Command-line Interface (CLI)

## aka Introduction to Linux
Shell

---

### Getting into the Terminal or Command Prompt

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

For Windows users:
- In the search bar in
the lower left-hand corner, type "cmd"
- Hit "Enter"

You should see somethign
like this:
![Windows Command
Prompt](http://cdn.technorms.com/assets/1starterimage19.png)

## Finding out
where you are:

###Displays your location in the file system

```{.python .input}
pwd     # pwd (Linux)
chdir   # chdir (Windows)
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


    ls     # ls
    dir    # dir

Create a file


    nano   # nano hello.txt
    dir >     # dir > hello.txt

Copies files


    cp     # cp thisfile.txt /home/thisdirectory
    copy   # copy thisfile.txt
C:/Users/thisdirectory

Moves files


    mv    # mv thisfile.txt /home/thisdirectory
	move  # move thisfile.txt
C:/Users/thisdirectory

Deletes files


    rm    # rm thisfile.txt
	del   # rm thisfile.txt

Compares the contents of files


    diff  # diff file1 file2
	fc    # diff file1 file2

Finds a string of text in a file


    grep    # grep word or phrase thisfile.txt
	find    # grep word or phrase
thisfile.txt

Views contents of a file


    less    # less thisfile.txt
	more    # less thisfile.txt

To get out type "q"


Renames a file


    mv     # mv thisfile.txt thatfile.txt
	ren    # ren thisfile.txt
thatfile.txt
