
# Week 2 - Printing and manipulating text

We started the first week by printing _Hello world_  (you can try it below). This taught us a number of things.  It taught us about strings, functions, statements. As we know, as biologists one of the primary entities that we deal with is string in the form of sequences, wether they be DNA, RNA, or amino acid sequences.


```python
print("Hello world")
```

To python, a sequences in a __string__. A string of what? A __string of characters__. A string is an ummutable (unchangeable) sequence of characters arranged in a specific order. What is a character? A character is letter, number, or punctuation mark...anything that can be represented on a keyboard.

Thus _Hello world_ is the string that we used in _print_ function of our _Hello world_ program.

    "Hello world"

What did we do with that string?

We "printed" or wrote the string to the terminal. The python command _print_ is a function, a collection of python source code that has been written to perform a particular action. We call or use a function by typing its name, followed by an open and closed parenthesis. __Functions always have parentheses!__ In the case of the _print_ function you must also include a parameter or string to print.

### Getting help

__NOTE__: Would you like to get more inforamtion on _print_? Type

    print?
    or
    help(print)


```python
help(print)
```

    Help on built-in function print in module builtins:

    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.



#### Single or double quotes?

As we can see from the code below, python does not care if we use single or double quotes around our text.


```python
"Hello world" == 'Hello world'
```
    True

```python
print("Hello world")
```
    Hello world
```python
print('Hello world')
```
    Hello world
```python
print("Hello world") # What happen when you try to run this cell?

```
    Hello world

### Comments, or what is that text at the end of the statement above?

Comments are a way to include text in your code and is ignored by the compiler. Comments are very helpful to understand your code without interfering with its execution or logic.

Comments are preceded by a pound sign "#" and a space.

    # This is a comment

__Advanced__:Docstrings

### Splitting a statement over two lines

Sometimes, in fact often, a python statement will be longer then one line on your screen. Good python practice declares that your programming line should be no longer than 80 characters. If a line of code is longer then 80 characters, you can wrap the python statement and add a backslash "\" to each line that is continued.

    print("This is a long python statement that needs to be wrapped.")

    print("This is a long python statement \
    that needs to be wrapped.")

Try typing each or something similar below to test it out.


```python
print("This is a long python statement that needs to be wrapped.")
```


```python
print("hello") # this is a test of
               # carry over
```

### Special characters

The backslash, also called the escape character, enables us to use invisible or special characters in our python statements.

Print a new line character and python will go to the next line. Like this:

    print("Hello world\n!")

To see what special characters are available see this [tutorial page](http://www.tutorialspoint.com/python/python_strings.htm).

What happens when you try it below?


```python
  print("Hello world\nThis is the date\nMy name\nreport title")
```
    Hello world
    This is the date
    My name
    report title


### Combining string

Strings can be combined using the plus operator. We know what one plus one is and so does python. 1 + 1 equals two. Well the plus operator also can work for string. Try this below:

    print("Hello" + "World!")

What is the result? Is there anything wrong with it? If so, how do you fix it?


### Variables for strings

Thus far we have been working directly with string or text. We can create a variable to store the text that we want.
```python
    message = "Hello world!"

We can then use that variable in our print statement:

```python
  print(message)

What happens when you run the statement above?


```python
:

message = "Hello world!"
print(message)
```

    Hello world!


### Variables as objects

In the cell above, the word "message" is a variable. It holds the string "Hello world!". From the python perspective, every variable is an object. In fact, everything in python is an object. What is an __object__? An object is a template or a cookie cutter that has certain characteristics, like strings, integers and floating point numbers. String objects have properties and methods or built-in functions. We will look at a number of methods below.


    variable_name_1 = "A value"
    variable_name_2 = 10

Check and see what type of object something is by using the built-in function "type":

    type(message)


```python
:
variable_name_1 = "A test"
variable_name_1
```




    'A test'



---
## Utilizing the python _str_ (string) methods

To see all available methods (functions) please look at the [Python Standard Library Documentation String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

## Methods available to all objects:

### Create a variable to work with

```python
new_dna = 'atgtag'
```

### _in_

To check to see if a nucleotide (i.e. a character) is in our DNA sequence use the __in__ operator.

    'a' in new_dna	  # Returns True
    'atg' in new_dna	# Returns True
    'aaa' in new_dna	# Returns False

More generically, to check to see if a python object (character, string, number, etc) is in another python object (string, list, etc):

    x in s	# Return True if an item of s is equal to x, else False


                x not in s	False if an item of s is equal to x, else True
                    s + t	the concatenation of s and t
            s * n or n * s	equivalent to adding s to itself n times


```python
:
message
```




    'Hello world!'




```python
message.upper()
```




    'HELLO WORLD!'



### _slice [ i : j : k ]_

To _slice_ a character or subsequence out of a sequence, use square brackets ("[", "]").

    new_dna[0]

    new_dna[0:3]

__NOTE__: The first number is INCLUSIVE (included), while the second number is EXCLUSIVE (not included).

    Generically - s[i]    ith item of s, origin 0

    s[i:j]	slice of s from i to j

    s[i:j:k]	slice of s from i to j with step k



```python
:
new_dna
```




    'atgtag'




```python
new_dna[0]
```




    'a'




```python
new_dna[::-1]
```




    'gatgta'



### _len_

To get teh length or total count of the residues in our sequence use the _len_ function:

    len(new_dna)	length of new_dna


```python
:

len(new_dna)
```




    6



### _count_

To count the number of times the nucleotide "A" occurs in our string we use the _count_ function:

    new_dna.count('A')	total number of occurrences of x in s


```python
:

new_dna.count('A')
```




    0



### String methods (that are particularly important in bioinformatics)

To see what methods or properties (object variables) are available, type the name of an object, usually a variable name, type a period "." afterwards and hit the tab key. __IF__ he variable has already been defined you will see what methods and properties are available.

    message.<hit tab>

### Concatenation

Like the plus sing (+) concatenation joins string together. The concatenation symbol __+__ will join two string into a single string. Lets say you would like to add two DNA sequences together. You would do the following:

    dna1 = "atgaattgg"
    dna2 = "ttaaggtag"
    new_dna = dna1 & dna2


```python
:

```

### Changing case

We can also change the case of a string using the built in method __name__. Lets see how:

For uppercase, use the _upper()_ method. In the documentation (above link) we see it listed as: str.__upper__()

    new_dna.upper()

For lowercase, use the _lower()_ method.

    new_dna.lower()


```python
:

```

### Substring

One can extract a substring from a sequence as well using a built-in method. As we mentioned above, a string is a sequence or collection of characters (Unicode characters).

We use square brackets "[" and "]" to extract a subsequence.




```python
:

```

### Find

In addition to pull out a subsequence, we can find if a subsequence exists in a sequence.


    str.find(sub[, start[, end]])
    Return the lowest index in the string where substring sub is found within the slice s[start:end].
    Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

    Note The find() method should be used only if you need to know the position of sub. To check if sub is a
    substring or not, use the __in__ operator:

    'Py' in 'Python'

Find the position of the codon for methionine:

    new_dna.find("atg")

Find the position of the stop codon:

    new_dna.find("tag")


```python
:
new_dna.find('tag')
```




    3




```python
new_dna[3:]
```




    'tag'



### Reversing

We can make use of a trick of the slicing capability to reverse a string. Use a -1 in the final position as step to reverse.

    new_dna[::-1]


```python
:


```
