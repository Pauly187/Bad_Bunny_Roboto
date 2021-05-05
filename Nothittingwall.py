#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

#motors
m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

#sensors
us = ev3.UltrasonicSensor()

#UltrasonicSensor in distance mode
us.mode='US-DIST-CM'

#unit of distance cm
units = us.units




















