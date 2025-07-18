# save this as test_camera.py

from picamera2 import Picamera2
import time

# Create camera instance
camera = Picamera2()

# Configure the preview and camera
camera.preview_configuration.main.size = (640, 480)
camera.preview_configuration.main.format = "RGB888"
camera.configure("preview")

# Start the camera
camera.start()
print("Camera warming up...")
time.sleep(2)  # wait for camera to warm up

# Capture a photo
camera.capture_file("test_photo.jpg")
print("Photo saved as test_photo.jpg")

# Stop the camera
camera.stop()
