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
<br>  

### Usage  
```python
cols = dfc.columns
cols_nm = np.array(['건물 층 수', 'x좌표(m)', 'y좌표(m)', '경도', '위도',\
           '건물 면적', '건물 표고', '일사량 손실률', '절대 높이', '음영원 수', \
           '음영원 총 면적', '음영원 평균 면적', '음영원 최대 앙각', '음영원 x좌표 분산', '음영원 y좌표 분산', \
           '건물 반경', '인접건물 수', '인접건물 총 면적', '인접건물 평균 면적', '인접건물 x좌표 분산', \
           '인접건물 y좌표 분산', '인접건물 절대 높이 분산', '인접건물 상대 높이 분산', '인접건물 최대 상대높이', '인접건물 앙각 분산', \
           '인접건물 최대 앙각', '인접건물 넓이반영 앙각 분산', '인접건물 넓이반영 최대앙각', '음영원 앙각 분산', '음영원 넓이반영 앙각 분산', \
           '음영원 넓이반영 최대 앙각'])


ncols = 4
nrows = 3
cols_plot = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
filename = 'corr_scatter_nb'

plot_scatter(ncols, nrows, dfc, cols_plot, filename)
``````  

![png](https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/plot_scatter/images/output_44_1.png)                 
