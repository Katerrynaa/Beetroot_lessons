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