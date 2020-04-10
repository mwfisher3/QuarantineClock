#!/usr/bin/env python

from phue import Bridge
from time import sleep
import os

b = Bridge('192.168.1.5')

lights = b.lights

os.system("sudo bash -c 'echo 0 > /sys/class/leds/led0/brightness'")
os.system("sudo bash -c 'echo 0 > /sys/class/leds/led1/brightness'")
os.system("sudo bash -c 'echo 0 > /sys/class/leds/rt2800usb-phy0::radio/brightness'")

LR = False

while True:
    LR = b.get_sensor(2, 'state').get("presence")
    if LR == True:
	os.system("sudo bash -c 'echo 0 > /sys/class/backlight/fb_s6d02a1/device/backlight/fb_s6d02a1/bl_power'")
	sleep(300)
    else:
	os.system("sudo bash -c 'echo 1 > /sys/class/backlight/fb_s6d02a1/device/backlight/fb_s6d02a1/bl_power'")
	sleep(1)
