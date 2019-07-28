

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
%matplotlib inline
```


```python
vCutIn = 3.5
vRated = 12
noutfile = 'output'
ninfile = 'measData_Hyosung_0118-0218.xls'

vMax = int(vRated + 4)
vMin = int(np.floor(vCutIn))
noutlog = noutfile + '.txt'
outlog = open(noutlog, 'w')
```


```python
data = pd.read_excel(ninfile)
data = data.iloc[:, :8]
data.head().style
```




<style  type="text/css" >
</style><table id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >month</th>        <th class="col_heading level0 col1" >day</th>        <th class="col_heading level0 col2" >hour</th>        <th class="col_heading level0 col3" >minute</th>        <th class="col_heading level0 col4" >windDirValidation</th>        <th class="col_heading level0 col5" >powerValidation</th>        <th class="col_heading level0 col6" >meanWindSpeed</th>        <th class="col_heading level0 col7" >meanWindSpeedTenMinutes</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col0" class="data row0 col0" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col1" class="data row0 col1" >18</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col2" class="data row0 col2" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col3" class="data row0 col3" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col4" class="data row0 col4" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col5" class="data row0 col5" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col6" class="data row0 col6" >10.3552</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row0_col7" class="data row0 col7" >9.09246</td>
            </tr>
            <tr>
                        <th id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col0" class="data row1 col0" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col1" class="data row1 col1" >18</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col2" class="data row1 col2" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col3" class="data row1 col3" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col4" class="data row1 col4" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col5" class="data row1 col5" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col6" class="data row1 col6" >9.32198</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row1_col7" class="data row1 col7" >9.09857</td>
            </tr>
            <tr>
                        <th id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col0" class="data row2 col0" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col1" class="data row2 col1" >18</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col2" class="data row2 col2" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col3" class="data row2 col3" >2</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col4" class="data row2 col4" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col5" class="data row2 col5" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col6" class="data row2 col6" >9.69929</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row2_col7" class="data row2 col7" >9.21075</td>
            </tr>
            <tr>
                        <th id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col0" class="data row3 col0" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col1" class="data row3 col1" >18</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col2" class="data row3 col2" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col3" class="data row3 col3" >3</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col4" class="data row3 col4" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col5" class="data row3 col5" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col6" class="data row3 col6" >8.50702</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row3_col7" class="data row3 col7" >9.23213</td>
            </tr>
            <tr>
                        <th id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col0" class="data row4 col0" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col1" class="data row4 col1" >18</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col2" class="data row4 col2" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col3" class="data row4 col3" >4</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col4" class="data row4 col4" >1</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col5" class="data row4 col5" >0</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col6" class="data row4 col6" >9.68915</td>
                        <td id="T_eb220622_afbd_11e9_8bd5_e470b83e82e8row4_col7" class="data row4 col7" >9.3297</td>
            </tr>
    </tbody></table>




```python
data.rename(columns={
                     'windDirValidation':'dir', 
                     'powerValidation':'pow', 
                     'meanWindSpeed':'mean1',
                     'meanWindSpeedTenMinutes':'mean10'
                      }, inplace=True)
