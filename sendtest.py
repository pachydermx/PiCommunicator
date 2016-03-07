import time
import transmit

r = transmit.Transmit("localhost", 8888, False)
r.set_filename("received_file")
s = transmit.Transmit("localhost", 8888, True)
s.set_filename("data.txt")

r.start()
time.sleep(1)
s.start()
