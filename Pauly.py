#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time

m_l = ev3.LargeMotor('outA')
m_r = ev3.LargeMotor('outD')

m_l.run_timed(time_sp=2000, speed_sp=500)
m_r.run_timed(time_sp=2000, speed_sp=500)

#25cm nach Vorne gefahren
m_r.run_timed(time_sp=1000, speed_sp=500)

#90° turn left
m_l.run_timed(time_sp=2000, speed_sp=500)
m_r.run_timed(time_sp=2000, speed_sp=500)

#25cm nach links gefahren (Ecke links unten)
m_l.run_timed(time_sp=1000, speed_sp=500)

#90° trun right (untenlinks)
m_l.run_timed(time_sp=4000, speed_sp=500)
m_r.run_timed(time_sp=4000, speed_sp=500)

#50cm gefahren nach oben (Ecke oben links)
m_l.run_timed(time_sp=1000, speed_sp=500)

#90° trun right (obenlinks)
m_l.run_timed(time_sp=4000, speed_sp=500)
m_r.run_timed(time_sp=4000, speed_sp=500)

#50cm gefahren nach rechts (Ecke oben rechts)
m_l.run_timed(time_sp=1000, speed_sp=500)

#90° trun right (obenrechts)
m_l.run_timed(time_sp=4000, speed_sp=500)
m_r.run_timed(time_sp=4000, speed_sp=500)

#50cm gefahren nach unten (Ecke unten rechts)
m_l.run_timed(time_sp=1000, speed_sp=500)

#90° turn right (untenrechts)
m_l.run_timed(time_sp=2000, speed_sp=500)
m_r.run_timed(time_sp=2000, speed_sp=500)

#25cm gefahren bis erster Turn
m_r.run_timed(time_sp=1000, speed_sp=500)

#90° turn left (facing home)
m_l.run_timed(time_sp=2000, speed_sp=500)
m_r.run_timed(time_sp=2000, speed_sp=500)
m_l.stop()
m_r.stop()
#25cm gefahren bis Home
