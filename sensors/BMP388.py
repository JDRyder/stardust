import time
import board
import adafruit_bmp3xx
import logging


i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
stardustLogger = logging.getLogger("StardustLogger")


def bmp388():
	print("Pressure: {:6.1f}".format(bmp.pressure))
	print("Temperature: {:5.2f}".format(bmp.temperature))
	
	
def logPressure():
	stardustLogger.debug("BMP388.logPressure()")
	stardustLogger.info("Pressure: {:6.1f}".format(bmp.pressure))
	
	
def logTemperature():
	stardustLogger.debug("BMP388.logTemperature()")
	stardustLogger.info("Temperature: {:5.2f}".format(bmp.temperature))

