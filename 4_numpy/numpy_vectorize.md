### Numpy Vectorization : numpy.vectorize() and decoration
> https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html

* `numpy.vectorize()` : object의 nested sequence느 numpy array를 input으로 받고, numpy array 또는 numpy array의 tuple을 return하는 vectorized function을 정의함.

#### Example 1. 비교연산함수


```python
def myfunc(a, b):
  "Return a-b if a > b, otherwise return a + b"
  return a-b if a > b else a+b

vfunc = np.vectorize(myfunc)
vfunc([1,2,3,4], 2)
```




    array([3, 4, 1, 2])



* docstring : 따로 정의되지 않으면 input function의 docstring을 가져감.


```python
print('1. default docstring (of input) : {}'.format(vfunc.__doc__))

vfunc = np.vectorize(myfunc, doc='Vectorized "myfunc"')
print('2. vectorization function docstring : {}'.format(vfunc.__doc__))
```

    1. default docstring (of input) : Vectorized "myfunc"
    2. vectorization function docstring : Vectorized "myfunc"
    

* output type: 따로 정의되지 않으면 input의 first argument를 따름.


```python
out = vfunc([1, 2, 3, 4], 2)
print('1. default output type (of input) : {}'.format(type(out[0])))

vfunc = np.vectorize(myfunc, otypes=[float])
out = vfunc([1, 2, 3, 4], 2)
print('2. vectorization function outtype: {}'.format(type(out[0])))
```

    1. default output type (of input) : <class 'numpy.int32'>
    2. vectorization function outtype: <class 'numpy.float64'>
    

#### Example 2. 다항함수
* exclude : 특정 argument를 vectorizing에서 제외함.  
`polyval`의 coefficients처럼 길이가 일정한 array-like arguments를 다룰 때 유용함.


```python
def mypolyval(p, x):
  _p = list(p)
  res = _p.pop()
  while _p:
    p1 = _p.pop()
    res = res*x + p1
  return res

vpolyval = np.vectorize(mypolyval, excluded=['p'])
vpolyval(p=[1,2,3], x=[0, 1, 2])
  
```




    array([ 1,  6, 17])



   ##### polynomial의 계수 list인 p를 exclude하지 않으면 아래와 같이 오류가 발생함.


```python
vpolyval = np.vectorize(mypolyval)
vpolyval(p=[1,2,3], x=[0,1])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-23-5466f131c677> in <module>
          1 vpolyval = np.vectorize(mypolyval)
    ----> 2 vpolyval(p=[1,2,3], x=[0,1])
    

    ~\Anaconda3\lib\site-packages\numpy\lib\function_base.py in __call__(self, *args, **kwargs)
       2089             vargs.extend([kwargs[_n] for _n in names])
       2090 
    -> 2091         return self._vectorize_call(func=func, args=vargs)
       2092 
       2093     def _get_ufunc_and_otypes(self, func, args):
    

    ~\Anaconda3\lib\site-packages\numpy\lib\function_base.py in _vectorize_call(self, func, args)
       2159             res = func()
       2160         else:
    -> 2161             ufunc, otypes = self._get_ufunc_and_otypes(func=func, args=args)
       2162 
       2163             # Convert args to object arrays first
    

    ~\Anaconda3\lib\site-packages\numpy\lib\function_base.py in _get_ufunc_and_otypes(self, func, args)
       2119 
       2120             inputs = [arg.flat[0] for arg in args]
    -> 2121             outputs = func(*inputs)
       2122 
       2123             # Performance note: profiling indicates that -- for simple
    

    ~\Anaconda3\lib\site-packages\numpy\lib\function_base.py in func(*vargs)
       2084                     the_args[_i] = vargs[_n]
       2085                 kwargs.update(zip(names, vargs[len(inds):]))
    -> 2086                 return self.pyfunc(*the_args, **kwargs)
       2087 
       2088             vargs = [args[_i] for _i in inds]
    

    <ipython-input-22-62002f79cfb3> in mypolyval(p, x)
          1 def mypolyval(p, x):
    ----> 2   _p = list(p)
          3   res = _p.pop()
          4   while _p:
          5     p1 = _p.pop()
    

    TypeError: 'numpy.int32' object is not iterable


#### Example 3. Pearson Correlation Coefficient with p-value
* signature : fixed length의 non-scalar array에 적용되는 vectorizing function을 허용함.  
`Pearson Correlation Coefficient`와 `p-value`에 대한 vectorization 예제


```python
from scipy.stats import pearsonr as P

pearsonr = np.vectorize(P, signature='(n),(n)->(),()')
pearsonr([[0, 1, 2, 3]], [[1, 2, 3, 4], [4, 3, 2, 1]])
```




    (array([ 1., -1.]), array([0., 0.]))



##### vectorization convolution


```python
convolve = np.vectorize(np.convolve, signature='(n),(m)->(k)')
convolve(np.eye(4), [1,2,1])
```




    array([[1., 2., 1., 0., 0., 0.],
           [0., 1., 2., 1., 0., 0.],
           [0., 0., 1., 2., 1., 0.],
           [0., 0., 0., 1., 2., 1.]])



### * numpy.vectorize as decoration


```python
@np.vectorize
def myfunc_decvec(a, b):
  "Return a-b if a > b, otherwise return a + b"
  return a-b if a > b else a+b

myfunc_decvec([1,2,3,4], 2)
```




    array([3, 4, 1, 2])



##### @decoration with options: Error!

> Note that `np.vectorize` isn't really meant as a decorator except for the simplest cases. If you need to specify an explicit `otype`, use the usual form `new_func = np.vectorize(old_func, otypes=...)` or use `functools.partial` to get a decorator.  
>  
> source : https://stackoverflow.com/questions/14986697/numpy-vectorize-as-a-decorator-with-arguments


```python
@np.vectorize(doc='Vectorized "myfunc"')
def myfunc_decvec(a, b):
  "Return a-b if a > b, otherwise return a + b"
  return a-b if a > b else a+b

print('vectorization function docstring : {}'.format(myfunc_decvec.__doc__))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-36-0cc9eadaea22> in <module>
    ----> 1 @np.vectorize(doc='Vectorized "myfunc"')
          2 def myfunc_decvec(a, b):
          3   "Return a-b if a > b, otherwise return a + b"
          4   return a-b if a > b else a+b
          5 
    

    TypeError: __init__() missing 1 required positional argument: 'pyfunc'

