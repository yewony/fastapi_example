# fastapi_example

## 구조
### app
    API 서버

    1. main.py
        > fastapi init 
    
    2. Dockerfile
        > api단 이미지용 Dockerfile

### nginx
    웹 서버
    
    1. Dockerfile : nginx 이미지용 Dockerfile

## 배포 관리
    1. 빌드
        > docker-compose_build.sh 실행
    
    2. 로컬 테스트
        > docker-compose rm -fs; docker-compose up --force-recreate
        > localhost 로 테스트

    3. 푸시
        > docker-compose_build_and_push.sh 실행 (아직 없음)