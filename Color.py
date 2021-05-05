#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time


cl = ev3.ColorSensor()

cl.mode = 'COL-COLOR'
colors = ('unknown','black','blue','green','yellow','red','white','brown')
while True:
    ev3.Sound.speak(colors[cl.value()])
