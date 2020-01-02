import RPi.GPIO as io
from valuesnpins import *
face=0
def motor():
    io.setmode(io.BCM)
    io.setwarnings(False)
    for i in range(4):
	io.setup(motordir[i],io.OUT)
	io.setup(motorpwm[i],io.OUT)
	motorin[i] = io.PWM(motorpwm[i],90)
	motorin[i].start(0)
	motorin[i].ChangeDutyCycle(0)
                
def setmotor(number,pwmvalue,d):
    io.output(motordir[number],d)
    motorin[number].ChangeDutyCycle(pwmvalue)
def forward():
	print "forward"
	face=0
	if face==0:
		for i in range(4):
			setmotor(i,sp[i],0)
	elif face==1:
		setmotor(0,sp[0],0)
		setmotor(1,sp[1],1)
		setmotor(2,sp[2],0)
		setmotor(3,sp[3],1)
	elif face==2:
		setmotor(0,sp[0],1)
		setmotor(1,sp[1],1)
		setmotor(2,sp[2],1)
		setmotor(3,sp[3],1)
	elif face==3:
		setmotor(0,sp[0],1)
		setmotor(1,sp[1],0)
		setmotor(2,sp[2],1)
		setmotor(3,sp[3],0)
def left():
	print "left"
	if face==0:
		setmotor(0,sp[0],1)
		setmotor(1,sp[1],0)
		setmotor(2,sp[2],1)
		setmotor(3,sp[3],0)
	elif face==1:
		for i in range(4):
			setmotor(i,sp[i],0)
	elif face==2:
		setmotor(0,sp[0],0)
		setmotor(1,sp[1],1)
		setmotor(2,sp[2],0)
		setmotor(3,sp[3],1)
	elif face==3:
		for i in range(4):
			setmotor(i,sp[i],1)
		
def right():
	print "right"
	if face==0:
		setmotor(0,sp[0],0)
		setmotor(1,sp[1],1)
		setmotor(2,sp[2],0)
		setmotor(3,sp[3],1)
	elif face==1:
		for i in range(4):
			setmotor(i,sp[i],1)
	elif face==2:
		setmotor(0,sp[0],1)
		setmotor(1,sp[1],0)
		setmotor(2,sp[2],1)
		setmotor(3,sp[3],0)
	elif face==3:
		for i in range(4):
			setmotor(i,sp[i],0)
	
		
def backright():
	if face==0:
		setmotor(0,sp[0],0)
		setmotor(1,sp[1],0)
		setmotor(2,sp[2]+cf,1)
		setmotor(3,sp[3]+cf,0)
	elif face==1:
		setmotor(0,sp[0]+cf,0)
		setmotor(1,sp[1],1)
		setmotor(2,sp[2],0)
		setmotor(3,sp[3]+cf,0)
	elif face==2:
		setmotor(0,sp[0]+cf,0)
		setmotor(1,sp[1]+cf,1)
		setmotor(2,sp[2],1)
		setmotor(3,sp[3],1)
	elif face==3:
		setmotor(0,sp[0],1)
		setmotor(1,sp[1]+cf,1)
		setmotor(2,sp[2]+cf,1)
		setmotor(3,sp[3],0)		
def backleft():
	if face==0:
		setmotor(0,sp[0],0)
		setmotor(1,sp[1],0)
		setmotor(2,sp[2]+cf,0)
		setmotor(3,sp[3]+cf,1)
	elif face==1:
		setmotor(0,sp[0]+cf,1)
		setmotor(1,sp[1],1)
		setmotor(2,sp[2],0)
		setmotor(3,sp[3]+cf,0)
	elif face==2:
		setmotor(0,sp[0]+cf,1)
		setmotor(1,sp[1]+cf,0)
		setmotor(2,sp[2],1)
		setmotor(3,sp[3],1)
	elif face==3:
		setmotor(0,sp[0],1)
		setmotor(1,sp[1]+cf,0)
		setmotor(2,sp[2]+cf,0)
		setmotor(3,sp[3],0)		
def stop():
    for i in range(4):
        setmotor(i,0,0)
#motor()
