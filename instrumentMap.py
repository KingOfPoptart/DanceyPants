from os import path

class instrumentMap:
  
  def __init__(self):
    self.instrumentPath = "instruments/"
    self.currInstrument = 0
    self.instruments = [
      {
        "A"    : "bassdrum.wav",
        "def"  : "snare.wav",
        "name" : "drums", 
      },
    ]
  
  def nextInstrument(self):
    self.currInstrument = self.currInstrument + 1
    if(self.currInstrument == len(self.instruments)):
      self.currInstrument = 0
  
  def getSoundFile(self):
    return self.instruments[self.currInstrument]
  
  def getInstrumentPath(self):
    return path.join( self.instrumentPath, self.instruments[self.currInstrument]['name'])
  