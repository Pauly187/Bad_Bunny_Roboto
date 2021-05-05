#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

#motors
m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

#sensors
us = ev3.UltrasonicSensor('in4')

#UltrasonicSensor in distance mode
us.mode='US-DIST-CM'

#unit of distance cm
units = us.units

distance = us.value()

m_l.run_forever(speed_sp=500)
m_r.run_forever(speed_sp=500)

if distance <= 5:
    m_l.stop and m_r.stop








