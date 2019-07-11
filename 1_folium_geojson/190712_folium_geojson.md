
# Overlay Administrative District on Map using folium and geojson
* The following code is taken from:  
> https://ericnjennifer.github.io/python_visualization/2018/01/21/PythonVisualization_Chapt6.html  
> https://python-visualization.github.io/folium/quickstart.html

## 0. Export map (.html) to image (.png)
* In this example, `google chrome` browser was used,  which requires **<a href="http://chromedriver.chromium.org/downloads">`ChromeDriver`-WebDriver for Chrome</a>**.
* `ChromeDriver` requires `path` to be called by python script. 


```python
from selenium import webdriver
import time, os

def export_png(m,                          # foium map instance
               html_name,                       # str. ex. 'testmap.html'
               png_name='map.png',    # str. ex. 'testmap.png'
               delay=5,                             # int or float. ex. 10
              ):
  
  delay=delay
  fn = html_name
  tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
  m.save(fn)

  browser = webdriver.Chrome()
  browser.get(tmpurl)
  
  #Give the map tiles some time to load
  time.sleep(delay)
  browser.save_screenshot(png_name)
  browser.quit()
```

## 1. Object creation


```python
import folium
map_osm = folium.Map(location=[37.566345, 126.977893])   # 서울특별시청
#map_osm.save('./map1.html')      # 파일이 저장될 위치
export_png(map_osm, 'map1.html', 'map1.png')
#map_osm
```

<img src="map1.png" height="400" width="400">

* 초기 화면 지정

* 다른 유형의 맵 호출
