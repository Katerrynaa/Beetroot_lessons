import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = "127.0.0.1"
PORT = 6688

s.bind((HOST, PORT))

while True:
    print("UDP server here and waiting client")
    data, addr = s.recvfrom(1024)
    print("Got message: ", data, "from", addr)