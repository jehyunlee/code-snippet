### Numpy Vectorization
> https://www.geeksforgeeks.org/vectorization-in-python/

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

* 8 byte size int


```python

a = array.array('q')
for i in range(100000):
  a.append(i);

b = array.array('q')
for i in range(100000, 200000):
  b.append(i)
```

##### 1.1. classic dot product of vectors implement


```python
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
    

##### 1.2. numpy dot product


```python
n_tic = time.process_time()
n_dot_product = np.dot(a, b)
n_toc = time.process_time()

print('dot_product = {}'.format(n_dot_product))
print('computation time = {} ms'.format(1000*(n_toc - n_tic)))
```

    dot_product = 833323333350000
    computation time = 0.0 ms
    
