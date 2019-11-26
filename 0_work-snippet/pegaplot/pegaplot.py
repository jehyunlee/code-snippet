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

# Nice representation of dataframe in markdown
import pandas as pd
import copy
from IPython.display import Markdown, display
import warnings
warnings.filterwarnings(action='ignore')

def df2md(df, maxlen=20, indexname='(index)'):
    '''
    Nice Representation of Pandas DataFrame and Series in Markdown Format.
    
    Parameters
    ----------------
    df : pandas.DataFrame or pandas.Series
    maxlen : (int) maximum length of data at markdown output.
             data exceeding maxlen will be presented as ' ...'
    indexname : (str) name of index, to be displayed on markdown output.
                To avoid overriding column name, if conflicts, the '_' will be added in front of the indexname.
    '''
    
    _df = copy.deepcopy(df)
    
    if 'Series' in str(type(df)):
      _idx = _df.index
      _df = pd.DataFrame(data=_df, index=_idx)
      
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

print("# Available Functions : {}".format('df2md(), bar(), pie(), donut(), dist(), dists()'))

#<<<<<< 3. Nice Representation of dataframe in markdown

#>>>>>> 4. Categorical Data Distribution

# Retrieving Variable Name
def namestr(x, Vars=vars()):
    for k in Vars:
        if type(x) == type(Vars[k]):
            if x is Vars[k]:
                return k
    return None
  
# Check type of variable
def chktype(var, typename):
    if typename in str(type(var)):
        return True
    else:
        return False

      
