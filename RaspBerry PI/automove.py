import RPi.GPIO as io
import Adafruit_MCP3008
import time
import cPickle as pickle
from valuesnpins import *
from align import *
from motion import *
from readsensor import *
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

def conditioncheck() :
	print "checking condition..."
	biCalculate()
	global node
	for i in range(4):
		print(bi[i])
	print face
	if bi[face][0]==1 and bi[face][1]==1 and bi[face][2]==1 and bi[face][3]==1 and bi[face][4]==1 and bi[face][5]==1 and bi[face][6]==1 and bi[face][7]==1:
		forward()
		flag=1
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
			forward()
			print ("SPECIAL")
			print (face)
			biCalculate()
			if (bi[(face+1)%4][2]==1 or bi[(face+1)%4][3]==1 or bi[(face+1)%4][4]==1 or bi[(face+1)%4][5]==1 ):
				print("IFK ANDR")
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
def mainfunc(f,special=0):
        global node,face
        node=0
        face=f
        if special==0:
            while conditioncheck() == 0:
                pass
        elif special==2 :
            while conditioncheck()==0:
                pass
            align(face)
            #throw()
            time.sleep(2)
                
        else:
                while specialconditioncheck() == 0:
                        pass    
        
"""
initialfunc()
while True:
	conditioncheck()
	#time.sleep(0.1)
"""
