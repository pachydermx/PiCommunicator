import socket

# config
host = "localhost"
port = 8888

s = socket.socket()
s.bind((host, port))
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

