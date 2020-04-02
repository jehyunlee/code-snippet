#!/usr/bin/env python
# coding: utf-8
# ver. 2020.04.01.
# Jehyun Lee (jehyun.lee@gmail.com)

"""
Pegaplot: A Visulization module wrapping Matplotlib and Seaborn

Default Settings
----------------
STYLE      : style for plots.
             plt.style.use(STYLE) is called.
             default = "seaborn-whitegrid" of matplotlib, equivalent to "whitegrid" of seaborn
CONTEXT    : set of font sizes.
             default = "talk" of seaborn
COLOR      : plot colors.             
             default = "green"
PALETTE    : sequence of plot colors.
             sns.set_palette(PALETTE) is called.
             default = "bright" of seaborn.

MATHFONT   : font for mathmatic expression, ex. MathJax.
             default = "cm"

KRFONT     : font for Korean characters
             default = "NanumGothic"

NEGSUPFONT : alternative font for superscription, due to the missing U+2212 in Korean fonts.
             default = "Liberation Sans"

DPI        : quality of images on screen.
             default = 72
PRINTDPI   : quality of image files.
             default = 200
"""

### Import libraries

import os, copy, sys, io, json
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

from krfont import add_KRFONT, set_KRFONT
from fn import chktype

get_ipython().run_line_magic("matplotlib", "inline")


### Default settings

with open('settings.json', 'r') as f:
    settings = json.load(f)

params = settings['params']    
params_def = copy.deepcopy(params)


### Korean Font Setting

KRFONT = set_KRFONT(params['krfont'])    # set Korean font from installed fonts
add_KRFONT(KRFONT)                       # add Korean font to matplotlib


### Plot Style Setting

def set(**kwargs):
    global params
    
    # 1. parameter settings 
    flag_any = 0
    
    if len(kwargs.keys()) == 0:    # recover defaults
        print('# Setting Default Values:')
        params = copy.deepcopy(params_def)
        for key, value in params.items():
            print(f'  {key:10s} = {value}')
        
    else:    # edit parameter as required
        for key, value in kwargs.items():
            if key in params.keys():
                flag_any += 1
                params[key] = value
                print(f'params[{key}]={value}')
            if key == 'palette':
                with sns.axes_style("darkgrid"):
                    sns.palplot(sns.color_palette(params['palette'])) # show palette
        
        if flag_any == 0:
            sys.exit(f'NotValidKey: "{key}" is not a member of param')
    
    # 2. apply settings
    plt.style.use(params['style'])        # style
    sns.set_palette(params['palette'])    # palette
    sns.set_context(params['context'])    # context
    plt.rcParams['mathtext.fontset'] = params['mathfont']  # math font
    plt.rcParams['figure.figsize'] = params['figsize']     # figure size
    plt.rcParams['figure.dpi'] = params['showdpi']  # image dpi on notebook
    plt.rcParams['savefig.dpi'] = params['filedpi'] # image dpi on savefile
    
    # 3. setting for Korean font
    add_KRFONT(KRFONT)

set()    


### Font Settings

fonts = settings['fonts']

# fontdicts
font_label = fonts['label']     # xlabel and ylabel
font_title = fonts['title']     # title
font_negsup = fonts['negsub']   # negative(-) on superscript 
font_math = fonts['math']       # math

# fontproperties:suptitle
font_suptitle = mpl.font_manager.FontProperties()
font_suptitle_ = fonts['suptitle']
font_suptitle.set_family(font_suptitle_['family'])
font_suptitle.set_size(font_suptitle_['size'])
font_suptitle.set_weight(font_suptitle_['weight'])


### Plot Settings
def subplots(xlabel=None, 
             ylabel=None, 
             title=None, 
             suptitle=None,
             ncols=1, nrows=1, 
             figsize=None, 
             sharex=False, 
             sharey=False,
             **kwargs):
    
    if figsize==None:
        figsize = params['figsize']
    
    if ncols * nrows > 1:
        figsize = [params['figsize'][0]*ncols, 
                   params['figsize'][1]*nrows]
        
        fig, ax = plt.subplots(ncols=ncols, nrows=nrows, figsize=figsize,
                              sharex=sharex, sharey=sharey)
        axes = ax.ravel() 
        
        # type check: xlabel and ylabel
        for i in range(len(axes)):
            if sharex==True and chktype(xlabel, 'str'):
                if i >= len(axes)-ncols:
                    axes[i].set_xlabel(xlabel, fontdict=font_label, labelpad=12)
            elif sharex==True and chktype(xlabel, 'list'):
                if i >= len(axes)-ncols:
                    axes[i].set_xlabel(xlabel[0], fontdict=font_label, labelpad=12)
            elif sharex==False and chktype(xlabel, 'list') and len(xlabel)==len(axes):
                axes[i].set_xlabel(xlabel[i], fontdict=font_label, labelpad=12)
            else:
                sys.exit(f'NotValidTypeOrLength: type={type(xlabel)}, xlabel={xlabel}')

            if sharey==True and chktype(ylabel, 'str'):
                if i % ncols == 0:
                    axes[i].set_ylabel(ylabel, fontdict=font_label, labelpad=12)
            elif sharey==True and chktype(ylabel, 'list'):
                if i % ncols == 0:
                    axes[i].set_ylabel(ylabel[0], fontdict=font_label, labelpad=12)
            elif sharey==False and chktype(ylabel, 'list') and len(ylabel)==len(axes):
                axes[i].set_ylabel(ylabel[i], fontdict=font_label, labelpad=12)
            else:
                sys.exit(f'NotValidTypeOrLength: type={type(ylabel)}, ylabel={ylabel}')

    else:
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlabel(xlabel, fontdict=font_label, labelpad=12)
        ax.set_ylabel(ylabel, fontdict=font_label, labelpad=12)
        ax.set_title(title, fontdict=font_title, pad=12)
    
    fig.suptitle(suptitle, y=1.05, fontproperties=font_suptitle)
    
    return fig, ax