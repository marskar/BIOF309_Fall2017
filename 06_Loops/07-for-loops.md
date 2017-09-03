---
title: "Iteration in Python"
teaching: 10
exercises: 15
questions:
- "How can I make a program do many things?"
objectives:
- "Implement a list comprehension to iterate over a collection."
- "Understand how a list comprehension is the application of a function to each element of a collection."
- "Understand that other types of comprehension exist."
- "Know the structure of a for loop."
- "Know about the existence of dictionary and generator comprehensions"
- "Know about for loops that use the Accumulator pattern to aggregate values."
keypoints:
- "The process of iteration executes commands once for each value in a collection."
- "Python uses comprehensions to iterate. List comprehensions are especially common."
- "Loop variables can be called anything (but it is strongly advised to have a meaningful name to the looping variable)."
- "Use `range` to iterate over a sequence of numbers."
- "Generator and dictionary comprehensions are similar to list comprehensions but their output is slightly different."
- "A `for` loop is made up of a loop variable, a collection, and a body."
- "The first line of the `for` loop must end with a colon, and the body must be indented."
- "Indentation is always meaningful in Python."
- "The body of a for loop can contain many statements."
- "The Accumulator pattern turns many values into one."
---
## Performing an operation many times

In our previous lesson we learnt how to store multiple numbers together in a
list. We constructed a list with a number of roi volumes, shown below, that we
would now like to perform some operations upon. For example, we want to divide
each number by 1000.

~~~
roi_volumes = [2.73,145.3,12.7,16.2, 27.6]
len(roi_volumes * 1000)
~~~
{: .python}

~~~
5000
~~~
{: .output}

That hasn't conveniently multiplied each element of the list by 1000. It has
instead replicated our list 1000 times. An attempt at division just fails
outright:

~~~
roi_volumes / 1000
~~~
{: .python}

~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-c4ca083b5b87> in <module>()
----> 1 roi_volumes/10

TypeError: unsupported operand type(s) for /: 'list' and 'int'
~~~
{: .output}

> ## The Numpy package
> 
> When dealing with arrays of numbers the package Numpy is the ideal place to
> start. It efficiently handles multi-dimension numeric data. With this package
> we have access to convenient operations for matrices of numbers that we
> attempted to perform above. For the purposes of instruction we will use list
> comprehensions to perform these operations instead. Although it presents an
> unrealistic way of operatic on matrices we will quickly see that it
> generalizes to other types of data.
{: .callout}


## Iteration in Python using a list comprehension


Python gives us a convenient tool to create lists using iteration called a list
comprehension. A list comprehension allows us to iterate over a variable (also
called traversing the variable) . Some variables, or rather some types, support
iteration and are called "iterables" while some do not. As we traverse our
collection we represent each element by a temporary variable called a looping
variable. The output of our list comprehension is the result some operation on
this looping variable.

In summary  In order to construct a list comprehension we need the following:

* a collection we want to iterate over ("roi_volumes")
* an arbitrary name for our looping variable ("x")
* an operation (a function) to apply to our looping variable
* square brackets to denote that the expression is a list comprehension

Lets implement our previous attempt to multiply "roi_volumes" by 1000 using a
list comprehension:

~~~
converted_roi_volumes = [x * 1000 for x in roi_volumes]
converted_roi_volumes
~~~
{: .python}

~~~
[2730.0, 145300.0, 12700.0, 16200.0, 27600.0]
~~~
{: .output}

This is a little messy because of the unnecessary precision after the
decimal point. We'll use the built-in function `round` to fix that:
~~~
converted_roi_volumes = [round(x * 1000) for x in roi_volumes]
converted_roi_volumes
~~~
{: .python}

~~~
[2730, 145300, 12700, 16200, 27600]
~~~
{: .output}

Now we have output that we wanted. 



> ## Python looping variables are elements of the collection
> 
> The looping variable may confuse some people. In other programming languages
> the value of the looping variable is a number, which can be used as an index
> into a collection. It can take a little time to get used to this switch. We
> will see later that we can easily access the current element's index too if
> we wish.
{: .callout}

## List comprehensions with strings

Another type of iterable is the string type. So as an example

~~~
roi_label = 'hippocampus'
[L for L in roi_label]
~~~
{: .python}

~~~
 ['h', 'i', 'p', 'p', 'o', 'c', 'a', 'm', 'p', 'u', 's']
 ~~~
{: .output}


## Use `range` to iterate over a sequence of numbers.

*   The built-in function `range` produces a sequence of numbers.
    *   This is *not* a list: the numbers are produced on demand to make
        looping over large ranges more efficient.
*   `range(N)` is the numbers 0..N-1
    *   This is the legal indices of a list or character string of length N

Some output generated using the `range()` function:

~~~
range(5)
~~~
{: .python}

~~~
range(0,5)
~~~
{: .output}

~~~
range(0, 5)
~~~
{: .python}

~~~
range(0,5)
~~~
{: .output}

~~~
list(range(0, 5))
~~~
{: .python}

~~~
[0, 1, 2, 3, 4]
~~~
{: .output}

* For the last command entered in the above code we converted the range object
into a list. This had the advantage that we could see every number it generates
but generally we don't want to do that. Usually we would just use it for
iteration and never generate all of its contents at once. 

* Note that when specifying the start and stop value for a range the resulting
  elements include the start value but not the stop value.

Here's an example of combining the range function, a useful type of iterable, with a list comprehension:

~~~
[str(x) for x in range(10)]
~~~
{: .python}

