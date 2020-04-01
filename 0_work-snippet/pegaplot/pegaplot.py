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

TICKFONT   : alternative font for superscription, due to the missing U+2212 in Korean fonts.
             default = "Liberation Sans"

DPI        : quality of images on screen.
             default = 72
PRINTDPI   : quality of image files.
             default = 200
"""
### Default settings

COLOR = "green"
STYLE = "seaborn-whitegrid"
PALETTE = "bright"
CONTEXT = "talk"
MATHFONT = "cm"
TICKFONT = "Liberation Sans"
KRFONT = "NanumGothic"
DPI = 72
PRINTDPI = 200


### Import libraries

import os, copy, sys, io
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

get_ipython().run_line_magic("matplotlib", "inline")


### Default settings

params = {
    "color" : COLOR,
    "style" : STYLE, 
    "palette" : PALETTE,
    "context" : CONTEXT,
    "mathfont" : MATHFONT,
    "tickfont" : TICKFONT,
    "krfont" : KRFONT,
    "showdpi" : DPI,
    "filedpi" : PRINTDPI,
}
params_def = copy.deepcopy(params)

### >>> Plot Style Setting

def set(*args, **kwargs):
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
            if key == 'color':
                sns.palplot(sns.color_palette(params['palette'])) # show palette
        
        if flag_any == 0:
            sys.exit(f'NotValidKey: "{key}" is not a member of param')
    
    # 2. apply settings
    plt.style.use(params['style'])        # style
    sns.set_palette(params['palette'])    # palette
    sns.set_context(params['context'])    # context
    plt.rcParams['figure.dpi'] = params['showdpi']  # image dpi on notebook
    plt.rcParams['savefig.dpi'] = params['filedpi'] # image dpi on savefile
    plt.rcParams['mathtext.fontset'] = params['mathfont']  # math font
    
    # 3. setting for Korean font
    mpl.rcParams['font.sans-serif'] = [KRFONT] + mpl.rcParams['font.sans-serif']
    mpl.rcParams['font.serif'] = [KRFONT] + mpl.rcParams['font.serif']
    mpl.rcParams['font.cursive'] = [KRFONT] + mpl.rcParams['font.cursive']
    mpl.rcParams['font.fantasy'] = [KRFONT] + mpl.rcParams['font.fantasy']
    mpl.rcParams['font.monospace'] = [KRFONT] + mpl.rcParams['font.monospace']


set()    

### >>> Korean Font Setting

import matplotlib.font_manager as fm
import platform

system = platform.system()

if system == 'Windows':
    datapath = os.getcwd() + '\\'
    imagepath = datapath + 'images\\'

    # ttf 폰트 전체개수
    font_list[:10]

    f = [f.name for f in fm.fontManager.ttflist]
    f[:10]

    [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

    path = 'C:\\Windows\\Fonts\\NanumBarunGothic.ttf'
    KRFONT = fm.FontProperties(fname=path, size=50).get_name()

    plt.rc('font', family=KRFONT)
    print(f"# matplotlib 한글 사용 가능: {KRFONT}")

elif system == 'Linux':
    datapath = os.getcwd() + '//'
    imagepath = datapath + 'images//'

#     !apt-get update -qq
#     !apt-get install fonts-nanum* -qq

    path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  
    KRFONT = fm.FontProperties(fname=path, size=10).get_name()

    mpl.rcParams['font.sans-serif'] = [KRFONT] + mpl.rcParams['font.sans-serif']

    fm._rebuild()
    mpl.rcParams['axes.unicode_minus'] = False
    print(f"# matplotlib 한글 사용 가능: {KRFONT}")

else:
    sys.exit('ERROR: Sorry, my code has compatibility with Windows and Linux only.')

### <<< Korean Font Setting

### >>> Font Settings

# suptitle
# font_suptitle = {
#     'family': 'sans-serif',
#     'size': 22,
#     'color': 'royalblue',
#     'weight': 'bold',
#     'verticalalignment': 'baseline',
#     'horizontalalignment': 'center'
# }

font_suptitle = mpl.font_manager.FontProperties()
font_suptitle.set_family('serif') # 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'
font_suptitle.set_size(22)
font_suptitle.set_weight('bold')

# title
font_title = {
    'family': 'sans-serif',
    'size': 20,
    'color': 'cornflowerblue',
    'weight': 'bold',
    'verticalalignment': 'baseline',
    'horizontalalignment': 'center'
}

# xlabel and ylabel
font_label = {
    'family': 'sans-serif',
    'color': 'gray',
    'weight': 'bold',
    'horizontalalignment': 'center'
}

# ticklabel
font_ticklabel = {
    'fontname': params['tickfont'],
    'horizontalalignment': 'center'
}

# math
font_math = {
    'verticalalignment': 'bottom',
    'horizontalalignment': 'center'
}


### <<< Font Settings