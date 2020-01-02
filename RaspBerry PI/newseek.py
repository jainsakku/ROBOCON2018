import RPi.GPIO as io
import Adafruit_MCP3008
import time
import cPickle as pickle
from valuesnpins import *
from numpy import interp
import copy

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
def slowforward(x_sf=20,direction=0):
        for i in range(4):
                setmotor(i,sp[i]-x_sf,direction)
def diag(m=0):
	setmotor(0,sp[0],0)
	setmotor(1,0,0)
	setmotor(2,sp[2],0)
	setmotor(3,0,0)
def backward(m=0):
#	print "backward"
	if face==0:
		for i in range(4):
			setmotor(i,sp[i]-m,1)
	elif face==1:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]-m,0)
	elif face==2:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]-m,0)
	elif face==3:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]-m,1)

def travel(x):
	global prevbi
	global face
#	print "forward"
	biCalculate()
	if (summ[face]==0):
		if (prevbi[face][0]==1 or prevbi[face][1]==1 or prevbi[face][2]==1):
			while (summ[face]==0):
				#print "front right"
				frontright()
				biCalculate()
		elif (prevbi[face][5]==1 or prevbi[face][6]==1 or prevbi[face][7]==1):
			while (summ[face]==0):
				#print "front left"
				frontleft()
				biCalculate()
	elif (summ[(face+2)%4]==0):
		if (prevbi[(face+2)%4][0]==1 or prevbi[(face+2)%4][1]==1 or prevbi[(face+2)%4][2]==1):
			while (summ[(face+2)%4]==0):
				#print "back left"
				backleft()
				biCalculate()
		elif (prevbi[(face+2)%4][5]==1 or prevbi[(face+2)%4][6]==1 or prevbi[(face+2)%4][7]==1):
			while (summ[(face+2)%4]==0):
				#print "back right"
				backright()
				biCalculate()
	else:
		x1=x[face]
		x2=x[(face+2)%4]
		if face==0:
			setmotor(0,sp[0]+x1,0)
			setmotor(1,sp[1]-x1,0)
			setmotor(2,sp[2]-x2,0)
			setmotor(3,sp[3]+x1,0)
		elif face==1:
			setmotor(0,sp[0]+x2,0)
			setmotor(1,sp[1]+x1,1)
			setmotor(2,sp[2]-x1,0)
			setmotor(3,sp[3]-x2,1)
		elif face==2:
			setmotor(0,sp[0]-x2,1)
			setmotor(1,sp[1]+x2,1)
			setmotor(2,sp[2]+x1,1)
			setmotor(3,sp[3]-x1,1)
		elif face==3:
			setmotor(0,sp[0]-x1,1)
			setmotor(1,sp[1]-x2,0)
			setmotor(2,sp[2]+x2,1)
			setmotor(3,sp[3]+x1,0)

def forward(m=0):	
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
def backright(m=0):        #right se left jhatka
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
def backleft(m=0):         #left se right jhatka
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

def frontright(m=0):    #right se left jhatka
	if face==0:
		setmotor(0,sp[0]+cf-m,1)
		setmotor(1,sp[1]+cf-m,0)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]-m,0)
	elif face==1:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]+cf-m,0)
		setmotor(2,sp[2]+cf-m,0)
		setmotor(3,sp[3]-m,1)
	elif face==2:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]+cf-m,0)
		setmotor(3,sp[3]+cf-m,1)
	elif face==3:
		setmotor(0,sp[0]+cf-m,1)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]+cf-m,1)		
def frontleft(m=0):         #left se right jhatka
	if face==0:
		setmotor(0,sp[0]+cf-m,0)
		setmotor(1,sp[1]+cf-m,1)
		setmotor(2,sp[2]-m,0)
		setmotor(3,sp[3]-m,0)
	elif face==1:
		setmotor(0,sp[0]-m,0)
		setmotor(1,sp[1]+cf-m,1)
		setmotor(2,sp[2]+cf-m,1)
		setmotor(3,sp[3]-m,1)
	elif face==2:
		setmotor(0,sp[0]-m,1)
		setmotor(1,sp[1]-m,1)
		setmotor(2,sp[2]+cf-m,1)
		setmotor(3,sp[3]+cf-m,0)
	elif face==3:
		setmotor(0,sp[0]+cf-m,0)
		setmotor(1,sp[1]-m,0)
		setmotor(2,sp[2]-m,1)
		setmotor(3,sp[3]+cf-m,0)		

def stop():
	print "STOP"
	for i in range(4):
		setmotor(i,0,0)

def backslow():
	global face
	biCalculate()
	while(bi[(face+1)%4][3]==1 or bi[(face+1)%4][4]==1 or bi[(face+3)%4][3]==1 or bi[(face+3)%4][4]==1):
		biCalculate()
	backward(20)
	while(bi[(face+1)%4][3]==0 and bi[(face+1)%4][4]==0 and bi[(face+3)%4][3]==0 and bi[(face+3)%4][4]==0):
		biCalculate()
	stop()
	
def diagonal(): #movees diagonally in startingsequence
	global face , nodeDetected
	face=0
	biCalculate()
	diag(15)
	time.sleep(0.5)
	while(not(bi[(face+1)%4][4]==1 or bi[(face+1)%4][3]==1)):
		diag(15)
		biCalculate()
	face=1
	#forward()
	#time.sleep(0.5)
	biCalculate()
	while not (nodeDetected):
		poscalculate()
		travel(cfactor)
		biCalculate()
	stop()
	biCalculate()