~~~
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
~~~
{: .output}

## Other types of comprehensions

In addition to list comprehensions, Python has what are called generator
comprehensions and dictionary comprehensions. These can be useful in different
situations. These comprehensions are constructed with parentheses and braces and  produce variables of type "generator" and "dict" respectively.
Later we will see that some of the functions in Python's standard library return the generator. In a similar manner to the range object we just saw it is enough to know that we can work with the data more easily by simply converting it to a list:


~~~
a_generator = (x for x in roi_label)
a_generator
~~~
{: .python}

~~~
<generator object <genexpr> at 0x2ba6900a2888>
~~~
{: .output}

~~~
list(a_generator)
~~~
{: .python}

~~~
['h', 'i', 'p', 'p', 'o', 'c', 'a', 'm', 'p', 'u', 's']
~~~
{: .output}


## A "for" loop in Python

Like other languages Python can also express iteration as  a for loop:

~~~
for x in roi_volumes:
    print(x)
~~~
{: .python}

*   This `for` loop is equivalent to:

~~~
print(2.73)
print(145.3)
print(12.7)
print(16.2)
print( 27.6)
~~~
{: .python}

*   And the `for` loop's output is:

~~~
2.73
145.3
12.7
16.2
27.6
~~~
{: .output}

## The first line of the `for` loop must end with a colon, and the body must be indented.

*   The colon at the end of the first line signals the start of a *block* of statements.
*   Python uses indentation rather than `{}` or `begin`/`end` to show *nesting*.
    *   Any consistent indentation is legal, but the Python [style
        guide](https://www.python.org/dev/peps/pep-0008/) for code encourages 4
        spaces.

~~~
for number in [2, 3, 5]:
print(number)
~~~
{: .python}
~~~
IndentationError: expected an indented block
~~~
{: .error}

*   Indentation is always meaningful in Python.

## The body of a loop can contain many statements.

*   No loop should be more than a few lines long. It makes it too hard for
    people   to keep larger chunks of code in mind.

~~~

for x in roi_volumes:
    squared = round(x ** 2)
    cubed = round(x ** 3)
    print(x, squared, cubed)
~~~
{: .python}

~~~
2.73 7 20
145.3 21112 3067587
12.7 161 2048
16.2 262 4252
27.6 762 21025
~~~
{: .output}

*   We will learn about functions later. With a function we can capture the
    code in the body of this for loop and have a simple one line expression to
    return the values we want given an input collection.




## The Accumulator pattern turns many values into one.

*   A common pattern in programs is to:
    1.  Initialize an *accumulator* variable to zero, the empty string, or the empty list.
    2.  Update the variable with values from a collection.

~~~
# Sum the integers 1 to 10.
total = 0
for number in range(1,11):
   total = total + number
print(total)
~~~
{: .python}
~~~
55
~~~
{: .output}

## Patterns of computation that a list comprehension doesn't work for.

* It is important to spot this accumulator pattern because list comprehensions
  cannot solve this task.
* The above code collapses (or aggregates) 10 numbers into a single integer
  using a loop. In this case we can see that we are just taking the sum of all
  the numbers. An easier way of doing this is by using the sum function in
  python:

~~~
sum(range(1,11))
~~~
{: .python}

~~~
55
~~~
{: .output}

* Another pattern of computation that list comprehensions cannot be used for is
  the application of a windowing function to some data. We will see an example
  in the cumulative sum exercise in this lesson. Later we will see that
  packages like Numpy and Pandas can typically do these types of operations for us.


> ## UPPERCASE
> 
> ~~~
> list_of_strings = list('hippocampus')
> ~~~
> {: .python}
> 
> What is the type of the variable list_of_strings? What is its length? Use a
> list comprehension to return a list with each element of the list containing
> a single letter of the word hippocampus but as an uppercase character.
> 
>> ## Solution
>> 
>> ~~~
>> print('Type: ', type(list_of_strings))
>> print('Length: ', len(list_of_strings))
>> answer = [x.upper() for x in list_of_strings]
>> print(answer)
>> ~~~
>> {: .python}
>> 
>> ~~~
>> Type:  <class 'list'> 
>> Length:  11
>> ['H', 'I', 'P', 'P', 'O', 'C', 'A', 'M', 'P', 'U', 'S']
>> ~~~
>> {: .output}
> {: .solution}
{: .challenge}

> ## Classifying Errors
> 
> Is an indentation error a syntax error or a runtime error?
{: .challenge}



> ## Cumulative Sum
> 
> ~~~
> data = [1,2,2,5]
> ~~~
> {: .python}
> 
> Given the above list, reorder and properly indent the lines of code below
> so that they print an array with the cumulative sum of data.
> The result should be `[1, 3, 5, 10]`.
> 
> 
> 
> ~~~
> cumulative += [sum]
> for number in data:
> cumulative = []
> sum += number
> print(cumulative)
> 
> sum=0
> ~~~
> {: .python}
> 
> > ## Solution
> > 
> > ~~~
> > sum=0
> > cumulative = []
> > for number in data:
> >     sum += number
> >     cumulative += [sum]
> > print(cumulative)
> >        
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}


> ## Identifying Item Errors
> 
> 1. Read the code below and try to identify what the errors are
>    *without* running it.
> 2. Run the code, and read the error message. What type of error is it?
> 3. Fix the error.
> 
> ~~~
> regions = ['hippocampus', 'hypothalamus', 'insula', 'LGN']
> print('My favorite brain region is ', regions[4])
> ~~~
> {: .python}
{: .challenge}
