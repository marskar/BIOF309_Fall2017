---
title: "Built-in Functions and Help"
teaching: 15
exercises: 10
questions:
- "How can I use built-in functions?"
- "How can I find out what they do?"
- "What kind of errors can occur in programs?"
objectives:
- "Explain the purpose of functions."
- "Correctly call built-in Python functions."
- "Correctly nest calls to built-in functions."
- "Use help to display documentation and source code for built-in functions."
- "Correctly describe situations in which SyntaxError and NameError occur."
keypoints:
- "Use comments to add documentation to programs."
- "A function may take zero or more arguments."
- "Commonly-used built-in functions include `max`, `min`, and `print`."
- "Functions may only work for certain (combinations of) arguments."
- "Functions may have default values for some arguments."
- "Use the built-in function `help` to get help for a function in python or '?' after the function in IPython."
- "Every function returns something."
- "Python reports a syntax error when it can't understand the source of a program."
- "Python reports a runtime error when something goes wrong while a program is executing."
- "Fix syntax errors by reading the source code, and runtime errors by tracing the program's execution."
---

## A function may take zero or more arguments.

*   We have seen some functions already --- now let's take a closer look.
*   An *argument* is a value passed into a function.
*   `len` takes exactly one.
*   `int`, `str`, and `float` create a new value from an existing one.
*   `print` takes zero or more.
*   `print` with no arguments prints a blank line.
    *   Must always use parentheses, even if they're empty,
        so that Python knows a function is being called.

~~~
print('before')
print()
print('after')
~~~
{: .python}

~~~
before

after
~~~
{: .output}

## Commonly-used built-in functions include `max`, `min`, and `round`.

*   Use `max` to find the largest value of one or more values.
*   Use `min` to find the smallest.
*   Both work on character strings as well as numbers.
    *   "Larger" and "smaller" use (0-9, A-Z, a-z) to compare letters.

~~~
max(1, 2, 3)
~~~
{: .python}

~~~
3
~~~
{: .output}

~~~
min('a', 'A', '0')
~~~
{: .python}

~~~
'0'
~~~
{: .output}

## Functions may only work for certain (combinations of) arguments.

*   `max` and `min` must be given at least one argument.
    *   "Largest of the empty set" is a meaningless question.
*   And they must be given things that can meaningfully be compared.

~~~
max(1, 'a')
~~~
{: .python}

~~~
TypeError: unorderable types: str() > int()
~~~
{: .error}

## Functions may have default values for some arguments.

*   `round` will round off a floating-point number.
*   By default, rounds to zero decimal places.

~~~
round(3.712)
~~~
{: .python}

~~~
4
~~~
{: .output}

*   We can specify the number of decimal places we want.

~~~
round(3.712, 1)
~~~
{: .python}

~~~
3.7
~~~
{: .output}



## Use the built-in function `help` to get help for a function.

*   Every built-in function has online documentation.

~~~
help(round)
~~~
{: .python}

~~~
Help on built-in function round in module builtins:

round(...)
    round(number[, ndigits]) -> number

    Round a number to a given precision in decimal digits (default 0 digits).
    This returns an int when called with one argument, otherwise the
    same type as the number. ndigits may be negative.
~~~
{: .output}

## IPython provides easier access to help

*   As we open a parenthesis of a function we can see some useful help
*   We can type `?` after a function or object to get help about it that
includes what is displayed by the Python help function.


~~~
print?
~~~
{: .python}

~~~
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method
~~~

Additionally IPython provides a convenient manner to view the source code of
functions. This help is available by using `??`. Most of the built-in functions
are not written in Python. For performance reasons they are written in compiled
languages like C. In these cases, the `??` help command will display the same
content as the previously mentioned help command. 


~~~
print??
~~~
{: .python}

~~~
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method
~~~
{: .output}


## Python reports a syntax error when it can't understand the source of a program.

*   Won't even try to run the program if it can't be parsed.

~~~
# Forgot to close the quotation marks around the string.
roi_label = 'hippocampus
~~~
{: .python}

~~~
...
SyntaxError: EOL while scanning string literal
~~~
{: .error}

~~~
# An extra '=' in the assignment.
brain_volume = = 1302
~~~
{: .python}

~~~
...
SyntaxError: invalid syntax
~~~
{: .error}

*   Look more closely at the error message:

~~~
# use a multiline expression by pressing ctrl + enter after each line
brain_volume = 1302
print( brain_volume 
# execute the multiline expression using shift + enter
~~~
{: .python}

~~~
  print( brain_volume # in ipython we must execute this command using shift + enter

  File "<ipython-input-408-c217d1563eb4>", line 2
    print( brain_volume # in ipython we must execute this command using shift + enter
                                                                            ^
SyntaxError: unexpected EOF while parsing
~~~
{: .error}

*   The message indicates a problem on first line of the input ("line 2").
    *   In this case the "ipython-input" section of the file name tells us that
        we are working with input into IPython.
*   Next is the problematic line of code, indicating the problem with a `^`
    pointer.

## Python reports a runtime error when something goes wrong while a program is executing.

~~~
brain_volume = 1302
grey_matter = 700 
csf_and_white_matter = brain_volume - grey_matters # mis-spelled 'grey_matter'
~~~
{: .python}

~~~
NameError: name 'grey_matters' is not defined
~~~
{: .error}

*   Fix syntax errors by reading the source and runtime errors by tracing execution.

## Every function returns something.

*   Every function call produces some result.
*   If the function doesn't have a useful result to return, it usually returns
    the special value `None`.

~~~
result = print('hippocampus')
~~~
{: .python}

~~~
hippocampus
~~~
{: .output}

~~~
print(result)
~~~
{: .python}

~~~
None
~~~
{: .output}

> ## What Happens When
>
> 1. Explain in simple terms the order of operations in the following program:
>    when does the addition happen, when does the subtraction happen,
>    when is each function called, etc.
> 2. What is the final value of `radiance`?
>
> ~~~
> radiance = 1.0
> radiance = max(2.1, 2.0 + min(radiance, 1.1 * radiance - 0.5))
> ~~~
> {: .python}
{: .challenge}

> ## Spot the Difference
>
> 1. Predict what each of the `print` statements in the program below will print.
> 2. Does `max(len(grey_matter), white_matter)` run or produce an error message?
>    If it runs, does its result make any sense?
>
> ~~~
> grey_matter = "the good stuff"
> white_matter = "the wires"
> print(max(grey_matter, white_matter))
> print(max(len(grey_matter), len(white_matter)))
> ~~~
> {: .python}
{: .challenge}

> ## Working with None
>
> Why don't `max` and `min` return `None` when they are given no arguments?
{: .challenge}

> ## Last Character of a String
>
> If Python starts counting from zero,
> and `len` returns the number of characters in a string,
> what index expression will get the last character in the string `roi_label`?
> (Note: we will see a simpler way to do this in a later episode.)
>
> > ## Solution
> >
> > `roi_label[len(roi_label) - 1]`
> {: .solution}
{: .challenge}
