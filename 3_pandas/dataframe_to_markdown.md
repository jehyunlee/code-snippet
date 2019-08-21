##### Nice representation of DataFrame to markdown
* Function definition


```python
from IPython.display import Markdown, display

def df2md(df):    
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))
```

* Use Case


```python
import pandas as pd

df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
```


```python
df2md(df)
```


City|Country|Latitude|Longitude
---|---|---|---
Buenos Aires|Argentina|-34.58|-58.66
Brasilia|Brazil|-15.78|-47.91
Santiago|Chile|-33.45|-70.66
Bogota|Colombia|4.6|-74.08
Caracas|Venezuela|10.48|-66.86



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
    
