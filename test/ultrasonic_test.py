#!/usr/bin/env pyhton
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# 초음파 센서 GPIO 핀 설정
TRIG_PINS = [2, 5, 7]
ECHO_PINS = [3, 6, 8]

for TRIG, ECHO in zip(TRIG_PINS, ECHO_PINS):
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def get_distance(trig_pin, echo_pin):
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)
    
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()
    
    while GPIO.input(echo_pin) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
