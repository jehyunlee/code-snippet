* Function Definition


```python
from IPython.display import Markdown, display

def df2md(df):
    if '<idx>' not in df.columns:
      df.insert(0, '(idx)', df.index)
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))
    df.drop(columns='(idx)', axis=1, inplace=True)
```

* Use Case


```python
import pandas as pd

df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})

df2md(df)
```


(idx)|City|Country|Latitude|Longitude
---|---|---|---|---
0|Buenos Aires|Argentina|-34.58|-58.66
1|Brasilia|Brazil|-15.78|-47.91
2|Santiago|Chile|-33.45|-70.66
3|Bogota|Colombia|4.6|-74.08
4|Caracas|Venezuela|10.48|-66.86



* Otherwise, if direct print() is converted to markdown,


```python
print(df)
```

               City    Country  Latitude  Longitude
    0  Buenos Aires  Argentina    -34.58     -58.66
    1      Brasilia     Brazil    -15.78     -47.91
    2      Santiago      Chile    -33.45     -70.66
    3        Bogota   Colombia      4.60     -74.08
    4       Caracas  Venezuela     10.48     -66.86
    
