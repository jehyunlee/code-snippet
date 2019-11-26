#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
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

# Nice representation of dataframe in markdown
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

print("# Available Functions : {}".format('df2md(), bar(), pie(), donut(), dist(), dists(), scatter()'))

#<<<<<< 3. Nice Representation of dataframe in markdown

# images directory check and make
try:
    if not(os.path.isdir('./images')):
        os.makedirs(os.path.join('./images'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise



# Fonts settings
fontsuptitle=mpl.font_manager.FontProperties()
fontsuptitle.set_weight('bold')
fontsuptitle.set_size(24)

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

#>>>>>> 4. Categorical Data Distribution      
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
    **kwargs
):
    """
    Numerical Data Distribution as historam
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    text : (Boolean) display mean, std, max, min on graph.
    maxbar : (Boolean) mark maximum bin as blue.
    kde : (Boolean) display kde (kernel density estimate) on graph.
    rug : (Boolean) display rug on graph
    xlog : (Boolean) set x-scale as log.
    ylog : (Boolean) set y-scale as log.
    **kwargs : keyword argument for seaborn.distplot()
    """

    def _plot(xcol):

        fig, ax = plt.subplots(figsize=(6, 6))
        f = sns.distplot(df[xcol], kde=kde, rug=rug, **kwargs)
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
            plt.xticks(fontname="Liberation Sans")
        if ylog == True:
            f.set(yscale="log")
            plt.yticks(fontname="Liberation Sans")

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
        

def dists(
    dfs,
    xcols,
    norm=True,
    label_df=None,
    labels=None,
    kde=True,
    rug=False,
    xlog=False,
    ylog=False,
    **kwargs
):
    """
    Numerical Data Distributions as historam
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    
    label_df : (dict) labels of the DataFrame, to be displayed on graph.
               if None, DataFrame name will be displayed.
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    kde : (Boolean) display kde (kernel density estimate) on graph.
    rug : (Boolean) display rug on graph
    xlog : (Boolean) set x-scale as log.
    ylog : (Boolean) set y-scale as log.
    **kwargs : keyword argument for seaborn.distplot()
    """

    def _plot(df, xcol):
        fig, ax = plt.subplots(figsize=(6, 6))
        labels_df = ""
        for df in dfs:
            df_name = namestr(df)
            f = sns.distplot(
                df[xcol],
                norm_hist=norm,
                kde=kde,
                rug=rug,
                label=label_df[df_name],
                **kwargs
            )

            mean_val = df[xcol].mean()
            std_val = df[xcol].std()
            max_val = df[xcol].max()
            min_val = df[xcol].min()

            print(
                "{}, {}: mean= {:.2f}, st.dev.= {:.2f}, min= {:.2f}, max= {:.2f}".format(
                    df_name, xcol, mean_val, std_val, min_val, max_val
                )
            )

            labels_df = labels_df + "_" + df_name

        f.set(xlabel=labels[xcol])

        if xlog == True:
            f.set(xscale="log")
            plt.xticks(fontname="Liberation Sans")
        if ylog == True:
            f.set(yscale="log")
            plt.yticks(fontname="Liberation Sans")

        plt.tight_layout()
        plt.legend()
        f.figure.savefig("./images/dists_{}_{}.png".format(labels_df, labels[xcol]))

    # if label_df == None
    if label_df == None:
        _df = []
        _label_df = []
        for df in dfs:
            df_name = namestr(df)
            _label_df.append(df_name)
            _df.append(df_name)

        label_df = dict(zip(_label_df, _df))

    # if labels == None
    if labels == None:
        if chktype(dfs, "DataFrame"):
            _labels = _cols = dfs.columns
        elif chktype(dfs, "list") or chktype(dfs, "ndarray"):
            _labels = _cols = dfs[0].columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(dfs, "DataFrame"):
        print(
            "WARNING: The purpose of `dists` is to compare data in two DataFrames. `dist` is called instead."
        )
        dist(
            dfs,
            xcols,
            labels=None,
            kde=True,
            rug=False,
            xlog=False,
            ylog=False,
            **kwargs
        )
        exit(1)
    elif chktype(xcols, "list") or chktype(xcols, "ndarray"):
        if chktype(dfs, "list") or chktype(dfs, "ndarray"):
            ### 모든 df에 대해 df[xcol]이 "Series"일때만 _plot(xcol) 실행
            ### 하나라도 df[xcol]이 "Series"가 아니라면 Error
            series_flag = 1
            for df in dfs:
                for xcol in xcols:
                    if not chktype(df[xcol], "Series"):
                        print(
                            "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name.\n \
                                    `{}` in `{}` raised error.".format(
                                col, namestr(df)
                            )
                        )
                        exit(1)

            for xcol in xcols:
                for df in dfs:
                    if chktype(df[xcol], "Series"):
                        _plot(df, xcol)
                    else:
                        print(
                            "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                        )
                        exit(1)
        else:
            print(
                "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
            )
            exit(1)
    else:
        for df in dfs:
            if not chktype(df[xcols], "Series"):
                print(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
                exit(1)
        for df in dfs:
            if chktype(df[xcols], "Series"):
                _plot(df, xcols)
            else:
                print(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
                exit(1)
                
                
#>>>>>> Scatter plots
import matplotlib.colors as mcolors
from matplotlib import gridspec

colorlist = {}
colorlist.update(mcolors.BASE_COLORS)
colorlist.update(mcolors.TABLEAU_COLORS)
colorlist.update(mcolors.CSS4_COLORS)

colornames = []
colorcodes = []
for name, color in colorlist.items():
  colornames.append(name)
  colorcodes.append(color)

def find_optdim(ncol, aspect_target=9 / 16, addcol=True):
    def _find_optdim(ncol, aspect_target, opt):
        for h in range(1, int(ncol / 2)):
            if ncol % h == 0:
                w = int(ncol / h)
                aspect = h / w
                aspect_diff = abs(aspect_target - aspect)
                opt = np.append(opt, [h, w, aspect_diff])
        opt = opt.reshape((-1, 3))
        optidx = np.argmin(opt[:, 2])
        #         print(opt)
        h_opt, w_opt, aspect_diff = opt[optidx]
        return h_opt, w_opt, aspect_diff

    opt = np.array([])

    aspect_diff = np.inf
    h_opt, w_opt, aspect_diff = _find_optdim(ncol, aspect_target, opt)

    opttol = 0.1
    dummy = 0
    if (addcol == True) and (aspect_diff > opttol):
        while aspect_diff > opttol:
            ncol += 1
            dummy += 1
            #             print("add +1, ncol=", ncol)
            h_opt, w_opt, aspect_diff = _find_optdim(ncol, aspect_target, opt)

    return int(h_opt), int(w_opt), dummy


def scatter(
    df,
    xcols,
    ycol,
    ncols=None,  # if None, ncols and nrows are given by `find_optdim`.
    # if specified, nrows are calculated with a few dummies
    ccol=None,  # column name. if None, default color (blue?)
    aspect_target=9 / 16, 
    addcol=True,
    cmin=None,  # vmin
    cmax=None,  # vmax
    size=1,    # scatter plot size
    labels=None,
    suptitle_aux=None,  # suptitle
    figid=True,  # figure id (a), (b), (c), ...
    yrange=None,  # None or [min, max]
    alpha=0.1,  # opacity of scatters
    xlog=False,
    ylog=False,
    filename=None,
):

    # figure dimension decision
    nxcols = len(xcols)
    if ncols == None:
        nrows, ncols, dummy = find_optdim(nxcols, aspect_target=9 / 16, addcol=True)
    else:
        nrows = (nxcols // ncols) + 1
        dummy = (nrows * ncols) - nxcols
    print(
        "Optimum no. of columns and rows are found as {} and {}, with {} dummy frame.".format(
            ncols, nrows, dummy
        )
    )
    
    # figure preparation
    fig, axes = plt.subplots(
        ncols=ncols,
        nrows=nrows,
        figsize=(5 * ncols, 5 * nrows),
        sharey=True,
        gridspec_kw={"wspace": 0.03, "hspace": 0.3},
    )
    
    # scatter colors
    if ccol == None:
      scatter_color = 'blue'
    elif chktype(df[ccol], 'Series'):
      scatter_color = df[ccol]
    elif ccol in colornames:  ### fix here
      scatter_color = ccol
      
    # x labels
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # scatter plots
    i = 0
    for ax in axes.ravel():
        if i < nxcols:
            points = ax.scatter(
                x=df[xcols[i]],
                y=df[ycol],
                c=scatter_color,
                cmap="jet",
                alpha=alpha,
                s=size,
                vmin=cmin,
                vmax=cmax,
            )
            sns.regplot(
                x=xcols[i],
                y=ycol,
                data=df,
                ax=ax,
                line_kws={"linewidth": 2, "color": "gray"},
                scatter=False,
            )
            if figid == True:
                ax.text(
                    0.02, 0.98,
                    "({})".format(chr(ord("a") + i)),
                    transform=ax.transAxes,
                    fontsize=20,
                    verticalalignment="top",
                )
            ax.set_xlabel(labels[xcols[i]])
            ax.set_ylabel("")

            if yrange != None:
                ymin = yrange[0]
                ymax = yrange[1]
                ax.set_ylim(ymin, ymax)

            i += 1
            
            if xlog == True:
                ax.set_xscale('log')
                for tick in ax.get_xticklabels():
                    tick.set_fontname("Liberation Sans")
            if ylog == True:
                ax.set_yscale('log')
                for tick in ax.get_yticklabels():
                    tick.set_fontname("Liberation Sans")


    if suptitle_aux == None:
        suptitle = labels[ycol]
    else:
        suptitle = "{} ({})".format(labels[ycol], suptitle_aux)
    plt.suptitle(suptitle, fontproperties=fontsuptitle)

    plt.tight_layout()
    
    df_name = namestr(df)
    if filename == None:
        filename = ''
        for xcol in xcols:
          filename += xcol
    plt.savefig("./images/scatter_{}_{}.png".format(df_name, filename))