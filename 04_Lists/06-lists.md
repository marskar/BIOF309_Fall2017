---
title: "Lists"
teaching: 15
exercises: 10
questions:
- "How can I store multiple values?"
objectives:
- "Explain why programs need collections of values."
- "Write programs that create flat lists, index them, slice them, and modify
them through assignment and method calls."
keypoints:
- "A list stores many values in a single structure."
- "Use an item's index to fetch it from a list."
- "Lists' values can be replaced by assigning to them."
- "Appending items to a list lengthens it."
- "Use `del` to remove items from a list entirely."
- "The empty list contains no values."
- "Lists may contain values of different types."
- "Character strings can be indexed like lists."
- "Character strings are immutable."
- "Indexing beyond the end of the collection is an error."
---
## A list stores many values in a single structure.

*   When we wish to work with hundreds of variables defining them all explicitly
would be at least as slow as doing them by hand. For example if we had many
regions in the brain that we wished to analyse we might have many numbers. Each
number would correspond to the volume of a particular ROI like `cingulate`,
`limbic`, etc.
*   Use a *list* to store many values together.
    *   Contained within square brackets: `[...]`.
    *   Values separated by commas: `,`.
*   Use `len` to find out how many values are in a list.

~~~
roi_volumes = [2.73,145.3,12.7,16.2, 27.6]
# Volume of ROIs :  
roi_volumes
~~~
{: .python}

~~~
[2.73,145.3,12.7,16.2, 27.6]
~~~
{: .output}

~~~
# length: 
len(roi_volumes)
~~~
{: .python}

~~~
5
~~~
{: .output}

## Use an item's index to fetch it from a list.

*   Just like strings.

~~~
# The item with index 0 in the list is : 
roi_volumes[0]
~~~
{: .python}

~~~
2.73
~~~
{: .output}

~~~
# The item with index 4 in the list is : 
roi_volumes[4]
~~~
{: .python}

~~~
27.6
~~~
{: .output}

## Lists' values can be replaced by assigning to them.

*   Use an index expression on the left of assignment to replace a value.

~~~
roi_volumes[0] = 26.5
# Our list is now: 
roi_volumes
~~~
{: .python}

~~~
Our list is now: [26.5,145.3,12.7,16.2, 27.6]
~~~
{: .output}

## Appending items to a list lengthens it.

*   Use `list_name.append` to add items to the end of a list.

~~~
# Our list is initially: 
roi_volumes 
~~~
{: .python}

~~~
[26.5,145.3,12.7,16.2, 27.6]
~~~
{: .output}

~~~
roi_volumes.append(14.2)
roi_volumes.append(140)
# Our list has now become: 
roi_volumes
~~~
{: .python}

~~~
[26.5,145.3,12.7,16.2, 27.6,14.2,140]
~~~
{: .python}

*   `append` is a *method* of lists.
    *   Like a function, but tied to a particular object.
*   Use `object_name.method_name` to call methods.
    *   Deliberately resembles the way we refer to things in a package. We'll learn about packages later.
*   We will meet other methods of lists as we go along.
    *   In IPython, after typing a period after an object we can preview the
        methods available to us by hitting the tab-key. Alternatively we can
        see the methods by using the `dir` function or by accessing the help for
        an object.

## Use `del` to remove items from a list entirely.

*   `del list_name[index]` removes an item from a list and shortens the list.
*   Not a function or a method, but a statement in the language.

~~~
# roi_volumes before removing last item: 
roi_volumes
~~~
{: .python}

~~~
[26.5,145.3,12.7,16.2, 27.6,14.2,140]
~~~
{: .output}

~~~
del roi_volumes[6]
# roi_volumes after removing last item: 
roi_volumes
~~~
{: .python}

~~~
[26.5,145.3,12.7,16.2, 27.6,14.2]
~~~
{: .output}

## The empty list contains no values.

*   Use `[]` on its own to represent a list that doesn't contain any values.
    *   "The zero of lists."
*   Helpful as a starting point for collecting values which we will see when we
learn about iteration.

## Lists may contain values of different types.

*   A single list may contain numbers, strings, and anything else.

~~~
goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
~~~
{: .python}

While this list can be created there are better ways of representing this type of information.

## Character strings can be indexed like lists.

*   As we saw before, indexing into strings is the same as lists.

~~~
label_for_roi = 'cortex_left'
# The character indexed by 0: 
label_for_roi[0]
# The character indexed by 3: 
~~~
{: .python}

~~~
c
~~~
{: .output}

~~~
label_for_roi[3]
~~~
{: .python}

~~~

t
~~~
{: .output}

## Character strings are immutable.

*   Cannot change the characters in a string after it has been created.
    *   *Immutable*: cannot be changed after creation.
    *   In contrast, lists are *mutable*: they can be modified in place.
