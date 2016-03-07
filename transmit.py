import socket
import threading

class Transmit(threading.Thread):

    def __init__(self, host, port, sender):
        threading.Thread.__init__(self)
        # config
        self.host = host
        self.port = port
        self.sender = sender

    def run(self):
        if self.sender == True:
            self.send()
        else:
            self.receive()

    def receive(self):
        s = socket.socket()

        s.connect((self.host, self.port))
        s.send("Hello server")

        with open('received_file', 'wb') as f:
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

            filename="data.txt"
            f = open(filename, 'rb')
            l = f.read(1024)
            while(l):
                conn.send(l)
                print('sent ', repr(l))
                l = f.read(1024)
            f.close()

            print('done')
            conn.send("done")
            conn.close()

