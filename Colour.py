#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

#motors
m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

#sensors
cl = ev3.ColorSensor()

#sensor mode
cl.mode = 'COL-COLOR'

#possible colors
ColorCode = cl.value()

m_l.run.forever(speed_sp=500)
m_r.run.forever(speed_sp=500)

if ColorCode == 4:
    m_l.forever(speed_sp=0)
    m_r.forever(speed_sp=0)
    ev3.speaker.say("yellow")













