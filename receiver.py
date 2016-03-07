import socket

# config
host = "localhost"
port = 8888

s = socket.socket()

s.connect((host, port))
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




