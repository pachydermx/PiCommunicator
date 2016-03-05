import socket

# config
host = "localhost"
port = 8888

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.bind((host, port))

while True:
    recv_msg, addr = c.recvfrom(1024)
    print recv_msg, addr




