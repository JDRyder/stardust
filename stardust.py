import sensors.BMP388 as bmp
import sensors.veml6075 as veml
import sensors.sam_m8q as sam
import sensors.scd_30 as scd
import leds.rgbLed as rgb

import logging
import time
import sys
import os

from logging.handlers import TimedRotatingFileHandler

logFormatter = logging.Formatter("%(asctime)s - %(levelname)s :\t%(message)s")
timedHandler = TimedRotatingFileHandler(filename="./logs/stardust.log", when="m", interval=10, backupCount=0)
timedHandler.setFormatter(logFormatter)
stardustLogger = logging.getLogger("StardustLogger")
stardustLogger.addHandler(timedHandler)
stardustLogger.setLevel(logging.INFO)

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
