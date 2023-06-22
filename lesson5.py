#практичне за 15.06, завдання, які змогла зробити
#task1 
s = input('Enter your name')
b = input('Enter your surname')
print(s + b)

a = input('Enter your name and surname')
print(a) 

s = input('Enter your name')
b = input('Enter your surname')
v = input('Enter your domain')
print( s + b + v)

#task2
sales = 5
user = 0
while user < sales:
    print('Do you need a call?')
    user += 1
    continue

print('Wish you good shopping!')
user += 1


#task3
sales = 10
user = 0
while user < sales:
    print('Do you need a call to order?')
    user += 1
    continue 

input('No, thanks')
user += 1


#homework 
#task1

import random 

print("Hi! Let's try to guess a number")

while True:
    random_number = random.randint(1, 10)
    player = int(input("Choose a number from 1 to 10: " ))
    if player == random_number:
        print("Congratulations, you guessed!")
        break
    elif player < random_number:
       print("You are far away, try again")
    elif player > random_number:
        print("You are close!")


#task2
name = input("Enter your name")
age = input("Enter your age")
new_age = '23'
print(f"Hi,{name}, on your next birthday you will be {new_age} years!") 


#task3
import random

s = 'universe'
s_string = 'universe'
a = random.sample(s_string, len(s_string))
print(a)

