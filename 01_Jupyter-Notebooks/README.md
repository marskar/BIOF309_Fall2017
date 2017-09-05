# BIOF309 Fall 2017 - Week 1 (Sept 11 2017)

## Plan for today

* [Intro survey](https://goo.gl/forms/hKJGAyI0JfjKLgq73)
* Course overview
* An introduction to programming
* Why Python?
* What can you do with Python?
* Troubleshooting software installation
* Introduction to Jupyter Notebook
* Ben's "What I wish I knew years ago"

## Why Python
- Python is a widely-used, general-purpose language.
- Python is easy to write/read/run etc.
- Python has an awesome community and is under constant development.
- Python has a great library ecosystem with relatively little redundancy.
- Python was voted the top language of 2017 by [IEEE Spectrum](https://spectrum.ieee.org/computing/software/the-2017-top-programming-languages).
- Python is popular in data science and machine learning. In fact, Python is more popular than the R programming language, according to [KDnuggets](http://www.kdnuggets.com/2017/08/python-overtakes-r-leader-analytics-data-science.html) and [DataScienceCentral](http://www.datasciencecentral.com/profiles/blogs/python-overtakes-r-for-data-science-and-machine-learning).

## What can you do with Python?
https://www.youtube.com/watch?v=-67hh86N42Q

### Examples:
* [Automate the boring stuff](https://automatetheboringstuff.com/)
* Bioinformatics pipelines
* Scrape data from a webpage
* Run machine learning algorithms on data
* Make games
* Build websites
* Analyze Excel data
* Analyze image data
* Program robots or drones

### Other examples:
* https://www.quora.com/What-can-I-do-build-with-Python

* https://wiki.python.org/moin/Applications

* https://www.python.org/about/apps/

* https://learnpythonthehardway.org/book/ex0.html

* http://pythonforbiologists.com/index.php/introduction-to-python-for-biologists/python-for-biologists-introduction/

### Notebook list

#### Intro2Jupyter

*  01-01-00_Installation.ipynb
*  01-01-01_Learning-objectives.ipynb
*  01-01-02_Jupyter-Intro-Background.ipynb
*  01-01-03_Introduction-to-Jupyter-Notebooks.ipynb
*  01-01-04_What-is-the-Jupyter-Notebook.ipynb
*  01-01-05_Running-Code.ipynb
*  01-01-06_Notebook-Basics.ipynb
*  01-01-07_Getting-started-with-jupyter-notebooks.ipynb
*  01-01-08_Navigating-the-notebook.ipynb
*  01-01-09_Working-With-Markdown-Cells.ipynb
*  01-01-10_Beyond-Plain-Python.ipynb
*  01-01-11_IPython-Magic.ipynb
*  01-01-12_Cell-Magics.ipynb
*  01-01-13_Capturing-Output.ipynb
*  01-01-14_Resources.ipynb
*  01-01-15_Take-Home-Messages.ipynb

#### Intro2Python

*  01-02-00_Hello-World.ipynb
*  01-02-01_Scientific-Computing-with-Python.ipynb
*  01-02-02_Introduction-to-Python-Programming.ipynb
*  01-02-03_Intro2Python.ipynb
*  01-02-04_Intro2Python2.ipynb
*  01-02-05_Introduction-to-Programming-with-python.ipynb
*  01-02-06_Intro-to-Python-Programming.ipynb
*  01-02-07_Built-in-functions.ipynb
*  01-02-08_Intro-to-reproducible-research.ipynb
*  01-02-09_More-ways-to-Run-Python-Code.ipynb
*  01-02-10_resources4python.ipynb

#### Variables and Types

*  01-03-01_variables.ipynb
*  01-03-02_variables.ipyn
*  01-03-03_types-conversion.ipynb
*  01-03-04_var-string-num.ipynb
*  01-03-05_variable-assignment.ipynb

## Ben's "What I wish I knew years ago"

Computer time is cheap, humans are expensive, their time is valuable. Given a task, they need to learn to minimize the time spent writing the code. Or given a stretch of time, they need to know how to maximize output. So they need to learn a few best practices to get the most out of their time (these are just some things I’ve learned that I wish someone told me early on):

* Modularize code, good coding frame work has functions which are agnostic to input
* Write pseudo-code
* Don’t get too cute with it, just solve the problem
* Use a style guide. Even if it’s your own made up style guide, just be consistent. Keep a format that makes bugs easy to spot.
* Minimize time spent debugging. That means writing code in chunks, where you get total confidence in one chunk before moving on to the next.
* Comment your code; make comments follow some consistent formatting.
* Error rate is ~proportional to the number of lines of code you write. Concise code with helpful comments minimizes error rate.
* Log your bugs, and don’t repeat them. Every time you spend time debugging, write down the issue once you solve it, and make a checklist for yourself like a pilot before takeoff. If something doesn’t work next time, you have a list of most probable candidates to check first.
* People type at about the same rate, codes usually run at about the same speed, people often get the right idea at about the same speed. These things often vary on a time scales of mere minutes. Yet, people vary in how fast they implement successful code on a time scales of hours, days, or even weeks. This is because debugging is your rate limiting factor. Get good at debugging, minimize time spent doing I. Solve your problem today, not two weeks from now.
* You’re going to have problems that you try and try to solve for days and make no progress, and then something will budge. Given a stretch of time to work on something, this means your progress is binary: you made headway, or you didn’t. These best practices are a starting point for you, but you (the student) need to figure out for yourself how maximize the frequency of making things budge.

## Reading

* Chapters 01-06 in [Whirlwind Tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
* Chapters 01.01-01.04 in [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks)

## Activity

* [DataCamp - Python Basics](https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics)

## Homework

Find a cool Jupyter notebook to share with the class! Use the resources notebook (01-01-14_Resources.ipynb), [nbviewer](https://nbviewer.jupyter.org/), Google, or any other means to find a notebook that interests you. You will have 60 seconds to discuss the notebook and tell everyone why you find it interesting. You can run the notebook in presentation mode or just scroll, but do **NOT** use powerpoint. Please add a link to the notebook you selected to the "cool-notebooks" channel on our [class Slack team](https://biof309.slack.com).

## Next week

Next week, we will present our chosen notebooks , learn to use UNIX commands, and talk about strings. We will then build on our UNIX skills in week 3, when we cover git. Also in week 3, we will create [GitHub](https://github.com) repositories for the homework assignments and final projects.
