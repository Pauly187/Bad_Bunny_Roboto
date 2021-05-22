#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

cl = ev3.ColorSensor()

cl.mode = 'COL-COLOR'
colors = ('unknown','black','blue','green','yellow','red','white','brown')
count = colors
while True:
    count = colors[cl.value()]
    m_l.run_to_rel_pos(position_sp=2000, speed_sp=500, stop_action="brake")
    m_r.run_to_rel_pos(position_sp=2000, speed_sp=500, stop_action="brake")

    if count = 4:
        m_l.stop()
        m_r.stop()
        break
ev3.Sound.speak(colors[cl.value()])