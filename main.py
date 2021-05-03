#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
# let one wheel of the Marsrover move foreward

# Connect the output A to the motor
motor_left = ev3.LargeMotor('outA')
motor_right = ev3.LargeMotor('outD')

motor_left.run_forever(speed_sp=500)
motor_right.run_forever(speed_sp=500)

time.sleep(5.0)

motor_left.stop()
motor_right.stop()


