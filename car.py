# duty中位：75
# 左轮正:75+, 右轮正:75-

from machine import Timer,PWM
import time
#PWM 通过定时器配置，接到 IO9 引脚
tim1 = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
tim2 = Timer(Timer.TIMER1, Timer.CHANNEL1, mode=Timer.MODE_PWM)

left = PWM(tim1, freq=500, duty=50, pin=8)
right = PWM(tim2, freq=500, duty=50, pin=10)
#循环发出不同频率响声。
left.duty(75)
right.duty(75)
time.sleep(5)

def run(left_speed, right_speed):
    left.duty(75+left_speed)
    right.duty(75-right_speed)
