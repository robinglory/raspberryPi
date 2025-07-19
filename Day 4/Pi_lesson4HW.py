import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
ON = 1
OFF = 0
try:
    num = int(input("How many number do you want the LED to Blink"))

    for i in range(num):
        GPIO.output(17,ON)
        time.sleep(0.5)
        GPIO.output(17,OFF)
        time.sleep(0.5)
        print(f"LED Blink {i+1} time")
except ValueError:
    print("Please enter a valid number!")
except KeyboardInterrupt:
    print("\nProgram stopped by user")
finally:
    GPIO.cleanup()
