#!/usr/bin/env python

from phue import Bridge
from time import sleep
import os

# Connect to Hue Bridge via IP
b = Bridge('192.168.1.5') 

# Turn off Raspberry Pi and USB Wifi Dongle LEDs
os.system("sudo bash -c 'echo 0 > /sys/class/leds/led0/brightness'")
os.system("sudo bash -c 'echo 0 > /sys/class/leds/led1/brightness'")
os.system("sudo bash -c 'echo 0 > /sys/class/leds/rt2800usb-phy0::radio/brightness'")

# LR = Living Room Motion Sensor (Hue Sensor Address 2)
LR = False

# Main Loop
while True:
    LR = b.get_sensor(2, 'state').get("presence")
    if LR == True:
	# Turn on Backlight for 5 minutes
	os.system("sudo bash -c 'echo 0 > /sys/class/backlight/fb_s6d02a1/device/backlight/fb_s6d02a1/bl_power'")
	sleep(300)
    else:
	# Turn off Backlight
	os.system("sudo bash -c 'echo 1 > /sys/class/backlight/fb_s6d02a1/device/backlight/fb_s6d02a1/bl_power'")
	sleep(1)