data.head().style
```




<style  type="text/css" >
</style><table id="T_eb29a200_afbd_11e9_beec_e470b83e82e8" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >month</th>        <th class="col_heading level0 col1" >day</th>        <th class="col_heading level0 col2" >hour</th>        <th class="col_heading level0 col3" >minute</th>        <th class="col_heading level0 col4" >dir</th>        <th class="col_heading level0 col5" >pow</th>        <th class="col_heading level0 col6" >mean1</th>        <th class="col_heading level0 col7" >mean10</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_eb29a200_afbd_11e9_beec_e470b83e82e8level0_row0" class="row_heading level0 row0" >0</th>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col0" class="data row0 col0" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col1" class="data row0 col1" >18</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col2" class="data row0 col2" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col3" class="data row0 col3" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col4" class="data row0 col4" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col5" class="data row0 col5" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col6" class="data row0 col6" >10.3552</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row0_col7" class="data row0 col7" >9.09246</td>
            </tr>
            <tr>
                        <th id="T_eb29a200_afbd_11e9_beec_e470b83e82e8level0_row1" class="row_heading level0 row1" >1</th>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col0" class="data row1 col0" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col1" class="data row1 col1" >18</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col2" class="data row1 col2" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col3" class="data row1 col3" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col4" class="data row1 col4" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col5" class="data row1 col5" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col6" class="data row1 col6" >9.32198</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row1_col7" class="data row1 col7" >9.09857</td>
            </tr>
            <tr>
                        <th id="T_eb29a200_afbd_11e9_beec_e470b83e82e8level0_row2" class="row_heading level0 row2" >2</th>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col0" class="data row2 col0" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col1" class="data row2 col1" >18</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col2" class="data row2 col2" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col3" class="data row2 col3" >2</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col4" class="data row2 col4" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col5" class="data row2 col5" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col6" class="data row2 col6" >9.69929</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row2_col7" class="data row2 col7" >9.21075</td>
            </tr>
            <tr>
                        <th id="T_eb29a200_afbd_11e9_beec_e470b83e82e8level0_row3" class="row_heading level0 row3" >3</th>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col0" class="data row3 col0" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col1" class="data row3 col1" >18</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col2" class="data row3 col2" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col3" class="data row3 col3" >3</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col4" class="data row3 col4" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col5" class="data row3 col5" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col6" class="data row3 col6" >8.50702</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row3_col7" class="data row3 col7" >9.23213</td>
            </tr>
            <tr>
                        <th id="T_eb29a200_afbd_11e9_beec_e470b83e82e8level0_row4" class="row_heading level0 row4" >4</th>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col0" class="data row4 col0" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col1" class="data row4 col1" >18</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col2" class="data row4 col2" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col3" class="data row4 col3" >4</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col4" class="data row4 col4" >1</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col5" class="data row4 col5" >0</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col6" class="data row4 col6" >9.68915</td>
                        <td id="T_eb29a200_afbd_11e9_beec_e470b83e82e8row4_col7" class="data row4 col7" >9.3297</td>
            </tr>
    </tbody></table>




```python
data['indexMinutes']= data['minute'] + 60*data['hour'] + 1440*(data['day']-18) + 44640*(data['month']-1)
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>10.355214</td>
      <td>9.092462</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>9.321984</td>
      <td>9.098566</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>9.699292</td>
      <td>9.210747</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>8.507020</td>
      <td>9.232127</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>9.689152</td>
      <td>9.329701</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
for i in range(20100):
  if data['indexMinutes'].loc[i+1] - data['indexMinutes'].loc[i] > 1:
    print(data.loc[i-2:i+2])
```

          month  day  hour  minute  dir  pow      mean1     mean10  indexMinutes
    5407      1   21    18       7    1    0  12.878672  12.753364          5407
    5408      1   21    18       8    1    0  12.105328  12.730868          5408
    5409      1   21    18       9    1    0  12.642123  12.771113          5409
    5410      1   21    18      15    1    0  13.257978  12.790544          5415
    5411      1   21    18      16    1    0  13.186538  12.713785          5416
          month  day  hour  minute  dir  pow      mean1     mean10  indexMinutes
    5747      1   21    23      52    0    0  11.131661  11.907336          5752
    5748      1   21    23      53    0    0  11.685295  11.969218          5753
    5749      1   21    23      54    0    0  12.517311  11.904316          5754
    5750      1   22     0       0    0    0  11.481346  11.841086          5760
    5751      1   22     0       1    0    0  10.568442  12.006772          5761



```python
df1 = data.loc[:20000]
```


```python
%matplotlib inline
font_time = fm.FontProperties(size = 4)
fig  = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(3,1,1)

