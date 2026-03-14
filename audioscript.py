import pyaudio
import wave

CARD = 3
DEVICE = 0

p = pyaudio.PyAudio()

#def find_device_index(pa, card, device):
#    for i in range(pa.get_device_count()):
#        info = pa.get_device_info_by_index(i)
#        if info['maxInputChannels'] > 0:
#            print(f"Index {i}: {info['name']}")
#
#find_device_index(p, CARD, DEVICE)

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=48000
RECORD_SECONDS=5

stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=2,
        frames_per_buffer=CHUNK)

frames = []
for _ in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    frames.append( stream.read(CHUNK) )

stream.stop_stream()
stream.close()
p.terminate()

with wave.open("out.wav", 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
