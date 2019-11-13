import pegab
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import copy, time, os
from pegab import df2md

# >>>>> 1. Font Settings
# suptitle
fontsuptitle=mpl.font_manager.FontProperties()
fontsuptitle.set_weight('bold')
fontsuptitle.set_size(24)
# <<<<< 1. Font Settings

# >>>>> 2. Return Variable Name
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj][0]
# <<<<< 2. Return Variable Name

# >>>>> 3. Categorical Distribution
def plot_cat(df, col, col_target):
    grouped = pd.DataFrame(df.groupby(col).count().reset_index())

    plt.figure(figsize=(6,6))
    ax = sns.barplot(x=col, y=col_target, data=grouped)
    ax.set(title=labels_en[col])
    ax.set(xlabel=None)
    ax.set(ylabel=None)
    for i in ax.patches:
        ax.text(i.get_x()+i.get_width()/2, i.get_height()+2000, str(int(i.get_height())), ha='center', fontsize=13)

    plt.tight_layout()
    df_name = namestr(df, globals())
    if not os.path.isdir("./images"):
        os.mkdir("./images")

    plt.savefig('./images/distrib_cat_{}_{}.png'.format(df_name, labels_en[col]))
    
    return 0  
# <<<<< 3. Categorical Distribution

# >>>>> 4. Numerical Distribution
def dist_plot(df, xk, xv, text=False, maxbar=False):

    fig, ax = plt.subplots(figsize=(6, 6))
    f = sns.distplot(df[xk], kde=False, rug=False)
    df_name = namestr(df, globals())
    
    if xv == "건물 면적":
        f.set(yscale="log")

    mean_val = df[xk].mean()
    std_val = df[xk].std()
    max_val = df[xk].max()
    min_val = df[xk].min()

    print(
        "{}, {}: mean= {:.2f}, st.dev.= {:.2f}, min= {:.2f}, max= {:.2f}".format(
            df_name, xk, mean_val, std_val, min_val, max_val
        )
    )

    if text != False:
        fig.text(0.3, 0.8, "     mean : {:>3.02f}".format(mean_val), fontsize=16)
        fig.text(0.3, 0.75, "        std : {:>3.02f}".format(std_val), fontsize=16)
        fig.text(0.3, 0.7, "       max : {:>3.02f}".format(max_val), fontsize=16)
        fig.text(0.3, 0.65, "       min : {:>3.02f}".format(min_val), fontsize=16)

    # The most frequent bin
    heights = [h.get_height() for h in f.patches]
    index_max = np.argmax(heights)
    
    if maxbar != False:
        max_x = f.patches[index_max].get_x() + np.array(
            [0, f.patches[index_max].get_width() / 2]
        )
    
    if text != False:
        fig.text(
            0.3,
            0.6,
            "max bin : {:>.02f}~{:>.02f}".format(max_x[0], max_x[1]),
            fontsize=16,
            color="blue",
        )
        
    if maxbar != False:
        f.patches[index_max].set_color("blue")

    f.set(xlabel=xv)
    plt.tight_layout()
    
    if not os.path.isdir("./images"):
        os.mkdir("./images")

    f.figure.savefig("./images/distrib_num_{}_{}.png".format(df_name, xv))
    
    return 0


def dist_plots(dfs, xk, xv, label, norm_hist=True, kde=True, **kwargs):

    fig, ax = plt.subplots(figsize=(6, 6))
    
    for df in dfs:
        
        df_name = namestr(df, globals())[0]
        f = sns.distplot(df[xk], norm_hist=norm_hist, kde=kde, rug=False, label=label[df_name], **kwargs)

        if xv == "건물 면적":
            f.set(yscale="log")

        mean_val = df[xk].mean()
        std_val = df[xk].std()
        max_val = df[xk].max()
        min_val = df[xk].min()

        print(
            "{}: mean= {:.2f}, st.dev.= {:.2f}, min= {:.2f}, max= {:.2f}".format(
                xk, mean_val, std_val, min_val, max_val
            )
        )

    f.set(xlabel=xv)
    plt.tight_layout()
    plt.legend()
    if not os.path.isdir("./images"):
        os.mkdir("./images")
        
    f.figure.savefig("./images/distrib_nums_{}.png".format(xv))
    
    return 0
# <<<<< 4. Numerical Distribution
