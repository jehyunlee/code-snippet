* rotate by 1 degree in every step  

```python
%matplotlib inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

PC1 = pca_result['PC1']
PC2 = pca_result['PC2']
PC3 = pca_result['PC3']
ax.scatter(PC1, PC2, PC3, c=pca_result['shadow'], s=1, cmap='jet')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
ax.auto_scale_xyz([-30, 40], [-30, 40], [-15, 55])

for ii in range(0,360,1):
    ax.view_init(elev=10., azim=ii)
    plt.savefig("./images/pca_movie%d.png" % ii)
```
![png](/2_matplotlib/ani_rotation/images/pca_movie0.png)

* create .mp4 file from the images  

```python
%%bash
ffmpeg -r 30 -i ./images/pca_movie%d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p pca_movie.mp4
```
