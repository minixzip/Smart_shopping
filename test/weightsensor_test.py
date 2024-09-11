#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

# 무게 센서 GPIO 핀 설정
GPIO.setmode(GPIO.BSD)
DT = 17
SCK = 27
sample=0
pre_gram=0

def get_weight():
    i=0
    Count=0
    GPIO.setup(DT,GPIO.OUT)
    GPIO.output(DT,1)
    GPIO.output(SCK,0)
    GPIO.setup(DT,GPIO.IN)
    while GPIO.input(DT)==1:
        i=0
    for i in range(24):
        GPIO.output(SCK,1)
        Count=Count<<1
        GPIO.output(SCK,0)
        if GPIO.input(DT)==0:
            Count=Count+1
    GPIO.output(SCK,1)
    Count=Count^0x800000
    GPIO.output(SCK,0)
    
    return Count

def send_weight():
    global pre_gram    
    w=0
    result_gram=0
    count=[]
    plus=[]
    minus=[]
    equal=[]
    for each in range(3):
        count.append(get_weight())
        time.sleep(0.5)
    
    cntArr={"+":0, "-":0, "=":0}
    
    for i in range(len(count)):
        w=((sample-count[i])/106)
    
#        print('round gram',round(w))
        gram=max(0,round(w))
#        print('gram[',i+1,']',gram,'g')
        count[i] = gram
        result_gram=gram-pre_gram
#        print('gram[',i+1,']',result_gram,'error g')
        if result_gram>80:
            cntArr['+'] += 1
            plus.append(count[i])
        elif result_gram<-80:
            cntArr['-'] += 1
            minus.append(count[i])
        else:
            cntArr['='] += 1
            equal.append(count[i])
    
    Max = cntArr["+"]
    MaxK = "+"
    for (eachK,eachV) in cntArr.items():
        if eachV > Max:
            Max = eachV
            MaxK = eachK
            

    if MaxK=="+": #plus min
        pre_gram = min(plus)
    elif MaxK =="-":# minus max
        pre_gram = max(minus)
    else:#equal min
        pre_gram = min(equal)
    print(MaxK)
    return MaxK

print("무게 감지 시작")

try:
    while True:
        GPIO.setup(SCK,GPIO.OUT)
        print(f"Weight: {send_weight()}")
        time.sleep(1)
except KeyboardInterrupt:
    print("무게 센서 종료")
    GPIO.cleanup()