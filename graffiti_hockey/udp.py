import socket
from contextlib import closing
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

seconds = 2.0

host = "192.168.1.190"
port = 10001
bufsize = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
with closing(sock):
	sock.bind((host, port))
	while True:
		print(sock.recv(bufsize))
		GPIO.output(18, GPIO.HIGH)
		time.sleep(seconds)
		GPIO.output(18, GPIO.LOW)
