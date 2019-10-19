## Docker 명령어  
> http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter03  
> https://www.sangkon.com/hands-on-docker-part1/  

#### 01. Image 검색: `docker search`  
- `Docker Hub` (https://registry.hub.docker.com)에서 이미지를 검색.  
- 유명 리눅스 배포판과 오픈 소스 프로젝트(Redis, Nginx)의 Docker 이미지는 모두 Docker Hub에서 구할 수 있음.  
- `Docker Hub`에서 이미지를 검색한 뒤 해당 이미지의 `Tags`를 보면 현재 사용 가능한 이미지 버전 확인 가능.  

#### 02. Image 받기: `docker pull`  
- `docker pull [이미지이름]:[태그]` 형식.  
- `[태그]`에 `latest`를 설정하면 최신 버전을 받음.  
- 이미지 이름에 `jehyunlee/geocoding`처럼 / 앞에 사용자명을 지정하면 `Docker Hub`에서 해당 사용자가 올린 이미지를 받음.  
- 공식 이미지에는 사용자 이름이 붙지 않음.  

#### 03. Image 목록: `docker images`  
- 내가 가지고 있는 이미지 목록 확인.  
- `docker image ubuntu`처럼 이미지 이름을 설정하면, 이름은 같지만 태그가 다른 이미지가 모두 출력됨.  

#### 04. 컨테이너 생성: `docker run`  
- `docker run [옵션] [이미지 이름] [실행할 파일or명령]` 형식.
- `[이미지 이름]` 대신 `[이미지 ID]` 실행 가능.  
- `[옵션]`  
  * `-it` (**i**nteractive, pseudo-**t**ty): 실행된 `bash` shell에 입력 및 출력 가능  
  * `-d`': 컨테이너를 백그라운드에서 계속 실행하기  
  * `--rm` (**r**e**m**ove): 실행 후 컨테이너 삭제 
  * `--name [컨테이너이름]` : 컨테이너 이름 지정
  
