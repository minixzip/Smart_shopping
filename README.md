<h1 align="center">스마트 쇼핑카트</h1>
<br>
<p align="center">
  <a href="https://github.com/abhishekapk/SMART-PARKING-SYSTEM">
    <img src="https://github.com/StealthBlack66/Smart_shopping/blob/main/image/%EC%95%84%EB%A7%88%EC%A1%B4_%EB%8C%80%EC%8B%9C%EC%B9%B4%ED%8A%B8_%ED%99%80%ED%91%B8%EB%93%9C.JPG" alt="Logo" width="auto" height="auto">
  </a></p>
<br>

## 목차
[1. 하드웨어](#하드웨어)\
[2. 서버](#서버)\
[3. 데이터베이스](#데이터베이스) 


<br>
<h2>개요</h2>
<p align="justify"> 아마존 후레시(Amazon Fresh)라는 외국의 대형마트에서는 'Dash Cart'라는 쇼핑카트를 사용하고 있다. 평범해 보이지만 이 카트는 일반적인 카트와는 차이나는 최첨단 기술을 담고 있다.

1. Dash Cart를 이용하기 위해서는 아마존 앱을 실행하고 본인인증을 한다. 
2. 카트에 바구니를 올리고 원하는 제품을 담는다.
3. Dash Cart 전용 출구로 나간다.

이 과정에서 등록된 회원정보에 따라 자동으로 결제가 진행된다. Dash Cart를 사용하면 결제를 하기 위해 줄을 서는 수고스러움을 덜 수 있는 것이다. 온라인 매장이 대세인 현재 이는 큰 메리트가 된다. 
<br>
</p>
<h2>소개</h2>
 <p align="justify">위 아마존 후레쉬의 Dash Cart를 모티브로 한 스마트 쇼핑카트를 만들 것이다.
 
 - 초음파 센서 : 들어오고 나가는 상품들을 감지한다.
 - 파이카메라 : 상품 탐지
 - 라즈베리파이 : 메인 서버와 카트의 통신 담당
 - 무게 센서 : 상품들 출입여부를 판단
 - 터치스크린 : 카트에 담은 상품 목록을 보여줌, 결제가 이뤄짐

동작순서는 다음과 같다. 

1. ShopCart.py 실행
2. 물품을 카메라 앞에 비춘다. 
3. 바운딩박스와 신뢰도가 뜨는지 확인한다. 
4. 검출 내용이 추가된 장바구니 화면 확인 
5. 결제(본 프로젝트에선 구현하지 않음)
 
 </p>
<br>
<h2>객체 탐지 모델 </h2>
<p align="justify">그리드 기반의 객체 탐지 기술의 YOLO 라이브러리를 이용하여 카트 현황을 탐지한다. 어떤 상품이 어느 만큼 들어왔거나 나갔는 지를 정확하게 판단하는 것이 목적이다. 
</p>
<br>
<h4>1) YOLO 동작과정</h4>
<p align="center">
  <a href="">
    <img src="https://blog.kakaocdn.net/dn/bu6BVv/btrSHXxejru/98bLdWyukyzkzsAfLh5Q8k/img.png" alt="Block Diagram" width="auto" height="auto">
  </a></p>
<br>
<p align="justify">사진을 입력받으면 훈련 받은 클래스에 포함되는 객체를 검출한다. 

위 사진상에선 개, 자전거, 자동차가 해당된다.

검출된 객체에서 바운딩 박스라는 객체를 두르는 네모 박스와 이 정보에 대한 신뢰도가 출력된다.
</p>
<h4>2) 모델 훈련방식</h4>
<p align="justify">

본 프로젝트에서는 다음과 같은 클래스를 훈련시켰다.

- 상품 클래스 : 코카콜라, 컵불닭볶음면(소짜), 칸쵸

YOLO-mark를 이용해 학습데이터 리사이징과 라벨링 등의 전처리

</p>
<br>
<h2>알고리즘 구조</h2>
<p align="justify">
<br>
<p align="center">
  <a href="">
    <img src="https://github.com/StealthBlack66/Smart_shopping/blob/main/image/졸작 알고리즘.png" alt="Algorithm" width="auto" height="auto">
  </a></p>
<br>
<h2>사용 모듈</h2>
<p align="justify">

|spec|Component|Product|
|--|--|--|
|HW|RaspberryPi|RaspberryPi 4+|
|  |PiCamera|PiCamera2|
|  |Ultrasonic Sensor|HC-SR04|
|  |LoadCell Amplifier|HX711|
|  |LoadCell|LoadCell 10kg|
|  |Raspbian OS|Raspbian OS 64-bit|
|  |Python|Python3.9|
|  |  |Python3.11|
|  |Picamera|Picamera2|
|  |Apache|Apache2|
|Server|YOLO|YOLOv5|
|      |GoogleColab|  |
|Database|MySQL|XAMPP|
|        |php|
|        |phpMyAdmin|
  </p>
<br>
<h2>📸 SCREENSHOT</h2>
<p align="justify">
  </p>
<br>
<p align="center">
  <a href="">
  <img src="" alt="null" width="auto" height="auto">
  </a></p>
<br>
<p align="justify">
  </p>
<br>
<p align="center">
  <a href="">
    <img src="" alt="Figure 1" width="auto" height="auto">
  </a></p>
<br>
<p align="center">
  <a href="">
    <img src="" alt="Figure 2" width="auto" height="auto">
  </a></p>
<br>
<h2>참고자료</h2>

[딥러닝 객체 탐지 기술을 사용한 스마트 쇼핑카트의 구현](https://statkclee.github.io/kic2020/paper/index_kor.pdf)

<br>


## 1. 하드웨어
#### 1) 터치스크린 및 파이카메라 설치
- [터치스크린 설치](https://youtu.be/SVthAlyMdjA?si=OZq-TKrlKnZZooR9)
- [파이카메라 설치](https://youtu.be/6uQfqRpOsz4?si=jbt9B6tkGoxHNDTj)

#### 2) 초음파센서 및 무게센서 연결
<p align="center">
  <a href="">
  <img src="https://github.com/StealthBlack66/Smart_shopping/blob/main/image/회로도.png" alt="회로도" width="auto" height="auto">
  </a></p>

#### 3) 라즈비안 OS 설치 및 Yolov5 환경 세팅

- [Yolov5 환경 세팅](https://velog.io/@tmdwns2127/Yolov5-%ED%99%98%EA%B2%BD%EC%84%B8%ED%8C%85)
- [Mjpg-streamer 스트림 및 스트림 영상 검출](https://velog.io/@tmdwns2127/Yolov5-%EC%8B%A4%EC%8B%9C%EA%B0%84%EA%B2%80%EC%B6%9C)

<p align="justify">실시간 객체 검출이 필요하기 때문에 메모리가 큰 64비트 os로 설치하기. 

파이썬 버전은 PyTotch버전에 맞게 깔아줘야 한다. 본 프로젝트에서는 cp39를 사용하여 python3.9 설치.

mjpg-streamer 사용을 시도해보았으나 지금 시점에서는 파이카메라와 호환되지 않았음. 따라서 picamera2로 대체함

- [picamrea2 깃허브](https://github.com/raspberrypi/picamera2)
- [picamrea 사용법](https://velog.io/@xxn1ik/%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC%ED%8C%8C%EC%9D%B44-OS-64bit-V2-%EC%B9%B4%EB%A9%94%EB%9D%BC-%EC%9B%90%EA%B2%A9-%EC%8A%A4%ED%8A%B8%EB%A6%AC%EB%B0%8D)
</p>

#### 4) detect.py 옵션 설정

- save_csv = True : 검출 결과를 csv 파일로 저장
- nosave = True : 결과 동영상 저장하지 않기
- max_frames= 5 : 프레임 수 5로 제한

프레임 수가 5에 도달하면 종료되도록 수정/
csv파일에 프레임수, 클래스 이름, 객체수, 신뢰도가 저장되게 수정

예)\
2, ramen, 1, 0.66\
3, ramen, 2 ,0.35\
3, ramen, 2, 0.86\
4, ramen, 2, 0.32\
4, ramen, 2, 0.86\
5, ramen, 2, 0.75\
5, ramen, 2, 0.89

1열은 객체가 검출된 순간의 프레임수를 의미.\
2열은 검출된 객체이다.\
3열은 검출된 순간의 프레임에 걸린 객체의 수이다.\
4열은 검출에 대한 신뢰도이다.\
검출된 객체마다 행이 추가되므로 한 프레임에 걸린 객체수와 최대 프레임의 곱만큼 행이 생긴다. 

#### 5) 아파치 설치
    sudo apt update
    sudo apt install apache2 -y
    sudo apt install php libapache2-mod-php -y

Apache 서버 확인\
설치 후 Apache 서버가 제대로 동작하는지 확인하기 위해 브라우저에서 라즈베리파이 IP 주소를 입력

- 예: http://라즈베리파이_IP주소

PHP 테스트\
/var/www/html 디렉토리 안에 PHP 파일을 생성하여 테스트

    sudo nano /var/www/html/index.php

#### 6) 전체구동 파일 생성
- ShopCart.py

## 2. 서버
#### 모델 훈련
- 사용한 클래스 : 코카콜라, 컵불닭볶음면(소), 칸쵸
- 클래스별 훈련 이미지 수
  - 코카콜라 : 252장
  - 불닭 : 257장
  - 칸쵸 : 333장

#### 중강
1. 수평 뒤집기
2. 회전(+15도, -15도)
3. Grayscale 15%

증강결과 총 **2066장**

#### 전처리
이미지 640*640으로 resize

#### 셋 비율
- train set : 1844장
- vaild set : 164장
- test set : 58장

## 3. 데이터베이스
#### 1) XAMPP 설치

[XAMPP 다운로드](https://www.apachefriends.org/)

#### 2) 사용자와 비밀번호 생성
php 파일에 연결하는 사용자와 비밀번호를 생성한다. 본 프로젝트에서는 root를 사용자로 사용. 

#### 3) 원격 접속을 위한 세팅
1. MySQL 설정 파일 수정


먼저 MySQL 설정 파일에서 MySQL이 모든 IP 주소에서의 접속을 허용하도록 설정

설정 파일 열기 (my.cnf 또는 mysqld.cnf):

    sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
    
bind-address 항목을 찾고 0.0.0.0으로 변경

    bind-address = 0.0.0.0

2. MySQL 서버 재시작

변경 사항을 적용하기 위해 MySQL 서버를 재시작

    sudo systemctl restart mysql

3. 원격 사용자에게 권한 부여

원격에서 접속할 사용자가 MySQL에 접속할 수 있도록 권한을 설정


4. 방화벽 설정

원격 접속을 위해 MySQL이 사용하는 포트(기본적으로 3306번 포트)를 열어야 합니다.

    sudo ufw allow 3306/tcp
    sudo ufw status
    sudo ufw enable

5. 원격에서 MySQL 접속

원격에서 MySQL에 접속하려면 다음 명령을 사용

    mysql -u username -p -h MySQL서버_IP주소

#### 4) 테이블 생성
<p align="center">
  <a href="">
  <img src="https://github.com/StealthBlack66/Smart_shopping/blob/main/image/테이블.png" alt="테이블" width="auto" height="auto">
  </a></p>

#### 5) php 파일 생성
- cart.php
