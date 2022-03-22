import time
import board
import busio
import logging
import adafruit_veml6075

i2c = busio.I2C(board.SCL, board.SDA)
veml = adafruit_veml6075.VEML6075(i2c, integration_time=100)
stardustLogger = logging.getLogger("StardustLogger")

def uv():
	print("UV a:", veml.uva)
	print("UV b:", veml.uvb)
	print("UV index:", veml.uv_index)
	
def logUv():
	stardustLogger.debug("veml6075.logUv()")
	stardustLogger.info("UV a:" + str(veml.uva))
	stardustLogger.info("UV b:" + str(veml.uvb))
	stardustLogger.info("UV index:" + str(veml.uv_index))
