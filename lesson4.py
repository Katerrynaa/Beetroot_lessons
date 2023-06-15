#task 1
print(len("figure something out ")) 
print(len("give someone a hand")) 

our_string = 'hello python' 
print(our_string[1:6]) 

name = 'programming language'
print(name[3:10]) 

our_str = "working with python"
print(our_str[-7:-2]) 

our_str = "let me see"
print(our_str[-10:-5]) 

#task2
our_number = "38097653192"
if our_number == '39056':
    print(f'You need to call "{our_number}", because you have a question')
elif our_number == '10':
    print(f'You need to call "{our_number}", because you have a question')
else:
    print('You do not have a number')


phone = "38097536187"
if phone == "38097536187":
    print(f'you must call today on this "{phone[:10]}"')
elif phone == "38097536170":
    print('this is not your number')



#task3
m = 5
i = 10
while i > m:
    print('Python genius')
    i += 2

string = 10
s = 5
while s < string:
    print('You have a good news')
    s += 1



#task4
s = 'kate'
name = input('Kate')
if s == 'kate':
    print('Enter your name:')
elif s == 'Kate':
    print('error')

#я довго думала і дійшла до цього варіанту реалізації, тому буду вдячна за фідбек, чи взагалі я в правильну сторону думала



# також сюди додам практичне завдання з лекції 13.06
#task1 
a = "Tarasss"
b = "Sheva"
d = "@kobzar.com"
s = a + b + d 
print(s)

name = "Ts"
surname = "Shev"
domain = "@kobzar.com"
s = name + surname + domain 
print(s)

print('Ts', 'Sheva', '@kobzar.com', sep='.')

#task2 
s = "18"
if s == "18":
    print("you can buy alcohol")
if s > "14":
    print("you can get only energy drink")
else:
    print("you are allowed juice")


#task3 
transaction_id = ";yu7i9om0iymn%"
print(transaction_id.replace(";", ""))
transaction_id_copy = ";yu7i9om0iymn%"
print(transaction_id_copy.replace("%", ""))


#task4
transaction_id = "yu&7i9om&0iym&n"
print(transaction_id.replace("&", "", 3))