*   Python considers the string to be a single value with parts,
    not a collection of values.

~~~
label_for_roi[0] = 'C'
~~~
{: .python}

~~~
TypeError: 'str' object does not support item assignment
~~~
{: .error}

*   Lists and character strings are both *collections*.

## Indexing beyond the end of the collection is an error.

*   Python reports an `IndexError` if we attempt to access a value that doesn't exist.
    *   This is a kind of [runtime error]({{ page.root }}/05-error-messages/).
    *   Cannot be detected as the code is parsed
        because the index might be calculated based on data.

~~~
# The character indexed by 99 is: 
label_for_roi[99]
~~~
{: .python}

~~~
IndexError: string index out of range
~~~
{: .output}

> ## Fill in the Blanks
> 
> Fill in the blanks so that the program below produces the output shown.
> 
> ~~~
> values = []
> values.____(1)
> values.____(3)
> values.____(5)
> print('first time:', values)
> values = values[____]
> print('second time:', values)
> ~~~
> {: .python}
> 
> ~~~
> first time: [1, 3, 5]
> second time: [3, 5]
> ~~~
> {: .output}
> 
> > ## Solution
> > 
> > ~~~
> > values = []
> > values.append(1)
> > values.append(3)
> > values.append(5)
> > print('first time:', values)
> > values = values[1:3]
> > print('second time:', values)
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## How Large is a Slice?
> 
> If 'low' and 'high' are both non-negative integers,
> how long is the list `values[low:high]`?
> 
> > ## Solution
> > 
> > ~~~
> > high-low
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## From Strings to Lists and Back
> 
> Given this:
> 
> ~~~
> print('string to list:', list('ADHD'))
> print('list to string:', ''.join(['c', 'n', 's']))
> ~~~
> {: .python}
> ~~~
> string to list: ['A', 'D', 'H', 'D']
> list to string: 'cns'
> ~~~
> {: .output}
> 
> 1.  Explain in simple terms what `list('some string')` does.
> 2.  What does `'-'.join(['x', 'y'])` generate?
{: .challenge}

> ## Working With the End
> 
> What does the following program print?
> 
> ~~~
> roi_label = 'hippocampus'
> print(roi_label[-1])
> ~~~
> {: .python}
> 
> 1.  How does Python interpret a negative index?
> 2.  If a list or string has N elements,
> what is the most negative index that can safely be used with it,
> and what location does that index represent?
> 3.  If `values` is a list, what does `del values[-1]` do?
> 4.  How can you display all elements but the last one without 
> changing `values`?
>     (Hint: you will need to combine slicing and negative indexing.)
> 
> > ## Solution
> > 
> > ~~~
> > 1: It retrieves elements by stepping backwards through the string.
> > 2: -N. This location is the first element in the list.
> > 3: It deletes the last element in the list.
> > 4: values[0:-1]
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Stepping Through a List
> 
> What does the following program print?
> 
> ~~~
> roi_label = 'hippocampus'
> print(roi_label[::2])
> print(roi_label[::-1])
> ~~~
> {: .python}
> 
> 1.  If we write a slice as `low:high:stride`, what does `stride` do?
> 2.  What expression would select every other element, starting from the second?
> 
> > ## Solution
> > 
> > ~~~
> > hpoaps
> > supmacoppih
> > 
> > ~~~
> > {: .output}
> > 1: stride is the step to go through the list
> > 
> > The answer to question 2 is:
> > 
> > ~~~
> > listobject[1::2]
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Slice Bounds
> 
> What does the following program print?
> 
> ~~~
> roi_label = 'hippocampus'
> print(roi_label[0:20])
> print(roi_label[-1:3])
> ~~~
> {: .python}
> 
> > ## Solution
> > 
> > ~~~
> > hippocampus
> >        
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## Sort and Sorted
> 
> ~~~
> roi_label_as_list = list(roi_label)
> ~~~
> {: .python}
> 
> In simple terms, explain the difference between `sorted(roi_label_as_list)`
> and `roi_label_as_list.sort()`.
{: .challenge}

> ## Copying (or Not)
> 
> What do these two programs print?
> In simple terms, explain the difference between `new = old` and `new = old[:]`.
> For more information read about [deep copy vs shallow copy](https://docs.python.org/3/library/copy.html) 
> 
> ~~~
> # Program A
> old = list('Brain')
> new = old      # simple assignment
> new[0] = 'D'
> print('new is', new, 'and old is', old)
> ~~~
> {: .python}
> 
> ~~~
> # Program B
> old = list('Brain')
> new = old[:]   # assigning a slice
> new[0] = 'D'
> print('new is', new, 'and old is', old)
> ~~~
> {: .python}
{: .challenge}
