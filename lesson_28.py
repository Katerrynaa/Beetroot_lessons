import random 
import time 
# task 1
# Підготуйте 2 масиви даних різної довжини. Можете скористатися бібліотекою random для генерування елементів списків. 
# Застосуйте 3 на вибір алгоритми сортування на кожен з масивів і порівняйте час виконання.

a = random.random()
print(a)
n = random.random()
print(n)

def selection_sort(array, size):
    for i in range(size):
        min_index = i

        for a in range(i + 1, size):
            if array[a] < array[min_index]:
                min_index = a
        
        (array[i], array[min_index]) = (array[min_index], array[i])

data = [0,5,5,3,9,3,1,9,0,8,2,2,5,4,0,4,6]
size = len(data)
selection_sort(data, size)

print("Sorted array: ")
print(data)

start_time = time.time()
end_time = time.time()
print(f"Selection sort algorithm took {start_time} - {end_time} seconds")

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = [0,1,7,0,6,6,4,9,0,3,4,0,1,5,5,1,1,6]
bubble_sort(array)

print("Sorted list: ")
for i in range(len(array)):
    print("%d" % array[i])

start_time = time.time()
end_time = time.time()
print(f"Bubble sort algorithm took {start_time} - {end_time} seconds")
