import RPi.GPIO as io
import Adafruit_MCP3008
import time
import cPickle as pickle
from valuesnpins import *
from readsensor import *
state=0
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
def rotate(i):
        if i>0:
                setmotor(0,sp[0],1)
                setmotor(1,sp[1],0)
                setmotor(2,sp[2],0)
                setmotor(3,sp[3],1)
        else :
                setmotor(0,sp[0],0)
                setmotor(1,sp[1],1)
                setmotor(2,sp[2],1)
                setmotor(3,sp[3],0)
def stop():
	setmotor(0,0,0)
	setmotor(1,0,0)
	setmotor(2,0,0)
	setmotor(3,0,0)
def calibrate():
	print('Reading Front values, press Ctrl-C to quit...')
	print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
	print('-' * 57)
	#rotate()
	x=time.time()
	u=1
	while True:
                rotate(u)
		for k in range(4):
			read_sensor(k)
			for i in range(8):
				if values[k][i] <= mini[k][i]:
					mini[k][i] = values[k][i]
				if values[k][i] > maxi[k][i]:
					maxi[k][i] = values[k][i]
		time.sleep(0.1)
	# Print the ADC values.
	#print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
                
		if time.time()-x >7:
			break

	#print(mini)
	#print(maxi)
	for j in range(4):
		for i in range(8):
			avg[j][i] = (mini[j][i] + maxi[j][i]) / 2
	print " -----------------------------"	
	for i in range(4):
		print maxi[i]
	print " -----------------------------"
	for i in range(4):
		print mini[i]
	print " -----------------------------"
	for i in range(4):
		print avg[i]
	filer = open('avgline', "wb")
	pickle.dump(avg, filer)
	filer.close()
	filer = open('maxi', "wb")
	pickle.dump(maxi, filer)
	filer.close()
	filer = open('mini', "wb")
	pickle.dump(mini, filer)
	filer.close()
	filer = open('state', "wb")
	pickle.dump(state, filer)
	filer.close()
	time.sleep(1)
motor()
calibrate()
stop()

