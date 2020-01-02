#!/usr/bin/env python

import RPi.GPIO as io
import Adafruit_MCP3008
import time
import cPickle as pickle
import numpy as np

if __name__ == "__main__":

######################################################################################
#MCP 3008
	CS =[25, 22, 27, 10, 14]
	mcp = [Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS[0], miso = MISO, mosi = MOSI)] * 5

	for i in range(5):
		mcp[i] = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS[i], miso=MISO, mosi=MOSI)
#####################################################################################


	# The test algo goes here
		#Initializing the variables
	#analog input mcp index 4
'''
	face=req.face
'''
	# get required pwm here
	# do not set direction it is to be done by forward(), only maintain pwm
	temp_pwm=[50,50,50,50]
'''
	temp_pwm[face]=temp_pwm[face]+req.pwm[face]
	temp_pwm[(face+2)%4]=temp_pwm[(face+2)%4]+req.pwm[(face+2)%4]
'''
	# temp

######################################################
	# pin numbers have to be updated
	
	m11 =3
	m21 =11
	m31 =8
	m41 =5
	
	m12 =motordir[0]
	m22 =motordir[1]
	m32 =motordir[2]
	m42 =motordir[3]
######################################################

	pwm=[50,50,50,50]
'''
	pwm[face]=pwm[face]+req.pwm[face]
	pwm[(face+2)%4]=pwm[(face+2)%4]+req.pwm[(face+2)%4]
'''
	# get required pwm
	thresh=800
	spd=50
	kp=3

			#These variables were not initialized in the original program (caution)
	flag=[False,False,False,False]
	count=[0,0,0,0]
	vals = [[False for _ in range(1000)]for _1 in range(4)]
	startt=0
	diff=0
	prev=[0,0,0,0]

		#Setting up the gpio
	io.setmode(io.BCM)
    	io.setwarnings(False)


	io.setup(m11,io.OUT)
	io.setup(m21,io.OUT)
	io.setup(m31,io.OUT)
	io.setup(m41,io.OUT)

	io.setup(m12,io.OUT)
	io.setup(m22,io.OUT)
	io.setup(m32,io.OUT)
	io.setup(m42,io.OUT)
	
	pm12=io.PWM(m12,90)
	pm22=io.PWM(m22,90)
	pm32=io.PWM(m32,90)
	pm42=io.PWM(m42,90)

	pm12.start(0)
	pm22.start(0)
	pm32.start(0)
	pm42.start(0)

	pm12.ChangeDutyCycle(0)
	pm22.ChangeDutyCycle(0)
	pm32.ChangeDutyCycle(0)
	pm42.ChangeDutyCycle(0)

	while(True):
		i=0
		for i in range(4):
			######################################################################################
			en[i] = mcp[4].read_adc(i*2)
			#Reading encoder values ##############################################################

		for _ in range(4):
			flag[_]=False
			count[_]=0

		for _ in range(1000):
			for _1 range(4):
				vals[_][_1]=en[_1]
		
		for _ in range(1000):
			for _1 range(4):
				if not vals[_][_1]== flag[_1]:
					if vals[_][_1]==True:
						count[_1]+=1
					vals[_][_1]= flag[_1]
		for i in range(4):
    			prev[i]=temp_pwm[i]-pwm[i]

		for i in range(4):
      			factor = int((count[i] -40)/kp)
      			temp_pwm[i] = pwm[i] - factor + prev[i]
      			print "%s-%s=%s |	"%(factor,prev[i],temp_pwm[i])

		pm12.ChangeDutyCycle(temp_pwm[0])
		pm22.ChangeDutyCycle(temp_pwm[1])
		pm32.ChangeDutyCycle(temp_pwm[2])
		pm42.ChangeDutyCycle(temp_pwm[3])
		
		print "------------"


