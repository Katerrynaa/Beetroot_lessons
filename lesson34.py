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

#практичне по потокам за 19.08
# task 1
import threading

my_list = [2, 8, 12, 16, 20, 22]

def even_nums(list):
    for i in list:
        index = list.index(i)
        if (index % 2) == 0:
            print(i)
        else:
            pass

def odd_nums(list):
    for i in list:
        index = list.index(i)
        if (index % 2) != 0:
            print(i)
        else:
            pass

t1 = threading.Thread(target=even_nums(my_list))
t2 = threading.Thread(target=odd_nums(my_list))
t1.start()
t2.start()
t1.join()
t2.join()

# task 2 
import time
from time import perf_counter

def first_th(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
            
if __name__ == "__main__":
    num = 1129
    start_time = time.perf_counter()
    first_th(num)
    end_time = time.perf_counter()

print(f'It took {end_time - start_time: } seconds to complete')

def second_th():
    print('starting program')
    time.sleep(3)
    print('done!')

start_time = perf_counter()

t1 = threading.Thread(target=second_th)
t2 = threading.Thread(target=second_th)
t1.start()
t1.join()
t2.start()
t2.join()

end_time = perf_counter()
print(f'It took {end_time - start_time: } seconds to complete')

#task 3
#3.1
import requests

def request(url):
    response = requests.get(url)
    print(f'response from {url}')
urls = [
    "https://restcountries.com/" "\n"
    "https://github.com/SteinRobert/python-restcountries"
]

threads = []
for url in urls:
    thread = threading.Thread(target=request, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

#3.2
urls = ["https://restcountries.com/"]
time1 = time.perf_counter()

for url in urls:
    response = requests.get(url)
    print(response.status_code)
    print(response.headers)

time2 = time.perf_counter()
print(f'Time: {time2 - time1: 0.2f} seconds')
