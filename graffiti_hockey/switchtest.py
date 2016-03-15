import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
while 1:
  print (GPIO.input(17))
  time.sleep(1)

#スイッチのOn/Off確認
