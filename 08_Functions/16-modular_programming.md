---
title: "Modular programming"
teaching: 15
exercises: 15
questions:
- "How can I create my own functions?"
objectives:
- "Learn about the advantages of modular programming"
- "Explain and identify the difference between function definition and function call."
- "Write a function that takes a small, fixed number of arguments and produces a single result."
keypoints:
- "Break programs down into functions to make them easier to understand."
- "Define a function using `def` with a name, parameters, and a block of code."
- "Defining a function does not run it."
- "Arguments in call are matched to parameters in definition."
- "Functions may return a result to their caller using `return`."
---

## Break programs down into functions to make them easier to understand.

*   Human beings can only keep a few items in working memory at a time.
*   Understand larger/more complicated ideas by understanding and combining pieces.
    *   Components in a machine.
    *   Lemmas when proving theorems.

*   Functions serve the same purpose in programs.
    *   *Encapsulate* complexity so that we can treat it as a single "thing".
*   Also enables *re-use*.
    *   Write one time, use many times.

## Define a function using `def` with a name, parameters, and a block of code.

*   Begin the definition of a new function with `def`.
*   Followed by the name of the function.
    *   Must obey the same rules as variable names.
*   Then *parameters* in parentheses.
    *   Empty parentheses if the function doesn't take any inputs.
    *   We will discuss this in detail in a moment.
*   Then a colon.
*   Then an indented block of code.

~~~
def print_greeting():
    """Print hello"""
    print('Hello!')
~~~
{: .python}

## Defining a function does not run it.

*   Defining a function does not run it.
    *   Like assigning a value to a variable.
*   Must call the function to execute the code it contains.

~~~
print_greeting()
~~~
{: .python}
~~~
Hello!
~~~
{: .output}


## Functions with arguments

