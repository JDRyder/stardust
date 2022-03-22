import board
import adafruit_scd30
import logging
import time
import busio

i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)
scd.measurement_interval = 4
stardustLogger = logging.getLogger("StardustLogger")

def CO2():
	if scd.data_available:
		print("Data Available!")
		print("CO2: %d PPM" % scd.CO2)
		print("Temperature: %0.2f degrees C" % scd.temperature)
		print("Humidity: %0.2f %% rH" % scd.relative_humidity)
	else:
		print("no new data from CO2 sensor")
	
	

def logCO2():
	stardustLogger.debug("logCO2()")
	if scd.data_available:
		#logging.info("Data available? " + str(scd.data_available))
		stardustLogger.info("CO2: " + str(scd.CO2) + " PPM")
		stardustLogger.info("Temperature: " + str(scd.temperature) + " degrees C")
		stardustLogger.info("Humidity: " + str(scd.relative_humidity))
	else:
		stardustLogger.info("no new data from CO2 sensor")
		
	
