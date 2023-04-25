THRESHOLD = (70, 255) # Grayscale threshold for dark things...
import sensor, image, time
from pyb import LED
import car
from pid import PID
rho_pid = PID(p=0.4, i=0)
theta_pid = PID(p=0.001, i=0)

LED(1).on()
LED(2).on()
LED(3).on()

scaler = 50

sensor.reset()
sensor.set_vflip(True)
sensor.set_hmirror(False)
sensor.set_transpose(True)
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQQVGA) # 80x60 (4,800 pixels) - O(N^2) max = 2,3040,000.
#sensor.set_windowing([0,20,80,40])
sensor.skip_frames(time = 2000)     # WARNING: If you use QQVGA it may take seconds
clock = time.clock()                # to process a frame sometimes.

while(True):
    clock.tick()
    img = sensor.snapshot()
    img.binary([THRESHOLD])
    img.erode(1)
    line = img.get_regression([(255, 255)], robust = True)
    if (line):
        rho_err = abs(line.rho())-img.width()/2
        if line.theta()>90:
            theta_err = line.theta()-180
        else:
            theta_err = line.theta()
        img.draw_line(line.line(), color = 127)
        #print(rho_err,line.magnitude(),rho_err)
        if line.magnitude()>8:
            #if -40<b_err<40 and -30<t_err<30:
            rho_output = rho_pid.get_pid(rho_err, scaler)
            theta_output = theta_pid.get_pid(theta_err, scaler)
            output = rho_output+theta_output
            print(output)
            if output>90:
                output = 90
            car.run(output, output)
        else:
            car.run(0, 0)
    else:
        car.run(10, -10)
        pass
    #print(clock.fps())
