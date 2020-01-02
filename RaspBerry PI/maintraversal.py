from newseek import *
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
src= raw_input("ENTER SOURCE :")
dest = raw_input("ENTER DESTINATION :")
traverse(src,dest)
time.sleep(100)
traverse("START","TZ1")
align()
traverse("TZ1","TZ3")
align()
traverse("TZ3","RIGHT_NODE")
align()
#traverse('TZ1','TZ3')
#hreloading()
#traverse('TZ1','LOADING')
#creloading()
#traverse('TZ3','LOADING')
while True:
    stop()
