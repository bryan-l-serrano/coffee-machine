#!/usr/bin/env python

# this program sends a signal to a relay
# to turn on a coffee machine 
# and shuts it off after ten minutes
# to make coffee


import gpiozero
import time
import sys

if len(sys.argv) > 1:
	t = sys.argv[1]
else:
	t = 600

signal = gpiozero.OutputDevice(18, active_high=True, initial_value=False)
signal.on()
while time >= 0:
    sys.stdout.write(str(t) + "\r" )
    sys.stdout.flush()
    time.sleep(1)
    t -=1
signal.off()

