# Week 3


## Printing Text (Chapter 2 of Python for Biologists)

* You should
be typing examples into a text file.
* Save the text file.
* Execute the text
file on the command line using python [name of your text file].
* DO NOT RUN
THIS DIRECTLY IN PYTHON (If you see >>> on your terminal you are in python)
##
Homework

1. Use this sequence as your input DNA (**COPY/PASTE THIS DIRECTLY
INTO YOUR FILE**)
  * ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
2.
Write a program that will print out the AT content (percentage) of this sequence
3. Use typical mathematical functions (+, - , / , \*)
4. Your script should be
named as follows your_name.ATcount.HW2.py
5. Submit your final script to the
proper drop it to me page.
6. If you are using python2 don't forget to add this
line to the top of your script:

## Homework review

Your tasks were to:
* Count
the number of A's
* Count the number of T's
* Determine the length of the
sequence
* Divide the total number of A's and T's vs the length of the sequence
* Report the percentage of the AT content

## Reading and Writing Files (Chapter
3 of Python for Biologists)

* You should be typing examples into a text file.
*
Save
the text file.
* Execute the text file on the command line using python
[name of
your text file].
* DO NOT RUN THIS DIRECTLY IN PYTHON (If you see >>>
on your
terminal you are in python)

## Homework

* Writing a FASTA file
* FASTA
file
format is a commonly-used DNA and protein sequence file format. A single
sequence in FASTA format looks like this:

```{.python .input .pyhon}
>sequence_name
ACTAGCTAGCTAGCATCG
```

* Write a program that will create a MULTI-FASTA file for the following three
sequences – make sure that all sequences are in upper case and only contain the
bases A, T, G and C.

```{.python .input}
SEQUENCE HEADER     DNA SEQUENCE
ABC123              ATCGTACGATCGATCGATCGCTAGACGTATCG
DEF456              actgatcgacgatcgatcgatcacgact
HIJ789              ACTGAC-ACTGT--ACTGTA----CATGTG
```
