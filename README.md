# Code-Snippet for myself
This repository `code-snippet` is for frequently used code.  
Some of them are open-sourced, and some are self-written.
Below are the list of them with proper links.


0. Work-snippet, a subset of `Code-snippet`  
  0.0. Readme [[Link](https://github.com/jehyunlee/code-snippet/blob/master/0_work-snippet/Readme.md)]    
  0.1. `base` : Korean Font + Figure Style + df2md() [[Download](https://github.com/jehyunlee/code-snippet/blob/master/0_work-snippet/pegab/pegab.py)]  


1. `bash` shell script  
  1.1. basic syntax of `bash` shell  [[Link](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter04)]    
  1.2. copy and run multiple shells using `nohup` [[Link](https://github.com/jehyunlee/code-snippet/blob/master/bash/copy_and_run.md)] 
  
2. geocoding with `folium`, `geopandas` and `geojson`  
  2.1. interactive geocoding with `folium` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/190712_folium_geojson.md'>Link</a>]  
  2.2. displaying data on map with administrative borders[<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/data_on_map/190914_DaejeonMap.md'>Link</a>]  
    * html2png [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/data_on_map/190914_DaejeonMap.md#12-function-capture-html-to-png'>Link</a>]   
    * read JSON from web [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/data_on_map/190914_DaejeonMap.md#221-function--load-json-from-web'>Link</a>]  
    * data validation (duplicated & missing ones) [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/data_on_map/190914_DaejeonMap.md#223-data-validataion'>Link</a>]  
    * map + admin. districts + data visualization with legend as independent `png` file [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/data_on_map/190914_DaejeonMap.md#33-function--map--admistrative-districts--data--customized-colormap'>Link</a>]     

    2.3. tips of `geopandas` from Pycon 2019 tutorial [<a href='https://www.notion.so/rollinstar/Python-cc8a370daf784bf9b084ca06a37c5a1e'>Lecture Link</a>][<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md'>1</a>][<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/2-1/lecture2-1.md'>2-1</a>][<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/2-2/lecture2-2.md'>2-2</a>]  
    * Korean font problem : try another encoding [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-%ED%95%9C%EA%B8%80%EC%9D%B4-%EA%B9%A8%EC%A7%88-%EA%B2%BD%EC%9A%B0-gpdread_file%EC%9D%98-encoding-%EC%98%B5%EC%85%98-%EB%B3%80%EA%B2%BD'>Link</a>]
    * Reading `geometry` data as text [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-geometry%EC%9D%98-%ED%98%95%EC%83%81%EC%9D%B4-%EC%95%84%EB%8B%8C-%EA%B0%92%EC%9D%84-%ED%99%95%EC%9D%B8%ED%95%98%EA%B3%A0-%EC%8B%B6%EC%9C%BC%EB%A9%B4-%EB%B2%94%EC%9C%84%EB%A1%9C-%ED%98%B8%EC%B6%9C'>Link</a>]
    * About geocoding `coordination system`, `epsg` and `proj` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-%ED%95%9C%EA%B5%AD%EC%9D%98-%EC%A3%BC%EC%9A%94-%EC%A2%8C%ED%91%9C%EA%B3%84-%EB%B0%8F-proj4-%EC%9D%B8%EC%9E%90-%EC%A0%95%EB%A6%AC'>Link</a>]
    * Geometry file type selection by `driver` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/1/lecture1.md#tip-geodataframe-%EC%A0%80%EC%9E%A5-%ED%98%95%EC%8B%9D%EC%9D%84-%EB%B0%94%EA%BF%80-%EB%95%8C%EB%8A%94-driver-%EC%82%AC%EC%9A%A9'>Link</a>]  
    * `dissolve`, agglomerating districts [[Link](https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/2-1/lecture2-1.md#dissolve%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-%ED%96%89%EC%A0%95%EB%8F%99---%EC%8B%9C%EA%B5%B0%EA%B5%AC-%EC%A7%80%EB%8F%84-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0)]  
    * `pd.merge`, map + data [[Link](https://github.com/jehyunlee/code-snippet/blob/master/1_folium_geojson/geopandas/pycon2019tutorial/2-2/lecture2-2.md)]



  
3. data visualization with `matplotlib` and `seaborn`.  
3.1. Multiple graphs in a frame [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/wind_analysis/WindAnalysis.md'>Link</a>]  
3.2. Data distribution (bar plot) with text, for Categorical data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/distrib_map/distrib_map.md#22111-categorical-data'>Link</a>] and Numerical data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/distrib_map/distrib_map.md#22112-numerical-data'>Link</a>]  
3.3. Scatter plot on a Map [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/distrib_map/distrib_map.md#2212-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B3%B5%EA%B0%84-%EB%B6%84%ED%8F%AC-%EB%B6%84%EC%84%9D'>Link</a>]  
3.4. Colors and Colormaps [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/colors/colors_and_maps.md'>Link</a>]  
3.5. Add color function [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/add_color/add_color.md'>Link</a>]  
3.6. Violin plot with Raw data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/violin_raw/violin_raw.md#322-violin-plot-with-scatter--line-plot--raw-data'>Link</a>], subplot control with `gridspec` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/violin_raw/violin_raw.md#321-violin-plot-hysteresis-on-and-off'>Link</a>]  
3.7. 3D Rotation animation, using `ax.view_init` and `ffmpeg` [[Link](https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/ani_rotation/ani_rotation.md)]  
3.8. `Stacked Bar` plot with relative values [[Link](https://github.com/jehyunlee/code-snippet/blob/master/2_matplotlib/stacked_bar/summary.md)]
  
4. data analysis with `pandas`.  
4.1. Nice representation of `pandas DataFrame` to `markdown` [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/df2md/df2md.md'>Link</a>]  
4.2. Find address (raw and column) by value [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/find_address_by_value.md#find-address-column-row-by-value'>Link</a>]  
4.3. Create Timestamp from split data [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/IEC61400.md#6-create-timestamp-from-split-data'>Link</a>]  
4.4. Find first data of each date [<a href='https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/IEC61400.md#8-first-data-of-each-date'>Link</a>]  
4.5. Retrieving the name of a variable [[Link](https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/varname.md)]  
4.6. Creating unicode dictionary [[Link](https://github.com/jehyunlee/code-snippet/blob/master/3_pandas/unicode_json.py)]

5. techniques of `numpy`.  
5.1. Numpy vectorization functions [<a href='https://github.com/jehyunlee/code-snippet/blob/master/4_numpy/vectorize.md'>Link</a>]  
5.2. numpy.vectorize() [<a href='https://github.com/jehyunlee/code-snippet/blob/master/4_numpy/numpy_vectorize.md'>Link</a>] and as decoration[<a href='https://github.com/jehyunlee/code-snippet/blob/master/4_numpy/numpy_vectorize.md#-numpyvectorize-as-decoration'>Link</a>]

6. image processing with `pillow`, `scikit-image`, `hyperspy` and `pyimagej`.  
6.1. Read metadata from `.dm3`(TEM) and `.tif`(SEM), then export to `.jpg`. [[Link](https://github.com/jehyunlee/image_processing/blob/master/meta2jpg/dm3_to_metajpg_190625.md)]

7. `docker`  
7.1. Installation of `docker` on `windows 10 home` [[Link](https://github.com/jehyunlee/docker/blob/master/Win10Home/text.md)]  
7.2. Basic commands [[Link](https://github.com/jehyunlee/code-snippet/blob/master/5_docker/01_basic.md)]  
7.3. Build and Run commands [[Link](https://github.com/jehyunlee/code-snippet/blob/master/5_docker/02_build.md)]  
7.4. Inspect commands [[Link](https://github.com/jehyunlee/code-snippet/blob/master/5_docker/03_inspect.md)]  
7.5. User account settings [[Link](https://github.com/jehyunlee/code-snippet/blob/master/5_docker/04_account.md)]  
7.6. Commit and Push [[Link](https://github.com/jehyunlee/code-snippet/blob/master/5_docker/05_commit.md)]  


