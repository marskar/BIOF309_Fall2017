---
title: "Conditionals"
teaching: 15
exercises: 5
questions:
- "How can programs do different things for different data?"
objectives:
- "Correctly write programs that use if and else statements and simple Boolean expressions (without logical operators)."
- "Trace the execution of unnested conditionals and conditionals inside loops."
keypoints:
- "Boolean values, either True or False, represent the truth of a statement in Python"
- "As well as functions that specifically return values of type bool,
  statements about truth use what are called comparative operators."
- "Use `if` statements to control whether or not a block of code is executed."
- "Conditionals are often used with iteration."
- "Use `else` to execute a block of code when an `if` condition is *not* true."
- "Use `elif` to specify additional tests."
- "Conditions are tested once, in order."
- "Create a table showing variables' values to trace a program's execution."
---

## Comparisons in Python

Python allows us to test the truth of statements using certain functions as
well as by using what are called comparison operators. These include `>`, '<',
`>=`, `<=`, `==`, `!=`, `is`, `is not`

Some examples of using these operators:


~~~
5 > 4
~~~
{: .python}

~~~
True
~~~
{: .output}

~~~
5 == 5
~~~
{: .python}

~~~
True
~~~
{: .output}

~~~
5 != 5
~~~
{: .python}

~~~
False
~~~
{: .output}



~~~
 5 is not 5.0
~~~
{: .python}

~~~
True
~~~
{: .output}

## The assert statement

The `assert` statement is an important tool available to us to make sure our
programs behave as we intend. We follow the assert command by an expression
that it will assess for truth. If the expression `False` is returned our
program will not execute. This is far better than continuing further to produce
an obscure runtime error. Worse still if our program is executed with some of
our assumptions not mess it may generate some content in error and we would
have no idea this has happened.

## Use `if` statements to control whether or not a block of code is executed.

*   An `if` statement (more properly called a *conditional* statement)
    controls whether some block of code is executed or not.
*   Structure is similar to a `for` statement:
    *   First line opens with `if` and ends with a colon
    *   Body containing one or more statements is indented (usually by 4 spaces)

~~~
metasearch_dir = Path('data_not_in_repo/metasearch')
data_exists = metasearch_dir.exists()
if data_exists:
    print('Data directory has been downloaded')
~~~
{: .python}

~~~
Data directory has been downloaded
~~~
{: .output}

If the statement does not evaluate to `True` the indented code will not be
evaluated and in this case nothing will be printed:

~~~
fake_dir = Path('metasearch/fast_cars')
if fake_dir.exists():
    print('Directory exists!')
~~~
{: .python}

## Recording changes to our analysis.

We should edit our script at this point to tidy it up. What changes can we make
that will best promote reproducibility? Ideally we would have written a
conditional statement at the beginning of our analysis so that we are certain
that both conditions of our if/else code block evaluated. In reality we will
always have bits of code that we have to add to our code in retrospect. Ideally
at this point we would delete our data directory to check that every condition
runs.


## Use `else` to execute a block of code when an `if` condition is *not* true.

*   `else` is always attached to `if`.
*   Allows us to specify an alternative to execute when the `if` *branch* isn't taken.

~~~
fake_dir = Path('metasearch/fast_cars')
if fake_dir.exists():
    print('Directory exists!')
else:
    print('There is no directory with the path: ', fake_dir)
~~~
{: .python}

~~~
There is no directory with the path: metasearch/fast_cars
~~~
{: .output}

## Use `elif` to specify additional tests.

*   May want to provide several alternative choices, each with its own test.
*   Use `elif` (short for "else if") and a condition to specify these.
*   Always associated with an `if`.
*   Must come before the `else` (which is the "catch all").

~~~
from pathlib import Path
metasearch_dir = Path('data_not_in_repo/metasearch')
data_exists = metasearch_dir.exists()
in_repro_course = Path.cwd().name == 'repro_course'
if data_exists and in_repro_course:
    print('Data directory has been downloaded')
elif in_repro_course:
    !git clone https://github.com/OpenNeuroLab/metasearch.git {metasearch_dir}
else:
    assert(False)
~~~
{: .python}

~~~
Data directory has been downloaded
~~~
{: .output}

We can see that at this point if we change to another directory our script will
no longer display text as expected when we execute it:

~~~
%cd .. # to change into the parent directory
%run repro_course/metasearch_analysis.py
~~~
{: .python}

If we run our file in debug mode and then press `c` for continue we can see the
exception we raised with our `assert` statement.

~~~
%run -d repro_course/metasearch_analysis.py
~~~
{: .python}

~~~
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
/usr/local/Anaconda/envs/py3.5/lib/python3.5/site-packages/IPython/core/interactiveshell.py in safe_execfile(self, fname, *where, **kw)
   2479                 py3compat.execfile(
   2480                     fname, glob, loc,
-> 2481                     self.compile if kw['shell_futures'] else None)
   2482             except SystemExit as status:
   2483                 # If the call was made with 0 or None exit status (sys.exit(0)

/usr/local/Anaconda/envs/py3.5/lib/python3.5/site-packages/IPython/utils/py3compat.py in execfile(fname, glob, loc, compiler)
    184         with open(fname, 'rb') as f:
    185             compiler = compiler or compile
