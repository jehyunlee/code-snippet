# Code-Snippet for myself
This repository `code-snippet` is for frequently used code.  
Some of them are open-sourced, and some are self-written.
Below are the list of them with proper links.

1. geocoding with `folium`, `geopandas` and `geojson`  
1.1. interactive geocoding with `folium` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/190712_folium_geojson.md'>Link</a>]  
1.2. displaying data on map with administrative borders (on-going) [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/data_on_map/190914_DaejeonMap.ipynb'>Link</a>]  
1.3. tips of `geopandas` from Pycon 2019 tutorial [<a href='https://www.notion.so/rollinstar/Python-cc8a370daf784bf9b084ca06a37c5a1e'>Lecture Link</a>][<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md'>Note1</a>] 
    * Korean font problem : try another encoding [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-%ED%95%9C%EA%B8%80%EC%9D%B4-%EA%B9%A8%EC%A7%88-%EA%B2%BD%EC%9A%B0-gpdread_file%EC%9D%98-encoding-%EC%98%B5%EC%85%98-%EB%B3%80%EA%B2%BD'>Link</a>]
    * Reading `geometry` data as text [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-geometry%EC%9D%98-%ED%98%95%EC%83%81%EC%9D%B4-%EC%95%84%EB%8B%8C-%EA%B0%92%EC%9D%84-%ED%99%95%EC%9D%B8%ED%95%98%EA%B3%A0-%EC%8B%B6%EC%9C%BC%EB%A9%B4-%EB%B2%94%EC%9C%84%EB%A1%9C-%ED%98%B8%EC%B6%9C'>Link</a>]
    * About geocoding `coordination system`, `epsg` and `proj` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-%ED%95%9C%EA%B5%AD%EC%9D%98-%EC%A3%BC%EC%9A%94-%EC%A2%8C%ED%91%9C%EA%B3%84-%EB%B0%8F-proj4-%EC%9D%B8%EC%9E%90-%EC%A0%95%EB%A6%AC'>Link</a>]
    * Geometry file type selection by `driver` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-geodataframe-%EC%A0%80%EC%9E%A5-%ED%98%95%EC%8B%9D%EC%9D%84-%EB%B0%94%EA%BF%80-%EB%95%8C%EB%8A%94-driver-%EC%82%AC%EC%9A%A9'>Link</a>]  


  
2. data visualization with `matplotlib` and `seaborn`.  
2.1. Multiple graphs in a frame [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/wind_analysis/WindAnalysis.md'>Link</a>]  
2.2. Data distribution (bar plot) with text, for Categorical data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/distrib_map/distrib_map.md#22111-categorical-data'>Link</a>] and Numerical data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/distrib_map/distrib_map.md#22112-numerical-data'>Link</a>]  
2.3. Scatter plot on a Map [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/distrib_map/distrib_map.md#2212-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B3%B5%EA%B0%84-%EB%B6%84%ED%8F%AC-%EB%B6%84%EC%84%9D'>Link</a>]  
2.4. Colors and Colormaps [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/colors/colors_and_maps.md'>Link</a>]  
2.5. Add color function [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/add_color/add_color.md'>Link</a>]  
2.6. Violin plot with Raw data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/violin_raw/violin_raw.md#322-violin-plot-with-scatter--line-plot--raw-data'>Link</a>], subplot control with `gridspec` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/violin_raw/violin_raw.md#321-violin-plot-hysteresis-on-and-off'>Link</a>]  
  
3. data analysis with `pandas`.  
3.1. Nice representation of `pandas DataFrame` to `markdown` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/df2md/df2md.md'>Link</a>]  
3.2. Find address (raw and column) by value [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/find_address_by_value.md#find-address-column-row-by-value'>Link</a>]  
3.3. Create Timestamp from split data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/IEC61400.md#6-create-timestamp-from-split-data'>Link</a>]  
3.4. Find first data of each date [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/IEC61400.md#8-first-data-of-each-date'>Link</a>]

4. techniques of `numpy`.  
4.1. Numpy vectorization functions [<a href='https://github.com/jehyunlee/code-snippet/blob/master/4_numpy/vectorize.md'>Link</a>]  
4.2. numpy.vectorize() [<a href='https://github.com/jehyunlee/code-snippet/blob/master/4_numpy/numpy_vectorize.md'>Link</a>] and as decoration[<a href='https://github.com/jehyunlee/code-snippet/blob/master/4_numpy/numpy_vectorize.md#-numpyvectorize-as-decoration'>Link</a>]
