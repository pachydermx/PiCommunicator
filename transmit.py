import socket
import threading
import time
import os

class Transmit(threading.Thread):

    def __init__(self, host, port, sender):
        threading.Thread.__init__(self)
        # config
        self.host = host
        self.port = port
        self.sender = sender
        # default parameters
        self.filename = "data.txt"

    def set_filename(self, filename):
        self.filename = filename

    def run(self):
        if self.sender:
            self.send()
        else:
            self.receive()

    def receive(self):
        s = socket.socket()

        while True:
            connected = True
            try:
                s.connect((self.host, self.port))
            except:
                connected = False
                time.sleep(1)
            if connected:
                break
        s.send("Hello server")

        with open(self.filename, 'wb') as f:
            print('file opened')
            while True:
                print('receiving data')
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break;
                f.write(data)

        f.close()
        print('successed')
        s.close()
        print('connection closed')

        if (hasattr(self, "client")):
            self.client.tell(True)

    def execute(self):
        print("executing ...")
        os.system("python " + self.filename)
        if (hasattr(self, "client")):
            self.client.tell(False)

    def send(self):
        s = socket.socket()
        s.bind((self.host, self.port))
        s.listen(5)

        print 'server listening...'

        while True:
            conn, addr = s.accept()
            print('connected with ', addr)
            data = conn.recv(1024)
            print('received ', repr(data))

            f = open(self.filename, 'rb')
            l = f.read(1024)
            while(l):
                conn.send(l)
                print('sent ', repr(l))
                l = f.read(1024)
            f.close()

            break;
        print('done')
        conn.close()

