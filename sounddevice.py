import sounddevice as sd

fs = 48000
duration = 5
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)

