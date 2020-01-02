import Adafruit_MCP3008
flag=0
cf = 0
sf = 15
CLK  = 5
MISO = 6
MOSI = 13
node = 0
gap = 0.1
ssp = 10
factor = 6
CS =[9, 10, 22, 27,17,4]
cfactor=[0,0,0,0]
pos=[0,0,0,0]
nodeDetected = False
#CSextra=17
#CSencoder=4
mcp = [Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS[0], miso = MISO, mosi = MOSI)] * 6

for i in range(6):
	mcp[i] = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS[i], miso=MISO, mosi=MOSI)
avg = [[0 for i in range(8)] for j in range(4)]
bi = [[0 for i in range(8)] for j in range(4)]
prevbi = [[0 for i in range(8)] for j in range(4)]
values = [[0 for i in range(8)] for j in range(6)]
maxi = [[0 for i in range(8)] for j in range(4)]
mini = [[1023 for i in range(8)] for j in range(4)]
summ = [0 for j in range(4)]
motordir = [16,24,8,21]
motorpwm=[20,7,25,12]
#motordir = [16,24,15,21]
#motorpwm=[20,7,14,12]
motorin =[0,0,0,0]
sp =[50,45,50,45]
correction = 20
