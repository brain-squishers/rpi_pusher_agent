import pyaudio
import collections

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
CHUNK = 1024
BUFFER_SIZE = 48000  # ~1 second at 44.1kHz

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

audio_buffer = collections.deque(maxlen=BUFFER_SIZE // CHANNELS)  # Rolling buffer

try:
    for i in range(20000):
        data = stream.read(CHUNK, exception_on_overflow=False)
        # Append raw bytes or process (e.g., np.frombuffer(data, dtype=np.int16))
        audio_buffer.extend(data)  # Example: treat as bytes
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()

