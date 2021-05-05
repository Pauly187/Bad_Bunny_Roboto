#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time


cl = ev3.ColorSensor()
ts = ev3.TouchSensor()
cl.mode = 'COL-COLOR'
colors = ('unknown','black','blue','green','yellow','red','white','brown')
while not ts.value():
    print(colors[cl.value()])
    sound.speak(colors[cl.value()]).wait()
    sleep(1)
sound.beep()