### Numpy Vectorization
* source : https://www.geeksforgeeks.org/vectorization-in-python/

> **outer(a, b) :** 외적.  
> **multiply(a, b) :** 행렬곱.  
> **dot(a, b) :** 내적.  
> **zeros((n,m)) :** (n,m) 크기의 영행렬 출력.  
> **process_time() :** 수행시간 = 해당 프로세스의 (system + user CPU) time.  

#### 1. Dot Product


```python
import time
import numpy as np
import array
```


```python
# 8 byte size int
a = array.array('q')
for i in range(100000):
  a.append(i);

b = array.array('q')
for i in range(100000, 200000):
  b.append(i)
```


```python
# classic dot product of vectors implement
tic = time.process_time()
dot = 0.0;

for i in range(len(a)):
  dot += a[i] * b[i]

toc = time.process_time()

print('dot_product = {}'.format(dot));
print('computation time = {} ms'.format(1000*(toc-tic)))
```

    dot_product = 833323333350000.0
    computation time = 31.25 ms
    
