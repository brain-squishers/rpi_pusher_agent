import pyaudio
p = pyaudio.PyAudio()

for i in range(20):
    info = p.get_device_info_by_index(i)
    print("===============")
    print(f"Index: {i}")
    print(f"Name: {info['name']}")
    print(f"maxInputChannels: {info['maxInputChannels']}")
    print(f"maxout: {info['maxOutputChannels']}")
    print(f"defsample: {info['defaultSampleRate']}")
p.terminate()
