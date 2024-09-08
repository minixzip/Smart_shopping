#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 초음파 센서 GPIO 핀 설정
TRIG_PINS = [2, 5, 7]
ECHO_PINS = [3, 6, 8]
result = [500,500,500]
print('초음파 거리 측정')

for i in range(3):
    GPIO.setup(TRIG_PINS[i], GPIO.OUT)
    GPIO.setup(ECHO_PINS[i], GPIO.IN)
    GPIO.output(TRIG_PINS[i], GPIO.LOW)

def get_distance(num):
    GPIO.output(TRIG_PINS[num], False)
    print('초음파 출력 초기화')
    time.sleep(0.01)
    GPIO.output(TRIG_PINS[num], True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PINS[num], False)
    
    while GPIO.input(ECHO_PINS[num]) == 0:
        start_time = time.time()
    
    while GPIO.input(ECHO_PINS[num]) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
    dis = round(time_elapsed*17000,2)
    
try:
    while True:
        for i in range(3):
            result[i] = get_distance(i)
            
            if result[i]<30 and result[i] >=3:
                print(f'센서{i+1} 거리는 {result[i]}cm')
        
        
except KeyboardInterrupt:
    print('거리 측정 완료')
    GPIO.cleanup()