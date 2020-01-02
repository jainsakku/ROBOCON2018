import RPi.GPIO as io
import Adafruit_MCP3008
import time
import cPickle as pickle
from valuesnpins import *

def motor():
    io.setmode(io.BCM)
    io.setwarnings(False)
    for i in range(4):
		io.setup(motordir[i],io.OUT)
		io.setup(motorpwm[i],io.OUT)
		motorin[i] = io.PWM(motorpwm[i],500)
		motorin[i].start(0)
		motorin[i].ChangeDutyCycle(0)
                
def setmotor(number,pwmvalue,d):
    io.output(motordir[number],d)
    motorin[number].ChangeDutyCycle(pwmvalue)
def slowforward():
        for i in range(4):
                setmotor(i,sp[i]-20,0)
def backward(m=0):
	print "backward"
	if face==0:
		for i in range(4):
			setmotor(i,sp[i]-m,1)
def forward(m=0):
	print "forward"
	if face==0:
		for i in range(4):
			setmotor(i,sp[i]-m,0)
	elif face==1:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]-m,1)
	elif face==2:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]-m,1)
	elif face==3:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]-m,0)
def left(m=0):
	print "left"
	if face==0:
		setmotor(0,sp[0]-sf-m,1)
		setmotor(1,sp[1]-sf-m,0)
		setmotor(2,sp[2]-sf-m,1)
		setmotor(3,sp[3]-sf-m,0)
	elif face==1:
		for i in range(4):
			setmotor(i,sp[i]-sf-m,0)
	elif face==2:
		setmotor(0,sp[0]-sf-m,0)
		setmotor(1,sp[1]-sf-m,1)
		setmotor(2,sp[2]-sf-m,0)
		setmotor(3,sp[3]-sf-m,1)
	elif face==3:
		for i in range(4):
			setmotor(i,sp[i]-sf-m,1)
		
def right(m=0):
	print "right"
	if face==0:
		setmotor(0,sp[0]-sf-m,0)
		setmotor(1,sp[1]-sf-m,1)
		setmotor(2,sp[2]-sf-m,0)
		setmotor(3,sp[3]-sf-m,1)
	elif face==1:
		for i in range(4):
			setmotor(i,sp[i]-sf-m,1)
	elif face==2:
		setmotor(0,sp[0]-sf-m,1)
		setmotor(1,sp[1]-sf-m,0)
		setmotor(2,sp[2]-sf-m,1)
		setmotor(3,sp[3]-sf-m,0)
	elif face==3:
		for i in range(4):
			setmotor(i,sp[i]-sf-m,0)
	
		
def backright(m=0):
	if face==0:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]+cf-m,1)
		setmotor(3,sp[3]+cf-m,0)
	elif face==1:
		setmotor(0,sp[0]+cf-m,0)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]+cf-m,0)
	elif face==2:
		setmotor(0,sp[0]+cf-m,0)
		setmotor(1,sp[1]+cf-m,1)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]-m,1)
	elif face==3:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]+cf-m,1)
		setmotor(2,sp[2]+cf-m,1)
		setmotor(3,sp[3]-m,0)		
def backleft(m=0):
	if face==0:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]+cf-m,0)
		setmotor(3,sp[3]+cf-m,1)
	elif face==1:
		setmotor(0,sp[0]+cf-m,1)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]+cf-m,1)
	elif face==2:
		setmotor(0,sp[0]+cf-m,1)
		setmotor(1,sp[1]+cf-m,0)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]-m,1)
	elif face==3:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]+cf-m,0)
		setmotor(2,sp[2]+cf-m,0)
		setmotor(3,sp[3]-m,0)		
def stop():
    for i in range(4):
        setmotor(i,0,0)
def read_sensor(i):
	index = 0
	for j in range(8):
		if i == 3:
			index = j
		else:
			index = j
		values[i][index] = mcp[i].read_adc(index)

def biCalculate():
	for k in range(4):
		read_sensor(k)
		print values[k]
		print avg[k]
		print "while averaging:.."
		for i in range(8):
			#print values[k][i], avg[k][i]
			if values[k][i]<=avg[k][i]:
				bi[k][i]=0
			else:
				bi[k][i]=1
	print "nikal gaya"

