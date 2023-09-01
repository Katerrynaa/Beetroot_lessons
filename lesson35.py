# task 3
import socket
import multiprocessing

def client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()

def func():
    HOST = "127.0.0.1"
    PORT = 3344

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(3)

    print(f"Listening on {HOST}: {PORT}")

    while True:
        c_sock, addrr = server.accept()
        print(f"Accept connection from {addrr}")

        client = multiprocessing.Process(target=client, args=(c_sock, ))
        client.start()
        client.join()

if __name__ == "__main__":
    func()