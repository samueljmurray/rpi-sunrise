# Requires https://github.com/jgarff/rpi_ws281x

import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

START_HOUR = 06
START_MINUTE = 30
ALARM_DURATION = 30 # Max 60 

def calculateTimeRemaining():
	current_minute = time.localtime().tm_min
	if current_minute < START_MINUTE:
		current_minute = current_minute + 60
	time_remaining = (START_MINUTE - current_minute) + ALARM_DURATION

	return 0 if time_remaining < 0 else time_remaining

if __name__ == '__main__':

	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, 0)
	strip.begin()
	for i in range(strip.numPixels()):
		strip.setPixelColorRGB(i, 0, 0, 0)
	strip.show()

	while True:
		current_time = time.localtime()
		minutes_remaining = calculateTimeRemaining()
		if (current_time.tm_hour == START_HOUR and current_time.tm_min >= START_MINUTE) or ((current_time.tm_hour - 1) == START_HOUR and current_time.tm_min < START_MINUTE):
			brightness = 255/ALARM_DURATION * (ALARM_DURATION - minutes_remaining + 1)
			strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
			strip.begin()
			for i in range(strip.numPixels()):
				strip.setPixelColorRGB(i, 255, brightness/2, brightness/10)
			strip.show()
			time.sleep(60)	
