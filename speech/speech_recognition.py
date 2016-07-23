import pyaudio
import wave
import audioop
import os
import time
import math


# Microphone stream config.
CHUNK = 1024  # CHUNKS of bytes to read each time from mic
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WAVE_OUTPUT_FILENAME = 'command.pcm'


SILENCE_LIMIT = 1  

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
					 channels=CHANNELS,
					 rate=RATE,
					 input=True,
					 frames_per_buffer=CHUNK)

def audio_int(num_samples=50):
	 """ Gets average audio intensity of your mic sound. You can use it to get
		  average intensities while you're talking and/or silent. The average
		  is the avg of the 20% largest intensities recorded.
	 """


	 values = [abs(audioop.avg(stream.read(CHUNK), 4)) for x in range(num_samples)] 
	 values = sorted(values, reverse=True)
	 intensity = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
	 print(intensity)
	 return intensity

def record(start_pulse):
	 frames = []
	 print("I RECORD YOU MOTHERFUCKER!!!")
	 i = 0
	 while True:
		 data = stream.read(CHUNK)
		 frames.append(data)
		 i = i + 1
		 if i >= 1000:
			 if (frames[-(int(RATE/CHUNK)*SILENCE_LIMIT)] < start_pulse) :
				 break
	 
	 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	 wf.setnchannels(CHANNELS)
	 wf.setsampwidth(p.get_sample_size(FORMAT))
	 wf.setframerate(RATE)
	 wf.writeframes(b''.join(frames))
	 wf.close()
	 print("I KNOW WHAT YOU SAID BITCH!")

start_level = audio_int() * 2

while True:
	level = abs(audioop.avg(stream.read(CHUNK), 4))
	n = int(level / 10000)
	print("#" * n)
	#if level > start_level:
		#record(start_level)
		#break