### Function: plot_scatter
* Generate nrows x ncols scatter plots with linear regression + confidence interval.
* `sharey` : by default, it is assumed that all plots are sharing y axis, for example, correlation plot.

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec

cols = df.columns               # list of column names in pd.DataFrame df
cols_nm = np.array([ col_title_1,  col_title_2, col_title_3, ...  col_title_N ]) # list of column titles, corresponding to cols

def plot_scatter(ncols,         # number of columns
                 nrows,         # number of rows
                 df,            # pandas DataFrame name
                 cols_plot,     # No. of columns to plot
                 filename,      # image file name
                 graphsize=5    # frame size of a plot : figure size becomes (graphsize*ncols * graphsize*nrows)
                 ):
                 
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=(graphsize*ncols,graphsize*nrows),
                             sharey=True, 
                             gridspec_kw={'wspace':0.03, 'hspace':0.3})

    i = 0
    for row in range(nrows):
        for col in range(ncols):
            sns.regplot(x=cols[cols_plot[i]], y='shadow', data=df, 
                color='orange', ax=axes[row][col],
                scatter_kws={'alpha':0.1},
                line_kws={'linewidth':2, 'color':'blue'}, )
            axes[row][col].text(0.02, 0.98, '({})'.format(chr(ord('a')+i)), transform=axes[row][col].transAxes, fontsize=20, verticalalignment='top')
            axes[row][col].set_xlabel(cols_nm[cols_plot[i]])
            axes[row][col].set_ylabel('')
            axes[row][col].set_ylim(-0.05, 1.05)

            i += 1

    plt.tight_layout()
    plt.savefig('./images/corr_scatter_{}.png'.format(filename))
```
