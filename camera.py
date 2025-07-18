import time
from picamera2 import Picamera2, Preview

# Initialize camera
picam2 = Picamera2()

# Use X11 or DRM (depends on whether you're using desktop or headless)
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Start preview window
picam2.start_preview(Preview.QTGL)  # Use Preview.NULL if no preview needed
picam2.start()

print("Camera preview running... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping preview...")
finally:
    picam2.stop()
