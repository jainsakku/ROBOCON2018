from newseek import *
from throwingmotor import *
import serial
from utrasonic_testing import *
import time
from p import *
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from valuesnpins import *
from motortest import *
# ******************ultrasonic*************
while (1):
	print(distance(2))
#*************************************

#******************nano******************	
nano('s')
nano('c')
nano('o')
time.sleep(2)
nano('g')
#***********************************

#************throwing_delay********
ini()
t = input("delay :")
setmotor_before_throw(2,t)
#*********ir laser*******************
while(1):
	for i in range(8):
		values[4][i] = mcp[4].read_adc(i)
	print "IR1 :" ,values[4][0]
	print "IR2 :" ,values[4][1]
	print "IR3 :" ,values[4][2]
	print "IR4 :" ,values[4][3]
	time.sleep(0.8)
#*************************************

#*************sensor array *******
while True:    
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[0][i] = mcp[0].read_adc(i)
        values[1][i] = mcp[1].read_adc(i)
        values[2][i] = mcp[2].read_adc(i)
        values[3][i] = mcp[3].read_adc(i)
     #Print the ADC values.
    print('1st| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    print('2nd| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values1))
    print('3rd| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values2))
    print('4th| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values3))
    
    time.sleep(0.8)

#***********************************

#************motortest**************
io.setmode(io.BCM)
io.setwarnings(False)
for i in range(4):
    io.setup(motordir[i],io.OUT)
    io.setup(motorpwm[i],io.OUT)
    motorin[i] = io.PWM(motorpwm[i],90)
    #io.output(motordir[i],0)                
    motorin[i].start(0)
    motorin[i].ChangeDutyCycle(0)
time.sleep(2)
for i in range(4):    
    io.output(motordir[i],0)
    motorin[i].ChangeDutyCycle(40)
    time.sleep(2)
    motorin[i].ChangeDutyCycle(0)
    io.output(motordir[i],1)
    motorin[i].ChangeDutyCycle(40)
    time.sleep(2)
    motorin[i].ChangeDutyCycle(0)
    time.sleep(1)
#******************************

#******throwingmotor******
ini()
s = input("speed  :  " )
motoralign()
setmotor1(s,1)
nano('t')
time.sleep(0.5)
motorstop()
#***************************
