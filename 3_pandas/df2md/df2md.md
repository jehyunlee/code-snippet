
#### Visualization of pd.DataFrame as a Markdown format
* Useful to generate markdown document
* **[ NOTICE ]** the output of the function is strongly influenced by `markdown` characters, such as `|`, `*`, `~`. The output of the `df2md` should be used only for **visualization**, not as input to another function.  

```python
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
```

##### Example: `geodataframe` of `geopandas` 


```python
# Defulat max. length = 20
df2md(seoul_h_dong_gdf.head(10))  
```


(index)|SGG_NM|DONG_NM|SGG_CODE|H_CODE|SEDAE|SEDAE_INGU|TOTAL_POP|MALE_POP|FEMALE_POP|65_OVER|geometry
---|---|---|---|---|---|---|---|---|---|---|---
0|종로구|사직동|11110|1111000|4414|2.14|9717|4467|5250|1708|POLYGON ((126.976888 ...
1|종로구|삼청동|11110|1111000|1414|2.06|3097|1459|1638|634|POLYGON ((126.982689 ...
2|종로구|부암동|11110|1111000|4325|2.39|10726|5160|5566|1748|POLYGON ((126.975851 ...
3|종로구|평창동|11110|1111000|7510|2.53|19163|9032|10131|3037|POLYGON ((126.975074 ...
4|종로구|무악동|11110|1111000|3024|2.75|8375|3921|4454|1279|POLYGON ((126.960673 ...
5|종로구|교남동|11110|1111000|4379|2.34|10363|4850|5513|1406|POLYGON ((126.969048 ...
6|종로구|가회동|11110|1111000|2085|2.17|4657|2194|2463|900|POLYGON ((126.989135 ...
7|종로구|종로1.2.3.4가동|11110|1111000|5378|1.41|8592|5045|3547|1865|POLYGON ((126.996499 ...
8|종로구|종로5·6가동|11110|1111000|3174|1.69|5690|3096|2594|1089|POLYGON ((127.010160 ...
9|종로구|이화동|11110|1111000|4462|1.85|8752|4075|4677|1302|POLYGON ((127.007332 ...




```python
# For shorter max. length = 5
df2md(seoul_h_dong_gdf.head(10), maxlen=5)  
```


(index)|SGG_NM|DONG_NM|SGG_CODE|H_CODE|SEDAE|SEDAE_INGU|TOTAL_POP|MALE_POP|FEMALE_POP|65_OVER|geometry
---|---|---|---|---|---|---|---|---|---|---|---
0|종로구|사직동|11110|11110 ...|4414|2.14|9717|4467|5250|1708|POLYG ...
1|종로구|삼청동|11110|11110 ...|1414|2.06|3097|1459|1638|634|POLYG ...
2|종로구|부암동|11110|11110 ...|4325|2.39|10726|5160|5566|1748|POLYG ...
3|종로구|평창동|11110|11110 ...|7510|2.53|19163|9032|10131|3037|POLYG ...
4|종로구|무악동|11110|11110 ...|3024|2.75|8375|3921|4454|1279|POLYG ...
5|종로구|교남동|11110|11110 ...|4379|2.34|10363|4850|5513|1406|POLYG ...
6|종로구|가회동|11110|11110 ...|2085|2.17|4657|2194|2463|900|POLYG ...
7|종로구|종로1.2 ...|11110|11110 ...|5378|1.41|8592|5045|3547|1865|POLYG ...
8|종로구|종로5·6 ...|11110|11110 ...|3174|1.69|5690|3096|2594|1089|POLYG ...
9|종로구|이화동|11110|11110 ...|4462|1.85|8752|4075|4677|1302|POLYG ...



* Contrary: standard print() function


```python
print(seoul_h_dong_gdf.head(10))
```

      SGG_NM      DONG_NM SGG_CODE   H_CODE  SEDAE  SEDAE_INGU  TOTAL_POP  \
    0    종로구          사직동    11110  1111000   4414        2.14       9717   
    1    종로구          삼청동    11110  1111000   1414        2.06       3097   
    2    종로구          부암동    11110  1111000   4325        2.39      10726   
    3    종로구          평창동    11110  1111000   7510        2.53      19163   
    4    종로구          무악동    11110  1111000   3024        2.75       8375   
    5    종로구          교남동    11110  1111000   4379        2.34      10363   
    6    종로구          가회동    11110  1111000   2085        2.17       4657   
    7    종로구  종로1.2.3.4가동    11110  1111000   5378        1.41       8592   
    8    종로구      종로5·6가동    11110  1111000   3174        1.69       5690   
    9    종로구          이화동    11110  1111000   4462        1.85       8752   
    
       MALE_POP  FEMALE_POP  65_OVER  \
    0      4467        5250     1708   
    1      1459        1638      634   
    2      5160        5566     1748   
    3      9032       10131     3037   
    4      3921        4454     1279   
    5      4850        5513     1406   
    6      2194        2463      900   
    7      5045        3547     1865   
    8      3096        2594     1089   
    9      4075        4677     1302   
    
                                                geometry  
    0  POLYGON ((126.9768888427482 37.57565077944879,...  
    1  POLYGON ((126.982689386493 37.5950655194224, 1...  
    2  POLYGON ((126.9758511377569 37.59656422224408,...  
    3  POLYGON ((126.9750746678809 37.63138628651299,...  
    4  POLYGON ((126.960673532739 37.58079784202972, ...  
    5  POLYGON ((126.9690483700185 37.56819441770833,...  
    6  POLYGON ((126.9891359030894 37.59130668631862,...  
    7  POLYGON ((126.9964997845193 37.5810225677299, ...  
    8  POLYGON ((127.0101604483956 37.57156810157083,...  
    9  POLYGON ((127.0073325396313 37.58320333921623,...  

