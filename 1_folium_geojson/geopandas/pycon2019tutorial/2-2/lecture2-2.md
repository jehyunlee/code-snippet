## 데이터 전처리
* 서울시 시군구 데이터의 새로운 컬럼에 스타벅스 개수 세어 저장하기


```python
# 라이브러리 import 
import geopandas as gpd
import pandas as pd
```


```python
# Nice representation of dataframe in markdown
import pandas as pd
import copy
from IPython.display import Markdown, display

def df2md(df, maxlen=20):
    _df = copy.deepcopy(df)
    
    for col in _df.columns:
        _df[col] = _df[col].astype('str')
        if (_df[col].str.len()> maxlen).any() :
            _df[col].loc[_df[col].str.len() > maxlen] = _df[col].str.slice(stop=maxlen) + ' ...'

    if '(index)' not in _df.columns:
        _df.insert(0, '(index)', df.index)
        
    fmt = ['---' for i in range(len(_df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=_df.columns)
    df_formatted = pd.concat([df_fmt, _df])
    display(Markdown(df_formatted.to_csv(sep="|", index=False)))
    _df.drop(columns='(index)', axis=1, inplace=True)
```


```python
# _01 파일 경로 서울시 시군구 통계, 서울시 스타벅스 매장 지도파일
_seoul_sgg = './maps/output/seoul_sgg.geojson'
_seoul_sb = './maps/final/seoul_starbucks.geojson'
```


```python
# _02 서울시 시군구 지도 데이터 불러오기
seoul_sgg_gdf = gpd.read_file(_seoul_sgg)
seoul_sgg_gdf.info()
df2md(seoul_sgg_gdf.head())
```

    <class 'geopandas.geodataframe.GeoDataFrame'>
    RangeIndex: 25 entries, 0 to 24
    Data columns (total 4 columns):
    SGG_CODE     25 non-null object
    SGG_NM       25 non-null object
    TOTAL_POP    25 non-null int64
    geometry     25 non-null object
    dtypes: int64(1), object(3)
    memory usage: 928.0+ bytes



(index)|SGG_CODE|SGG_NM|TOTAL_POP|geometry
---|---|---|---|---
0|11680|강남구|561052|POLYGON ((127.111035 ...
1|11740|강동구|440359|POLYGON ((127.145800 ...
2|11305|강북구|328002|POLYGON ((127.022029 ...
3|11500|강서구|608255|POLYGON ((126.883166 ...
4|11620|관악구|520929|POLYGON ((126.970490 ...




```python
# _03 서울시 스타벅스 매장 지도 데이터 불러오기
seoul_sb_gdf = gpd.read_file(_seoul_sb)
seoul_sb_gdf.info()
df2md(seoul_sb_gdf.head())
```

    <class 'geopandas.geodataframe.GeoDataFrame'>
    RangeIndex: 495 entries, 0 to 494
    Data columns (total 5 columns):
    STORE_NAME    495 non-null object
    STORE_TYPE    495 non-null object
    SIG_CD        495 non-null object
    SIG_KOR_NM    495 non-null object
    geometry      495 non-null object
    dtypes: object(5)
    memory usage: 19.5+ KB



(index)|STORE_NAME|STORE_TYPE|SIG_CD|SIG_KOR_NM|geometry
---|---|---|---|---|---
0|역삼아레나빌딩|general|11680|강남구|POINT (127.043069 37 ...
1|논현역사거리|general|11680|강남구|POINT (127.022223 37 ...
2|대치대원빌딩R|reserve|11680|강남구|POINT (127.062583 37 ...
3|삼성역섬유센터R|reserve|11680|강남구|POINT (127.060651 37 ...
4|압구정R|reserve|11680|강남구|POINT (127.033061 37 ...




```python
# _04 pandas를 이용해 서울시 시군구별 스타벅스 매장 개수 세기
starbucks_sgg_count = seoul_sb_gdf.pivot_table(
    index = 'SIG_CD', 
    values='SIG_KOR_NM', 
    aggfunc='count').rename(columns={'SIG_KOR_NM':'COUNT'})

df2md(starbucks_sgg_count.head())
```


(index)|COUNT
---|---
11110|37
11140|50
11170|17
11200|9
11215|14




```python
# _05 pandas merge를 이용해 서울시 시군구 데이터에 스타벅스 매장 개수 컬럼 병합하기
seoul_sgg_final = pd.merge(
  seoul_sgg_gdf,
  starbucks_sgg_count,
  how = 'left',
  left_on = 'SGG_CODE',
  right_on = 'SIG_CD'
)

df2md(seoul_sgg_final.head())
```


(index)|SGG_CODE|SGG_NM|TOTAL_POP|geometry|COUNT
---|---|---|---|---|---
0|11680|강남구|561052|POLYGON ((127.111035 ...|75
1|11740|강동구|440359|POLYGON ((127.145800 ...|13
2|11305|강북구|328002|POLYGON ((127.022029 ...|5
3|11500|강서구|608255|POLYGON ((126.883166 ...|14
4|11620|관악구|520929|POLYGON ((126.970490 ...|10




```python
type(seoul_sgg_final)
```




    geopandas.geodataframe.GeoDataFrame




```python
# _06 서울시 시군구별 통계 지도 데이터 저장하기
seoul_sgg_final.to_file('./maps/final/seoul_sgg_stat.geojson', driver='GeoJSON', encoding='utf-8')
```
