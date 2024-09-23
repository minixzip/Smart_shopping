import RPi.GPIO as GPIO
import time
import os
import requests
import subprocess

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 초음파 센서 핀 설정
TRIG = 2
ECHO = 3

# 무게 센서 핀 설정
DT = 17
SCK = 27
sample = 0
pre_weight = 0

# 초음파 센서 설정
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# 무게 센서 설정
def get_weight():
    i = 0
    Count = 0
    GPIO.setup(DT, GPIO.OUT)
    GPIO.output(DT, 1)
    GPIO.output(SCK, 0)
    GPIO.setup(DT, GPIO.IN)
    while GPIO.input(DT) == 1:
        i = 0
    for i in range(24):
        GPIO.output(SCK, 1)
        Count = Count << 1
        GPIO.output(SCK, 0)
        if GPIO.input(DT) == 0:
            Count = Count + 1
    GPIO.output(SCK, 1)
    Count = Count ^ 0x800000
    GPIO.output(SCK, 0)
    
    return Count

# 초음파 거리 측정 함수
def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2  # 거리 계산 (cm)
    return distance

# 메인 함수
def main():
    global pre_weight
    
    # mjpeg_server_2.py 실행
    print("mjpeg_server_2.py loading...")
    mjpeg_server_proc = subprocess.Popen(["python", "~/mjpeg_server_2.py"])

    try:
        while True:
            distance = measure_distance()
            print(f"Distance: {distance} cm")
            
            # 3~30cm 이내에 물체가 감지되면
            if 3 <= distance <= 30:
                # YOLOv5 탐지 결과 디렉토리 삭제
                print("initing detect exp...")
                subprocess.run(["rm", "-rf", "~/yolov5/runs/detect/exp/"], check=True)
                
                # cart.php 실행
                print("cart.php loading...")
                subprocess.run(["xdg-open", "http://localhost/cart.php"])
                
                # yolov5 탐지 실행
                print("YOLOv5 detecting...")
                subprocess.run(["python3", "~/yolov5/detect_new.py", 
                                "--source", "http://localhost:8000/stream.mjpg", 
                                "--weights", "~/yolov5/cart_best.pt", 
                                "--conf", "0.25"], check=True)
                
            
            
            # 무게 변화 감지
            # weight = get_weight()
            # weight_difference = abs((sample - weight) / 106) - pre_weight
            
            # if abs(weight_difference) > 50:  # 50g 이상의 무게 변화 감지
                # print(f"무게 변화 감지됨: {weight_difference} g")
                
                # cart.php 새로고침
                print("cart.php reloading")
                subprocess.run(["xdg-open", "http://localhost/cart.php"])
                
                
                # 무게 업데이트
                # pre_weight = weight_difference
            
            time.sleep(1)  # 1초 대기

    except KeyboardInterrupt:
        print("The end")
        
    finally:
        # mjpeg_server_2.py 종료
        print("mjpeg_server_2.py exiting")
        mjpeg_server_proc.terminate()
        mjpeg_server_proc.wait()  # 프로세스가 종료될 때까지 대기
        GPIO.cleanup()

if __name__ == '__main__':
    main()
