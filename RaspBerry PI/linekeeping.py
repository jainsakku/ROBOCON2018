import RPi.GPIO as io
import Adafruit_MCP3008
import time
import cPickle as pickle

CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
#sp = 15
CS2 = 27
mcp2 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS2, miso=MISO, mosi=MOSI)
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
mini=[1000,1000,1000,1000,1000,1000,1000,1000]
maxi=[0,0,0,0,0,0,0,0]
avg=[0,0,0,0,0,0,0,0]
bi =[0,0,0,0,0,0,0,0]
values = [0]*8
values2 = [0]*8
mini2=[1000,1000,1000,1000,1000,1000,1000,1000]
maxi2=[0,0,0,0,0,0,0,0]
avg2=[0,0,0,0,0,0,0,0]
bi2=[0,0,0,0,0,0,0,0]
motordir = [6,4,2,19]
motorpwm = [13,17,3,26]
motorin =[0,0,0,0]
sp =[30,35,35,60]
cf=35
def motor():
    io.setmode(io.BCM)
    io.setwarnings(False)
    for i in range(4):
	io.setup(motordir[i],io.OUT)
	io.setup(motorpwm[i],io.OUT)
	motorin[i] = io.PWM(motorpwm[i],90)
	motorin[i].start(0)
	motorin[i].ChangeDutyCycle(0)
                
def setmotor(number,pwmvalue,d):
    io.output(motordir[number],d)
    motorin[number].ChangeDutyCycle(pwmvalue)
def forward():
    for i in range(4):
	setmotor(i,sp[i],0)
def left():
    setmotor(0,sp[0],1)
    setmotor(1,sp[1],0)
    setmotor(2,sp[2],1)
    setmotor(3,sp[3],0)
def right():
    setmotor(0,sp[0],0)
    setmotor(1,sp[1],1)
    setmotor(2,sp[2],0)
    setmotor(3,sp[3],1)
def backright() :
    setmotor(0,sp[0],0)
    setmotor(1,sp[1],0)
    setmotor(2,sp[2]+cf,1)
    setmotor(3,sp[3]+cf,0)
def backleft() :
    setmotor(0,sp[0],0)
    setmotor(1,sp[1],0)
    setmotor(2,sp[2]+cf,0)
    setmotor(3,sp[3]+cf,1)
def stop():
    for i in range(4):
        setmotor(i,0,0)
def calibrate():
    print('Reading Front values, press Ctrl-C to quit...')
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
    print('-' * 57)
    x=time.time()
    while True:
            #values = [0]*8
            for i in range(8):
                    values[i] = mcp.read_adc(i)
                    if values[i]<mini[i]:
                            mini[i]=values[i]
                    if values[i]>maxi[i]:
                            maxi[i]=values[i]
            time.sleep(0.1)
        # Print the ADC values.
            print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
            if time.time()-x >5:
                    break

    print(mini)
    print(maxi)
    for i in range(8):
        avg[i]=(mini[i]+maxi[i])/2
    print( avg)
    filer = open('avg', "wb")
    pickle.dump(avg, filer)
    filer.close()
    time.sleep(3)
    print('Reading back values, press Ctrl-C to quit...')
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
    print('-' * 57)
    x=time.time()
    while True:
            values2 = [0]*8
            for i in range(8):
				values2[i] = mcp2.read_adc(7-i)
				if values2[i]<mini2[i]:
					mini2[i]=values2[i]
				if values2[i]>maxi2[i]:
					maxi2[i]=values2[i]
            time.sleep(0.1)
        # Print the ADC values.
            print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values2))
            if time.time() - x > 5:
                    break

    print(mini2)
    print(maxi2)
    for i in range(8):
        avg2[i]=(mini2[i]+maxi2[i])/2
    print( avg2)
    filer = open('avg2', "wb")
    pickle.dump(avg2, filer)
    filer.close()

def readback():
    for i in range(8):
        values2[i]=mcp2.read_adc(7-i)
        if values2[i]<=avg2[i]:
            bi2[i]=1
        else:
            bi2[i]=0

motor()
calibrate()
filer = open('avg', "rb")
avg = pickle.load(filer)
filer.close()
filer = open('avg2', "rb")
avg2 = pickle.load(filer)
filer.close()
while True:
    for i in range(8):
        values[i] = mcp.read_adc(i)
        if values[i]<=avg[i]:
            bi[i]=1
        else :
            bi[i]=0
    print(bi)
    if bi[3] == 1 or bi[4] ==1:
        readback()
        if bi2[3]==1 or bi2[4] ==1 :
            print("forward")
            forward()
        elif bi2[0] ==1 or bi2[1]==1 or bi2[2]==1 :
            print("backleft")
            backright()
        elif bi2[5] ==1 or bi2[6] ==1 or bi2[7] ==1:
            print("backright")
            backleft()
    elif bi[0]==1 or bi[1]==1 or bi[2]==1 :
	print("left")
	left()
    elif bi[5] ==1 or bi[7] ==1 or bi[6] ==1:
	print("right")
        right()
    else:
	print("else case")
	stop()
	time.sleep(0.1)
