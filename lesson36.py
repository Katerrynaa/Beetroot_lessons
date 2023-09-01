import asyncio
import socket
import time 
import multiprocessing

# task 1
# async functions
# factorial 
async def factorial(num):
    if num < 0:
        print("Factorial does not exist negative numbers")
    elif num == 0:
        return 1 
    else:
        return num * await factorial(num-1)

async def func():
    num = 10
    res = await factorial(num)
    print(f"Factorial of {num} is {res} ")

asyncio.run(func())
       
#squares 
async def squares_numbers(nums):
    return nums * nums 

async def func():
    list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tasks = [squares_numbers(nums) for nums in list_of_nums]
    res = await asyncio.gather(*tasks)
    print(f"Square of {list_of_nums} is {res}")

asyncio.run(func())

#cubic
async def cubic_numbers(nums):
    return nums * nums * nums

async def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tasks = [cubic_numbers(nums) for nums in numbers]
    result = await asyncio.gather(*tasks)
    print(f"Cubic of {numbers} is {result}")

asyncio.run(main())

#fibonacci
async def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return await fibonacci(num-1) + await fibonacci(num-2)

async def calculate():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tasks  = [fibonacci(num) for num in numbers]
    res = await asyncio.gather(*tasks)
    print(f"Fibonacci of {numbers} is {res}")

asyncio.run(calculate())

start_time = time.time()
duration = time.time() - start_time
print(f"The process of tasks took {duration} seconds") 

# multiprocessing functions 
def cube(num):
    print("Cube list: {}".format(num*num*num))

def square(num):
    print("Square list: {}".format(num*num))

def factorial(num):
    print("Factorial list: {}".format(num*num-1))

def fibonacci(num):
    print("Fibonacci list: {}".format(num-1+num-2))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=cube, args=(10, ))
    p2 = multiprocessing.Process(target=square, args=(10, ))
    p3 = multiprocessing.Process(target=factorial, args=(10, ))
    p4 = multiprocessing.Process(target=fibonacci, args=(10, ))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()

start_time = time.time()
duration = time.time() - start_time
print(f"Process took {duration} seconds")

# task 3
async def echo_server(reader, writer):
    data = await reader.read(100)
    msg = data.decode()
    addrr = writer.get_info('info')
    print(f"Got {msg} from {addrr}")

    print(f"Send: {msg} ")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def func():
    server = await asyncio.start_server(
        echo_server, "127.0.0.1", 5566
    )
    async with server:
        await server.serve_forever()

asyncio.run(func())

# practice 24.08
# Асинхронний REST API запит:
# Створіть програму, яка асинхронно взаємодіє з публічним REST API за допомогою aiohttp, отримуючи та оброблюючи дані з відповідей
import aiohttp
import asyncio
import aiofiles

async def func():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://russianwarship.rip/api/v2/war-info/status/en") as response:
            print(response.status)
            print(await response.text())
asyncio.run(func())

async def func():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://russianwarship.rip/api/v2/statistics?offset=0&limit=50&date_from=2022-02-24&date_to=2022-03-01") as response:
            print(response.status)
            print(await response.text())
asyncio.run(func())

# Асинхронний таймер:
# Напишіть програму, яка використовує asyncio для запуску функції через певний інтервал часу. Наприклад, виводьте повідомлення кожну секунду.
async def words():
    for word in "Hi", "HRU?":
        print(word)
        await asyncio.sleep(1)

async def numbers():
    for i in range(1, 3):
        print(i)
        await asyncio.sleep(1)

async def inititals():
    for initial in "AO", "BP", "SR":
        print(initial)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(numbers())
    task2 = asyncio.create_task(words())
    task3 = asyncio.create_task(inititals())
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())

# Асинхронний зчитувач файлів:
# Створіть програму, яка асинхронно читає дані з кількох файлів та виводить їх зміст в консоль.
async def read_file(file_name):
    async with aiofiles.open(file_name, "r") as file:
        content = await file.read()
        return content 

async def func():
    file_names = ['async_file1.txt', 'async_file2.txt']
    t = [read_file(file_name) for file_name in file_names]
    results = await asyncio.gather(*t)

    for file_name, content in zip(file_names, results):
        print(file_name, content)

asyncio.run(func())
