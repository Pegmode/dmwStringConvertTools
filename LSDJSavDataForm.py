#LSDJSavDataForm.py
#By Dan Chu (Pegmode)

#Pads out and formats hex dump outputs
#from Little Sound DJ save data

#note: needs to automatically search and copy wavetable samples. Tool only pads data

OUTPATH = "waveDataString.txt"#filepath to the output file
INTPATH = "inWaveDataString.txt"#filepath to 

f  = open(INTPATH,"r")
waves = f.readlines()
f.close()

f  = open(OUTPATH,"w")
outWaves = []
for wave in waves:
    temp = wave.replace(" ","")
    f.write(temp.replace(""," "))
f.close()
