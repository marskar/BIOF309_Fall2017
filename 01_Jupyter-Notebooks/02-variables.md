---
title: "Variables and Assignment"
teaching: 10
exercises: 10
questions:
- "How can I store data in programs?"
objectives:
- "Write programs that assign scalar values to variables and perform calculations with those values."
- "Correctly trace value changes in programs that use scalar assignment."
keypoints:
- "Use variables to store values."
- "Use `print` to display values."
- "Variables must be created before they are used."
- "Variables can be used in calculations."
- "Use an index to get a single character from a string."
- "Use a slice to get a substring."
- "Use the built-in function `len` to find the length of a string."
- "Python is case-sensitive."
- "Use meaningful variable names."
- "Variables in the current environment can be displayed or deleted using the
`%whos` and `%reset` IPython magics."
---

## Use variables to store values.

*   Variables are names for values.
*   In Python the `=` symbol assigns the value on the right to the name on the left.
*   The variable is created when a value is assigned to it.
*   Here, Python assigns a volume size to a variable `roi_vol`
    and a name in quotation marks to a variable `roi_label`.

~~~
roi_vol = 130
roi_label = 'hippocampus'
~~~
{: .python}

*   Variable names:
    *   cannot start with a digit
    *   cannot contain spaces, quotation marks, or other punctuation
    *   *may* contain an underscore (typically used to separate words in long variable names)
*   Underscores at the start like `__roi_vol` have a special meaning
    so we won't do that until we understand the convention.

## Variables can be displayed by simply executing them as an expression


~~~
roi_vol
~~~
{: .python}

~~~
130
~~~
{: .output}

~~~
roi_label
~~~
{: .python}

~~~
'hippocampus'
~~~
{: .output}

## Variables must be created before they are used.

*   If a variable doesn't exist yet, or if the name has been mis-spelled,
    Python reports an error.
    *   Unlike some languages, which "guess" a default value.

~~~
brain_volume
~~~
{: .python}
~~~
----------------------------------------------------------
NameError                Traceback (most recent call last)
<ipython-input-12-dec7c88e2504> in <module>()
----> 1 brain_volume

NameError: name 'brain_volume' is not defined
~~~
{: .error}

*   The last line of an error message is usually the most informative.
<!-- *   We will look at error messages in detail [later]({{ page.root }}/05-error-messages/). -->

## Use comments to add documentation to programs.

~~~
# This sentence isn't executed by Python.
# print(brain_volume)
brain_volume = 1351   # Neither is this - anything after '#' is ignored.
~~~
{: .python}


## Variables can be used in calculations.

*   We can use variables in calculations just as if they were values.
    *   Remember, we assigned 130 to `roi_vol` a few lines ago.

~~~
corrected_roi_vol = roi_vol + 3
# Volume with a correction for a systematic bias: 
corrected_roi_vol
~~~
{: .python}
~~~
133
~~~
{: .output}

## Use an index to get a single character from a string.

*   Sometimes called a "subscript".
*   Each character in a string is in a particular location.
*   Use the location's index in square brackets to get the character.
*   Locations are numbered from 0 rather than 1.

~~~
roi_label = 'hippocampus'
roi_label[0]
~~~
{: .python}
~~~
h
~~~
{: .output}

## Use a slice to get a substring.

*   A slice extracts elements, based on a start and stop value
*   A slice consists of `[start:stop]`.
*   From the start value (inclusive) up to but not including the stop value (exclusive).
*   So the difference between stop and start is the slice's length.

~~~
roi_label[0:5]
~~~
{: .python}
~~~
hippo
~~~
{: .output}

## A slice with a different step
* We don't have to take every element in the range we specify. We can specify
the step  by which we take elements from the string.

~~~
roi_label[0:5:2]
~~~
{: .python}
~~~
hpo
~~~
{: .output}


## Use the built-in function `len` to find the length of a string.

~~~
len(roi_label)
~~~
{: .python}
~~~
11
~~~
{: .output}

*   Nested functions are evaluated from the inside out,
    just like in mathematics.



## Python is case-sensitive.

*   Python thinks that upper- and lower-case letters are different,
    so `Name` and `name` are different variables.
