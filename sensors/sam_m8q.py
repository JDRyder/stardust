import melopero_samm8q as samm8q
import time
import logging

sensor = samm8q.SAM_M8Q()#default address 0x42

latitude = ''
longitude = ''
stardustLogger = logging.getLogger("StardustLogger")

def gps():
	try:
		sensor.get_pvt()
		time.sleep(1)
		longitude = sensor.pvt_data["longitude"]
		latitude = sensor.pvt_data["latitude"]
		print("We are at latitude " + str(latitude) + " and longitude " + str(longitude))
		#print(sensor.get_pvt())
	except OSError:
		stardustLogger.error("Caught OSError in sam_m8q!")
	
def logGps():
	stardustLogger.debug("logGPS()")
	try:
		stardustLogger.debug("sensor.get_pvt()")
		sensor.get_pvt()
		stardustLogger.debug("sensor.get_pvt() = " + str(sensor.pvt_data))
		latitude = sensor.pvt_data["latitude"]
		longitude = sensor.pvt_data["longitude"]
	
		stardustLogger.info("We are at latitude " + str(latitude) + " and longitude " + str(longitude))
	except OSError:
		stardustLogger.error("Caught OSError!")
	except KeyError:
		raise KeyError
