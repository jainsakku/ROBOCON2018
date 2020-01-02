import RPi.GPIO as io
import time
motordir=15
motorpwm=14
def test():
    io.setmode(io.BCM)
    io.setwarnings(False)
    io.setup(motordir,io.OUT)
    io.setup(motorpwm,io.OUT)
    motorin = io.PWM(motorpwm,1000)
    motorin.start(0)
    time.sleep(2)
    io.output(motordir,0)
    motorin.ChangeDutyCycle(20)
    time.sleep(5)
    print "ruk"
    motorin = io.PWM(motorpwm,1000)
    io.output(motordir,0)
    motorin.ChangeDutyCycle(0)

test()
