* Nice Representation of `pandas` `DataFrame` as `markdown`
```python
from IPython.display import Markdown, display

def df2md(df):    
    fmt = ['---' for i in range(len(df.columns))]  
    df_fmt = pd.DataFrame([fmt], columns=df.columns)  
    df_formatted = pd.concat([df_fmt, df])  
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))  
```
  
> Use Case  

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
