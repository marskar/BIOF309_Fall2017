#Enable opening markdown (.md) files as Jupyter Notebooks using notedown!
#You must have notedown installed for this to work: https://github.com/aaren/notedown

c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'


#Automatically save a html, script, md file, and/or others whenever you save a jupyter notebook
#You must have nbconvert for this to work. Luckily, nbconvert is part of Jupyter
#and comes with the Anaconda Distribution (https://www.anaconda.com/download/) of Python.
#https://nbconvert.readthedocs.io/en/latest/install.html#installing-nbconvert)

c = get_config()
import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    #comment out  your choice of the options below
    check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
    check_call(['jupyter', 'nbconvert', '--to', 'markdown', fname], cwd=d)
    #check_call(['jupyter', 'nbconvert', '--to', 'slides', fname], cwd=d)
    #use the line above only if you want to generate a slideshow presentation
    #check_call(['jupyter', 'nbconvert', '--to', 'pdf', fname], cwd=d)
    #check_call(['jupyter', 'nbconvert', '--to', 'latex', fname], cwd=d)
    #the two lines above each produce an error unless you have LaTeX installed
    #https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex

c.FileContentsManager.post_save_hook = post_save
