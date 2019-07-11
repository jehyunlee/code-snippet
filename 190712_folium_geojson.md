
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
  fn = 'html/' + html_name
  tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
  m.save(fn)

  browser = webdriver.Chrome()
  browser.get(tmpurl)
  
  #Give the map tiles some time to load
  time.sleep(delay)
  browser.save_screenshot('./images/'+png_name)
  browser.quit()
```

## 1. Basic : Seoul Map
### 1.0. Object creation


```python
import folium

map_osm = folium.Map(location=[37.566345, 126.977893])   # Seoul City Hall
#map_osm.save('./map1.html')      # Save map as html
export_png(map_osm, 'map1.html', 'map1.png')   # Save map as png
#map_osm    # Show map on Notebook
```

<img src="./images/map1.png" height="400" width="400">

### 1.1. Set Initial Zoom


```python
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)  # Zoom Level Set
export_png(map_osm, 'map2.html', 'map2.png')
```

<img src="./images/map2.png" height="400" width="400">

### 1.2. Another Map Type
* Stamen Terrain : Good for visualizaiton of landscape, such as mountains and rivers.


```python
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17,
                    tiles='Stamen Terrain'  # Tiles setting
                    )  
export_png(map_osm, 'map3.html', 'map3.png')
```

<img src="./images/map3.png" height="400" width="400">

* Stamen Toner


```python
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17,
                    tiles='Stamen Toner'  # Tiles setting
                    )  
export_png(map_osm, 'map4.html', 'map4.png')
```

<img src="./images/map4.png" height="400" width="400">

* CartoDBPositron


```python
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17, 
                     tiles='cartodbpositron'
                    )
export_png(map_osm, 'map5.html', 'map5.png')
```

<img src="./images/map5.png" height="400" width="400">

### 1.3. Marker and Popup
* Marker


```python
map_osm = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
folium.Marker([37.566345, 126.977893], popup='서울특별시청').add_to(map_osm)
folium.Marker([37.5658859, 126.9754788], popup='덕수궁').add_to(map_osm)
export_png(map_osm, 'map6.html', 'map6.png')