*   There are conventions for using upper-case letters at the start of variable names
    so we will use lower-case letters for now.

## Use `print` to display values.

*   Python has a built-in function called `print` that prints things as text.
*   Call the function (i.e., tell Python to run it) by using its name.
*   Provide values to the function (i.e., the things to print) in parentheses.
*   The values passed to the function are called 'arguments'


~~~
print(roi_label)
~~~
{: .python}

~~~
hippocampus
~~~
{: .output}

~~~
print('The', roi_label, 'is', roi_vol, 'cubic mm')
~~~
{: .python}
~~~
The hippocampus is 130 cubic mm
~~~
{: .output}

*   `print` automatically puts a single space between items to separate them.
*   And wraps around to a new line at the end.


## Use meaningful variable names.

*   Python doesn't care what you call variables as long as they obey the rules
    (alphanumeric characters and the underscore).

~~~
flabadab = 42
ewr_422_yY = 'Ahmed'
print(ewr_422_yY, 'is', flabadab, 'years old')
flabadab = 700
ewr_422_yY = 'frontal cortex'
print('The',ewr_422_yY, 'is', flabadab, 'cubic mm')
~~~
{: .python}

~~~
Ahmed is 42 years old
The frontal cortex is 700 cubic mm
~~~
{: .output}

*   Use meaningful variable names to help other people understand what the program does.
*   The most important "other person" is your future self.

## Variables exist in the IPython environment
We can list the variables we have defined, along with some details about them,
by executing the IPython magic `%whos`:
~~~
%whos
~~~
{: .python}

* These variables do not exist on the hard disk of the computer. They will not
  continue to exist if we stop our current IPython kernel (by executing
  `exit`). Ideally, in any time in our analysis we should be able to remove
  these variables and regenerate them  again by running a script file
  containing all of the commands we used to get to our current state.

* We will learn the tools that IPython provides to do this.

* For now we will simply learn how to delete all of the variables in the
  current environment. This is done using the `%reset` IPython magic and typing
  `y` and enter to confirm:

~~~
%reset
~~~
{: .python}

~~~
Once deleted, variables cannot be recovered. Proceed (y/[n])? 
~~~
{: .output}

~~~
y
~~~
{: .source}


> ## Swapping Values
>
> Draw a table showing the values of the variables in this program
> after each statement is executed.
> In simple terms, what do the last three lines of this program do?
>
> ~~~
> lowest = 1.0
> highest = 3.0
> volume = lowest
> lowest = highest
> highest = volume
> ~~~
> {: .python}
{: .challenge}

> ## Predicting Values
>
> What is the final value of `important_label` in the program below?
> (Try to predict the value without running the program,
> then check your prediction.)
>
> ~~~
> label = "hippocampus"
> important_label = label
> label = "visual"
> ~~~
> {: .python}
{: .challenge}

> ## Challenge
>
> If you assign `roi_vol = 130`,
> what happens if you try to get the second digit of `roi_vol`?
>
> > ## Solution
> > Numbers are not stored in the written representation,
> > so they can't be treated like strings.
> >
> > ~~~
> > roi_vol = 130
> > print(roi_vol[1])
> > ~~~
> > {: .python}
> > ~~~
> > TypeError: 'int' object is not subscriptable
> > ~~~
> > {: .error}
> {: .solution}
{: .challenge}

> ## Choosing a Name
>
> Which is a better variable name, `m`, `min`, or `minutes`?
> Why?
> Hint: think about which code you would rather inherit
> from someone who is leaving the lab:
>
> 1. `ts = m * 60 + s`
> 2. `tot_sec = min * 60 + sec`
> 3. `total_seconds = minutes * 60 + seconds`
>
> > ## Solution
> >
> > `minutes` is better because `min` might mean something like "minimum"
> > (and actually does in Python, but we haven't seen that yet).
> {: .solution}
{: .challenge}

> ## Slicing
>
> What does the following program print?
>
> ~~~
> sequence_type = 'MP_RAGE'
> print('sequence_type[1:3] is:', sequence_type[1:3])
> ~~~
> 
> > ## Solution
> >~~~
> >sequence_type[1:3] is: P_
> >~~~
> >{: .output}
>  {: .solution}
{: .challenge}
