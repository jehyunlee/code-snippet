## Docker 살펴보기
> http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter05 

#### 08. `history`: 이미지 히스토리 살펴보기  
* `docker history [이미지 이름]:[태그]` 형식.  
* 이미지 이름 대신 이미지 ID를 사용해도 됨.
```bash
$ docker history hello:0.1
```

#### 09. `cp`: 파일 꺼내기
* `docker cp [컨테이너 이름]:[경로] [호스트 경로]` 형식.
```bash
$ docker cp hello-nginx:/etc/nginx/nginx.conf ./
```

#### 10. `commit`: 컨테이너의 변경사항을 이미지로 생성하기
* `docker commit [옵션] [컨테이너 이름] [이미지 이름]:[태그]` 형식.  
* 컨테이너 이름 대신 컨테이너 ID를 사용해도 됨.
```bash
$ `docker commit -a "Jehyun Lee <jehyun.lee@gmail.com>" -m "add hello.txt" hello-nginx hello:0.2
```

#### 11. `diff`: 컨테이너에서 변경된 파일 확인하기
* `docker diff [컨테이너 이름]` 형식.  
* 컨테이너 이름 대신 컨테이너 ID를 사용해도 됨.  
```bash
$ docker diff hello-nginx
```
`A`: 추가된 파일, `C`: 변경된 파일, `D`: 삭제된 파일.  

#### 12. `inspect`: 세부 정보 확인하기  
* `docker inspect [이미지 or 컨테이너 이름]` 형식.
* 이미지나 컨테이너 이름 대신 ID를 사용해도 됨.  
```bash
$ docker inspect hello-nginx
```
