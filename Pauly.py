#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
# let one wheel of the Marsrover move foreward

# Connect the output A to the motor
m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

m_l.run_timed(speed_sp=500)
m_r.run_timed(speed_sp=500)

time.sleep(5.0)

motor_left.stop()
motor_right.stop()


