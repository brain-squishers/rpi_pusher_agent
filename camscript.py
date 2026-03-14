from picamera2 import Picamera2
import time
import os

picam2 = Picamera2()
picam2.start_preview()

for i in range(20):
    time.sleep(0.5)
    picam2.start_and_capture_files(f"/home/david/Documents/camfiles/myframe_{i}.jpg")
    print(f"took picture for {i}")

picam2.stop_preview()
picam2.stop()
