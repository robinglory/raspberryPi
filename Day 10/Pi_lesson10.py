import RPi.GPIO as GPIO
from time import sleep
dt = 0.1
b1 = 40
b2 = 38
b1State = 1
b1StateOld = 1
b2State = 1
b2StateOld = 1

LEDPin = 37
DutyCycle = 99
GPIO.setmode(GPIO.BOARD)
GPIO.setup(b1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(b2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LEDPin,GPIO.OUT)
           
myPWM = GPIO.PWM(LEDPin,100)
myPWM.start(DutyCycle)
try:
    while True:
        print("The Diming and Brighting The LED with PUSH Button Starts")
        b1State = GPIO.input(b1)
        b2State = GPIO.input(b2)
        if b1StateOld == 0 and b1State == 1:
            DutyCycle = DutyCycle - 20
            print("Dim Event")
        if b2StateOld == 0 and b2State == 1:
            DutyCycle = DuctyCycle +20
            print("Bright Event")
        if DutyCycle>99:
            DutyCycle = 99
        if DutyCycle<0:
            DutyCycle = 0
        myPWM.ChangeDutyCycle(DutyCycle)
        b1StateOld = b1State
        b2StateOld = b2State
        sleep(dt)
except KeyboardInterrupt:
    myPWM.stop()
    GPIO.cleanup()
    