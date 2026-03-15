import pyaudio
import collections
import wave
import numpy as np

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK = 1024
BUFFER_SIZE = 48000

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

#audio_buffer = collections.deque(maxlen=BUFFER_SIZE // CHANNELS)
audio_buffer = []

try:
    for i in range(500):
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_buffer.extend(data)  # raw bytes going in
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()

# --- Convert buffer to WAV ---

# 1. Reassemble raw bytes from the deque
raw_bytes = bytes(audio_buffer)

# 2. Write to WAV using the `wave` module
output_path = "output.wav"
with wave.open(output_path, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 2 bytes for paInt16
    wf.setframerate(RATE)
    wf.writeframes(raw_bytes)

print(f"Saved {len(raw_bytes)} bytes → {output_path}")
