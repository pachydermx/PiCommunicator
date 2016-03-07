import time
import transmit

r = transmit.Transmit("localhost", 8888, False)
s = transmit.Transmit("localhost", 8888, True)

r.start()
time.sleep(1)
s.start()
