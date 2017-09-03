---
title: "Data Types and Type Conversion"
teaching: 10
exercises: 10
questions:
- "What kinds of data do programs store?"
- "How can I convert one type to another?"
objectives:
- "Explain key differences between integers and floating point numbers."
- "Explain key differences between numbers and character strings."
- "Use built-in functions to convert between integers, floating point numbers, and strings."
keypoints:
- "Every value has a type."
- "Use the built-in function `type` to find the type of a value."
- "Types control what operations can be done on values."
- "Strings can be added and multiplied."
- "Strings have a length (but numbers don't)."
- "Must convert numbers to strings or vice versa when operating on them."
- "Can mix integers and floats freely in operations."
- "Variables only change value when something is assigned to them."
---
## Every value has a type.

*   Every value in a program has a specific type.
*   Integer (`int`): counting numbers like 3 or -512.
*   Floating point number (`float`): fractional numbers like 3.14159 or -2.5.
    *   Integers are used to count, floats are used to measure.
*   Character string (usually just called "string", `str`): text.
    *   Written in either single quotes or double quotes (as long as they match).
    *   The quotation marks aren't printed when the string is displayed.

## Use the built-in function `type` to find the type of a value.

*   Use the built-in function `type` to find out what type a value has.
*   Works on variables as well.
    *   But remember: the *value* has the type --- the *variable* is just a label.

~~~
type(52)
~~~
{: .python}
~~~
<class 'int'>
~~~
{: .output}

~~~
disease = 'schizophrenia'
type(disease)
~~~
{: .python}
~~~
str
~~~
{: .output}

## Types control what operations can be done on values.

*   A value's type determines what the program can do to it.

~~~
5 - 3
~~~
{: .python}
~~~
2
~~~
{: .output}

~~~
'frontotemporal' - 'fronto'
~~~
{: .python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-67f5626a1e07> in <module>()
----> 1 print('frontotemporal' - 'fronto')

TypeError: unsupported operand type(s) for -: 'str' and 'str'
~~~
{: .error}

## Strings can be added and multiplied.

*   "Adding" character strings concatenates them.

~~~
roi_label = 'fronto' + 'temporal'
roi_label
~~~
{: .python}
~~~
fronto temporal
~~~
{: .output}

*   Multiplying a character string by an integer replicates it.
    *   Since multiplication is just repeated addition.

~~~
dna_repeat_sequence = 'CAG' * 10
dna_repeat_sequence
~~~
{: .python}
~~~
CAGCAGCAGCAGCAGCAGCAGCAGCAGCAG
~~~
{: .output}

## Strings have a length (but numbers don't).

*   The built-in function `len` counts the number of characters in a string.

~~~
len(dna_repeat_sequence)
~~~
{: .python}
~~~
30
~~~
{: .output}

*   But numbers don't have a length (not even zero).

~~~
len(52)
~~~
{: .python}
~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-f769e8e8097d> in <module>()
----> 1 print(len(52))

TypeError: object of type 'int' has no len()
~~~
{: .error}

## Must convert numbers to strings or vice versa when operating on them.

*   Cannot add numbers and strings.

~~~
1 + '2'
~~~
{: .python}

~~~
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-fe4f54a023c6> in <module>()
----> 1 1 + '2')

TypeError: unsupported operand type(s) for +: 'int' and 'str'
~~~
{: .error}

*   Not allowed because it's ambiguous: should `1 + '2'` be `3` or `'12'`?
*   Some types can be converted to other types by using the type name as a function.

~~~
1 + int('2')
~~~
{: .python}

~~~
3
~~~
{: .output}

~~~
str(1) + '2'
~~~
{: .python}

~~~
12
~~~
{: .output}

## Can mix integers and floats freely in operations.

*   Integers and floating-point numbers can be mixed in arithmetic.
    *   Python automatically converts integers to floats as needed.

~~~
1 / 2.0
~~~
{: .python}

~~~
0.5
~~~
{: .output}

> ## Division Types
> 
> The `//` operator calculates the whole-number result of division,
> while the '%' operator calculates the remainder from division:
> 
> ~~~
> 5 // 3
> ~~~
> {: .python}
> 
> ~~~
> 1
> ~~~
> {: .output}
> 
> ~~~
> 5 % 3
> ~~~
> {: .python}
> 
> ~~~
> 2
> ~~~
> {: .output}
> 
{: .callout}

~~~
# three squared is:
3.0 ** 2
~~~
{: .python}
~~~
# three squared is :
9.0
~~~
{: .output}

## Variables only change value when something is assigned to them.

*   If we make one cell in a spreadsheet depend on another,
    and update the latter,
    the former updates automatically.
*   This does **not** happen in programming languages.

~~~
brain_volume = 1246
brain_volume_corrected = brain_volume * 1.2
brain_volume = 1400
brain_volume
~~~
{: .python}

~~~
1400
~~~
{: .output}

~~~
brain_volume_corrected
~~~
{: .python}

~~~
1495.2
~~~
{: .output}

*   The computer reads the value of `brain_volume` when doing the multiplication,
    creates a new value, and assigns it to `brain_volume_corrected`.
*   After that, `brain_volume_corrected` does not remember where it came from.

> ## Fractions
> 
> What type of value is 3.4?
> How can you find out?
> 
> > ## Solution
> > 
> > It is a floating-point number (often abbreviated "float").
> > 
> > ~~~
> > print(type(3.4))
> > ~~~
> > {: .python}
> > ~~~
> > <class 'float'>
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Automatic Type Conversion
> 
> What type of value is 3.25 + 4?
> 
> > ## Solution
> > 
> > It is a float:
> > integers are automatically converted to floats as necessary.
> > 
> > ~~~
> > result = 3.25 + 4
> > print(result, 'is', type(result))
> > ~~~
> > {: .python}
> > ~~~
> > 7.25 is <class 'float'>
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Choose a Type
> 
> What type of value (integer, floating point number, or character string)
> would you use to represent each of the following?
> 
> 1. Number of days since the start of the year.
> 2. Time elapsed since the start of the year.
> 3. Brain volume.
> 4. Number of scan sequences used in a scan session.
> 5. Disease state.
> 6. Scan sequence name.
{: .challenge}

> ## Type Conversions with Numbers
> 
> `float` will convert a string to a floating point number,
> and `int` will convert a floating point number to an integer:
> 
> ~~~
> float("3.4")
> ~~~
> {: .python}
> 
> ~~~
> 3.4
> ~~~
> {: .output}
> 
> ~~~
> int(3.4)
> ~~~
> {: .python}
> 
> ~~~
> 3
> ~~~
> {: .output}
> 
> Given that,
> what do you expect this program to do?
> What does it actually do?
> Why do you think it does that?
> 
> ~~~
> int("3.4")
> ~~~
> {: .python}
> > ## Solution
> > ~~~
> > We would expect to return an integer value of 3.
> > However, it returns the error:
> > 
> > ~~~
> > {: .output}
> > 
> > ~~~
> > ----------------------------------------------------------
> > ValueError               Traceback (most recent call last)
> > <ipython-input-92-ec6729dfccdc> in <module>()
> > ----> 1 int("3.4")
> > 
> > ValueError: invalid literal for int() with base 10: '3.4'
> > ~~~
> > {: .error}
> {: .solution}
{: .challenge}
