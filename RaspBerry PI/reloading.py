from newseek import *
from throwingmotor import *
import serial
from utrasonic_testing import *
import time
from p import *
ser= serial.Serial('/dev/ttyUSB0',9600)
flag=0
definition ={'START' :0 ,
            'RIGHT_NODE':1 ,
            'LOADING':2 ,
            'LAST' :3 ,
            'TZ1'  :4 ,
            'TZ2'  :5 ,
            'TZ3'  :6 }
pathtotake=[]
#numerical=[]
walk=[]
graph={ 'START'     :['RIGHT_NODE'],
        'RIGHT_NODE':['LOADING','START'],
        'LOADING'   :['LAST','TZ1','RIGHT_NODE'] ,
        'TZ1'       :['LOADING'],
        'LAST'      :['LOADING','TZ2'],
        'TZ2'       :['TZ3','LAST'],
        'TZ3'       :['TZ2'] }
def searchpath(graph,source,dest):
    explored =[]
    queue=[[source]]
    #print (queue)
    if source==dest:
        return "NO MOVEMENT"

    while queue:
        path=queue.pop(0)
        #print (path)
        node =path[-1]
        #print (node)
        if node not in explored:
            adjacent= graph[node]
            #print (adjacent)
            for adj in adjacent:
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)
                if adj == dest:
                    return new_path

            explored.append(node)



    return "NO PATH"
def traverse(src,dest):
	pathtotake = searchpath(graph,src,dest)
	print(pathtotake)
	faceposition=[[5,0,5,5,5,5,5],[2,5,1,5,5,5,5],[5,3,5,1,0,5,5],[5,5,3,5,5,0,5],[5,5,2,5,5,5,5],[5,5,5,2,5,5,0],[5,5,5,5,5,2,5]]
	snode=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,2,0,0],[0,0,0,0,0,2,0],[0,0,2,0,0,0,0],[0,0,0,2,0,0,2],[0,0,0,0,0,2,0]]
	index = len(pathtotake)-1
	for i in range(index):
		I=faceposition[definition[pathtotake[i]]][definition[pathtotake[i+1]]]
		S=snode[definition[pathtotake[i]]][definition[pathtotake[i+1]]] + 1
		if pathtotake[i+1] == 'RIGHT_NODE':
			mainfunc(I,S,1)
		elif (dest=='TZ1' and pathtotake[i+1]=='TZ1') or (dest=='TZ2'and pathtotake[i+1]=='TZ2') or(dest=='TZ3' and  pathtotake[i+1]=='TZ3'):
			mainfunc(I,S,0)
		else:
			mainfunc(I,S,0)
		backslow()


initialfunc()
ini()

#print "initial"
#nano('q')      #testing variable
src= raw_input("ENTER SOURCE :")
dest = raw_input("ENTER DESTINATION :")
traverse(src,dest)

zones = ['TZ1','TZ2']
areas = ['LOADING','LAST']

for zone in range(2):
	isManualThere = False
	while isManualThere:
		traverse(zones[zone],areas[zone])
		isManualThere = False
		for i in range(100):
			d = distance()    
			print d
			if d < 30 and not d==0:
				isManualThere = True
				break

		if isManualThere:
			while(distance()>10):
				print distance()
			time.sleep(3)
			motoralign()
			c=nano('s')
			while(1):
				if c==1:
					nano('c')
					break
				elif c==0:
					c=nano('s')
				 
			else :
				pass
			traverse(areas[zone],zones[zone])
			time.sleep(3)
			align()
			motoron()
			c=nano('t')
			motoralign()
			stop()
		elif zone==0:
			traverse('LOADING','TZ2')
		elif zone==1:
			face = 0
			forward()
			time.sleep(1)
			stop()
			
slowforward()
time.sleep(3)
stop()

while distance()>10:
	print distance()

print "LOAD RACK"
time.sleep(2)

traverse('LAST','TZ3')

i=0
while(i<5):
	motoralign()
	c=nano('s')
	while(1):
		if c==1:
			nano('c')
			break
		elif c==0:
			c=nano('s')
		i+=1
		print i
		if i==4:
			break
	i+=1
	print i
	if i<5:
		align()
		motoron()
		c=nano('t')

motorstop()
stop()

print "RUN COMPLETED"

