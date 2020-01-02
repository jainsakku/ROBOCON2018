import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

def nano(c) :
	ser.write(c)
	while(1):
		i = ser.readline()
		i = i.strip()[:4]
		if i == "TRUE":
			print "true"
			return True
		elif i == "FALS":
			print "false"
			return False
		else:
			print i
