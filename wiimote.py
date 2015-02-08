import cwiid, time, pygame

    
    
def connect():
  # This code attempts to connect to your Wiimote and if it fails the program quits
  connected = False
  while not connected:
    try:
      print 'Please press buttons 1 + 2 on your Wiimote now ...'
      wii=cwiid.Wiimote()
      connected = True
    except RuntimeError:
      print "Cannot connect to your Wiimote. Trying again, make sure you are holding buttons 1 + 2!"
  
  print "Connected"
  wii.rpt_mode = cwiid.RPT_BTN
  
  wii.rumble = 1
  time.sleep(0.3)
  wii.rumble = 0
  return wii
