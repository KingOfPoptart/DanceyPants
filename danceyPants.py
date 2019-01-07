#!/usr/bin/python
import cwiid, time, pygame, wiimote, threading
from os import path
from instrumentMap import instrumentMap

threads = []

def threadJoiner():
  while True:
      for i in xrange(len(threads) - 1, -1, -1):
        threads[i].join()
        del threads[i]
      time.sleep(0.5)

def playSound(soundChannel, sound):
  soundChannel.play(sound)

button_delay = 0.1
instruments = instrumentMap()

wii = wiimote.connect()
wii.led = 1
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)

soundA = pygame.mixer.Sound( path.join(instruments.getInstrumentPath(), instruments.getSoundFile()['A'])  )
soundDef =pygame.mixer.Sound( path.join(instruments.getInstrumentPath(), instruments.getSoundFile()['def'])  )

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)


joinerThread = threading.Thread(target=threadJoiner, args=(), kwargs={})
joinerThread.start()

while(True):
  acc = wii.state['acc']
  buttons = wii.state['buttons']
  
  #If moved suddenly
  if(acc[0] < 50 | acc[1] > 175 | acc[2] > 175):  
    if (buttons & cwiid.BTN_A):
      t = threading.Thread(target=playSound, args=(soundChannelA, soundA), kwargs={})
      t.start()
      threads.append(t)
    else:
      t = threading.Thread(target=playSound, args=(soundChannelB, soundDef), kwargs={})
      t.start()
      threads.append(t)
    time.sleep(0.1)
  
  # Detects if + and - are held down simultaneously and if they are it quits the program
  elif (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
  

joinerThread.join()
