import time
import transmit

s = transmit.Transmit("192.168.111.2", 8888, True)
s.set_filename("data.txt")

s.start()
