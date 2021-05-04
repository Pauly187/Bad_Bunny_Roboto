#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

m_l.run_to_rel_pos(position_sp=520, speed_sp=500, stop_action="brake")
m_r.run_to_rel_pos(position_sp=520, speed_sp=500, stop_action="brake")
m_l.wait_while('running')
m_r.wait_while('running')
m_l.run_to_rel_pos(position_sp=90, speed_sp=500, stop_action="brake")
m_l.wait_while('running')


m_l.stop()
m_r.stop()