import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
rPin = 37
gPin = 35
bPin = 33

GPIO.setup(rPin,GPIO.OUT)
GPIO.setup(gPin,GPIO.OUT)
GPIO.setup(bPin,GPIO.OUT)

GPIO.output(rPin,1)


