import picamera
import time

camera = picamera.PiCamera()
try:
    camera.start_preview()
    time.sleep(180)
    camera.stop_preview()
except KeyboardInterrupt:
    camera.close()
    print("Camera closed")
