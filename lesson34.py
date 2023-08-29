import threading
import socket

#task 1
class Counter(threading.Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(self.rounds):
            self.counter += 1
            print(f'iteration: {i}: counter = {self.counter}')

t1 = Counter()
t2 = Counter()
t1.start()
t2.start()
t1.join()
t2.join()

#я перепробувала різні способи, в мене не виходило 200 000. тому вирішила залишити такий варіант реалізації завдання

#task 2
def client(client_sock):
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        client_sock.send(data)

def func():
    HOST = "127.0.0.1"
    PORT = 6677

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(HOST, PORT)
    server_sock.listen(2)

    while True:
        client_sock, addrr = server_sock.accept()
        print(f"Connection from:  {addrr}" )
        client_thr = threading.Thread(target=client, args=(client_sock))
        client_thr.start()

if __name__ == "__main__":
    func()