--> 186             exec(compiler(f.read(), fname, 'exec'), glob, loc)
    187 
    188     # Refactor print statements in doctests.

/home/rodgersleejg/repro_course/metasearch_analysis.py in <module>()
      1 # coding: utf-8
----> 2 from pathlib import Path
      3 metasearch_dir = Path('data_not_in_repo/metasearch')
      4 data_exists = metasearch_dir.exists()
      5 in_repro_course = Path.cwd().name == 'repro_course'

AssertionError: 
~~~
{: .output}


We will now change back to our repro_course directory to continue with our analysis.

~~~
%cd repro_course
~~~
{: .python}

~~~
/home/this_user/repro_course
~~~
{: .output}


## Final points on conditionals

*   Python steps through the branches of the conditional in order, testing each in turn.
*   So ordering matters.

*   Often use conditionals in a loop to "evolve" the values of variables.
*   Conditionals are often used inside loops.
*   Conditional statements can be incorporated into list comprehensions:


~~~
[ x for x in range(10) if x > 4]
~~~
{: .python}

~~~
[5, 6, 7, 8, 9]
~~~
{: .output}

*  It is important to be aware of all of the different cases that can arise
   from our conditional testing. In our example with testing for certain
   conditions on our file system we tested two statements using two outcomes.
   This yields 4 unique states that our program could theoretically encounter.
   Have we written our code to account for each of these situations?
*  A useful set of tools are provided by the itertools package. In our current
   situation the `product` function can quickly show us all of the test cases
   that we should consider:


~~~
import itertools
meta_exist = ['metasearch in pwd', 'metasearch not in pwd']
repro_as_pwd = ['repro_course is pwd', 'repro_course not pwd']
list(itertools.product(meta_exist, repro_as_pwd))
~~~
{: .python}

~~~
[('metasearch in pwd', 'repro_course is pwd'),
 ('metasearch in pwd', 'repro_course not pwd'),
 ('metasearch not in pwd', 'repro_course is pwd'),
 ('metasearch not in pwd', 'repro_course not pwd')]
~~~
{: .output}


## Saving our work.

First we should search for our command where we used an else statement (`%hist
-n -g else`) then we should append this command to our script.

~~~
%save -a metasearch_analysis.py 42 # enter the number of the multi-line if-else statement
~~~
{: .python}

~~~
The following commands were written to file `metasearch_analysis.py`:
from pathlib import Path
metasearch_dir = Path('data_not_in_repo/metasearch')
data_exists = metasearch_dir.exists()
in_repro_course = Path.cwd().name == 'repro_course'
if data_exists and in_repro_course:
    print('Data directory has been downloaded')
elif in_repro_course:
    get_ipython().system('git clone https://github.com/OpenNeuroLab/metasearch.git {metasearch_dir}')
else:
    assert(False)
~~~
{: .output}


> ## Identifying Variable Name Errors
> 
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code and read the error message.
>    What type of `NameError` do you think this is?
>    Is it a string with no quotes, a misspelled variable, or a 
>    variable that should have been defined but was not?
> 3. Fix the error.
> 4. Repeat steps 2 and 3, until you have fixed all the errors.
> 
> ~~~
> for number in range(10):
>     # use a if the number is a multiple of 3, otherwise use b
>     if (Number % 3) == 0:
>         message = message + a
>     else:
>         message = message + "b"
> print(message)
> ~~~
> {: .python}
{: .challenge}


> ## Compound Relations Using `and`, `or`, and Parentheses
> 
> Often, you want some combination of things to be true.  You can combine
> relations within a conditional using `and` and `or`.  Continuing the example
> above, suppose you have
> 
> ~~~
> mass     = [ 3.54,  2.07,  9.22,  1.86,  1.71]
> velocity = [10.00, 20.00, 30.00, 25.00, 20.00]
> 
> i = 0
> for i in range(5):
>     if mass[i] > 5 and velocity[i] > 20:
>         print "Fast heavy object.  Duck!"
>     elif mass[i] > 2 and mass[i] <= 5 and velocity[i] <= 20:
>         print "Normal traffic"
>     elif mass[i] <= 2 and velocity <= 20:
>         print "Slow light object.  Ignore it"
>     else:
>         print "Whoa!  Something is up with the data.  Check it"
> ~~~
> {: .python}
> 
> Just like with arithmetic, you can and should use parentheses whenever there
> is possible ambiguity.  A good general rule is to *always* use parentheses
> when mixing `and` and `or` in the same condition.  That is, instead of:
> 
> ~~~
> if mass[i] <= 2 or mass[i] >= 5 and velocity[i] > 20:
> ~~~
> {: .python}
> 
> write one of these:
> 
> ~~~
> if (mass[i] <= 2 or mass[i] >= 5) and velocity[i] > 20:
> if mass[i] <= 2 or (mass[i] >= 5 and velocity[i] > 20):
> ~~~
> {: .python}
> 
> so it is perfectly clear to a reader (and to Python) what you really mean.
{: .callout}

> ## Tracing Execution
> 
> What does this program print?
> 
> ~~~
> pressure = 71.9
> if pressure 50.0:
>     pressure = 25.0
> elif pressure <= 50.0:
>     pressure = 0.0
> print(pressure)
> ~~~
> {: .python}
{: .challenge}

