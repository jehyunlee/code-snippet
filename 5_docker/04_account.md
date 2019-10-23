## 계정 관리

#### 1. root 계정으로 접속
* `docer exec -u [사용자ID] [옵션] [컨테이너 이름] [명령어]` 형식.  
```bash
docker exec -u 0 -it test01 bash
```
* `-u 0`: `root`계정 접속
* `-it`: 키보드 입력 가능

#### 2. root 암호 변경
```bash
$ passwd
```
* root 암호 입력, 암호 확인 재입력  

#### 3. 사용자 암호 변경
```bash
$ passwd jehyunlee
```
* 사용자계정(jehyunlee) 암호 입력, 암호 확인 재입력. 