def align():
	
	face=0
	while(not(bi[face][3]==1 and bi[face][4] ==1 and  bi[(face+2)%4][3]==1 and bi[(face+2)%4][4]==1 and bi[(face+1)%4][3]==1 and bi[(face+3)%4][4]==1 and bi[(face+3)%4][3]==1 and bi[(face+3)%4][4]==1)):
		while True:
			biCalculate()
			if ( bi[face][3]==1 and bi[face][4] ==1) :
				if( bi[(face+2)%4][0]==1 or bi[(face+2)%4][1]==1 or bi[(face+2)%4][2]==1):
			   		backleft(18)
				elif( bi[(face+2)%4][5]==1 or bi[(face+2)%4][6]==1 or bi[(face+2)%4][7]==1):
					backright(18)
				elif ( bi[(face+2)%4][3]==1 and bi[(face+2)%4][4]==1):
					stop()
					break
				

			elif( bi[face][0]==1 or bi[face][1]==1 or bi[face][2]==1) :
				left(10)
			elif( bi[face][5]==1 or bi[face][6]==1 or bi[face][7]==1) :
				right(10)
		print "ALIGNED"
		while True: 
			biCalculate()     
			if ((bi[(face+1)%4][3]==1 and bi[(face+3)%4][4]==1) and (bi[(face+3)%4][3]==1 and bi[(face+3)%4][4]==1)):
				stop()
				break
			elif((bi[(face+1)%4][6]==1 or bi[(face+1)%4][7]==1) or (bi[(face+3)%4][1]==1 or bi[(face+3)%4][0]==1)):
				backward(20)
			elif((bi[(face+1)%4][0]==1 or bi[(face+1)%4][1]==1) or (bi[(face+3)%4][6]==1 or bi[(face+3)%4][7]==1)):
				forward(20)
			else:
				forward(20)
		biCalculate()
def conditioncheck() :
	print "checking condition..."
	biCalculate()
	global node
	global snodes
	for i in range(4):
		print(bi[i])
	print face
	if  bi[face][2]==1 and bi[face][3]==1 and bi[face][4]==1 and bi[face][5]==1 :
                        forward()
                        if ( snodes==0):
                                flag=1
                        else:
                                snodes=snodes-1
                                while( bi[face][2]==1 and bi[face][3]==1 and bi[face][4]==1 and bi[face][5]==1 ) :
                                        biCalculate()
                                        forward()
	elif bi[face][3]==1 or bi[face][4]==1 :
		biCalculate()
		if (bi[(face + 2) % 4][3]==1 or bi[(face + 2) % 4][4]==1) :
			forward()
		elif bi[(face + 2) % 4][0]==1 or bi[(face + 2) % 4][1]==1 or bi[(face + 2) % 4][2]==1:
			backleft()
		elif bi[(face + 2) % 4][5]==1 or bi[(face + 2) % 4][6]==1 or bi[(face + 2) % 4][7]==1:
			backright()
		else:
			forward()

	elif bi[face][0]==1 or bi[face][1]==1 or bi[face][2]==1 :
		left()
	elif bi[face][5]==1 or bi[face][6]==1 or bi[face][7]==1 :
		right()
	else:
		print "stop case"
		stop()
	global flag
	
	if flag==1:
		print "check"
		if (bi[(face+3)%4][0]==1 or bi[(face+3)%4][1]==1 or bi[(face+3)%4][2]==1 or bi[(face+3)%4][3]==1 or bi[(face+3)%4][4]==1 or bi[(face+3)%4][5]==1 or bi[(face+3)%4][6]==1 or bi[(face+3)%4][7]==1) and ( bi[(face+1)%4][0]==1 or bi[(face+1)%4][1]==1 or bi[(face+1)%4][2]==1 or bi[(face+1)%4][3]==1 or bi[(face+1)%4][4]==1 or bi[(face+1)%4][5]==1 or bi[(face+1)%4][6]==1 or bi[(face+1)%4][7]==1 ) :
			node = node + 1
			flag=0
		
	return node
def specialconditioncheck() :
	print "checking condition..."
	biCalculate()
	global node
	for i in range(4):
		print(bi[i])
	print face
	if bi[face][3]==1 or bi[face][4]==1 :
		biCalculate()
		if (bi[(face + 2) % 4][3]==1 or bi[(face + 2) % 4][4]==1) :
			forward()
		elif bi[(face + 2) % 4][0]==1 or bi[(face + 2) % 4][1]==1 or bi[(face + 2) % 4][2]==1:
			backleft()
		elif bi[(face + 2) % 4][5]==1 or bi[(face + 2) % 4][6]==1 or bi[(face + 2) % 4][7]==1:
			backright()

	elif bi[face][0]==1 or bi[face][1]==1 or bi[face][2]==1 :
		left()
	elif bi[face][5]==1 or bi[face][6]==1 or bi[face][7]==1 :
		right()
	else:
		while True:
			slowforward()
			print ("SPECIAL")
			print (face)
			biCalculate()
			if (bi[(face+1)%4][2]==1 or bi[(face+1)%4][3]==1 or bi[(face+1)%4][4]==1 or bi[(face+1)%4][5]==1 ):
				print("IF K ANDR")
				node=node+1
				break
		
	return node
	
def initialfunc():
        motor()
        global avg
        filer = open('avgline', "rb")
        avg = pickle.load(filer)
        for i in range(4):
                print avg[i]
        filer.close()
def mainfunc(f,s,special=0):
        global node,face,snodes
        node=0
        snodes=s
        face=f
        if special==0:
                while conditioncheck() == 0:
                    pass
        else:
                while specialconditioncheck() == 0:
                    pass    
        
"""
initialfunc()
while True:
	conditioncheck()
	#time.sleep(0.1)
"""

