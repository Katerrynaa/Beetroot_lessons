import socket
#client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = "127.0.0.1"
PORT = 6688

msg = "Hello python world"
print("UDP IP here: ", HOST)
print("UDP PORT here: ", PORT)
s.sendto(msg,(HOST, PORT))
