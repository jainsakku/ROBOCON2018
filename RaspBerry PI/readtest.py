import RPi.GPIO as io
import Adafruit_MCP3008
import time
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
CS2 =  27
mcp2 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS2, miso=MISO, mosi=MOSI)
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
mini=[1000,1000,1000,1000,1000,1000,1000,1000]
maxi=[0,0,0,0,0,0,0,0]
avg=[0,0,0,0,0,0,0,0]
bi =[0,0,0,0,0,0,0,0]
mini2=[1000,1000,1000,1000,1000,1000,1000,1000]
maxi2=[0,0,0,0,0,0,0,0]
avg2=[0,0,0,0,0,0,0,0]
bi2 =[0,0,0,0,0,0,0,0]


print('Reading FRONT values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
x=time.time()
while True:
	values = [0]*8
	for i in range(8):
		values[i] = mcp.read_adc(i)
		if values[i]<mini[i]:
			mini[i]=values[i]
        if values[i]>maxi[i]:
			maxi[i]=values[i]
        time.sleep(0.3)
    # Print the ADC values.
	print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
	if time.time()-x >10:
		break

print(mini)
print(maxi)
for i in range(8):
	avg[i]=(mini[i]+maxi[i])/2
print( avg)

time.sleep(3)

print('Reading BACK values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
x=time.time()
while True:
	values2 = [0]*8
	for i in range(8):
		values2[i] = mcp2.read_adc(i)
		if values2[i]<mini2[i]:
			mini2[i]=values2[i]
		if values2[i]>maxi2[i]:
			maxi2[i]=values2[i]
        time.sleep(0.3)
    # Print the ADC values.
	print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
	if time.time()-x >10:
		break

print(mini2)
print(maxi2)
for i in range(8):
    avg2[i]=(mini2[i]+maxi2[i])/2
print( avg2)

