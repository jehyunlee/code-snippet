
### **Multiple Plots in a Figure, using `Matplotlib`**  
* Simple example : time vs wind speed

#### **1.Load important libraries**


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from IPython.display import display, HTML
%matplotlib inline
```

* Nice representation of `dataframe` as table on `markdown`


```python
from IPython.display import Markdown, display

def df2md(df):    
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))
```

#### **2.Set variables**


```python
vCutIn = 4
vRated = 12
noutfile = 'output'
ninfile = 'measData_Hyosung_0118-0218.xls'

vMax = int(vRated + 4)
vMin = int(np.floor(vCutIn))
noutlog = noutfile + '.txt'
outlog = open(noutlog, 'w')
```

#### **3.1. Glancing on data**


```python
data = pd.read_excel(ninfile)
data = data.iloc[:, :8]
df2md(data.head())
```


month|day|hour|minute|windDirValidation|powerValidation|meanWindSpeed|meanWindSpeedTenMinutes
---|---|---|---|---|---|---|---
1|18|0|0|1|0|10.355213963333378|9.092461652000043
1|18|0|1|1|0|9.321983706666611|9.098565504333349
1|18|0|2|1|0|9.699291810000195|9.210747028000025
1|18|0|3|1|0|8.507020326666794|9.232126642666683
1|18|0|4|1|0|9.689152010000056|9.329700709



#### **3.2. Shortening Column names, for ease**


```python
data.rename(columns={
                     'windDirValidation':'dir', 
                     'powerValidation':'pow', 
                     'meanWindSpeed':'mean1',
                     'meanWindSpeedTenMinutes':'mean10'
                      }, inplace=True)
df2md(data.head())
```


month|day|hour|minute|dir|pow|mean1|mean10
---|---|---|---|---|---|---|---
1|18|0|0|1|0|10.355213963333378|9.092461652000043
1|18|0|1|1|0|9.321983706666611|9.098565504333349
1|18|0|2|1|0|9.699291810000195|9.210747028000025
1|18|0|3|1|0|8.507020326666794|9.232126642666683
1|18|0|4|1|0|9.689152010000056|9.329700709



#### **3.3. Adding a 'standard' Timestamp : 'indexMinutes'**


```python
data['indexMinutes']= data['minute'] + 60*data['hour'] + 1440*(data['day']-18) + 44640*(data['month']-1)
df2md(data.head())
```


month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|0|0|1|0|10.355213963333378|9.092461652000043|0
1|18|0|1|1|0|9.321983706666611|9.098565504333349|1
1|18|0|2|1|0|9.699291810000195|9.210747028000025|2
1|18|0|3|1|0|8.507020326666794|9.232126642666683|3
1|18|0|4|1|0|9.689152010000056|9.329700709|4



**3.3.1 Check : "Is the indexMinutes formular working properly?"**


```python
print(data['indexMinutes'].max())
print(data.index.size)
```

    46070
    46021


* **maximum value of `indexMunutes` and data size does not match!**

**3.3.2. Further Check: "Is there missing data which results in larger `indexMinutes`?"**


```python
for i in range(20100):
  if data['indexMinutes'].loc[i+1] - data['indexMinutes'].loc[i] > 1:
    df2md(data.loc[i-2:i+2])
```


month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|21|18|7|1|0|12.878672190000099|12.753364234333343|5407
1|21|18|8|1|0|12.105328079999992|12.730867705333342|5408
1|21|18|9|1|0|12.642122946666376|12.771113493333349|5409
1|21|18|15|1|0|13.257977526666936|12.790543501000064|5415
1|21|18|16|1|0|13.186538026666689|12.713785215000017|5416




month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|21|23|52|0|0|11.131661466666994|11.907336194333306|5752
1|21|23|53|0|0|11.685294546666684|11.96921816466661|5753
1|21|23|54|0|0|12.517311226666333|11.904315762999953|5754
1|22|0|0|0|0|11.481346296666917|11.841086428333323|5760
1|22|0|1|0|0|10.56844166666666|12.006772296666625|5761



Proven to be TRUE.  
Keep going.

#### **3.4. Slicing Dataset, for Visualization Efficiency**


```python
df1 = data.loc[:32000]
```

**3.4.1. Check Plot Feasibility**


```python
%matplotlib inline
font_time = fm.FontProperties(size = 4)
fig  = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1,1,1)

