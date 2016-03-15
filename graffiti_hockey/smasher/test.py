import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

seconds = 2.0

try: 
 while True:

  flag = input("flag=")

  if flag == 1:
   GPIO.output(18, GPIO.HIGH)
   time.sleep(seconds)
   GPIO.output(18, GPIO.LOW)
  else:
   GPIO.output(21, GPIO.HIGH)
   time.sleep(seconds)
   GPIO.output(21, GPIO.LOW)

except KeyboardInterrupt:
 GPIO.cleanup()
