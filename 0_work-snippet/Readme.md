# Work-snippet  
**Definition :** 효율적인 코딩생활을 위한 토막코드 집합체.
------------------------
### 1. 사용 방법  
#### 1.1. Download  
* 아래 work-snippet 중 원하는 것을 다운로드 받습니다.  

#### 1.2. Establish Access to the `Work-snippet`
##### 1.2.1. `python`에서는 `library`를 불러오는 `path`를 운영 체제에 따라 다르게 설정하고 있습니다.  
* `sys.path`명령으로 확인이 가능합니다.
```python
import sys
print(sys.path)
```
##### 1.2.2. 실제 `path` 환경 설정의 예를 들어보겠습니다.   
* 제 Windows 10 컴퓨터의 `base`가상환경의 경우 다음과 같이 설정되어 있습니다.
> ['C:\\Users\\sec\\Anaconda3\\python36.zip', 'C:\\Users\\sec\\Anaconda3\\DLLs', ... (생략) ... ]  

* 같은 PC에서 작동되는 `WSL2`의 경우 이렇게 설정되어 있네요.  
> ['/home/jehyun/PycharmProjects/base', '/home/jehyun/anaconda3/envs/geocoding/lib/python37.zip', ... (생략) ...]
  
##### 1.2.3. 다운로드 받은 `.py` 파일을 어디에서나 호출하려면,  
(1) 이들 중 한 위치에 `.py` 파일을 복사하거나  
(2) `.py`파일이 위치한 폴더를 저 목록에 포함시켜야 합니다.  

##### 1.2.4. 저는 (2)를 택했습니다.  
`Linux`에서는 `.bashrc`파일에 ```export PYTHONPATH="${PYTHONPATH}:/my/other/path"``` 처럼 추가하면 되고, [[Link](https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath)]   
`Windows`에서는 `환경 변수 설정`에서 추가하면 됩니다. [[Link](https://sshkim.tistory.com/158)]  
<br>  

### 2. Work-snippet 목록  
#### [1]. `pegab` : pega-base   
* 기능 : (1) 한글 사용 설정, (2) Figure Style 설정, (3) df2md  
![png](https://github.com/jehyunlee/code-snippet/blob/master/0_work-snippet/pegab/images/run.png)
