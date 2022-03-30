import logging
from logging.handlers import TimedRotatingFileHandler

logFormatter = logging.Formatter("%(asctime)s - %(levelname)s :\t%(message)s")
timedHandler = TimedRotatingFileHandler(filename="./logs/stardust.log", when="m", interval=10, backupCount=0)
timedHandler.setFormatter(logFormatter)
stardustLogger = logging.getLogger("StardustLogger")
stardustLogger.addHandler(timedHandler)
stardustLogger.setLevel(logging.INFO)

try:
	import leds.rgbLed as rgb
except:
	stardustLogger.error("Error importing led script. Check file structure."
	
try:
	import sensors.veml6075 as veml
except:
	rgb.vemlError()
	stardustLogger.error("Error importing veml6075.")

try:
	import sensors.sam_m8q as sam
except:
	rgb.samError()
	stardustLogger.error("Error importing sam_m8q.")

try:
	import sensors.scd_30 as scd
except:
	rgb.scd30Error()
	stardustLogger.error("Error importing scd_30.")

try:
	import sensors.BMP388 as bmp
except:
	rgb.bmpError()
	stardustLogger.error("Error importing BMP388.")

import time
import sys
import os



def start():
	try:
		stardustLogger.debug("start(): Run all sensors once to remove bad reads.")
		rgb.startup()
		bmp.bmp388()
		veml.uv()
		try:
			sam.gps()
		except KeyError:
			pass
		scd.CO2()
	except KeyboardInterrupt:
		rgb.off()
		raise KeyboardInterrupt

def main():
	stardustLogger.debug("Begin startdust.py main")
	start()
	stardustLogger.debug("Begin mainloop")
	while(True):
		rgb.statusOk()
		try:
			stardustLogger.debug("bmp")
			bmp.bmp388()			#bmp to console
			bmp.logPressure()		#bmp log pressure
			bmp.logTemperature()	#bmp log temperature
			time.sleep(1)
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			stardustLogger.error("bmp error")
			rgb.bmpError()
				
		rgb.statusOk()
		try:
			stardustLogger.debug("veml")
			veml.uv()				#veml uv to console
			time.sleep(1)
			veml.logUv()			#veml log uv
			time.sleep(1)
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			stardustLogger.error("veml error")
			rgb.vemlError()
				
		rgb.statusOk()
		try:
			stardustLogger.debug("sam")
			sam.gps()				#sam gps to console
			time.sleep(1)
			sam.logGps()			#sam log gps
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			stardustLogger.error("sam error")
			rgb.samError()
			
		rgb.statusOk()
		try:
			stardustLogger.debug("scd-30")
			scd.CO2()				#scd CO2 to console
			scd.logCO2()			#scd log CO2
		except KeyboardInterrupt:
			raise KeyboardInterrupt
		except:
			stardustLogger.error("scd-30 error")
			rgb.scd30Error()
		

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:#USE THIS BLOCK TO CLEANUP OPEN CONNECTIONS.
		print("Detected Keyboard Interrupt")
		rgb.off()
		try:
			print("trying sys.exit")
			sys.exit(0)
		except SystemExit:
			print("doing os.exit")
			logging.shutdown()
			os._exit(0)
