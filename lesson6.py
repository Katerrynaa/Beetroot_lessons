#task1
import random 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
n = 5
max_number = my_list

while n > s:
    random = max_number
    max_number = max(my_list)
    print("The largest numbers is: ", max_number)
    break



#task2

list1 = [1, 3, 5, 4, 7, 6, 10, 8, 9, 2]
list2 = [2, 1, 4, 3, 5, 10, 6, 8, 9, 7]
list3 = []

a = 5
while a != 0:
    list3 = random.randint(0, 10)
    list3 = list(dict.fromkeys(list1, list2))
    print(list3)
    break
    


#task3
numbers_list = [1, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

result = 0
new_list = []

while result < len(numbers_list):
    if (numbers_list[result] % 7 == 0 and numbers_list[result] % 5 !=0):
        new_list.append(numbers_list[result])
    result += 1
print(new_list)




    




          



