#Quelle: http://www.horter.de/blog/i2c-analog-output-4-kanaele-10-bit/
#Datum: 01.10.2018
#!/usr/bin/env python
import smbus
import time

bus = smbus.SMBus(1)
aout = 0

try:

	while True:
		aout = aout + 1
		Hby = int (aout / 256)
		LBY = int (aout - Hby * 256)
		field = [LBY, Hby]
		print (field)
		bus.write_i2c_block_data (0x58, 0x00, field)
		time.sleep(0.1)
		print (aout)

		if aout > 1023:
			aout = 0
			break

except:
	pass
