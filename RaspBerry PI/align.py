def align(face):
    while True:
        biCalculate()
		if ( bi[face][3]==1 or bi[face][4] ==1) :
        	if( bi[(face+2)%4][0]==1 or bi[(face+2)%4][1]==1 or bi[(face+2)%4][2]==1):
           		backright(20)
        	elif( bi[(face+2)%4][5]==1 or bi[(face+2)%4][6]==1 or bi[(face+2)%4][7]==1):
            	backleft(20)
			elif ( bi[(face+2)%4][3]==1 or bi[(face+2)%4][4]==1):
				if ((bi[(face+1)%4][3]==1 or bi[(face+3)%4][4]==1) and (bi[(face+3)%4][6]==1 or bi[(face+3)%4][7]==1)):
					stop()
					break
				elif((bi[(face+1)%4][6]==1 or bi[(face+1)%4][7]==1) and (bi[(face+3)%4][1]==1 or bi[(face+3)%4][0]==1)):
					forward(25)
				elif((bi[(face+1)%4][0]==1 or bi[(face+1)%4][1]==1) and (bi[(face+3)%4][6]==1 or bi[(face+3)%4][7]==1)):
					backward(25)
				else:
					backward(25)

        elif( bi[face][0]==1 or bi[face][1]==1 or bi[(face+1)%4][2]==1) :
            left(20)
        elif( bi[face][5]==1 or bi[face][6]==1 or bi[face][7]==1) :
            right(20)
        
        
