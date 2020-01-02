from newseek import *
from throwingmotor import *
import serial
from utrasonic_testing import *
import time
from p import *
import cPickle as pi
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
def startingseq():
	mainfunc(0,0,1)
	backslow()

def checkstate():
	global state
	filer=open('state','rb')
	state = pi.load(filer)
	filer.close()

def traverse(src,dest,x=1):
	
	pathtotake = searchpath(graph,src,dest)
	print(pathtotake)
	faceposition=[[5,0,5,5,5,5,5],[2,5,1,5,5,5,5],[5,3,5,1,0,5,5],[5,5,3,5,5,0,5],[5,5,2,5,5,5,5],[5,5,5,2,5,5,0],[5,5,5,5,5,2,5]]
	snode=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,2,0,0],[0,0,0,0,0,2,0],[0,0,2,0,0,0,0],[0,0,0,2,0,0,2],[0,0,0,0,0,2,0]]
	index = len(pathtotake)-1
	
	for i in range(index):
		I=faceposition[ definition[ pathtotake[ i ]]][ definition[ pathtotake[ i+1 ]]]
		S=snode[ definition[ pathtotake[ i ]]][ definition[ pathtotake[ i+1 ]]] + x		
		mainfunc(I,S,0)		
		print i,pathtotake[i],index
		if i<(index-1):
			if (pathtotake[i]=="LAST" and pathtotake[i+1]=="TZ2") or (pathtotake[i]=="TZ3" and pathtotake[i+1]=="TZ2"):
				pass
			else:
				backslow()
		else:
			backslow()
	stop()

initialfunc()
ini()
#for testing 
src= raw_input("ENTER SOURCE :")
dest = raw_input("ENTER DESTINATION :")
if src == "START":
	pass
else:
	traverse(src,dest)
	align()
	time.sleep(1000)
#for testing
#align()
#startingseq()
checkstate()


state=0
if state ==0:
	traverse('LOADING','TZ1')
	gold=0
elif state ==1:
	traverse('LOADING','TZ2')
	gold=0
elif state ==2:
	traverse('LOADING','LAST')
	gold=1

if gold ==0:
	zones = ['TZ1','TZ2']
	areas = ['LOADING','LAST']
	speeds = [41.5,46]
	commands = ['t','u']
	waitTime = [50,25]
	if state ==0:
		x=0
	elif state ==1:
		x=1
	for zone in range(x,2):
		first = True
		isManualThere = True
		while isManualThere:
			traverse(zones[zone],areas[zone])
			if first:
				slowforward()
				time.sleep(1)
				stop()
			#align()
			isManualThere = False
			
			for i in range(waitTime[zone]):
				d = distance()   
				print d
				if d < 25 and not d==0:
					isManualThere = True
					break

			if isManualThere:
				while(d > 12 or d==0):
					d = distance()
					print d
				nano('o')
				time.sleep(1.5)
				motoralign()
				c=nano('s')
				while(1):
					if c==1:
						check_lower = False
						setmotor_before_throw(2,0.9)
						for i in range(15):
							d = distance(2)
							print (d)
							if d < 18 and not d==0:
								check_lower = True
								break
						setmotor1(0)
						if(check_lower):
							break
						else:
							nano('o')
							time.sleep(1.5)
							motoralign()
							c=nano('s')
					if(check_lower):
						break
					elif c==0:
						nano('o')
						time.sleep(1.5)
						motoralign()
						c=nano('s')
				if c==1:
					if first:
						traverse(areas[zone],zones[zone],0)
						first = True
					else:
						traverse(areas[zone],zones[zone])					
					align()
					setmotor1(speeds[zone],1)
					t=nano(commands[zone])
					time.sleep(0.5)
					motorstop()			
			elif zone==0:
				state=1
				filer=open('state','wb')
				pi.dump(state,filer)
				filer.close()
				slowforward(20,1)
				time.sleep(1)
				stop()
				traverse('LOADING','TZ2')
			elif zone==1:
				state=2
				filer=open('state','wb')
				pi.dump(state,filer)
				filer.close()		

align()
slowforward()
time.sleep(2)
stop()

while distance()>10:
	print distance()

print "LOAD RACK"
time.sleep(2)

traverse('LAST','TZ3',0)
i=0
while(i<5):
	nano('o')
	time.sleep(1.5)
	motoralign()
	c=nano('s')
	while(1):
		if c==1:
			check_lower = False
			setmotor_before_throw(2,0.9)
			for i in range(15):
				print (distance(2))
				#setmotor1(1,0)
				if distance(2) < 18:
					check_lower = True
					break
			setmotor1(0)
			if(check_lower):
				break
			else:
				nano('o')
				time.sleep(1.5)
				motoralign()
				#align()
				c=nano('s')
		if(check_lower):
			break
		elif c==0:
			nano('o')
			time.sleep(1.5)
			motoralign()
			#align()
			c=nano('s')
		i+=1
		if i==4:
			break
	i+=1
	if i<5 and c==1:
		align()
		setmotor1(52,1)
		t=nano('v')
		time.sleep(0.5)
		motorstop()

motorstop()
stop()

print "RUN COMPLETED"
