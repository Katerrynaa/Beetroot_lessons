import time 
# task 1
# Дослідіть, які є алгоритми для хешування паролів в Джанго.
# Обґрунтуйте, чому ви вибрали той чи інший алгоритм для хешування паролів у своєму проекті.

# за замовчування джанго використовує алгоритм PBKDF2 із хешем SHA256 - це безпечно, а для зламування потрібна 
# значна кількість часу. 

# Argon2 
# цей алгоритм хешування паролів не є типовим для джанго, тому що потрібна спеціальна бібліотека. 

# Bcrypt 
# цей алгоритм спеціально розроблений для тривалого зберігання паролів. 

# Scrypt 
# спецально розроблений так, щоб використовувати більше пам"яті порівняно з іншими функціями виведення ключів на основі 
# пароля, щоб обмежити кількість паралелізму, який може використовувати зловмисник 

# для свого проекту я б обрала алгоритм PBKDF2 із хешем SHA256, тому що на першому місці стоїть безпека і те, що потрібно 
# дуже багато часу для зламування. 


# task 2
# Використайте готову реалізацію лінійного та бінарного пошуків. 
# Застосуйте ці алгоритми на 3-х заздалегідь підготовлених семплах даних - у вас може бути 3 списки різної довжини. 
# Порівняйте час виконання двох алгоритмів на різних масивах даних.

def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
 
array = [24, 41, 31, 11, 9]
x = 31
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element is Present at Index: ", result)

start_time = time.time()
end_time = time.time()
print(f"Linear took {start_time - end_time} seconds")

def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
        return -1
    
array = [2, 4, 5, 17, 14, 7, 11, 22]
x = 17
result = binarySearch(array, x, 0, len(array)-1)
 
if result != -1:
    print(str(result))
else:
    print("Not found")

start_time = time.time()
end_time = time.time()
print(f"Binear took {start_time - end_time} seconds")

# виконання двох алгоритмів на різних масивах даних по часу однакове. 