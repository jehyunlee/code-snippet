### **Additive Color Model Operation for 3 colors**

#### 1. import libraries, and set 3 colors


```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

c1 = 'darkred'
c2 = 'teal'     # matplotlib defined color names
c3 = '#0000FF'    # 'blue'

c1 = np.array(mpl.colors.to_rgb(c1))
c2 = np.array(mpl.colors.to_rgb(c2))
c3 = np.array(mpl.colors.to_rgb(c3))

print(c1, c2, c3)
```

    [0.54509804 0.         0.        ] [0.         0.50196078 0.50196078] [0. 0. 1.]


#### 2. function definition


```python
def add_color(c1, c2, c3, ipol=0):
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    c3=np.array(mpl.colors.to_rgb(c3))
    if ipol < 0.25:
        c = c1 + 4*ipol * c2
    elif ipol < 0.5:
        c = (2 - 4*ipol) * c1 + c2
    elif ipol < 0.75:
        c = c2 + (4*ipol-2) * c3
    else:
        c = (4 - 4*ipol) * c2 + c3
    
    if c.max() > 1:
        c = c/c.max()
        
    return mpl.colors.to_hex(c)
```

#### 3. visualize


```python
%matplotlib inline

n = 200
fig, ax = plt.subplots(figsize=(8, 5))
for x in range(n+1):
    color = add_color(c1,c2,c3, x/n)
    if x in [0, 50, 100, 150, 200]:
        print(color)
    ax.axvline(x, color=color, linewidth=4) 
plt.show()
```

    #8b0000
    #8b8080
    #008080
    #0055ff
    #0000ff



![png](output_6_1.png)

