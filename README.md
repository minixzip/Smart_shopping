<h1 align="center">스마트 쇼핑카트</h1>
<br>
<p align="center">
  <a href="https://github.com/abhishekapk/SMART-PARKING-SYSTEM">
    <img src="https://storage.googleapis.com/cdn.media.bluedot.so/bluedot.techsnack/2022/07/%EC%95%84%EB%A7%88%EC%A1%B4_%EB%8C%80%EC%8B%9C%EC%B9%B4%ED%8A%B8_%ED%99%80%ED%91%B8%EB%93%9C.JPG" alt="Logo" width="auto" height="auto">
  </a></p>
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
 
 - 초음파 센서 : 들어오고 나가는 상품들을 탐지한다.
 - 파이카메라 : 상품 인식
 - 라즈베리파이 : 메인 서버와 카트의 통신 담당
 - 무게 센서 : 상품들의 무게 측정

동작순서는 다음과 같다. 

쇼핑카트와 본인의 스마트폰 연결 -- 상품을 담거나 빼면 초음파 센서가이를 인식 해서 현재 화면을 라즈베리파이에 저장 -- 신호를 받은 서베에서 라즈베리파이의 화면을 읽어온다 -- 인공지능을 이용해 카트 현황(상품의 종류 및 수량)을 판단 -- 판단 내용을 안드로이드 앱으로 전달 -- 앱의 장바구니를 해당 데이터에 따라 수정 -- 쇼핑이 끝나면 안드로이드 앱을 통해 결제
 
 </p>
<br>
<h2>객체 탐지 모델 </h2>
<p align="justify">그리드 기반의 객체 탐지 기술의 YOLO 라이브러리를 이용하여 카트 현황을 판단한다. 어떤 상품이 얼만큼 들어왔거나 나갔는 지를 정확하게 판단하는 것이 목적이다. 
</p>
<br>
<h4>1) YOLO 동작과정</h4>
<p align="center">
  <a href="">
    <img src="https://blog.kakaocdn.net/dn/bu6BVv/btrSHXxejru/98bLdWyukyzkzsAfLh5Q8k/img.png" alt="Block Diagram" width="auto" height="auto">
  </a></p>
<br>
<p align="justify">먼저 사진이 입력되면  가로 세로를 동일한 그리드 영역으로 나눈다. 


그 후 각 그리드 영역에 대해서 어디에 사물이 존재하는지 바운딩박스와 박스에 대한 신뢰도 점수를 예측한다. 신뢰도가 높을수록 굵게 박스를 그려 준다. 이와 동시에 (2)에서와 같이 어떤 사물인지에 대한 classification작업이 동시에 진행된다.


그러면 굵은 박스들만 남기고 얇은 것들 즉, 사물이 있을 확률이 낮은 것들은 지워 준다.
 

최종 경계박스들을  NMS(Non- Maximum Suppression) 알고리즘을 이용해 선별하면 (4) 이미지처럼 3개만 남게 된다.
</p>
<h4>2) 모델 훈련방식</h4>
<p align="justify">

- 상품 클래스 : 5개()
- 클래스 당 데이터 개수 : 300장

YOLO-mark를 이용해 학습데이터 리사이징과 라벨링 등의 전처리

</p>
<br>
<h2>알고리즘 구조</h2>
<p align="justify">
<br>
<p align="center">
  <a href="">
    <img src="https://github.com/StealthBlack66/Smart_shopping/blob/main/image/System Diagram.png" alt="Algorithm" width="auto" height="auto">
  </a></p>
<br>
<h2>사용 모듈</h2>
<p align="justify">

|spec|Component|
|--|--|
|HW|RaspberryPi|
|  |PiCamera|
|  |Ultrasonic distance sensor|
|  |Weight sensor|
|  |Raspbian OS|
|  |Python|
|  |MJPG-streamer|
|Server|YOLO|
|Android|Android|
|       |JDK|
|Database|Apache|
|        |MySQL|
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