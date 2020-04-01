#!/usr/bin/env python
# coding: utf-8
# ver. 2019.11.28.
# Jehyun Lee (jehyun.lee@gmail.com)

COLOR="green"
SEABORN_STYLE = "whitegrid"
SEABORN_PALETTE = "bright"
SEABORN_CONTEXT = "talk"
PRINTDPI = 200

# -------------------------------------------------------------

import numpy as np
import pandas as pd
import seaborn as sns
import os, copy, sys, io
from IPython.display import Markdown, display
import matplotlib.colors as mcolors
from matplotlib import gridspec

sns.set(font_scale=1)

# >>>>>> Korean Font Setting
import platform

system = platform.system()

# -*- coding: UTF-8 -*-
get_ipython().run_line_magic("matplotlib", "inline")

import matplotlib as mpl  # 기본 설정 만지는 용도
import matplotlib.pyplot as plt  # 그래프 그리는 용도
import matplotlib.font_manager as fm  # 폰트 관련 용도

print("버전: ", mpl.__version__)
print("설치 위치: ", mpl.__file__)
print("설정 위치: ", mpl.get_configdir())
print("캐시 위치: ", mpl.get_cachedir())
print("설정 파일 위치: ", mpl.matplotlib_fname())
font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")

if system == "Windows":
    datapath = os.getcwd() + "\\"
    imagepath = datapath + "images\\"

    # ttf 폰트 전체개수
    font_list[:10]

    f = [f.name for f in fm.fontManager.ttflist]
    f[:10]

    [(f.name, f.fname) for f in fm.fontManager.ttflist if "Nanum" in f.name]

    path = "C:\\Windows\\Fonts\\NanumBarunGothic.ttf"
    font_name = fm.FontProperties(fname=path, size=50).get_name()

    print(font_name)
    plt.rc("font", family=font_name)
    print("# matplotlib 한글 사용 가능")

elif system == "Linux":
    datapath = os.getcwd() + "//"
    imagepath = datapath + "images//"

    #     !apt-get update -qq
    #     !apt-get install fonts-nanum* -qq

    path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 설치된 나눔글꼴중 원하는 녀석의 전체 경로를 가져오자
    font_name = fm.FontProperties(fname=path, size=10).get_name()

    print(font_name)
    plt.rc("font", family=font_name)

    fm._rebuild()
    mpl.rcParams["axes.unicode_minus"] = False
    print("# matplotlib 한글 사용 가능")

else:
    sys.exit("ERROR: Sorry, my code has compatibility with Windows and Linux only.")

# <<<<<< Korean Font Setting

# >>>>>> Figure Style Setting
plt.style.context("seaborn")
sns.set_style(SEABORN_STYLE)
sns.set_palette(SEABORN_PALETTE)
sns.palplot(sns.color_palette(SEABORN_PALETTE))
sns.set_context(SEABORN_CONTEXT)
plt.rc("font", family=font_name)
fm._rebuild()
mpl.rcParams["axes.unicode_minus"] = False
print(
    "# Seaborn Figure Style : {}, {}, {}".format(
        SEABORN_STYLE, SEABORN_PALETTE, SEABORN_CONTEXT
    )
)
print("# Default color : {}".format(COLOR))

# <<<<<< 2.Figure Style Setting

# >>>>>> 3. Nice Representation of dataframe in markdown

# Nice representation of dataframe in markdown
import warnings

warnings.filterwarnings(action="ignore")


