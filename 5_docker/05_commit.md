## commit & push
> https://nicewoong.github.io/development/2018/03/06/docker-commit-container/

#### 1. Docker 컨테이너 commit
* 컨테이너에 발생한 변경사항을 이미지로 저장  
* ```docker commit [컨테이너 이름] [이미지 이름]```  
```bash
$ docker commit ubuntu-cpp-driver ubuntu-cpp-driver
```

#### 2. Docker Image Push
1. docker cloud 로그인  
```bash
$ docker login
```

2. docker user id 저장
```bash
$ export DOCKER_ID_USER="jehyunlee"
```

3. docker image 태그 달기
```bash
$ docker tag ubuntu-driver $DOCKER_ID_USER/ubuntu-cpp-driver
```

4. Tag가 적용된 Image를 docker cloud에 push
```bash
docker push $DOCKER_ID_USER/ubuntu-cpp-driver
```
