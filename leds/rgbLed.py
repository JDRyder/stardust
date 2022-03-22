import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D21, 1)

GREEN = (255, 0, 0) #
RED = (0,255,0) #
BLUE = (0,0,255) #
YELLOW = (255,255,0) #
CYAN = (255,0,255) #
VIOLET = (0,127,255) #
WHITE = (255,255,255) #
OFF = (0,0,0) #

def off():
	pixels[0] = OFF

def startup():
	pixels[0] = GREEN
	time.sleep(1)
	pixels[0] = RED
	time.sleep(1)
	pixels[0] = BLUE
	time.sleep(1)
	pixels[0] = YELLOW
	time.sleep(1)
	pixels[0] = CYAN
	time.sleep(1)
	pixels[0] = VIOLET
	time.sleep(1)
	pixels[0] = WHITE
	time.sleep(1)
	pixels[0] = OFF
	
def statusOk():
	pixels[0] = GREEN
	time.sleep(0.5)
	pixels[0] = OFF
	time.sleep(0.5)
	pixels[0] = GREEN
	time.sleep(0.5)
	pixels[0] = OFF
	time.sleep(0.5)
	
	
def bmpError():
	pixels[0] = BLUE
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
	pixels[0] = BLUE
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
	
def vemlError():
	pixels[0] = YELLOW
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
	pixels[0] = YELLOW
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
	
def samError():
	pixels[0] = RED
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
	pixels[0] = RED
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)

def scd30Error():
	pixels[0] = CYAN
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
	pixels[0] = CYAN
	time.sleep(1)
	pixels[0] = OFF
	time.sleep(1)