map_osm
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgCiAgICAgICAgPHNjcmlwdD4KICAgICAgICAgICAgTF9OT19UT1VDSCA9IGZhbHNlOwogICAgICAgICAgICBMX0RJU0FCTEVfM0QgPSBmYWxzZTsKICAgICAgICA8L3NjcmlwdD4KICAgIAogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjQuMC9kaXN0L2xlYWZsZXQuanMiPjwvc2NyaXB0PgogICAgPHNjcmlwdCBzcmM9Imh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0xLjEyLjQubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9qcy9ib290c3RyYXAubWluLmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5qcyI+PC9zY3JpcHQ+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuLmpzZGVsaXZyLm5ldC9ucG0vbGVhZmxldEAxLjQuMC9kaXN0L2xlYWZsZXQuY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vYm9vdHN0cmFwLzMuMi4wL2Nzcy9ib290c3RyYXAubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLXRoZW1lLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9mb250LWF3ZXNvbWUvNC42LjMvY3NzL2ZvbnQtYXdlc29tZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL0xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLzIuMC4yL2xlYWZsZXQuYXdlc29tZS1tYXJrZXJzLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL3Jhd2Nkbi5naXRoYWNrLmNvbS9weXRob24tdmlzdWFsaXphdGlvbi9mb2xpdW0vbWFzdGVyL2ZvbGl1bS90ZW1wbGF0ZXMvbGVhZmxldC5hd2Vzb21lLnJvdGF0ZS5jc3MiLz4KICAgIDxzdHlsZT5odG1sLCBib2R5IHt3aWR0aDogMTAwJTtoZWlnaHQ6IDEwMCU7bWFyZ2luOiAwO3BhZGRpbmc6IDA7fTwvc3R5bGU+CiAgICA8c3R5bGU+I21hcCB7cG9zaXRpb246YWJzb2x1dGU7dG9wOjA7Ym90dG9tOjA7cmlnaHQ6MDtsZWZ0OjA7fTwvc3R5bGU+CiAgICAKICAgICAgICAgICAgPG1ldGEgbmFtZT0idmlld3BvcnQiIGNvbnRlbnQ9IndpZHRoPWRldmljZS13aWR0aCwKICAgICAgICAgICAgICAgIGluaXRpYWwtc2NhbGU9MS4wLCBtYXhpbXVtLXNjYWxlPTEuMCwgdXNlci1zY2FsYWJsZT1ubyIgLz4KICAgICAgICAgICAgPHN0eWxlPgogICAgICAgICAgICAgICAgI21hcF9kOTMyNTM0MjUzNzA0NTE3OWJlOTZlZTU2ZmI3M2E5NyB7CiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlOwogICAgICAgICAgICAgICAgICAgIHdpZHRoOiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICAgICAgbGVmdDogMC4wJTsKICAgICAgICAgICAgICAgICAgICB0b3A6IDAuMCU7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+CiAgICAgICAgCjwvaGVhZD4KPGJvZHk+ICAgIAogICAgCiAgICAgICAgICAgIDxkaXYgY2xhc3M9ImZvbGl1bS1tYXAiIGlkPSJtYXBfZDkzMjUzNDI1MzcwNDUxNzliZTk2ZWU1NmZiNzNhOTciID48L2Rpdj4KICAgICAgICAKPC9ib2R5Pgo8c2NyaXB0PiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFwX2Q5MzI1MzQyNTM3MDQ1MTc5YmU5NmVlNTZmYjczYTk3ID0gTC5tYXAoCiAgICAgICAgICAgICAgICAibWFwX2Q5MzI1MzQyNTM3MDQ1MTc5YmU5NmVlNTZmYjczYTk3IiwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICBjZW50ZXI6IFszNy41NjYzNDUsIDEyNi45Nzc4OTNdLAogICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcsCiAgICAgICAgICAgICAgICAgICAgem9vbTogMTcsCiAgICAgICAgICAgICAgICAgICAgem9vbUNvbnRyb2w6IHRydWUsCiAgICAgICAgICAgICAgICAgICAgcHJlZmVyQ2FudmFzOiBmYWxzZSwKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgKTsKCiAgICAgICAgICAgIAoKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgdGlsZV9sYXllcl85ZTQ2YzdiZTBhN2I0MzMxYWExNTMzZmJiMDM2NGIzMSA9IEwudGlsZUxheWVyKAogICAgICAgICAgICAgICAgImh0dHBzOi8ve3N9LnRpbGUub3BlbnN0cmVldG1hcC5vcmcve3p9L3t4fS97eX0ucG5nIiwKICAgICAgICAgICAgICAgIHsiYXR0cmlidXRpb24iOiAiRGF0YSBieSBcdTAwMjZjb3B5OyBcdTAwM2NhIGhyZWY9XCJodHRwOi8vb3BlbnN0cmVldG1hcC5vcmdcIlx1MDAzZU9wZW5TdHJlZXRNYXBcdTAwM2MvYVx1MDAzZSwgdW5kZXIgXHUwMDNjYSBocmVmPVwiaHR0cDovL3d3dy5vcGVuc3RyZWV0bWFwLm9yZy9jb3B5cmlnaHRcIlx1MDAzZU9EYkxcdTAwM2MvYVx1MDAzZS4iLCAiZGV0ZWN0UmV0aW5hIjogZmFsc2UsICJtYXhOYXRpdmVab29tIjogMTgsICJtYXhab29tIjogMTgsICJtaW5ab29tIjogMCwgIm5vV3JhcCI6IGZhbHNlLCAib3BhY2l0eSI6IDEsICJzdWJkb21haW5zIjogImFiYyIsICJ0bXMiOiBmYWxzZX0KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDkzMjUzNDI1MzcwNDUxNzliZTk2ZWU1NmZiNzNhOTcpOwogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBtYXJrZXJfMGU3Y2QzNjJlMGYzNGMzZmI4NTkxODNkYTFiMDJlZTUgPSBMLm1hcmtlcigKICAgICAgICAgICAgICAgIFszNy41NjYzNDUsIDEyNi45Nzc4OTNdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDkzMjUzNDI1MzcwNDUxNzliZTk2ZWU1NmZiNzNhOTcpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwX2ViYWFjN2I5MTlkOTRmNTA4MjQwYmY3MGUyOTcwZjc5ID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hMjc4NzRkOGY4MjQ0ODQ0YmRkZDJkMWM3M2QwOTVhZiA9ICQoYDxkaXYgaWQ9Imh0bWxfYTI3ODc0ZDhmODI0NDg0NGJkZGQyZDFjNzNkMDk1YWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPuyEnOyauO2KueuzhOyLnOyyrTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF9lYmFhYzdiOTE5ZDk0ZjUwODI0MGJmNzBlMjk3MGY3OS5zZXRDb250ZW50KGh0bWxfYTI3ODc0ZDhmODI0NDg0NGJkZGQyZDFjNzNkMDk1YWYpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfMGU3Y2QzNjJlMGYzNGMzZmI4NTkxODNkYTFiMDJlZTUuYmluZFBvcHVwKHBvcHVwX2ViYWFjN2I5MTlkOTRmNTA4MjQwYmY3MGUyOTcwZjc5KQogICAgICAgIDsKCiAgICAgICAgCiAgICAKICAgIAogICAgICAgICAgICB2YXIgbWFya2VyXzVkZWQ1ZTlhYjdkZTQ5ZGI4MjVhNmIxNWI3ZmY3YmNhID0gTC5tYXJrZXIoCiAgICAgICAgICAgICAgICBbMzcuNTY1ODg1OSwgMTI2Ljk3NTQ3ODhdLAogICAgICAgICAgICAgICAge30KICAgICAgICAgICAgKS5hZGRUbyhtYXBfZDkzMjUzNDI1MzcwNDUxNzliZTk2ZWU1NmZiNzNhOTcpOwogICAgICAgIAogICAgCiAgICAgICAgdmFyIHBvcHVwXzgxZTk2YmUyMzFmYTRiNjViNTQyYzU5MzRlZjkxM2YwID0gTC5wb3B1cCh7Im1heFdpZHRoIjogIjEwMCUifSk7CgogICAgICAgIAogICAgICAgICAgICB2YXIgaHRtbF9hNWJhMzFiNTc1NzE0NTEyYjIwNThmNGQxMWUyNThhNiA9ICQoYDxkaXYgaWQ9Imh0bWxfYTViYTMxYjU3NTcxNDUxMmIyMDU4ZjRkMTFlMjU4YTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPuuNleyImOq2gTwvZGl2PmApWzBdOwogICAgICAgICAgICBwb3B1cF84MWU5NmJlMjMxZmE0YjY1YjU0MmM1OTM0ZWY5MTNmMC5zZXRDb250ZW50KGh0bWxfYTViYTMxYjU3NTcxNDUxMmIyMDU4ZjRkMTFlMjU4YTYpOwogICAgICAgIAoKICAgICAgICBtYXJrZXJfNWRlZDVlOWFiN2RlNDlkYjgyNWE2YjE1YjdmZjdiY2EuYmluZFBvcHVwKHBvcHVwXzgxZTk2YmUyMzFmYTRiNjViNTQyYzU5MzRlZjkxM2YwKQogICAgICAgIDsKCiAgICAgICAgCiAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



<img src="./images/map6.png" height="400" width="400">


```python

```
