import RPi.GPIO as GPIO                    #Import GPIO library
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 

TRIG1 = 15                                  #Associate pin 19 to TRIG
ECHO1= 14                             #Associate pin 26 to ECHO
TRIG2= 2
ECHO2= 3
def distance(num=1):
	#print "Distance measurement in progress"
	TRIG=0
	ECHO=0
	if(num==1):
		TRIG=TRIG1
		ECHO=ECHO1
	else:
		TRIG=TRIG2
		ECHO=ECHO2
	GPIO.setwarnings(False)
	GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
	GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

	while True:
		GPIO.output(TRIG, False)                 #Set TRIG as LOW
		#print "Waitng For Sensor To Settle"
		time.sleep(0.2)                            #Delay of 2 seconds
		GPIO.output(TRIG, True)                  #Set TRIG as HIGH
		time.sleep(0.00001)                      #Delay of 0.00001 seconds
		GPIO.output(TRIG, False)                 #Set TRIG as LOW
		x= time.time()
		while GPIO.input(ECHO)==0 :               #Check whether the ECHO is LOW
		    pulse_start = time.time()              #Saves the last known time of LOW pulse
		    if time.time()-x>1:
		    	if num==1:
		    		return 100
		    	else:
		    		return 27
		    	
		pulse_start = time.time()              #Saves the last known time of LOW 
		y= time.time()
		while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
		    pulse_end = time.time()                #Saves the last known time of HIGH pulse 
		    if time.time()-y >1:
		    	if num ==1 :
		    		return 100
		    	else:
		    		return 27
		    	
		pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

		distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
		distance = round(distance,2)
		return distance

#while True:
	#print(distance())