def read_sensor(i):     #reads value from sensor
	index = 0
	for j in range(8):
		if i == 3:
			index = j
		else:
			index = j
		values[i][index] = mcp[i].read_adc(index)
		if values[i][index]>maxi[i][index]:
			values[i][index]=100
		elif values[i][index]<mini[i][index]:
			values[i][index]=0
		else:
			values[i][index]=interp(values[i][index],[mini[i][index],maxi[i][index]],[0,100])
#	print values[i],"\n"
#	print values

def biCalculate():        
	global prevbi
	global nodeDetected
	global summ
	#global face
	nodeDetected = False
	for i in range(4):
		prevbi[i] = bi[i][:]
	for k in range(4):
		read_sensor(k)
#		print values[k]
		#print avg[k]
		summ[k] = 0
		for i in range(8):
			#print values[k][i], avg[k][i]
			if values[k][i]<=50:
				bi[k][i]=0
			else:
				global face
				summ[k]+=1
				#if k==(face+1)%4 or k==(face+3)%4:
					#nodeDetected=True
				bi[k][i]=1
	if summ[(face+1)%4] >=2 or summ[(face+3)%4] >=2:
		nodeDetected = True

def poscalculate():
	global cfactor
	global correction
	for k in range(4):
		read_sensor(k)
		v = values[k]
		ma = max(v)
		gmin = min(v)
		d = ma - gmin
		p = v.index(ma)
		if not p==0 and not p==7 and not d==0:
			if v[p-1] <= v[p+1]:
				mi = v[p-1]
			else:
				mi = v[p+1]
			d = ma - mi
			n = v[p+1] - v[p-1]
			r = (n*1.0)/(d*2.0)
			pos[k] = p + r -3.5
		elif p == 0 and not d==0:
			n = d - v[p] + v[p+1]
			r = (n*1.0)/(d*2.0)
			pos[k] = p + r -3.5
		elif p == 7 and not d==0:
			n = d + v[p-1] - v[p]
			r = (n*1.0)/(d*2.0)
			pos[k] = p - r -3.5	
	cfactor=interp(pos ,[-3.5,3.5],[-correction,correction])

def align():
	face = 0
	#print "ALIGNING"
	poscalculate()
	global gap , ssp , factor , cfactor
	while pos[face] > gap or pos[face] < -gap or pos[(face+2)%4] > gap or pos[(face+2)%4] < -gap or pos[(face+1)%4] > gap or pos[(face+1)%4] < -gap or pos[(face+3)%4] > gap or pos[(face+3)%4] < -gap:
		face = 0
		#print "BIG WHILE"
		poscalculate()
		while pos[face] > gap or pos[face] < -gap or pos[(face+2)%4] > gap or pos[(face+2)%4] < -gap:
			cfactor = factor*interp(pos ,[-3.5,3.5],[-ssp,ssp])
			x1 = cfactor[face]
			x2 = cfactor[(face+2)%4]
			#print x1,x2
			if x1 < 0:
				setmotor(0,-x1,1)
				setmotor(1,-x1,0)
			else:
				setmotor(0,x1,0)
				setmotor(1,x1,1)
			if x2 < 0:
				setmotor(2,-x2,0)
				setmotor(3,-x2,1)
			else:
				setmotor(2,x2,1)
				setmotor(3,x2,0)
			poscalculate()

		face = 1
		poscalculate()
		while pos[face] > gap or pos[face] < -gap or pos[(face+2)%4] > gap or pos[(face+2)%4] < -gap:
			cfactor = factor*interp(pos ,[-3.5,3.5],[-ssp,ssp])
			x1 = cfactor[face]
			x2 = cfactor[(face+2)%4]
			#print x1,x2
			if x1 < 0:
				setmotor(1,-x1,0)
				setmotor(2,-x1,0)
			else:
				setmotor(1,x1,1)
				setmotor(2,x1,1)
			if x2 < 0:
				setmotor(0,-x2,1)
				setmotor(3,-x2,1)
			else:
				setmotor(0,x2,0)
				setmotor(3,x2,0)
			poscalculate()
	#print "ALiGNED"
	
	stop()
def conditioncheck() :	
	global nodeDetected
	biCalculate()
	global node
	global snodes
	poscalculate()
	  
	if  nodeDetected:
		if ( snodes==0):
			flag=1
			node+=1
			print "Big Node"
		else:
			snodes=snodes-1
			print "Small Node"
			while(nodeDetected) :
				biCalculate()
				poscalculate()
				travel(cfactor)
	else:
		travel(cfactor)
	return node

def specialconditioncheck() :
	#print "checking condition..."
	biCalculate()
	global node
	if bi[face][0]==1 or bi[face][1]==1 or bi[face][2]==1 or bi[face][3]==1 or bi[face][4]==1 or bi[face][5]==1 or bi[face][6]==1 or bi[face][7]==1:
		biCalculate()
		poscalculate()
		travel(cfactor)
	else:
		while True:
			slowforward()
			biCalculate()
			if (bi[(face+1)%4][2]==1 or bi[(face+1)%4][3]==1 or bi[(face+1)%4][4]==1 or bi[(face+1)%4][5]==1 ):
				node=node+1
				break
		
	return node
	
def initialfunc():
	motor()
	global avg , maxi , mini
	filer = open('avgline', "rb")
	avg = pickle.load(filer)
	#for i in range(4):
		#print avg[i]
	filer.close()
	filer = open('maxi', "rb")
	maxi = pickle.load(filer)
	filer.close()
	filer = open('mini', "rb")
	mini = pickle.load(filer)
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
		diagonal()

'''initialfunc()
while True:
	poscalculate()
'''
