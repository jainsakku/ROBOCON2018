# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 5
MISO = 6
MOSI = 13
CS   = 9
CS5 =17
CS6 = 4
CS2 = 10
CS3 = 22
CS4 = 27
mcp2 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS2, miso=MISO, mosi=MOSI)
mcp3= Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS3, miso=MISO, mosi=MOSI)
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
mcp4 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS4, miso=MISO, mosi=MOSI)
mcp5 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS5, miso=MISO, mosi=MOSI)
mcp6 = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS6, miso=MISO, mosi=MOSI)
# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    values1 = [0] * 8
    values2 = [0] * 8
    values3 = [0] * 8
    values4 = [0] * 8
    values5 = [0] * 8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
        values1[i] = mcp2.read_adc(i)
        values2[i] = mcp3.read_adc(i)
        values3[i] = mcp4.read_adc(i)
        values4[i] = mcp5.read_adc(i)
        values5[i] = mcp6.read_adc(i)
    # Print the ADC values.
    print('1st| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    print('2nd| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values1))
    print('3rd| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values2))
    print('4th| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values3))
    print('5th| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values4))
    #print('6th| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values5))
    # Pause for half a second.
    
    time.sleep(0.8)
    
