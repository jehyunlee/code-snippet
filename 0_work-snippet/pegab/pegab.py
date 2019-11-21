#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, copy
from IPython.display import Markdown, display

sns.set(style='whitegrid')
sns.set(font_scale=1)

#>>>>>> 1. Korean Font Setting
import platform
system = platform.system()

# -*- coding: UTF-8 -*-
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl  # 기본 설정 만지는 용도
import matplotlib.pyplot as plt  # 그래프 그리는 용도
import matplotlib.font_manager as fm  # 폰트 관련 용도
print ('버전: ', mpl.__version__)
print ('설치 위치: ', mpl.__file__)
print ('설정 위치: ', mpl.get_configdir())
print ('캐시 위치: ', mpl.get_cachedir())
print ('설정 파일 위치: ', mpl.matplotlib_fname())
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

if system == 'Windows':
    datapath = os.getcwd() + '\\'
    imagepath = datapath + 'images\\'

    # ttf 폰트 전체개수
    font_list[:10]

    f = [f.name for f in fm.fontManager.ttflist]
    f[:10]

    [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

    path = 'C:\\Windows\\Fonts\\NanumBarunGothic.ttf'
    font_name = fm.FontProperties(fname=path, size=50).get_name()

    print(font_name)
    plt.rc('font', family=font_name)
    print("# matplotlib 한글 사용 가능")

elif system == 'Linux':
    datapath = os.getcwd() + '//'
    imagepath = datapath + 'images//'
  
#     !apt-get update -qq
#     !apt-get install fonts-nanum* -qq

    path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # 설치된 나눔글꼴중 원하는 녀석의 전체 경로를 가져오자
    font_name = fm.FontProperties(fname=path, size=10).get_name()

    print(font_name)
    plt.rc('font', family=font_name)

    fm._rebuild()
    mpl.rcParams['axes.unicode_minus'] = False
    print("# matplotlib 한글 사용 가능")

else:
    print('# Sorry, my code has compatibility with Windows and Linux only.')
    exit(0)

#<<<<<< 1. Korean Font Setting

#>>>>>> 2.Figure Style Setting
style = 'whitegrid'
palette = 'muted'
context = 'talk'

sns.set_style(style)
sns.palplot(sns.color_palette(palette))
sns.set_context(context)
plt.rc('font', family=font_name)
fm._rebuild()
mpl.rcParams['axes.unicode_minus'] = False
print("# Seaborn Figure Style : {}, {}, {}".format(style, palette, context))

#<<<<<< 2.Figure Style Setting

#>>>>>> 3. Nice Representation of dataframe in markdown

def df2md(df, maxlen=20, indexname='(index)'):
    _df = copy.deepcopy(df)
    
    for col in _df.columns:
        _df[col] = _df[col].astype('str')
        if (_df[col].str.len()> maxlen).any() :
            _df[col].loc[_df[col].str.len() > maxlen] = _df[col].str.slice(stop=maxlen) + ' ...'

    if indexname in _df.columns:
        while(indexname in _df.columns):
            indexname='_'+indexname
        warnings.warn("The index name shouldn't overlap other column names. {} will be used instead.\nConsider changing the indexname parameter.".format(indexname), SyntaxWarning)
    _df.insert(0, indexname, df.index)
    
    fmt = ['---' for i in range(len(_df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=_df.columns)
    df_formatted = pd.concat([df_fmt, _df])
    display(Markdown(df_formatted.to_csv(sep='|', index=False)))
    _df.drop(columns=indexname, axis=1, inplace=True)

print("# Function : {} is available!".format('df2md()'))

#<<<<<< 3. Nice Representation of dataframe in markdown
    