def df2md(df, maxlen=20, indexname="(index)", showindex=True):
    """
    Nice Representation of Pandas DataFrame and Series in Markdown Format.
    
    Parameters
    ----------------
    df : pandas.DataFrame or pandas.Series
    maxlen : (int) maximum length of data at markdown output.
             data exceeding maxlen will be presented as ' ...'
    indexname : (str) name of index, to be displayed on markdown output.
                To avoid overriding column name, if conflicts, the '_' will be added in front of the indexname.
    showindex : (Boolean) show index or not.
    """

    _df = copy.deepcopy(df)

    if "Series" in str(type(df)):
        _idx = _df.index
        _df = pd.DataFrame(data=_df, index=_idx)

    for col in _df.columns:
        _df[col] = _df[col].astype("str")
        if (_df[col].str.len() > maxlen).any():
            _df[col].loc[_df[col].str.len() > maxlen] = (
                _df[col].str.slice(stop=maxlen) + " ..."
            )

    if showindex == True:
        if indexname in _df.columns:
            while indexname in _df.columns:
                indexname = "_" + indexname
            warnings.warn(
                "The index name shouldn't overlap other column names. {} will be used instead.\nConsider changing the indexname parameter.".format(
                    indexname
                ),
                SyntaxWarning,
            )
        _df.insert(0, indexname, df.index)

    fmt = ["---" for i in range(len(_df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=_df.columns)
    df_formatted = pd.concat([df_fmt, _df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))
    # _df.drop(columns=indexname, axis=1, inplace=True)
    del _df


print(
    "# Available Functions : {}".format(
        "df2md(), bar(), pie(), donut(), dist(), dists(), scatter()"
    )
)

# <<<<<< Nice Representation of dataframe in markdown

# >>>>>> images directory check and make if not
try:
    if not (os.path.isdir("./images")):
        os.makedirs(os.path.join("./images"))
        print("# Directory created : ./images")
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

# <<<<<< images directory check and make if not

# >>>>>> list colors in matplotlib
colorlist = {}
colorlist.update(mcolors.BASE_COLORS)
colorlist.update(mcolors.TABLEAU_COLORS)
colorlist.update(mcolors.CSS4_COLORS)

colornames = []
colorcodes = []
for name, color in colorlist.items():
    colornames.append(name)
    colorcodes.append(color)

# <<<<<< list colors in matplotlib


# >>>>>> Fonts settings
# suptitle
fontsuptitle = mpl.font_manager.FontProperties()
fontsuptitle.set_weight("bold")
fontsuptitle.set_size(20)

# <<<<<< Fonts settings

# >>>>>> Figure settings
mpl.rcParams['figure.dpi'] = 200

# >>>>>> Utilities
# Figure Settings
styles = ["whitegrid", "dark", "white", "ticks", "darkgrid"]
palettes = ["pastel", "muted", "deep", "bright", "colorblind", "dark", "hls", "husl"]
contexts = ["notebook", "paper", "talk", "poster"]

def set(dpi=None, style=None, color=None, palette=None, context=None):    
    """
    Figure Style Setting
    
    Parameters
    ----------------
    dpi : (float) image resolution. dot per inch
    style : (str) seaborn style: "whitegrid", "dark", "white", "ticks", "darkgrid".
    color : (str) default color: a member of colorlist. if 'list', print color list.
    palette : (str) seaborn color palette: matplotlib colormap | hls | husl
    context : (str) seaborn context: "notebook", "paper", "talk", and "poster"
    """
    global SEABORN_STYLE, SEABORN_PALETTE, SEABORN_CONTEXT, COLOR, PRINTDPI
    
    if dpi != None:
        PRINTDPI = dpi
        
    if (style != None) and (style in styles):
        SEABORN_STYLE = style
        sns.set_style(style) 
    
    if (color != None) :
        if (color == 'list'):
            print("Color List:\n{}".format(colorlist))
        else:
            COLOR=color
        
    if (palette != None) and (palette in []):
        SEABORN_PALETTE = palette
        sns.set_palette(palette)
        sns.palplot(sns.color_palette(palette))        
        
    if context != None:
        SEABORN_CONTEXT = context
        sns.set_context(context)        
        
    print('Figure dpi for file = {}'.format(PRINTDPI))
    print('Seaborn Style = {}'.format(SEABORN_STYLE))
    print('Default Color = {}'.format(COLOR))
    print('Seaborn Palette = {}'.format(SEABORN_PALETTE))
    print('Seaborn Context = {}'.format(SEABORN_CONTEXT))

# Retrieving Variable Name
import traceback

def namestr(order, *expr):
#     for i in range(-10, -1):
#         (filename, line_number, function_name, text) = traceback.extract_stack()[i]
#         print('### {},\n# filename = {}, \n# line_number={}, \n# function_name={}, \n# text={}\n\n'.format(traceback.extract_stack()[i], filename, line_number, function_name, text))
#         if '<ipython-input-' in filename:
# #             result = traceback.print_tb(filename)
# #             print('# filename extract=\nresult={}', result)
#               print(
    
#               exc_type, exc_value, exc_traceback = sys.exc_info()
#               print(exc_type, exc_value, exc_traceback)
#               print('\n## traceback.print_exc\n', traceback.print_exc())
# #               print('\n## traceback.print_last\n', traceback.print_last())
#               print('\n## traceback.print_tb\n', traceback.print_tb(exc_traceback))
#               print('\n## traceback.print_stack\n', traceback.print_stack())
#               print('\n## traceback.extract_stack\n', traceback.extract_stack())  
    
    (filename, line_number, function_name, text) = traceback.extract_stack()[order]
    begin = text.find("(") + 1
    end = text.find(",", begin)
    ans = text[begin:end].strip(" ")
    if "=" in ans:
        ans = ans.split("=")[1].strip(" ")
    return ans


# Check type of variable
def chktype(var, typename):
    if typename in str(type(var)):
        return True
    else:
        return False

# Fix label for figure file name
def fixlabel(labels, fixcol):
    fixchars = ['\n', '\t', '/', '<', '>', '^']
    fixstr = labels[fixcol]
    for fixchar in fixchars:
        if fixchar in fixstr:
            fixstr = fixstr.replace(fixchar, '')
        fixstr = fixstr.strip('')
    return fixstr

# <<<<<< Utilities

# >>>>>> Plots
# bar plot
def bar(df, xcols, rcols=None, labels=None, gap=0.03, **kwargs):
    """
    Categorical Data Distribution as Barplot
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list or str) column name(s) of pandas.DataFrame.
    rcol : (list or str) column name(s) of pandas.DataFrame to restrict data.
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    gap : (float) distance between bar top and annotation
    """

    # Plotting function
    def _plot2(df, xcol, rcol):

        grouped = pd.DataFrame(df.groupby(xcol).count().reset_index())

        plt.figure(figsize=(6, 6))

        ax = sns.barplot(x=xcol, y=rcol, data=grouped, **kwargs)

        # fontsize of the data number
        fontsize = 16

        # adjusting ylims to bare numbers
        # - find min, max values of the bars
        xys = np.array([h.xy for h in ax.patches])
        hs = np.array([h.get_height() for h in ax.patches])
        y0min = xys[:, 1].min()
        hmax = hs.max()
        hmin = hs.min()

        if gap != None:
            # - setting the graph ylims
            absgap = hmax * gap
            ymin, ymax = ax.get_ylim()
            if absgap > 0:
                ymax += absgap
            if hmin + absgap < ymin:
                ymin += absgap
            ax.set_ylim(ymin, ymax)

            # - add data on bar
            for i in ax.patches:
                ax.text(
                    i.get_x() + i.get_width() / 2,
                    i.get_height() + absgap,
                    str(int(i.get_height())),
                    ha="center",
                    fontsize=fontsize,
                )

        ax.set(title="  ")
        ax.set(xlabel=labels[xcol])
        ax.set(ylabel=None)

        if rcol == "@pega@dummy@pega@":
            suptitle = ""
        else:
            suptitle = "{} ({})".format(labels[rcol], df[rcol].iloc[0])

        plt.suptitle(suptitle, fontproperties=fontsuptitle, position=(0.5, 1))
        plt.tight_layout()

        figxlabel = fixlabel(labels, xcol)
        print(figxlabel)
        figname = "./images/cat_bar_{}_{}".format(df_name, figxlabel)
        if rcol == "@pega@dummy@pega@":
            figname += ".png"
        else:
            figrlabel = fixlabel(labels, rcol)
            figname += "_{}.png".format(figrlabel + str(df[rcol].iloc[0]))
        
        plt.savefig(figname, dpi=PRINTDPI)

    def _plot1(df, xcol, rcols):
        if rcols == None:
            _df = copy.deepcopy(df)
            dummyname = "@pega@dummy@pega@"
            _df[dummyname] = _df.index
            _plot2(_df, xcol, dummyname)
        else:
            if chktype(df[rcols], "Series") and (rcols != xcol):
                rcolu = np.unique(df[rcols])
                for yu in rcolu:
                    _df = df[df[rcols] == yu]
                    _plot2(_df, xcol, rcols)
            elif chktype(rcols, "list") or chktype(rcols, "np.array"):
                for rcol in rcols:
                    if chktype(df[rcol], "Series") and (rcol != xcol):
                        rcolu = np.unique(df[rcol])
                        for yu in rcolu:
                            _df = df[df[rcol] == yu]
                            _plot2(_df, xcol, rcol)
            else:
                sys.exit("ERROR: `rcols` is not valid column.")

    df_name = namestr(-3, df)

    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot1(df, xcol, rcols)
            else:
                sys.exit(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
    elif chktype(df[xcols], "Series"):
        _plot1(df, xcols, rcols)
    else:
        sys.exit(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )


def calc_abs(pct, data_array: list):
    absolute = int(pct / 100.0 * np.sum(data_array))
    return "{:.1f}%\n({:d})".format(pct, absolute)


# Pie Chart
def pie(
    df,
    xcols,
    rcols=None,
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
    xcols : (list or str) column name(s) of pandas.DataFrame.
    rcols : (list or str) column name(s) of pandas.DataFrame to restrict data.
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    cmap : (Matplotlib colormap) default is 'tab20'.
    startangle : (float) starting angle of wedges in degrees.
    annotate : (Boolean) Adding informations on graph.
    legend : (Boolean) Adding legend box on rightside of graph
    """

    def _plot2(df, xcol, rcol):
        grouped = pd.DataFrame(df.groupby(xcol).count().reset_index())
        fig, ax = plt.subplots(figsize=(10, 6))

        # Categorical Data to plot
        colormap = plt.get_cmap(cmap)
        cats = grouped[xcol].values  # Categories, to be one-hot encoded
        ncat = grouped[xcol].shape[0]  # Number of Categories
        nums = grouped[rcol].values  # Number of data for each categories

        # print out as tables, if annotate == False
        if annotate == False:
            _grouped = grouped[[xcol, rcol]]
            if rcol == "@pega@dummy@pega@":
                newrcol = "No. of Data"
            else:
                newrcol = "{} = {}".format(labels[rcol], str(df[rcol].iloc[0]))
            _grouped.rename(columns={xcol: labels[xcol], rcol: newrcol}, inplace=True)
            df2md(_grouped, showindex=False)

        # masking pie charts with given colors
        colors = [colormap(i) for i in np.linspace(0, 1, ncat)]
        wedges, texts, autotexts = ax.pie(
            nums,
            colors=colors,
            autopct=lambda pct: calc_abs(pct, nums) if annotate == True else None,
            startangle=startangle,
            textprops={"color": "w"},
        )
        plt.setp(autotexts, size=16, weight="bold")

        # legend
        if legend == True:
            ax.legend(
                wedges, cats, title=labels[xcol], loc="center right", title_fontsize=16
            )
        else:
            ax.legend(title=labels[xcol], loc="center", title_fontsize=16, framealpha=1)

        # title
        if rcol == "@pega@dummy@pega@":
            title = ""
        else:
            title = "{} ({})".format(labels[rcol], df[rcol].iloc[0])
        ax.set_title(title)

        # save as file
        ax.axis("equal")
        figname = "./images/cat_pie_{}_{}".format(df_name, labels[xcol])
        if rcol == "@pega@dummy@pega@":
            figname += ".png"
        else:
            figname += "_{}.png".format(labels[rcol] + str(df[rcol].iloc[0]))
        plt.savefig(figname, dpi=PRINTDPI)

    def _plot1(df, xcol, rcols):
        if rcols == None:
            _df = copy.deepcopy(df)
            dummyname = "@pega@dummy@pega@"
            _df[dummyname] = _df.index
            _plot2(_df, xcol, dummyname)
        else:
            if chktype(df[rcols], "Series"):
                rcolu = np.unique(df[rcols])
                for yu in rcolu:
                    _df = df[df[rcols] == yu]
                    _plot2(_df, xcol, rcols)
            elif chktype(rcols, "list") or chktype(rcols, "np.array"):
                for rcol in rcols:
                    if chktype(df[rcol], "Series"):
                        rcolu = np.unique(df[rcol])
                        for yu in rcolu:
                            _df = df[df[rcol] == yu]
                            _plot2(_df, xcol, rcol)
            else:
                sys.exit("ERROR: `rcols` is not valid column.")

    df_name = namestr(-3, df)

    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot1(df, xcol, rcols)
            else:
                sys.exit(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
    elif chktype(df[xcols], "Series"):
        _plot1(df, xcols, rcols)
    else:
        sys.exit(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )


# Donut Chart
def donut(
    df,
    xcols,
    rcols=None,
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
    xcols : (list or str) column name(s) of pandas.DataFrame.
    rcols : (list or str) column name(s) of pandas.DataFrame to restrict data.
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    cmap : (Matplotlib colormap) default is 'tab20'.
    startangle : (float) starting angle of wedges in degrees.
    annotate : (Boolean) Adding informations on graph.
    legend : (Boolean) Adding legend box on rightside of graph
    """

    def _plot2(df, xcol, rcol):
        # Categorical Data to plot
        grouped = pd.DataFrame(df.groupby(xcol).count().reset_index())
        colormap = plt.get_cmap(cmap)
        cats = grouped[xcol].values  # Categories, to be one-hot encoded
        ncat = grouped[xcol].shape[0]  # Number of Categories
        nums = grouped[rcol].values  # Number of data for each categories

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
        # print out as tables, if annotate == False
        else:
            _grouped = grouped[[xcol, rcol]]
            if rcol == "@pega@dummy@pega@":
                newrcol = "No. of Data"
            else:
                newrcol = "{} = {}".format(labels[rcol], str(df[rcol].iloc[0]))
            _grouped.rename(columns={xcol: labels[xcol], rcol: newrcol}, inplace=True)
            df2md(_grouped, showindex=False)

        ax.axis("equal")
        if rcol == "@pega@dummy@pega@":
            title = "  "
        else:
            title = "{} ({})".format(labels[rcol], df[rcol].iloc[0])
        ax.set_title(title)

        if legend != True:
            ax.text(
                0.5,
                0.5,
                labels[xcol],
                transform=ax.transAxes,
                fontsize=16,
                verticalalignment="center",
                horizontalalignment="center",
            )
        if legend == True:
            ax.legend(
                wedges, cats, title=labels[xcol], loc="center right", title_fontsize=16
            )

        figname = "./images/cat_donut_{}_{}".format(df_name, labels[xcol])
        if rcol == "@pega@dummy@pega@":
            figname += ".png"
        else:
            figname += "_{}.png".format(labels[rcol] + str(df[rcol].iloc[0]))
        plt.savefig(figname, dpi=PRINTDPI)

    def _plot1(df, xcol, rcols):
        if rcols == None:
            _df = copy.deepcopy(df)
            dummyname = "@pega@dummy@pega@"
            _df[dummyname] = _df.index
            _plot2(_df, xcol, dummyname)
        else:
            if chktype(df[rcols], "Series"):
                rcolu = np.unique(df[rcols])
                for yu in rcolu:
                    _df = df[df[rcols] == yu]
                    _plot2(_df, xcol, rcols)
            elif chktype(rcols, "list") or chktype(rcols, "np.array"):
                for rcol in rcols:
                    if chktype(df[rcol], "Series"):
                        rcolu = np.unique(df[rcol])
                        for yu in rcolu:
                            _df = df[df[rcol] == yu]
                            _plot2(_df, xcol, rcol)
            else:
                sys.exit("ERROR: `rcols` is not valid column.")

    df_name = namestr(-3, df)

    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot1(df, xcol, rcols)
            else:
                sys.exit(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
    elif chktype(df[xcols], "Series"):
        _plot1(df, xcols, rcols)
    else:
        sys.exit(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )


# Numerical data distribution
def dist(
    df,
    xcols,
    rcols=None,
    rsep=False,
    bins=None,
    norm_hist=False,
    xlims=None,
    ylims=None,
    labels=None,
    text=False,
    maxbar=False,
    kde=True,
    rug=False,
    xlog=False,
    ylog=False,
):
    """
    Numerical Data Distribution as historam
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list or str) column name(s) of pandas.DataFrame.
    rcols : (list or str) column name(s) of pandas.DataFrame to restrict data.
    rsep : (Boolean) If True, separate category of rcols as independent images.
    bins : argument for matplotlib hist(), or None, optional
           Specification of hist bins, or None to use Freedman-Diaconis rule.
    norm_hist : (Boolean) If True, the histogram height shows a density rather than a count.
    xlims : (list) range of y values on graph. [xmin, xmax]
    ylims : (list) range of y values on graph. [ymin, ymax]
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    text : (Boolean) If True, display mean, std, max, min on graph.
    maxbar : (Boolean) If True, mark maximum bin as blue.
             But overridden by rsep, that rsep=False disables maxbar option
    kde : (Boolean) if True, display kde (kernel density estimate) on graph.
    rug : (Boolean) if True, display rug on graph
    xlog : (Boolean) if True, set x-scale as log.
    ylog : (Boolean) if True, set y-scale as log.
    **kwargs : keyword argument for seaborn.distplot()
    """

    def _plot2(df, xcol, rcol):

        fig, ax = plt.subplots(figsize=(6, 6))
        
        _df0 = copy.deepcopy(df[[xcol, rcol]])
        size_before_dropna = _df0.shape[0]
        _df0.dropna(inplace=True)
        size_after_dropna = _df0.shape[0]
        size_diff_dropna = size_before_dropna - size_after_dropna
        
        if (size_diff_dropna != 0) and (rcol != "@pega@dummy@pega@"):
            print('## Missing data dropped in {}["{}"] ({}): {}'.format(df_name, rcol, labels[rcol].replace('\n', ''), size_diff_dropna))
            
        rcolu = np.unique(_df0[rcol])
        nrcolu = len(rcolu)

        for yu in rcolu:
            _df = _df0[_df0[rcol] == yu]
            
            size_before_dropna = _df.size
            _df.dropna(inplace=True)
            size_after_dropna = _df.size
            size_diff_dropna = size_before_dropna - size_after_dropna

            if (rsep != True) and (rcol != "@pega@dummy@pega@"):
                plotlabel = "{}={}".format(labels[rcol], _df[rcol].iloc[0])
            else:
                plotlabel = None

            f = sns.distplot(
                _df[xcol], norm_hist=norm_hist, kde=kde, rug=rug, label=plotlabel, bins=bins
            )

            mean_val = _df[xcol].mean()
            std_val = _df[xcol].std()
            max_val = _df[xcol].max()
            min_val = _df[xcol].min()

            distsummary = ": mean= {:.2f}, st.dev.= {:.2f}, min= {:.2f}, max= {:.2f}".format(
                mean_val, std_val, min_val, max_val
            )
            prefix = "{}, {}".format(df_name, xcol)

            if rcol == "@pega@dummy@pega@":
                pass
            else:
                prefix += ", {}({})".format(rcol, yu)
            
            if size_diff_dropna != 0:
                if rcol == "@pega@dummy@pega@":
                    print('# Missing data dropped in {}["{}"] ({}): {}'.format(df_name, xcol, labels[xcol], size_diff_dropna))
                else:
                    print('# Missing data dropped in {}["{}"] ({}) @{}={}: {}'.format(df_name, xcol, labels[xcol], rcol, yu, size_diff_dropna))
            
            print(prefix + distsummary)

            if (text == True) and (nrcolu == 1):
                fig.text(
                    0.3, 0.8, "     mean : {:>3.02f}".format(mean_val), fontsize=16
                )
                fig.text(
                    0.3, 0.75, "        std : {:>3.02f}".format(std_val), fontsize=16
                )
                fig.text(
                    0.3, 0.7, "       max : {:>3.02f}".format(max_val), fontsize=16
                )
                fig.text(
                    0.3, 0.65, "       min : {:>3.02f}".format(min_val), fontsize=16
                )

            # The most frequent bin
            heights = [h.get_height() for h in f.patches]
            index_max = np.argmax(heights)

            max_x = f.patches[index_max].get_x() + np.array(
                [0, f.patches[index_max].get_width() / 2]
            )

            if (text == True) and (maxbar == True) and (nrcolu == 1):
                fig.text(
                    0.3,
                    0.6,
                    "max bin : {:>.02f}~{:>.02f}".format(max_x[0], max_x[1]),
                    fontsize=16,
                    color="blue",
                )

            if (maxbar == True) and (nrcolu == 1):
                f.patches[index_max].set_color("blue")

        if xlims != None:
            xmin = xlims[0]
            xmax = xlims[1]
            ax.set_xlim(xmin, xmax)

        if ylims != None:
            ymin = ylims[0]
            ymax = ylims[1]
            ax.set_ylim(ymin, ymax)

        ax.set(title="  ")

        f.set(xlabel=labels[xcol])

        if xlog == True:
            f.set(xscale="log")
            plt.xticks(fontname="Liberation Sans")
        if ylog == True:
            f.set(yscale="log")
            plt.yticks(fontname="Liberation Sans")

        if rcol == "@pega@dummy@pega@":
            suptitle = ""
        elif rsep == True:
            suptitle = "{} ({})".format(labels[rcol], df[rcol].iloc[0])
        else:
            suptitle = "{}".format(labels[rcol])
            plt.legend()

        plt.suptitle(suptitle, fontproperties=fontsuptitle, position=(0.5, 0.98))

        plt.tight_layout()

        
        figxcol = fixlabel(labels, xcol)
        if rcol != '@pega@dummy@pega@':
            figrcol = fixlabel(labels, rcol)
            
        figname = "./images/dist_{}_{}".format(df_name, figxcol)
        if rcol == "@pega@dummy@pega@":
            figname += ".png"
        elif rsep == True:
            figname += "_{}.png".format(figrcol + str(df[rcol].iloc[0]))
        else:
            figname += "_{}.png".format(figrcol)
        f.figure.savefig(figname, dpi=PRINTDPI)

    def _plot1(df, xcol, rcols):
        if rcols == None:
            _df = copy.deepcopy(df)
            dummyname = "@pega@dummy@pega@"
            _df[dummyname] = 0
            _plot2(_df, xcol, dummyname)
        else:
            if chktype(df[rcols], "Series"):
                if rsep == True:
                    rcolu = np.unique(df[rcols])
                    for yu in rcolu:
                        _df = df[df[rcols] == yu]
                        _plot2(_df, xcol, rcols)
                else:
                    _plot2(df, xcol, rcols)
            elif chktype(rcols, "list") or chktype(rcols, "np.array"):
                for rcol in rcols:
                    if chktype(df[rcol], "Series"):
                        if rsep == True:
                            rcolu = np.unique(df[rcol])
                            for yu in rcolu:
                                _df = df[df[rcol] == yu]
                                _plot2(_df, xcol, rcol)
                        else:
                            _plot2(df, xcol, rcol)
            else:
                sys.exit("ERROR: `rcols` is not valid column.")

    df_name = namestr(-3, df)

    # if labels == None
    if labels == None:
        _labels = _cols = df.columns
        labels = dict(zip(_labels, _cols))

    # check data validity and run
    if chktype(xcols, "list") or chktype(xcols, "ndarray"):
        for xcol in xcols:
            if chktype(df[xcol], "Series"):
                _plot1(df, xcol, rcols)
            else:
                sys.exit(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
    elif chktype(df[xcols], "Series"):
        _plot1(df, xcols, rcols)
    else:
        sys.exit(
            "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
        )


# Numerical data distributions, comparing multiple dataframe
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
    Numerical Data Distributions as historam, comparing multiple DataFrame
    
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
        f.figure.savefig("./images/dists_{}_{}.png".format(labels_df, labels[xcol]), dpi=PRINTDPI)

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
    elif chktype(xcols, "list") or chktype(xcols, "ndarray"):
        if chktype(dfs, "list") or chktype(dfs, "ndarray"):
            ### 모든 df에 대해 df[xcol]이 "Series"일때만 _plot(xcol) 실행
            ### 하나라도 df[xcol]이 "Series"가 아니라면 Error
            series_flag = 1
            for df in dfs:
                for xcol in xcols:
                    if not chktype(df[xcol], "Series"):
                        sys.exit(
                            "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name.\n \
                                    `{}` in `{}` raised error.".format(
                                col, namestr(df)
                            )
                        )

            for xcol in xcols:
                for df in dfs:
                    if chktype(df[xcol], "Series"):
                        _plot(df, xcol)
                    else:
                        sys.exit(
                            "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                        )
        else:
            sys.exit(
                "ERROR: `xcols` is supposed to be a list of pandas.DataFrame column name(s)"
            )
    else:
        for df in dfs:
            if not chktype(df[xcols], "Series"):
                sys.exit(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )
        for df in dfs:
            if chktype(df[xcols], "Series"):
                _plot(df, xcols)
            else:
                sys.exit(
                    "ERROR: element of `xcols` is supposed to be a list of pandas.DataFrame column name"
                )


# Scatter plots
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
    ncols=None,
    aspect_target=9 / 16,
    addcol=True,
    ccol="blue",  # column name. if None, default color (blue?)
    cmap="jet",
    cmin=None,  # vmin
    cmax=None,  # vmax
    size=1,  # scatter plot size
    alpha=0.3,  # opacity of scatters
    figid=True,  # figure id (a), (b), (c), ...
    ylims=None,  # None or [min, max]
    xlog=False,
    ylog=False,
    labels=None,
    suptitle_aux=None,  # suptitle
    filename=None,
):
    """
    Data Distribution as scatter plot
    
    Parameters
    ----------------
    df : pandas.DataFrame
    xcols : (list, numpy.ndarray or str) column name(s) of pandas.DataFrame.
    ycol : (str) target column name 
    
    ncols : (int) number of columns of the figure
    aspect_target : (float) aspect ratio of the figure (default=16:9)
    addcol : (Boolean)
    
    ccol : (str) column name or Matplotlib color name.
    cmap : (str) Matplotlib color name. Valid only if ccol is a column name.
    cmin : (float) minimum value of the scatter colormap
    cmax : (float) maximum value of the scatter colormap
    size : (float) scatter size
    alpha : (float) scatter opacity
    
    figid : (Boolean) figure id, such as (a), (b), ...
    ylims : (list) range of y values on graph. [ymin, ymax]
    xlog : (Boolean) set x-scale as log.
    ylog : (Boolean) set y-scale as log.
    
    labels : (dict) label names to be displayed on graph.
             if None, column name will be displayed.
    suptitle_aux : (str) auxiliary text on suptitle
    filename : (str) filename to be added after DataFrame name. 
                     the filename will be './images/scatter_{DataFrame_name}_{filename}.png'
                     if None, all `xcols` will be enlisted.
    """
    df_name = namestr(-3, df)

    # figure dimension decision
    nxcols = len(xcols)
    if ncols == None:
        nrows, ncols, dummy = find_optdim(nxcols, aspect_target=9 / 16, addcol=True)
    else:
        nrows = (nxcols // ncols)
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
    errorflag = 0
    try:
        if chktype(df[ccol], "Series"):
            scatter_color = df[ccol]
        else:
            errorflag = 1
    except:
        if ccol in colornames:
            scatter_color = ccol
        else:
            errorflag = 1

    if errorflag == 1:
        sys.exit("ERROR: `ccol` should be a color name or column name in DataFrame")

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
                cmap=cmap,
                alpha=alpha,
                s=size,
                vmin=cmin,
                vmax=cmax,
                edgecolors='gray'
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
                    0.02,
                    0.98,
                    "({})".format(chr(ord("a") + i)),
                    transform=ax.transAxes,
                    fontsize=20,
                    verticalalignment="top",
                )
            ax.set_xlabel(labels[xcols[i]])
            ax.set_ylabel("")

            if ylims != None:
                ymin = ylims[0]
                ymax = ylims[1]
                ax.set_ylim(ymin, ymax)

            i += 1

            if xlog == True:
                ax.set_xscale("log")
                for tick in ax.get_xticklabels():
                    tick.set_fontname("Liberation Sans")
            if ylog == True:
                ax.set_yscale("log")
                for tick in ax.get_yticklabels():
                    tick.set_fontname("Liberation Sans")

    if suptitle_aux == None:
        suptitle = labels[ycol]
    else:
        suptitle = "{} ({})".format(labels[ycol], suptitle_aux)
    plt.suptitle(suptitle, fontproperties=fontsuptitle)

    plt.subplots_adjust(left=0.03, bottom=0.2, right=0.97, top=0.9)
    if filename == None:
        filename = ""
        for xcol in xcols:
            filename += xcol
    plt.savefig("./images/scatter_{}_{}.png".format(df_name, filename), dpi=PRINTDPI)
    

def truepred(y_true, y_pred, ccol='green', alpha=0.5, size=1, linecolor='blue', xylims=None, suptitle=None, suptitle_aux=None):
    fig, ax = plt.subplots(figsize=(5,5))
    x = y_pred
    y = y_true
        
    sns.regplot(x, y, color=ccol, 
                scatter_kws={'alpha':alpha, 's':size},
                line_kws={'linewidth':2, 'color':linecolor})
    
#     ax.text(0.5, 0.4, 'RMSE = {:.3f}'.format(rmse), transform=ax.transAxes, fontsize=20, verticalalignment='top')
#     ax.text(0.5, 0.3, 'R2 = {:.3f}'.format(r2), transform=ax.transAxes, fontsize=20, verticalalignment='top')
    
    
    # xlim, ylim
    if xylims == None:
        axmin = min(min(y_true), min(y_pred))
        axmax = max(max(y_true), max(y_pred))
#     elif chktype(xylims, 'list') or chktype(xylims, 'array'):
    else:
        axmin = xylims[0]
        axmax = xylims[1]
    
    ax.set_xlim(axmin, axmax)
    ax.set_ylim(axmin, axmax)
    
    # xticklabels, yticklabels
    plt.draw()
    xtl = ax.get_xticklabels()
    ytl = ax.get_yticklabels()
    
    if len(xtl) < len(ytl):
        ticklabels = xtl
    else:
        ticklabels = ytl
    
    ticks = [float(str(label).split("'")[-2].strip('')) for label in ticklabels]
    
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.plot([ticks[0], ticks[-1]], [ticks[0], ticks[-1]], color='gray', linestyle=':')
    
    # labels and titles
    ax.set_xlabel('Prediction')    
    ax.set_ylabel('True')
    ax.set_title(' ')
    
    if suptitle != None:
        if suptitle_aux == None:
            suptitle = suptitle
        else:
            suptitle = "{} ({})".format(suptitle, suptitle_aux)
        plt.suptitle(suptitle, fontproperties=fontsuptitle)
    
    
    plt.tight_layout()
    plt.savefig(f'./images/truepred_{suptitle}.png', dpi=PRINTDPI)

# def truepreddf(df, y_true, y_pred, ccol, cmap='jet', alpha=0.5, size=1, linecolor='blue', suptitle=None, suptitle_aux=None):
#     fig, ax = plt.subplots(figsize=(5,5))
#     x = y_pred
#     y = y_true
    
#     sns.regplot(x, y, color=ccol, 
#                 scatter_kws={'alpha':alpha, 's':1},
#                 line_kws={'linewidth':2, 'color':linecolor})
#     ax.plot([0,1], [0,1], color='gray', linestyle=':')
# #     ax.text(0.5, 0.4, 'RMSE = {:.3f}'.format(rmse), transform=ax.transAxes, fontsize=20, verticalalignment='top')
# #     ax.text(0.5, 0.3, 'R2 = {:.3f}'.format(r2), transform=ax.transAxes, fontsize=20, verticalalignment='top')
#     ax.set_xlabel('Prediction')    
#     ax.set_xlim(0,1)
#     ax.set_ylim(0,1)
#     ax.set_ylabel('True')
    
#     if suptitle != None:
#         if suptitle_aux == None:
#             suptitle = suptitle
#         else:
#             suptitle = "{} ({})".format(suptitle, suptitle_aux)
#         plt.suptitle(suptitle, fontproperties=fontsuptitle)
    
#     plt.tight_layout()
#     plt.savefig(f'./images/truepred_{suptitle}.png', dpi=PRINTDPI)    