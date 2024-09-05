#!/usr/bin/env pyhton
import RPi.GPIO as GPIO
from hx711 import HX711

# 무게 센서 GPIO 핀 설정
DT_PIN = 17
SCK_PIN = 27

hx = HX711(DT_PIN, SCK_PIN)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()
hx.tare()

print("Tare done! Add weight now...")

try:
    while True:
        val = hx.get_weight(5)
        print(f"Weight: {val} g")
        hx.power_down()
        hx.power_up()
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()