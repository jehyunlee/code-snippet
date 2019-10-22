## Docker File Build
> docker file: http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter04/02
> build: http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter04/03

#### 05. Dockerfile 작성
- directory를 만들고 그 안에 dockerfile 작성  
```bash
$ mkdir example
$ cd example
```

- dockerfile 내용
```
FROM ubuntu:16.04
MAINTAINER Jehyun Lee <jehyun.lee@gmail.com>

RUN apt-get update
RUN apt-get install --allow-unauthenticated -y nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/enginx

VOLUME ["/data", "/etc/nginx/site-enabled", "/var/log/nginx"]

WORKDIR /etc/nginx

CMD ["nginx"]

EXPOSE 80
EXPOSE 443
```
* FROM: `[이미지 이름]:[태그]` 형식. 어떤 이미지를 기반으로 할지 설정.
* MAINTAINER: 메인테이너 정보
* RUN: Shell script나 명령을 실행  
  * 이미지 생성 중에는 입력을 받을 수 없으므로 `apt-get install`에 `-y` 옵션 포함.  
  * 나머지는 `nginx`설정
* VOLUME: 호스트와 공유할 디렉토리 목록. `run`에서 디렉토리 연결 설정 가능 [Link](https://github.com/jehyunlee/code-snippet/blob/master/5_docker/01_basic.md#04-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-%EC%83%9D%EC%84%B1-docker-run)
* CMD: 컨테이너가 시작되었을 때 실행할 파일 또는 셸 스크립트.  
* WORKDIR: CMD에서 설정한 실행 파일이 실행될 디렉토리.  
* EXPOSE: 호스트와 연결할 포트.  

#### 06. `build`: 이미지 생성
- directory 밖에서 build 실행.  
```bash
$ docker build example --tag hello:0.1.
```
- `docker build [옵션] [dockerfile 경로]` 형식.  
  - `--tag`형식으로 `[이미지이름]:[태그]` 설정 가능. `[이미지이름]`만 하면 `[태그]`는 자동으로 `latest`로 설정됨.  

- 이미지 목록 출력.  
```bash
$ docker images
```

#### 07. `run`: 컨테이너 실행
- 방금 만든 `hello:0.1` 이미지를 컨테이너에 실어서 실행.  
```bash
$ docker run --name hello-nginx -d -p 80:80 -v /root/data:/data hello:0.1
```
* `-d`: 컨테이너를 백그라운드로 실행  
* `-p 80:80`: 호스트의 80번 포트와 컨테이너의 80번 포트를 연결하고 외부에 노출함.  
  * `http:[호스트IP]:80`을 웹브라우저에 입력하면 컨테이너의 80번 포트로 접속됨.  
  * `[호스트IP]`를 알아내기 위해서는 docker에서 `$ docker-machine ip`를 실행. 기본값은 `192.168.99.100`.  
  * 또는, `Kimanetic`의 `Web Preview`에 작게 출력된 화면을 클릭하면 웹브라우저로 열기가 실행됨.  
* `exit`를 입력하면 컨테이너가 정지(`stop`)되고 컨테이너에서 빠져나옴.
  * `Ctrl+P`, `Ctrl+Q`를 차례대로 입력하면 컨테이너를 정지하지 않고 빠져나옴.

#### 08. `ps`: 실행된 컨테이너 목록 확인
```bash
$ docker ps
```

#### 09. `start`: 컨테이너 시작하기
* `docker start [컨테이너 이름]` 형식.  
* 컨테이너 이름 대신 컨테이너 ID를 사용해도 됨.  
```bash
$ docker start hello
```

#### 10. `restart`: 컨테이너 재시작 
* `docker restart [컨테이너 이름]` 형식. 
* 컨테이너 이름 대신 컨테이너 ID를 사용해도 됨. 
* OS 재부팅과 같음.
```bash
$ docker restart hello
```

#### 11. `attach`: 컨테이너 접속
* `docker attach [컨테이너 이름]` 형식.  
* 앞에서 `/bin/bash`를 실행했기 때문에 명령어 입력이 가능하지만 다른 어플리케이션 실행시 입력 불가하기도 함.
```bash
$ docker attach hello
```
* `exit`를 입력하면 컨테이너가 정지(`stop`)되고 컨테이너에서 빠져나옴.
  * `Ctrl+P`, `Ctrl+Q`를 차례대로 입력하면 컨테이너를 정지하지 않고 빠져나옴.  
  
#### 12. `exec`: 외부에서 컨테이너 명령 실행
* `docker exec [컨테이너 이름] [명령] [매개 변수]` 형식.  
* 컨테이너가 실행되고 있는 상태에서만 사용 가능하며 정지된 상태에서는 사용할 수 없음.
```bash
$ docker exec hello echo "Hello World"
```
* 실행중인 컨테이너에 `apt-get`, `yum`등의 명령어로 패키지를 설치하거나 각종 데몬을 실행할 때 활용 가능.  

#### 13. `stop`: 컨테이너 정지
* `docker stop [컨테이너 이름]` 형식.  
```bash
$ docker stop hello
```

#### 14. `rm`: 컨테이너 삭제
* `docker rm [컨테이너 이름]` 형식.  
```bash
$ docker rm hello
```

#### 15. `rmi`: 이미지 삭제
* `docker rmi [이미지 이름]` 형식.  
* `docker rmi ubuntu` 처럼 이미지 이름만 지정하면 **태그**는 다르지만 **이름**이 같은 모든 이미지가 삭제됨.
```bash
$ docker rmi ubuntu:latest
```

