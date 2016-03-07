import time
import receiver

r = receiver.Transmit("localhost", 8888, False)
s = receiver.Transmit("localhost", 8888, True)

r.start()
time.sleep(1)
s.start()
