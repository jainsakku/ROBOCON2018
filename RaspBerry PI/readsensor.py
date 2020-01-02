from valuesnpins import *
def read_sensor(i):
	index = 0
	for j in range(8):
		if i == 2:
			index = j
		else:
			index = j
		values[i][index] = mcp[i].read_adc(index)