* Functions are more useful than this if they take arguments.
* You can specify default values for these arguments
* Use the return function to provide output from a function (that isn't of type NoneType)

~~~
def increase_magnitude(x=5,i=2):
    """This increases the magnitude of a number by by 10 to the power of i"""
    x = x * (10 ** i)
    return x

increase_magnitude(50, 3)
~~~
{: .python}

~~~
50000
~~~
{: .output}


## Return statements

*   May occur anywhere in the function.
*   But functions are easier to understand if `return` occurs:
    *   At the start to handle special cases.
    *   At the very end, with a final result.

## Reading the head of a file

We wish to determine the appropriate files to work with for our analysis. We
could write a for loop and perform the appropriate operations within the body
of the loop. Let's write some basic functions for this instead. We'll start by working on
the console interactively on the console to figure out what it is that we want
to do. 

~~~
filepath = csvs[0]
with filepath.open('r') as f:
    output = []
    for line in range(2):
        output.append(f.readline())
output
~~~
{: .python}

~~~
['https://s3.amazonaws.com/fcp-indi/data/Projects/ABIDE_Initiative/Outputs/freesurfer/5.1/Pitt_0050002/mri/T1.mgz,50002,abide_initiative\n',
 'https://s3.amazonaws.com/fcp-indi/data/Projects/ABIDE_Initiative/Outputs/freesurfer/5.1/Pitt_0050003/mri/T1.mgz,50003,abide_initiative\n']
~~~
{: .output}

We'll now encapsulate that in a function. In addition we wish to:
*    specify the number of lines returned programmatically.
*    document what our function does.
*    explicitly define the dependency on pathlib before we define our function.
     This helps when we save our function to a file.

~~~
from pathlib import Path
def get_lines(filepath,nlines=2):
    """Return a list of length nlines, for as many lines of the file"""
    with filepath.open('r') as f:
        output = []
        for line in range(nlines):
            output.append(f.readline())
    return output
~~~
{: .python}

Let's save this function to a file so that we can maintain a module of functions that are useful for reuse:

~~~
%save my_funcs N # enter the last line number
~~~
{: .python}

~~~
The following commands were written to file `my_funcs.py`:
from pathlib import Path
def get_lines(filepath,nlines=2):
    """Return a list of length nlines, for as many lines of the file"""
    with filepath.open('r') as f:
        output = []
        for line in range(nlines):
            output.append(f.readline())
    return output
~~~
{: .output}

## Counting the number of lines in a file

Another useful operation we would like is to count the number of lines in the
file:

~~~
 def count_lines(filepath):
    """Count the number of lines in a text file"""
    if filepath.stat().st_size == 0:
        return 0
    else:
        with filepath.open('r') as f:
            for i, _ in enumerate(f):
                pass
        
        return i+1 # because enumerate starts counting at 0    
~~~
{: .python}


~~~
count_lines(file_path)
~~~
{: .python}

~~~
8060
~~~
{: .output}

~~~
%save my_funcs N # the line number of the function definition
~~~
{: .python}

~~~
The following commands were written to file `my_funcs.py`:
def count_lines(filepath):
    """Count the number of lines in a text file"""
    if filepath.stat().st_size == 0:
        return 0
    else:
        with filepath.open('r') as f:
            for i, _ in enumerate(f):
                pass
        
        return i+1 # because enumerate starts counting at 0
~~~
{: .output}

## Another layer of encapsulation

Finally we'll write a function that encapsulates the functionality of our previous functions:

~~~
def get_file_info(filepath,nlines=2):
    """"
    get_file_info(filepath[, nlines]) -> list

    Return a line count and the first few lines of  a file as a string"""
    
    output = filepath.name + ': Num lines: ' + str(count_lines(filepath)) + '\n\n'
    output += ''.join(get_lines(filepath, nlines))
    return output
~~~
{: .python}


~~~
%save -a my_funcs N # the number of the last command
~~~
{: .python}

~~~
The following commands were written to file `my_funcs.py`:
def get_file_info(filepath,nlines=2):
    """"
    get_file_info(filepath[, nlines]) -> list

    Return a line count and the first few lines of  a file as a string"""
    
    output = filepath.name + ': Num lines: ' + str(count_lines(filepath)) + '\n\n'
    output += ''.join(get_lines(filepath, nlines))
    return output
~~~
{: .output}

Now we can look through the csv files in metasearch to see if they contain
useful data for our analysis:

~~~
for f in csvs:
    print(get_file_info(f))
~~~
{: .python}

~~~
...


ngl_wyoming.csv: Num lines: 8267

d_first_name,d_mid_name,d_last_name,d_suffix,d_birth_date,d_death_date,section_id,row_num,site_num,cem_name,cem_addr_one,cem_addr_two,city,state,zip,cem_url,cem_phone,relationship,v_first_name,v_mid_name,v_last_name,v_suffix,branch,rank,war
"Paul","Frederick","Kratzer","","05/12/1924","04/28/2007","C","","764","OREGON TRAIL STATE VETERANS CEMETERY","80 VETERANS ROAD","BOX 669","EVANSVILLE","WY","82636","","307-235-6673","Veteran (Self)","Paul","Frederick","Kratzer","","US NAVY","GM2","WORLD WAR II",

nutrients.csv: Num lines: 7638

name,group,"protein (g)","calcium (g)","sodium (g)","fiber (g)","vitaminc (g)","potassium (g)","carbohydrate (g)","sugars (g)","fat (g)","water (g)",calories,"saturated (g)","monounsat (g)","polyunsat (g)"
"Beverage, instant breakfast powder, chocolate, not reconstituted","Dairy and Egg Products",19.9,0.285,0.385,0.4,0.0769,0.947,66.2,65.8,1.4,7.4,357,0.56,0.314,0.278
~~~
{: .output}

We probably don't want all this output permanently although it can be useful
now. For now let's save the list of csv files along with how many lines they
have:

~~~
for f in csvs:
    print(f, 0)
~~~
{: .python}


~~~
%save -a metasearch_analysis.py N # the line number of the above command
~~~
{: .python}

~~~
The following commands were written to file `metasearch_analysis.py`:
for f in csvs:
    print(f, 0)
~~~
{: .output}

> ## Running scripts in debugger mode
> 
> Now is a good time to try using the ipdb debugger to see how one can observe
> what is happening as the flow of execution through the file occurs..
{: .callout}


> ## Order of Operations
> 
> The example above:
> 
> ~~~
> result = print_date(1871, 3, 19)
> print('result of call is:', result)
> ~~~
> {: .python}
> 
> printed:
> ~~~
> 1871/3/19
> result of call is: None
> ~~~
> {: .output}
> 
> Explain why the two lines of output appeared in the order they did.
{: .challenge}


> ## Find the python scripts
> 
> Write a function that calls at least one of the functions developed in the
> lesson. When given a directory as input the function should return a list
> with as many elements as there are python files (.py) in the directory. Each
> element should contain the name and the number of lines for a specific python
> file (.py).
> 
> 
>> ## Solution
>> 
>> ~~~
>> def get_py_files(dir_path,nlines=0):
>>    """Returns a list of the python files in the dir_path
>>    dir_path should be a Path object from pathlib with
>>    a name of a directory""""
>>    
>>    py_files = dir_path.glob('**/*.py')
>>    output = []
>>    for f in py_files:
>>        output.append(get_file_info(f,nlines))
>>     return output
>>     
>> print(*get_py_files(metasearch_dir))
>> ~~~
>> {: .python}
>> 
>> ~~~
>> data_not_in_repo/metasearch/crawler/brain-development/extract.py:
>> Num lines: 12
>> 
>> data_not_in_repo/metasearch/docs/data/merge_csv.py:
>> Num lines: 25
>> ~~~
>> {: .output}
>> 
> {: .solution}
{: .challenge}