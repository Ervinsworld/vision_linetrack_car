from pyb import Pin, Timer, delay
inverse_left=False
inverse_right=True
left =  Pin('P7', Pin.OUT_PP)
right =  Pin('P8', Pin.OUT_PP)
left.low()
right.low()
tim = Timer(4, freq=100)
ch1 = tim.channel(1, Timer.PWM, pin=left)
ch2 = tim.channel(2, Timer.PWM, pin=right)
ch1.pulse_width(2880)
ch2.pulse_width(2880)
delay(5000)
def run(left_speed, right_speed):
    if left_speed>0:
        left_speed+=40
    elif left_speed<0:
        left_speed-=40
    else:
        left_speed=0

    if right_speed>0:
        right_speed+=40
    elif right_speed<0:
        right_speed-=40
    else:
        right_speed=0

    ch1.pulse_width(2880+int(abs(left_speed)))
    ch2.pulse_width(2880-int(abs(right_speed)))