# bar plot      
def bar(df, xcols, ycol, labels=None, gap=10):
    """
    Categorical Data Distribution as Barplot
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    ycol : (str) target column name 
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    gap : (float) distance between bar top and annotation
    """

    # Plotting function
    def _plot(xcol):
        grouped = pd.DataFrame(df.groupby(xcol).count().reset_index())

        plt.figure(figsize=(6, 6))
        ax = sns.barplot(x=xcol, y=ycol, data=grouped)
        ax.set(title=labels[xcol])
        ax.set(xlabel=None)
        ax.set(ylabel=None)
        for i in ax.patches:
            ax.text(
                i.get_x() + i.get_width() / 2,
                i.get_height() + gap,
                str(int(i.get_height())),
                ha="center",
                fontsize=16
            )

        plt.tight_layout()
        df_name = namestr(df)#, locals())
        plt.savefig("./images/cat_bar_{}_{}.png".format(df_name, labels[xcol]))

    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot(xcol)
            else:
                print(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
                exit(1)
    elif chktype(df[xcols], "Series"):
        _plot(xcols)
    else:
        print(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )
        exit(1)
        
        
def calc_abs(pct, data_array: list):
    absolute = int(pct / 100.0 * np.sum(data_array))
    return "{:.1f}%\n({:d})".format(pct, absolute)

  
# Pie Chart  
def pie(
    df,
    xcols,
    ycol,
    labels=None,
    cmap="tab20",
    startangle=90,
    annotate=True,
    legend=True,
):
    """
    Categorical Data Distribution as Pieplot
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    ycol : (str) target column name 
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    cmap : (Matplotlib colormap) default is 'tab20'.
    startangle : (float) starting angle of wedges in degrees.
    annotate : (Boolean) Adding informations on graph.
    legend : (Boolean) Adding legend box on rightside of graph
    """

    def _plot(xcol):
        grouped = pd.DataFrame(df.groupby(xcol).count().reset_index())
        fig, ax = plt.subplots(figsize=(10, 6))

        # Categorical Data to plot
        colormap = plt.get_cmap(cmap)
        cats = grouped[xcol].values  # Categories, to be one-hot encoded
        ncat = grouped[xcol].shape[0]  # Number of Categories
        nums = grouped[ycol].values  # Number of data for each categories

        # masking pie charts with given colors
        colors = [colormap(i) for i in np.linspace(0, 1, ncat)]
        wedges, texts, autotexts = ax.pie(
            nums,
            colors=colors,
            autopct=lambda pct: calc_abs(pct, nums) if annotate == True else None,
            startangle=startangle,
        )
        if legend == True:
            ax.legend(
                wedges, cats, loc="center right"
            )  # , bbox_to_anchor=(0.8, 0, 0.5, 1))
        ax.axis("equal")
        df_name = namestr(df)
        ax.set_title(labels[xcol])
        plt.setp(autotexts, size=16)
        plt.savefig("./images/cat_pie_{}_{}.png".format(df_name, labels[xcol]))

    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot(xcol)
            else:
                print(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
                exit(1)
    elif chktype(df[xcols], "Series"):
        _plot(xcols)
    else:
        print(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )
        exit(1)
        

# Donut Chart        
def donut(
    df,
    xcols,
    ycol,
    labels=None,
    cmap="tab20",
    startangle=-40,
    annotate=True,
    legend=False,
):
    """
    Categorical Data Distribution as Donutplot
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    ycol : (str) target column name 
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    cmap : (Matplotlib colormap) default is 'tab20'.
    startangle : (float) starting angle of wedges in degrees.
    annotate : (Boolean) Adding informations on graph.
    legend : (Boolean) Adding legend box on rightside of graph
    """

    def _plot(xcol):
        # Categorical Data to plot
        grouped = pd.DataFrame(df.groupby(xcol).count().reset_index())
        colormap = plt.get_cmap(cmap)
        cats = grouped[xcol].values  # Categories, to be one-hot encoded
        ncat = grouped[xcol].shape[0]  # Number of Categories
        nums = grouped[ycol].values  # Number of data for each categories

        # preparation of texts to be marked on graph
        text_list = []
        count_sum = df[xcol].value_counts().sum()
        text_y_list = []
        for i in range(ncat):
            count_portion = nums[i] / count_sum * 100
            count_portion_value = "{:1.2f} %".format(count_portion)
            text_entity = "{}: {} ({})".format(cats[i], count_portion_value, nums[i])
            text_list.append(text_entity)

        # Donut plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # masking donut charts with given colors
        colormap = plt.get_cmap(cmap)
        colors = [colormap(i) for i in np.linspace(0, 1, ncat)]
        wedges, texts = ax.pie(
            nums, wedgeprops=dict(width=0.5), startangle=startangle, colors=colors
        )

        # annotating box
        if annotate == True:
            bbox_props = dict(boxstyle="round, pad=0.3", fc="w", ec="gray")
            kw = dict(
                xycoords="data",
                textcoords="data",
                arrowprops=dict(arrowstyle="-", color="gray"),
                bbox=bbox_props,
                zorder=0,
                va="center",
            )

            for i, p in enumerate(wedges):
                ang = (p.theta2 - p.theta1) / 2.0 + p.theta1
                y = np.sin(np.deg2rad(ang))
                text_y = 1.2 * y
                text_y_list.append(text_y)

                if len(text_y_list) >= 2:
                    if abs(text_y_list[i] - text_y_list[i - 1]) * 1.2 < 0.5:
                        if text_y_list[i] > text_y_list[i - 1]:
                            text_y = text_y_list[i - 1] + 0.25
                        else:
                            text_y = text_y_list[i - 1] - 0.25
                        text_y_list[i] = text_y
                x = np.cos(np.deg2rad(ang))
                horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
                connectionstyle = "angle,angleA=0,angleB={}".format(ang)
                kw["arrowprops"].update({"connectionstyle": connectionstyle})
                ax.annotate(
                    text_list[i],
                    xy=(x, y),
                    xytext=(1.35 * np.sign(x), text_y),
                    horizontalalignment=horizontalalignment,
                    fontsize=16,
                    **kw
                )

        ax.axis("equal")
        ax.set_title(labels[xcol])
        if legend == True:
            ax.legend(wedges, cats, loc="center right", bbox_to_anchor=(0.8, 0, 0.5, 1))
        df_name = namestr(df)
        plt.savefig("./images/cat_donut_{}_{}.png".format(df_name, labels[xcol]))

    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot(xcol)
            else:
                print(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
                exit(1)
    elif chktype(df[xcols], "Series"):
        _plot(xcols)
    else:
        print(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )
        exit(1)
#<<<<<< 4. Categorical Data Distribution        


#>>>>>> 5. Numerical Data Distribution
def dist(
    df,
    xcols,
    labels=None,
    text=False,
    maxbar=False,
    kde=False,
    rug=False,
    xlog=False,
    ylog=False,
):
    """
    Numerical Data Distribution as historam
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    ycol : (str) target column name 
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    text : (Boolean) display mean, std, max, min on graph.
    maxbar : (Boolean) mark maximum bin as blue.
    kde : (Boolean) display kde (kernel density estimate) on graph.
    rug : (Boolean) display rug on graph
    xlog : (Boolean) set x-scale as log.
    ylog : (Boolean) set y-scale as log.
    """
    def _plot(xcol):
               
        fig, ax = plt.subplots(figsize=(6, 6))
        f = sns.distplot(df[xcol], kde=kde, rug=rug)
        df_name = namestr(df)

        mean_val = df[xcol].mean()
        std_val = df[xcol].std()
        max_val = df[xcol].max()
        min_val = df[xcol].min()

        print(
            "{}, {}: mean= {:.2f}, st.dev.= {:.2f}, min= {:.2f}, max= {:.2f}".format(
                df_name, xcol, mean_val, std_val, min_val, max_val
            )
        )

        if text == True:
            fig.text(0.3, 0.8, "     mean : {:>3.02f}".format(mean_val), fontsize=16)
            fig.text(0.3, 0.75, "        std : {:>3.02f}".format(std_val), fontsize=16)
            fig.text(0.3, 0.7, "       max : {:>3.02f}".format(max_val), fontsize=16)
            fig.text(0.3, 0.65, "       min : {:>3.02f}".format(min_val), fontsize=16)

        # The most frequent bin
        heights = [h.get_height() for h in f.patches]
        index_max = np.argmax(heights)

        max_x = f.patches[index_max].get_x() + np.array(
            [0, f.patches[index_max].get_width() / 2]
        )

        if (text == True) and (maxbar == True):
            fig.text(
                0.3,
                0.6,
                "max bin : {:>.02f}~{:>.02f}".format(max_x[0], max_x[1]),
                fontsize=16,
                color="blue",
            )

        if maxbar == True:
            f.patches[index_max].set_color("blue")

        f.set(xlabel=labels[xcol])

        if xlog == True:
            f.set(xscale="log")
            plt.xticks(fontname = "Liberation Sans")
        if ylog == True:
            f.set(yscale="log")
            plt.yticks(fontname = "Liberation Sans")

        plt.tight_layout()
        f.figure.savefig(
            "./images/dist_{}_{}.png".format(df_name, labels[xcol].replace("\n", " "))
        )
        
    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot(xcol)
            else:
                print(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
                exit(1)
    elif chktype(df[xcols], "Series"):
        _plot(xcols)
    else:
        print(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )
        exit(1)   
        
        
