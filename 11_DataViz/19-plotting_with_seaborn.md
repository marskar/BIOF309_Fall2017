---
title: "Plotting with Seaborn"
teaching: 15+
exercises: 15+
start: true
---

## Imports 
~~~
# Some library functionality we shall use.
import seaborn as sns
import pandas  as pd
import numpy   as np
import matplotlib.pyplot as plt
~~~
{: .python}

~~~
# see sns.set() for selecting a few basic parameters: style,
# colorpalette, font family, etc.
sns.set()
~~~
{: .python}

~~~
# load the data
df = pd.read_csv('https://raw.githubusercontent.com/OpenNeuroLab/metasearch/master/docs/data/phenotype_mri.csv')
~~~
{: .python}

## Quantitative and categorical vars via dtypes 

~~~
# get types of data: data frame method: ``select_dtypes``

# To select all *numeric* types use the numpy dtype ``numpy.number``
var_qnt = list(df.select_dtypes(include=[np.number]))
~~~
{: .python}

~~~
# To get some quick summary info on each quant variable across groups,
# use the following (returns a DataFrame):
df.describe()
~~~
{: .python}

~~~
# To select Pandas categorical dtypes, use 'category'
var_cat = list(df.select_dtypes(include=['category']))
~~~
{: .python}

~~~
# However, in this case, we haven't made any specific 'category'
# variables. See the types we have for each col (returns a Series):
df.dtypes
~~~
{: .python}

~~~
# So there are type "object" for non-quant ones, which we can select
# as non-numerical
var_cat = list(df.select_dtypes(exclude=[np.number]))
# or could include 'object' type:
# var_cat = list(df.select_dtypes(include=['object']))
~~~
{: .python}

For more about categorical variables, see [this pandas
page](http://pandas.pydata.org/pandas-docs/stable/categorical.html).


## dealing with missing values (NaNs) 

~~~
# some data will be missing, possibly.  Too see how many non-Nans are
# there for each variable, use (returns a Series):
df.count()
~~~
{: .python}

~~~
# If one has missing data in columns, some seaborn plotting functions
# can remove them; some have a ``dropna=True`` ability to remove NaNs
# from a column.  For many that *don't*, we can make a mini data
# frame.  Note this function has two outputs: a (potentially) smaller
# data frame, and the reduction in the number of rows.  There could be
# much better ways of writing a related function, this is just a
# quick example.
def NoNoNaNette( df, cols=[] ):

    if not(cols):
        df2 = df[:].dropna()
    else:
        df2 = df[cols].dropna()

    shin  = df.shape
    shout = df2.shape

    print("Input  shape:", shin)
    print("Output shape:", shout)

    # might be useful to return how many variables were left *out*
    return df2, shin[0] - shout[0]
~~~
{: .python}

## some plotting 

~~~
# -------------------  1a) Basic scatterplot -------------------------
# quant vs quant, plots a confidence interval of fit by default.  This
# function does *not* deal well with NaNs, so use the remover:
df3, diff    = NoNoNaNette( df, ['age', 'full_iq'])
my_lmplot    = sns.lmplot( 'age', 'full_iq', data=df3 )
plt.show()
~~~
{: .python}

~~~
# -------------------  1b) Basic scatterplot, extra cat ----------------

# Can also divvy up with a category; here and below, generally given
# as 'hue' because it adds a color variation to the plot
df3, diff    = NoNoNaNette( df, ['age', 'full_iq', 'diagnosis'] )
my_lmplot    = sns.lmplot( 'age', 'full_iq', data=df3, hue='diagnosis' )
plt.show()
~~~
{: .python}

~~~
# -------------------  1c) Basic scatterplot, extra opts ----------------

df3, diff    = NoNoNaNette( df, ['age', 'full_iq', 'diagnosis'] )
my_lmplot    = sns.lmplot( 'age', 'full_iq', data=df3, hue='diagnosis' )
sns.plt.suptitle('Important data')   # useful plot title
sns.plt.xlabel('age'+' (years)')     # change labels, e.g., with units
#plt.tight_layout()  # see about this...
plt.show()
~~~
{: .python}

~~~
# ------------------ 2a) all quantitative pairs -------------------

# Plot all quant pairs vs each other, and histograms along diagonal;
# leave off first 'quant' var because it is just subj ID integer.

# This plotting function *does* have a ``dropna=True`` in it.
# However, the diagonal-plotter STILL complains about NaNs, so we can
# either use the above NoNoNaNette(), or set the diagonal to be the
# "kernel density estimate" instead of the bog standard histogram
# along the diagonals.  NB: in this case, the NoNoNaNette-d version
# would produce something different, because it gets rid of *any* row
# with a nonzero, then plots the pairs; the other way, two variables
# are selected and *then* the NaNy-rows between that pair are
# deleted-- that can generally have different behavior!

my_pairplot = sns.pairplot( df, diag_kind='kde' )
plt.show()
~~~
{: .python}

## Sidenote:  plotting_context() 

~~~
# What are default sundry values for various plot settings?  Check 'em
# out: 
sns.plotting_context()
~~~
{: .python}

~~~
# these can be changed in one fell swoop with some batched presets:
sns.set_context("talk")
# also have: "notebook", "paper" and "poster"
~~~
{: .python}

~~~
# ... and check the new normal:
sns.plotting_context()
~~~
{: .python}

~~~
# To change some of these, one can do, for example:
sns.set_context( rc={'lines.markeredgewidth': 0.0,
                     'xtick.labelsize': 8.0})
my_pairplot = sns.pairplot( df, diag_kind='kde')
plt.show()
~~~
{: .python}


## Back to plotting 

~~~
# -------------- 2b) all quantitative pairs, no NaNs ----------------

# might be fun:
sns.set_context("poster")
df4, diff = NoNoNaNette(df, var_qnt[1:]) 
my_pairplot = sns.pairplot( df4 )
#plt.show()

# Either plot or save fig (or both); one can control, for example, the
# DPI, etc.
fname = "plot.png" 
plt.savefig(fname, dpi=300)
#plt.show()
~~~
{: .python}

Note: see [here](http://seaborn.pydata.org/tutorial/aesthetics.html):
  for more on aesthetics description and settings, and
  [here](http://seaborn.pydata.org/tutorial/color_palettes.html#palette-tutorial)
  for some examples of color palettes.

## Sidenote: displaying correlation values 

Unfortunately, there isn't a simple option to directly show the
correlation values for the scatterplots, even though that might be
nice to know when looking at things.  One reason for this could be
that one can do a 'believability' test before, just looking for strong
correlations by eye rather than become enamored with high values that
might arise due to quirks-- fair deuce.  Some online comments about
this say essentially, 'Well, plotting should be for viewing and
calculating numbers should be separate'-- advocating this kind of
purposeful limitation makes no sense to me here.

Anyways, this is all to say that one has to 'hack' a bit to add
correlation values to the plots.  And by 'hack', I mean: thank you,
[Stackoverflow!](http://stackoverflow.com/questions/30942577/seaborn-correlation-coefficient-on-pairgrid).

~~~
# ------------- 2c) all quantitative pairs, corr values --------------

# trivially modified from above (-> names changed to protect the
# innocent):
import scipy.stats as spst
def corrfunc(x, y, **kws):
    r, _ = spst.pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.1, .9), xycoords=ax.transAxes)

my_pairplot = sns.pairplot( df4,diag_kind='kde' )
# this just puts the corr values into the LHT
my_pairplot.map_lower(corrfunc)
plt.show()
~~~
{: .python}





