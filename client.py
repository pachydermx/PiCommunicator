import transmit
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.interval = 1

    def start(self):
        self.t = transmit.Transmit(self.host, self.port, False)
        self.t.set_filename("recv")
        self.t.start()
        self.t.client = self

    def tell(self, finished):
        if finished:
            self.t.execute()
        else:
            self.t.receive()

if __name__ == '__main__':
    c = Client("localhost", 8888)
    c.start()