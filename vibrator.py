#!/usr/bin/python
import cwiid, time, pygame, wiimote


button_delay = 0.1


wii = wiimote.connect()

wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

while True:
  buttons = wii.state['buttons']
  
  if (buttons & cwiid.BTN_A):
    check = 0
    wii.rumble = 1
    time.sleep(0.1)
  else:
    wii.rumble = 0