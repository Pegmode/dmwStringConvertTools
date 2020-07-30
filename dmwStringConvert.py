#dmwStringConvert.py
#By Dan Chu (Pegmode)

#usage: run this script in the same directory as file INPUTTPATH where each wave is separated by a newline
#change the variables in USER VARIABLES to change behaviour
#
#To change input data to decimal input, change ISHEX to false
#
#proper updates to come later
#


import sys

#USER VARIABLES
#================================================================================
#change these values to modify program behaviour (program args to come later)

ISHEX = True #is the wave string in hex or decimal?
OUTPUTNAME = "output"#what each outputted .dmw file will be named
SYSTEM = "GB"#what system are you targeting GB or PCE
INPUTPATH = "waveDataString.txt"#filepath to the input file
#================================================================================

#CONSTANTS
GBBITDEPTH = 16
PCEBITDEPTH = 32
PSYSTEMS = ["GB","PCE"]



def writeWaveNewFormat(f,waveData):#don't need to use this.
  print("Writing wave: {}\nWaveSize: {}\n".format(waveData,len(waveData)))
  f.write(len(waveData).to_bytes(4,"little"))#wavesize
  f.write(GBBITDEPTH.to_bytes(1,"little"))#bit depth
  for sample in waveData:
    f.write(sample.to_bytes(1,"little"))
  f.close()

def writeWaveOldFormat(f,waveData):
  print("Writing wave: {}\nWaveSize: {}\n".format(waveData,len(waveData)+1))
  if len(waveData) != 31:
    print("WARNING: Wave size does not match normal GB/PCE size! (size = 32 samples)\nWave may be malformatted!!\n")
  if not SYSTEM in PSYSTEMS:
    print("ERROR: {} is not a valid system!!\nValid systems: {}".format(SYSTEM,PSYSTEMS))
    sys.exit()
  f.write(len(waveData).to_bytes(4,"little"))#wavesize
  if SYSTEM == "GB":
    f.write(GBBITDEPTH.to_bytes(1,"little"))#bit depth
  elif SYSTEM == "PCE":
    f.write(PCEBITDEPTH.to_bytes(1,"little"))#bit depth
  for sample in waveData:
    f.write(sample.to_bytes(1,"little"))
  f.close()

f = open("waveDataString.txt","r")
waveStrings = f.readlines()
f.close()

waveData = []
for wavestring in waveStrings:
  waveData.append(wavestring.split())

#convert values
for i in range(len(waveData)):
  for j in range(len(waveData[i])):
    if ISHEX:
      pass
      waveData[i][j] = int("0x"+ waveData[i][j] ,16)
    else:
      waveData[i][j] = int( waveData[i][j])

for i in range(len(waveData)):
  f = open("{}{}.dmw".format(OUTPUTNAME,i),"wb")
  writeWaveOldFormat(f,waveData[i])
print("FINISHED!")
