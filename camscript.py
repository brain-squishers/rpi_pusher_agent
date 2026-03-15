from picamera2 import Picamera2
import time
import os
from libcamera import controls

picam2 = Picamera2()
picam2.start_preview()

def set_day_mode():
    picam2.set_controls({
        "AeEnable": True,
        "AeExposureMode": controls.AeExposureModeEnum.Normal,
        "AeMeteringMode": controls.AeMeteringModeEnum.Matrix,
        "AwbEnable": True,
        "AwbMode": controls.AwbModeEnum.Daylight,  # or Outdoor/Auto
        # Optional: cap maximum gain/exposure so it doesn’t over‑brighten
        # "AnalogueGain": 1.0,
        # "ExposureTime": 10000,  # in microseconds, example
    })

set_day_mode()
#for i in range(20):
#    time.sleep(0.5)
#    picam2.start_and_capture_files(f"/home/david/Documents/camfiles/myframe_{i}.jpg")
#    print(f"took picture for {i}")
picam2.start_and_capture_files(f"/home/david/Documents/camfiles/myframe.jpg")

picam2.stop_preview()
picam2.stop()
