import RPi.GPIO as io
import Adafruit_MCP3008
import time
from p import *
from newseek import *
from utrasonic_testing import *
CLK  = 5
MISO = 6
MOSI = 13
CS =17
ir =0
#sp = float(input('Enter speed : '))
value = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
motortdir=19
motortpwm=26
motortin=0
lsp =10
size = 2000

def ini():
    global motortin
    io.setmode(io.BCM)
    io.setwarnings(False)
    io.setup(motortdir,io.OUT)
    io.setup(motortpwm,io.OUT)
    motortin= io.PWM(motortpwm,500)
    motortin.start(0)
    motortin.ChangeDutyCycle(0)

                
def setmotor1(pwmvalue,dir_sm=1):
	if pwmvalue > 70:
		pwmvalue = 70
	elif pwmvalue <= 0:
		pwmvalue = 0
	io.output(motortdir,dir_sm)
	motortin.ChangeDutyCycle(pwmvalue)

'''def pause():
    while(x>lsp):
        setmotor1(x,0)
        x=x-10
        time.sleep(0.1)
'''
def motoralign():
	align_speed=lsp
	align_dir=0
	received = True
	align_ir = value.read_adc(0)
	#ir=900
	if align_ir < 200:
		while align_speed>0:
		    #print "ALIGNING"
		    align_ir = value.read_adc(0)
		    #print (ir)
		    if align_ir > 400 and not received:
		        received = True
		        align_speed=align_speed-1
		        setmotor1(align_speed,align_dir)
		    elif align_ir < 200 and received:
		        align_dir=1-align_dir
		        received = False	
		        align_speed=align_speed-1
		        setmotor1(align_speed,align_dir)
	setmotor1(0,1)

def motorstop(pwmvalue=0):
    print "stop"
    setmotor1(0,0)
def setmotor_before_throw(pwmvalue=2,t=0.55):
	io.output(motortdir,0)
	print "bthrow"
	motortin.ChangeDutyCycle(pwmvalue)
	time.sleep(t)
	io.output(motortdir,0)
	motortin.ChangeDutyCycle(0)

'''ini()
initialfunc()
while(1):
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
		align()
		#41.5
		setmotor1(47.5,1)
		t=nano('u')
		time.sleep(0.5)
		motorstop()			
#s = input("speed : ")
''''''
align()
time.sleep(0.7)
setmotor1(s,1)
c=nano('u')
time.sleep(0.5)
motorstop()'''
