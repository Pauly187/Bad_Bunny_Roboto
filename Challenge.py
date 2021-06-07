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

while True:
    distance = us.value
    m_r.run_forever(speed_sp=300)
    m_l.run_forever(speed_sp=300)
    if distance > 100:
        m_r.run_forever(speed_sp=0)
        m_l.run_forever(speed_sp=0)
        break

while True:
    distance = us.value
    m_r.run_forever(speed_sp=300)
    m_l.run_forever(speed_sp=300)
    if distance < 100:
        m_r.run_forever(speed_sp=0)
        m_l.run_forever(speed_sp=0)
        break

m_l.run_to_rel_pos(position_sp=-278, speed_sp=300, stop_action="brake")
m_l.wait_while('running')

m_l.run_to_rel_pos(position_sp=-520, speed_sp=300, stop_action="brake")
m_r.run_to_rel_pos(position_sp=-520, speed_sp=300, stop_action="brake")
m_l.wait_while('running')
m_r.wait_while('running')

m_r.run_to_rel_pos(position_sp=-100, speed_sp=300, stop_action="brake")
m_r.wait_while('running')