ax1.scatter(df1['indexMinutes'], df1['mean1'], 
           c=np.floor(df1['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
ax1.plot(df1['indexMinutes'], df1['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax1.set_xlim(df1['indexMinutes'].min(), df1['indexMinutes'].max())
```




    (0, 20010)




![png](output_7_1.png)



```python
df2 = df1.loc[df1['dir'] == 1]
```


```python
print(df2.shape)
df2.head()
```

    (11147, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>10.355214</td>
      <td>9.092462</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>9.321984</td>
      <td>9.098566</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>9.699292</td>
      <td>9.210747</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>8.507020</td>
      <td>9.232127</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>9.689152</td>
      <td>9.329701</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_miss = df1.loc[df1['dir'] == 0]
print(df2_miss.shape)
df2_miss.head(10)
```

    (8854, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>822</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>42</td>
      <td>0</td>
      <td>0</td>
      <td>5.200186</td>
      <td>5.522727</td>
      <td>822</td>
    </tr>
    <tr>
      <th>823</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>43</td>
      <td>0</td>
      <td>0</td>
      <td>6.000861</td>
      <td>5.568884</td>
      <td>823</td>
    </tr>
    <tr>
      <th>824</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>44</td>
      <td>0</td>
      <td>0</td>
      <td>5.941006</td>
      <td>5.485398</td>
      <td>824</td>
    </tr>
    <tr>
      <th>825</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>5.999678</td>
      <td>5.522969</td>
      <td>825</td>
    </tr>
    <tr>
      <th>826</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>46</td>
      <td>0</td>
      <td>0</td>
      <td>5.689354</td>
      <td>5.499900</td>
      <td>826</td>
    </tr>
    <tr>
      <th>827</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>47</td>
      <td>0</td>
      <td>0</td>
      <td>4.718054</td>
      <td>5.488752</td>
      <td>827</td>
    </tr>
    <tr>
      <th>828</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>4.823738</td>
      <td>5.612992</td>
      <td>828</td>
    </tr>
    <tr>
      <th>829</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>49</td>
      <td>0</td>
      <td>0</td>
      <td>5.630866</td>
      <td>5.659463</td>
      <td>829</td>
    </tr>
    <tr>
      <th>830</th>
      <td>1</td>
      <td>18</td>
      <td>13</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>5.533847</td>
      <td>5.626228</td>
      <td>830</td>
    </tr>
    <tr>
      <th>879</th>
      <td>1</td>
      <td>18</td>
      <td>14</td>
      <td>39</td>
      <td>0</td>
      <td>0</td>
      <td>5.887802</td>
      <td>6.172314</td>
      <td>879</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3 = df1.loc[df1['pow'] == 1]
print(df3.shape)
df3.head()
```

    (10420, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1013</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>53</td>
      <td>1</td>
      <td>1</td>
      <td>5.098772</td>
      <td>5.171323</td>
      <td>1013</td>
    </tr>
    <tr>
      <th>1014</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>54</td>
      <td>1</td>
      <td>1</td>
      <td>4.862361</td>
      <td>5.101587</td>
      <td>1014</td>
    </tr>
    <tr>
      <th>1015</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>55</td>
      <td>1</td>
      <td>1</td>
      <td>5.205256</td>
      <td>5.140628</td>
      <td>1015</td>
    </tr>
    <tr>
      <th>1016</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>56</td>
      <td>1</td>
      <td>1</td>
      <td>5.734953</td>
      <td>5.118339</td>
      <td>1016</td>
    </tr>
    <tr>
      <th>1017</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>57</td>
      <td>1</td>
      <td>1</td>
      <td>5.699771</td>
      <td>5.051515</td>
      <td>1017</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3_miss = df1.loc[df1['pow'] == 0]
print(df3_miss.shape)
df3_miss.head(10)
```

    (9581, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>10.355214</td>
      <td>9.092462</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>9.321984</td>
      <td>9.098566</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>9.699292</td>
      <td>9.210747</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>8.507020</td>
      <td>9.232127</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>9.689152</td>
      <td>9.329701</td>
      <td>4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>9.794867</td>
      <td>9.326783</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>8.924304</td>
      <td>9.329908</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>0</td>
      <td>9.512228</td>
      <td>9.292910</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>7.677831</td>
      <td>9.188567</td>
      <td>8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>7.442725</td>
      <td>9.314998</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4 = df1.loc[df1['mean10'] < 16].loc[df1['mean10'] >= 3.5]
print(df4.shape)
df4.head()
```

    (16209, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>10.355214</td>
      <td>9.092462</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>9.321984</td>
      <td>9.098566</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>9.699292</td>
      <td>9.210747</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>8.507020</td>
      <td>9.232127</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>18</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>0</td>
      <td>9.689152</td>
      <td>9.329701</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4_miss1 = df1.loc[df1['mean10'] < 3.5]
df4_miss2 = df1.loc[df1['mean10'] >= 16]
df4_miss = pd.concat([df4_miss1, df4_miss2])
print(df4_miss.shape)
df4_miss.head(10)
```

    (3792, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1123</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>43</td>
      <td>0</td>
      <td>0</td>
      <td>3.320098</td>
      <td>3.484611</td>
      <td>1123</td>
    </tr>
    <tr>
      <th>1124</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>44</td>
      <td>0</td>
      <td>0</td>
      <td>3.840377</td>
      <td>3.461828</td>
      <td>1124</td>
    </tr>
    <tr>
      <th>1125</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>45</td>
      <td>0</td>
      <td>0</td>
      <td>4.197129</td>
      <td>3.322789</td>
      <td>1125</td>
    </tr>
    <tr>
      <th>1126</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>46</td>
      <td>0</td>
      <td>0</td>
      <td>3.844018</td>
      <td>3.162602</td>
      <td>1126</td>
    </tr>
    <tr>
      <th>1127</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>47</td>
      <td>0</td>
      <td>0</td>
      <td>3.244971</td>
      <td>2.950882</td>
      <td>1127</td>
    </tr>
    <tr>
      <th>1128</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>3.624645</td>
      <td>2.777635</td>
      <td>1128</td>
    </tr>
    <tr>
      <th>1129</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>49</td>
      <td>0</td>
      <td>0</td>
      <td>3.563991</td>
      <td>2.697473</td>
      <td>1129</td>
    </tr>
    <tr>
      <th>1130</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>50</td>
      <td>0</td>
      <td>0</td>
      <td>3.376420</td>
      <td>2.669073</td>
      <td>1130</td>
    </tr>
    <tr>
      <th>1131</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>51</td>
      <td>0</td>
      <td>0</td>
      <td>2.915658</td>
      <td>2.737356</td>
      <td>1131</td>
    </tr>
    <tr>
      <th>1132</th>
      <td>1</td>
      <td>18</td>
      <td>18</td>
      <td>52</td>
      <td>0</td>
      <td>0</td>
      <td>2.918808</td>
      <td>2.971647</td>
      <td>1132</td>
    </tr>
  </tbody>
</table>
</div>




```python
df5 = df4.loc[df1['pow'] * df1['dir']== 1]
print(df5.shape)
df5.head()
```

    (5213, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>minute</th>
      <th>dir</th>
      <th>pow</th>
      <th>mean1</th>
      <th>mean10</th>
      <th>indexMinutes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1013</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>53</td>
      <td>1</td>
      <td>1</td>
      <td>5.098772</td>
      <td>5.171323</td>
      <td>1013</td>
    </tr>
    <tr>
      <th>1014</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>54</td>
      <td>1</td>
      <td>1</td>
      <td>4.862361</td>
      <td>5.101587</td>
      <td>1014</td>
    </tr>
    <tr>
      <th>1015</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>55</td>
      <td>1</td>
      <td>1</td>
      <td>5.205256</td>
      <td>5.140628</td>
      <td>1015</td>
    </tr>
    <tr>
      <th>1016</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>56</td>
      <td>1</td>
      <td>1</td>
      <td>5.734953</td>
      <td>5.118339</td>
      <td>1016</td>
    </tr>
    <tr>
      <th>1017</th>
      <td>1</td>
      <td>18</td>
      <td>16</td>
      <td>57</td>
      <td>1</td>
      <td>1</td>
      <td>5.699771</td>
      <td>5.051515</td>
      <td>1017</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.loc[20000]
```




    month               1.000000
    day                31.000000
    hour               21.000000
    minute             30.000000
    dir                 1.000000
    pow                 1.000000
    mean1              17.986673
    mean10             17.504355
    indexMinutes    20010.000000
    Name: 20000, dtype: float64




```python
%matplotlib inline

fig  = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(5,1,1)

ax1.scatter(df1['indexMinutes'], df1['mean1'], 
           c=np.floor(df1['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
ax1.plot(df1['indexMinutes'], df1['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax1.set_xlim(df1['indexMinutes'].min(), 12500)
ax1.set_ylim(-3, df1['mean1'].max()*1.1)
ax1.set_xticks([])


ax2 =fig.add_subplot(5,1,2)

ax2.scatter(df2['indexMinutes'], df2['mean1'], 
           c=np.floor(df2['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
#ax2.bar(df2_miss['indexMinutes'], [10]*df2_miss.shape[0], width=0.01, color='red', linewidth=None, zorder=0, alpha=0.1)
ax2.plot(df2['indexMinutes'], df2['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax2.set_xlim(df1['indexMinutes'].min(), 12500)
ax2.set_ylim(-3, df1['mean1'].max()*1.1)
ax2.set_xticks([])

ax3 =fig.add_subplot(5,1,3)

ax3.scatter(df3['indexMinutes'], df3['mean1'], 
           c=np.floor(df3['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
ax3.plot(df3['indexMinutes'], df3['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax3.set_xlim(df1['indexMinutes'].min(), 12500)
ax3.set_ylim(-3, df1['mean1'].max()*1.1)
ax3.set_xticks([])

ax4 =fig.add_subplot(5,1,4)

ax4.scatter(df4['indexMinutes'], df4['mean1'], 
           c=np.floor(df4['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
ax4.plot(df4['indexMinutes'], df4['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax4.set_xlim(df1['indexMinutes'].min(), 12500)
ax4.set_ylim(-3, df1['mean1'].max()*1.1)
ax4.set_xticks([])

ax5 =fig.add_subplot(5,1,5)

ax5.scatter(df5['indexMinutes'], df5['mean1'], 
           c=np.floor(df5['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
ax5.plot(df5['indexMinutes'], df5['mean10'], linewidth=2, color='lightgrey',zorder=0)
ax5.set_xlim(df1['indexMinutes'].min(), 12500)
ax5.set_ylim(-3, df1['mean1'].max()*1.1)

boxprops = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)
boxprops_e = dict(boxstyle='round', facecolor='lightyellow', alpha=0.5)
ax1.text(0.02, 0.9, '(a) as is', transform=ax1.transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
ax2.text(0.02, 0.9, '(b) filtered : direction', transform=ax2.transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
ax3.text(0.02, 0.9, '(c) filtered : power', transform=ax3.transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
ax4.text(0.02, 0.9, '(d) filtered : wind speed', transform=ax4.transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
ax5.text(0.02, 0.9, '(e) filtered : direction, power and wind speed', transform=ax5.transAxes, fontsize=14, verticalalignment='top', bbox=boxprops_e)

ax1.tick_params(axis='y', labelsize=15)
ax2.tick_params(axis='y', labelsize=15)
ax3.tick_params(axis='y', labelsize=15)
ax4.tick_params(axis='y', labelsize=15)
ax5.tick_params(axis='y', labelsize=15)
ax5.tick_params(axis='x', labelsize=15)
ax5.set_xlabel('Time (minutes since 18. Jan. 00:00)', labelpad = 20, fontsize=20)

plt.subplots_adjust(hspace=0, left=0.05, right=0.95, top=0.99, bottom=0.12)
# plt.tight_layout()
plt.savefig('wind.png', dpi=200)
plt.show()
```


![png](output_17_0.png)



```python
%matplotlib inline

fig, axes = plt.subplots(figsize=(10, 10), nrows=5, ncols=1, sharex=True)

axes[0].scatter(df1['indexMinutes'], df1['mean1'], 
           c=np.floor(df1['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
axes[0].plot(df1['indexMinutes'], df1['mean10'], linewidth=2, color='lightgrey',zorder=0)
axes[0].set_xlim(df1['indexMinutes'].min(), 12500)
axes[0].set_ylim(-3, df1['mean1'].max()*1.1)


axes[1].scatter(df2['indexMinutes'], df2['mean1'], 
           c=np.floor(df2['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
axes[1].plot(df2['indexMinutes'], df2['mean10'], linewidth=2, color='lightgrey',zorder=0)
axes[1].set_ylim(-3, df1['mean1'].max()*1.1)

axes[2].scatter(df3['indexMinutes'], df3['mean1'], 
           c=np.floor(df3['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
axes[2].plot(df3['indexMinutes'], df3['mean10'], linewidth=2, color='lightgrey',zorder=0)
axes[2].set_ylim(-3, df1['mean1'].max()*1.1)

axes[3].scatter(df4['indexMinutes'], df4['mean1'], 
           c=np.floor(df4['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
axes[3].plot(df4['indexMinutes'], df4['mean10'], linewidth=2, color='lightgrey',zorder=0)
axes[3].set_ylim(-3, df1['mean1'].max()*1.1)

axes[4].scatter(df5['indexMinutes'], df5['mean1'], 
           c=np.floor(df5['mean1']), 
           cmap='jet',
           linewidth=0.1, s=3, edgecolor='k',
           vmin=vCutIn, vmax=vMax, 
           zorder=1)
axes[4].plot(df5['indexMinutes'], df5['mean10'], linewidth=2, color='lightgrey',zorder=0)
axes[4].set_ylim(-3, df1['mean1'].max()*1.1)

boxprops = dict(boxstyle='round', facecolor='lightgrey', alpha=0.5)
boxprops_e = dict(boxstyle='round', facecolor='lightyellow', alpha=0.5)
axes[0].text(0.02, 0.9, '(a) as is', transform=axes[0].transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
axes[1].text(0.02, 0.9, '(b) filtered : direction', transform=axes[1].transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
axes[2].text(0.02, 0.9, '(c) filtered : power', transform=axes[2].transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
axes[3].text(0.02, 0.9, '(d) filtered : wind speed', transform=axes[3].transAxes, fontsize=14, verticalalignment='top', bbox=boxprops)
axes[4].text(0.02, 0.9, '(e) filtered : direction, power and wind speed', transform=axes[4].transAxes, fontsize=14, verticalalignment='top', bbox=boxprops_e)

axes[0].tick_params(axis='y', labelsize=15)
axes[1].tick_params(axis='y', labelsize=15)
axes[2].tick_params(axis='y', labelsize=15)
axes[3].tick_params(axis='y', labelsize=15)
axes[4].tick_params(axis='y', labelsize=15)
axes[4].tick_params(axis='x', labelsize=15)
axes[4].set_xlabel('Time (minutes since 18. Jan. 00:00)', labelpad = 20, fontsize=20)

plt.subplots_adjust(hspace=0, left=0.05, right=0.95, top=0.99, bottom=0.12)
plt.savefig('winds.png', dpi=200)
plt.show()
```


![png](output_18_0.png)



```python
no1 = data.index.size
print('(a) # of all data={}'.format(no1))

data2 = data.loc[data['dir'] == 1]
no2 = data2.index.size
print('(b) # of dir filtered ={}'.format(no2))

data3 = data.loc[data['pow'] == 1]
no3 = data3.index.size
print('(c) # of pow filtered ={}'.format(no3))

data4 = data.loc[data['mean10'] < 16].loc[data['mean10'] >= 3.5]
no4 = data4.index.size
print('(d) # of wind speed filtered ={}'.format(no4))

data5 = data4.loc[data['dir'] * data['pow'] == 1]
no5 = data5.index.size
print('(e) # of direction, power and wind speed filtered ={}'.format(no5))
```

    (a) # of all data=46021
    (b) # of dir filtered =27116
    (c) # of pow filtered =24619
    (d) # of wind speed filtered =36568
    (e) # of direction, power and wind speed filtered =14739



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
  ax.text(pos[i], Y[i]+1000, '    {:>.0f}%'.format(Yp[i]), fontsize=18, color='blue')
  
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.set_ylim(0, 50000)
ax.set_xlabel('Data Filtering', labelpad = 20, fontsize=20)

plt.tight_layout()
plt.savefig('num_data.png', dpi=200)
```

    [-0.4, 0.6, 1.6, 2.6, 3.6]
    [0.8, 0.8, 0.8, 0.8, 0.8]



![png](output_20_1.png)

