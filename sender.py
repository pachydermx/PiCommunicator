import socket

# config
host = "localhost"
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("hello", (host, port))
