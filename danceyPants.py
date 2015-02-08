#!/usr/bin/python
import cwiid, time, pygame, wiimote


button_delay = 0.1

wii = wiimote.connect()



pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)


while(True):
  buttons = wii.state['buttons']
  
  wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
  while True:
    acc = wii.state['acc']
    if(acc[0] < 50 | acc[1] > 200 | acc[2] > 200):
      print "Y: " + str(acc[1])
      sound = pygame.mixer.Sound("drumroll.wav")
      sound.play()
      time.sleep(button_delay)
      print(acc)
    time.sleep(0.01)
  
  
  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
  
  if (buttons & cwiid.BTN_A):
    sound = pygame.mixer.Sound("drumroll.wav")
    sound.play()
    time.sleep(button_delay)



