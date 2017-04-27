from midiutil.MidiFile import MIDIFile
import os
import time as tme
import random
os.chdir("C:/Users/Seb/Desktop/py/Music")
melodie = [60,62,64,65,67,69,71,72,74,76]
accords = [24,26,28,29,31,33,35,36,38,40]
dur = [0.25,0.5,1]

mf = MIDIFile(1)     # only 1 track
track = 0   # the only track
"""
time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 0             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)
"""

def musique():
	time = 0    
	mf.addTrackName(track, time, "Sample Track")
	mf.addTempo(track, time, 120)
	
	channel = 0
	volume = 100
	i=0
	while i < 100:
		pitch = accords[random.randint(0,9)]
		time = i            # start on beat 0
		duration = 4
		mf.addNote(track, channel, pitch, time, duration, volume)


		

		pitch = melodie[random.randint(0,9)]
		time = i + random.randint(0,2)              # start on beat 0
		duration = dur[random.randint(0,2)]
		mf.addNote(track, channel, pitch, time, duration, volume)

		i=i+1
		time = time+2
	fichier = open("output.mid", 'r+b')
	mf.writeFile(fichier)
	"""else:
		with open("output.mid", 'wb') as outf:
		    mf.writeFile(outf)"""

musique()
print('Done')
