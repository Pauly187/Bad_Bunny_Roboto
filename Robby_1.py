#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')
move_short = (m_l.run_to_rel_pos(position_sp=520, speed_sp=500, stop_action="brake") , m_r.run_to_rel_pos(position_sp=520, speed_sp=500, stop_action="brake"))
move_long = (m_l.run_to_rel_pos(position_sp=1040, speed_sp=500, stop_action="brake") , m_r.run_to_rel_pos(position_sp=1040, speed_sp=500, stop_action="brake"))
turn_right = (m_l.run_to_rel_pos(position_sp=556, speed_sp=500, stop_action="brake"))
turn_left = (m_r.run_to_rel_pos(position_sp=556, speed_sp=500, stop_action="brake"))
turn_180 = (m_l.run_to_rel_pos(position_sp=1112, speed_sp=500, stop_action="brake"))
move_short()
m_l.wait_while('running')
m_r.wait_while('running')
turn_left()
m_l.wait_while('running')
m_r.wait_while('running')
move_short()
m_l.wait_while('running')
m_r.wait_while('running')
turn_right()
m_l.wait_while('running')
m_r.wait_while('running')
move_long()
m_l.wait_while('running')
m_r.wait_while('running')
turn_right()
m_l.wait_while('running')
m_r.wait_while('running')
move_long()
m_l.wait_while('running')
m_r.wait_while('running')
turn_right()
m_l.wait_while('running')
m_r.wait_while('running')
move_long()
m_l.wait_while('running')
m_r.wait_while('running')
turn_right()
m_l.wait_while('running')
m_r.wait_while('running')
move_short()
m_l.wait_while('running')
m_r.wait_while('running')
turn_left()
m_l.wait_while('running')
m_r.wait_while('running')
move_short()
m_l.wait_while('running')
m_r.wait_while('running')
turn_180()
m_l.wait_while('running')
m_r.wait_while('running')
m_l.stop()
m_r.stop()