#!/usr/bin/python

# this program sends a signal to a relay
# to turn on a coffee machine 
# and shuts it off after ten minutes
# to make coffee


import gpiozero
import time

signal = gpiozero.OutputDevice(14, active_high=True, initial_value=False)
signal.on()
t = 600
while t >= 0:
    time.sleep(1)
    t -=1
signal.off()