ax1.scatter(df1['indexMinutes'], df1['mean1'], 
           c=np.floor(df1['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
ax1.plot(df1['indexMinutes'], df1['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax1.set_xlim(df1['indexMinutes'].min(), df1['indexMinutes'].max())
```




    (0, 32020)




![png](./images/data.png)


**3.4.2. Plot Preparation One by One**  
  
3.4.2.1. Filter by `Wind Direction`


```python
df2 = df1.loc[df1['dir'] == 1]
```


```python
print(df2.shape)
df2md(df2.head())
```

    (17116, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|0|0|1|0|10.355213963333378|9.092461652000043|0
1|18|0|1|1|0|9.321983706666611|9.098565504333349|1
1|18|0|2|1|0|9.699291810000195|9.210747028000025|2
1|18|0|3|1|0|8.507020326666794|9.232126642666683|3
1|18|0|4|1|0|9.689152010000056|9.329700709|4



* Missing data by `Wind Direction`


```python
df2_miss = df1.loc[df1['dir'] == 0]
print(df2_miss.shape)
df2md(df2_miss.head(10))
```

    (14885, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|13|42|0|0|5.200185733333339|5.522726625999989|822
1|18|13|43|0|0|6.000861213333301|5.568884224666662|823
1|18|13|44|0|0|5.941005666666772|5.485398335000005|824
1|18|13|45|0|0|5.999678236666705|5.522969366666663|825
1|18|13|46|0|0|5.689354266666526|5.499899785333338|826
1|18|13|47|0|0|4.718053606666666|5.488752150666675|827
1|18|13|48|0|0|4.823737976666672|5.612992354666669|828
1|18|13|49|0|0|5.630866056666617|5.659463365333331|829
1|18|13|50|0|0|5.533846606666677|5.626227866333335|830
1|18|14|39|0|0|5.887802443333319|6.172314476999999|879



3.4.2.2. Filter by `Power Generation`


```python
df3 = df1.loc[df1['pow'] == 1]
print(df3.shape)
df2md(df3.head())
```

    (15865, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|16|53|1|1|5.098772369999969|5.1713226389999845|1013
1|18|16|54|1|1|4.862361396666568|5.1015869326666605|1014
1|18|16|55|1|1|5.205255633333375|5.140628235333339|1015
1|18|16|56|1|1|5.734952640000007|5.118339111333343|1016
1|18|16|57|1|1|5.699770606666643|5.051514756666676|1017



* Missing data by `Power Generation`


```python
df3_miss = df1.loc[df1['pow'] == 0]
print(df3_miss.shape)
df2md(df3_miss.head(10))
```

    (16136, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|0|0|1|0|10.355213963333378|9.092461652000043|0
1|18|0|1|1|0|9.321983706666611|9.098565504333349|1
1|18|0|2|1|0|9.699291810000195|9.210747028000025|2
1|18|0|3|1|0|8.507020326666794|9.232126642666683|3
1|18|0|4|1|0|9.689152010000056|9.329700709|4
1|18|0|5|1|0|9.794867106666851|9.326783211999977|5
1|18|0|6|1|0|8.924303823333334|9.32990811399996|6
1|18|0|7|1|0|9.51222786333323|9.292910134666627|7
1|18|0|8|1|0|7.6778305000000024|9.188566983666604|8
1|18|0|9|1|0|7.442725409999975|9.314997998999932|9



3.4.2.3. Filter by `Wind Speed`


```python
df4 = df1.loc[df1['mean10'] < vMax].loc[df1['mean10'] >= vCutIn]
print(df4.shape)
df2md(df4.head())
```

    (23953, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|0|0|1|0|10.355213963333378|9.092461652000043|0
1|18|0|1|1|0|9.321983706666611|9.098565504333349|1
1|18|0|2|1|0|9.699291810000195|9.210747028000025|2
1|18|0|3|1|0|8.507020326666794|9.232126642666683|3
1|18|0|4|1|0|9.689152010000056|9.329700709|4



* Missing data by `Wind Speed`


```python
df4_miss1 = df1.loc[df1['mean10'] < vCutIn]
df4_miss2 = df1.loc[df1['mean10'] >= vMax]
df4_miss = pd.concat([df4_miss1, df4_miss2])
print(df4_miss.shape)
df2md(df4_miss.head(10))
```

    (8048, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|10|22|1|0|4.36961320666667|3.973335995666681|622
1|18|10|36|1|0|4.35885887333337|3.9939044263333314|636
1|18|10|37|1|0|3.8495950999999495|3.9441425896666615|637
1|18|10|38|1|0|4.171579839999957|3.9684074383333297|638
1|18|10|39|1|0|3.344771330000074|3.8649753329999994|639
1|18|10|40|1|0|3.3566779133333613|3.86031563399999|640
1|18|10|41|1|0|5.39895654000006|3.829174157333315|641
1|18|10|42|1|0|3.8025525733333168|3.607032647999973|642
1|18|10|43|1|0|4.15219131333326|3.6238309166666376|643
1|18|10|44|1|0|3.7094200466666916|3.6095184353333094|644



3.4.2.4. Filter by `Wind Direction, Power and Speed`


```python
df5 = df4.loc[df1['pow'] * df1['dir']== 1]
print(df5.shape)
df2md(df5.head())
```

    (8295, 9)



month|day|hour|minute|dir|pow|mean1|mean10|indexMinutes
---|---|---|---|---|---|---|---|---
1|18|16|53|1|1|5.098772369999969|5.1713226389999845|1013
1|18|16|54|1|1|4.862361396666568|5.1015869326666605|1014
1|18|16|55|1|1|5.205255633333375|5.140628235333339|1015
1|18|16|56|1|1|5.734952640000007|5.118339111333343|1016
1|18|16|57|1|1|5.699770606666643|5.051514756666676|1017



**3.4.3. Plot Wind Speed**  


```python
%matplotlib inline

fig, axes = plt.subplots(figsize=(10, 10), nrows=5, ncols=1, sharex=True)

texts = [
        '(a) as is',
        '(b) filtered : direction',
        '(c) filtered : power',
        '(d) filtered : wind speed',
        '(e) filtered : direction, power and wind speed'
        ]

def windplot(df,    # pandas DataFrame
             ax     # axes number
             ):
        axes[ax].scatter(df['indexMinutes'], df['mean1'], 
                         c=np.floor(df['mean1']), 
                         cmap='jet',
                         linewidth=0.1, s=3, edgecolor='k',
                         vmin=vCutIn, vmax=vMax, 
                         zorder=1)
        axes[ax].plot(df['indexMinutes'], df['mean10'], linewidth=2, color='lightgrey',zorder=0)
        axes[ax].set_xlim(0, 32000)
        axes[ax].set_ylim(0, 25)
        axes[ax].tick_params(axis='y', labelsize=15)
        
        boxcolor = 'lightgrey' if ax < 4 else 'lightyellow'
        boxprops = dict(boxstyle='round', facecolor=boxcolor, alpha=0.5)
        axes[ax].text(0.02, 0.9, texts[ax], transform=axes[ax].transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)

for i in range(5):
    windplot(eval('df' + str(i+1)), i)

axes[4].tick_params(axis='x', labelsize=15)                                       
axes[4].set_xlabel('Time (minutes since 18. Jan. 00:00)', labelpad = 20, fontsize=20)

plt.subplots_adjust(hspace=0, left=0.05, right=0.95, top=0.99, bottom=0.12)
plt.savefig('winds.png', dpi=200)
plt.show()
```


![png](./images/winds.png)


#### **3.5. Analysis : Data Loss by Filtering**


```python
print(vCutIn, vMax)
```

    4 16



```python
no1 = data.index.size
print('(a) # of all data= {}'.format(no1))

data2 = data.loc[data['dir'] == 1]
no2 = data2.index.size
print('(b) # of dir filtered = {}'.format(no2))

data3 = data.loc[data['pow'] == 1]
no3 = data3.index.size
print('(c) # of pow filtered = {}'.format(no3))

data4 = data.loc[data['mean10'] < vMax].loc[data['mean10'] >= vCutIn]
no4 = data4.index.size
print('(d) # of wind speed filtered = {}'.format(no4))

data5 = data4.loc[data4['dir'] * data4['pow'] == 1]
no5 = data5.index.size
print('(e) # of direction, power and wind speed filtered = {}'.format(no5))
```

    (a) # of all data= 46021
    (b) # of dir filtered = 27116
    (c) # of pow filtered = 24619
    (d) # of wind speed filtered = 35066
    (e) # of direction, power and wind speed filtered = 14564


**3.5.2. Plot Bar Graph with Proportions**


```python
X = ['(a)', '(b)', '(c)', '(d)', '(e)']
Y = [no1, no2, no3, no4, no5]
Yp = np.array(Y)/no1 * 100

fig, ax = plt.subplots(figsize=(10, 10))
f = ax.bar(X, Y, color='lightgrey', edgecolor='black')

pos = [h.get_x() for h in f.patches]
ws = [h.get_width() for h in f.patches]

print(pos)
print(ws)

for i in range(len(Yp)):
  ax.text(pos[i]+ws[i]/2, Y[i]+1000, '{:>.0f}%'.format(Yp[i]), fontsize=18, color='blue', ha='center')
  
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.set_ylim(0, 50000)
ax.set_xlabel('Data Filtering', labelpad = 20, fontsize=20)

plt.tight_layout()
plt.savefig('num_data.png', dpi=200)
```

    [-0.4, 0.6, 1.6, 2.6, 3.6]
    [0.8, 0.8, 0.8, 0.8, 0.8]



![png](./images/num_data.png)

