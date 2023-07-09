#task1
#1 variant
username = input("Hello file world!")

with open("user.txt", "w+") as file:
    file.write(username)
with open("user.txt", "r") as file:
    username = file.read()

#2 variant
file = open("user2.txt", "w")
file.write("Hello file world!")
file.close()

file = open("user2.txt", "r") 
file.read()
file.close()


#task2
import json

#write data
my_list = [{
    'name': 'Karolina',
    'surname': 'Belluchi',
    'number': '49000 3444',
    'city': 'Chicago',
    'id': '446'
}, {
    'name': 'Monika',
    'surname': 'Goil',
    'number': '496630999',
    'city': 'Los-Angeles',
    'id': '009'
}, {
    'name': 'Nick',
    'surname': 'Fredeik',
    'number': '4977734',
    'city': 'Washington',
    'id': '777'
}, {
    'name': 'Anny',
    'surname': 'Jonson',
    'number': '4988895050',
    'city': 'New York',
    'id': '133'
}, {
    'name': 'Ben',
    'surname': 'Ciel',
    'number': '4911207700',
    'city': 'San Francisco',
    'id': '500'
}]

data = json.dumps(my_list, indent=4)
with open("my_file2.json", "w") as file:
    file.write(data)

with open("my_file2.json", "r") as file:
    data = json.load(file)
    print(data)


#add data 
with open("my_file2.json", "r") as file:
    data = json.load(file)

data.append({
        "name": "Mary",
        "surname": "GUl",
        "number": "47898980664",
        "city": "Oslo",
        'id': '000'})

with open("my_file2.json", "w") as file:
    json.dump(data, file)
    file.close()


#delete data 
with open("my_file2.json", "r") as file:
    data = json.load(file)

new_list = data

new_list = [item for item in data if item['name'] != 'Karolina' and item['surname'] != 'Belluchi']

with open("my_file2.json", "w") as file:
    json.dump(new_list, file, indent=4)



#update data
find_data = 'surname'
replace_data = 'last name'

with open("my_file2.json", "r") as file:
    data = file.read()
    data = data.replace(find_data, replace_data)

with open("my_file2.json", "w") as file:
    file.write(data)



#search data
import json

with open("my_file2.json", "r") as file:
    data = json.load(file)
    
my_list = data

search_name = input("Enter name to find: ")
for item in data:
    if item['name'] == search_name:
        print("name is found ")
    else:
        print("Try again")

search_number = input("Enter number to find: ")
for number in data:
    if number['number'] == search_number:
        print("number is found")
    else:
        print("None")




#практичні завдання з лекції 01.07 які вийшло зробити
#task1
#1
file = open("my perfect file.txt", "w+")

ways_of_data = str((1, 2, 3, 4, 5))
file.write(ways_of_data)

file.close()

#2
file = open('practice file from lecture.txt', 'w+')

data_sctructure = 'have a nice day'
file.write(data_sctructure)

file.close() 


#3
file = open("programming.txt", 'w+')

program = 'python is not a snake'
file.write(program)

file.close()



#task2
#1
lines = [
    "Line1.",
    "Line2.",
    "Line3.",
    "Line4.",
    "Line5."
]

count = 0
with open("file.txt", "w") as file:
    for line in lines:
        count += 1
        file.write(str(lines) + "\n") 
    file.close() 


#2
lines = {
    'line': '2',
    'line': '4',
    'line': '6',
    'line': '8',
    'line': '10'
}


with open('new_file.txt', 'w') as new_file:
    for line in lines:
        new_file.write(str(lines))
        count += 1
    file.close()



#task3
import json

#read 
with open("name.json", "r") as file:
    data = json.load(file)
    print(data)


#append
with open("name.json", "r") as file:
    data = json.load(file)

data.append({
      "name": "BVG45",
      "processor": "CVT POOO",
      "memory": "8GB",
      "storage": "1TB",
      "location": "Chicago Data Center",
      "region": "Asia Pacific (Chicago)",
      "provider": "Provider NH"})

with open("name.json", "w") as file:
    json.dump(data, file)
    file.close()


#update
find_string = "Europe (Germany)"
replace_string = "Europe (Belgium)"

with open("name.json", "r") as file:
    data = file.read()
    data = data.replace(find_string, replace_string)

with open("name.json", "w") as file:
    file.write(data)


#task4
import csv
#read
with open("file.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)

#add
from csv import writer 

data = ['Alina, Milo, 29, +33 65423906, Paris, France, HR Manager']
with open('file.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    file.close()



#my data to another csv file
with open("my_file", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['Mary, Roser, 23, Oslo, Norway, Software Engineer'])
    writer.writerow(['Bil, Bush, 31, Helsinki, Finland, JavaScript Developer'])
    writer.writerow(['Nick, Loyer, 49, Amsterdam, Netherlands, Entrepreneur'])
    writer.writerow(['Bella, Sap, 33, Warszaw, Poland, Sales Manager'])

with open("my_file", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#dict in csv file 
headers = ['Name', 'Surname', 'Age', 'Country', 'Profession']
values = [
    {'Name': 'Mary', 'Surname': 'Roser', 'Age': '23', 'Country': 'Norway', 'Profession': 'Software Engineer' },
    {'Name': 'Nick', 'Surname': 'Loyer', 'Age': '49', 'Country': 'Netherlands', 'Profession': 'Sales Manager'}
]

with open("my_file.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writerows(values)




#практичні завдання з лекції 04.07
#завдання csv файли 
#Додати функціонал на перевірку наявності файлу та відловити виняткові ситуації, якщо файл відсутній або має неправильний формат.
import csv

try:
    with open("file.scv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)
except ValueError:
    pass
except FileNotFoundError:
    pass


#Записати вміст файлу в інший файл
with open("my_file.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)

with open("file.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)
        
    

#Записати у файл дані, які введе користувач з терміналу. Передбачити можливість запису в файли різних форматів - txt/json/csv
print("Hi! What's your name?")
input1 = input()
print("How old are you?")
input2 = input()

file = open("data.txt", "a")
file.write(input1)
file.write(" ")
file.write(input2)
file.write("\n")

file.close()




print("What's your name and surname?")
input_1 = input()
print("I need your phone number")
input_2 = input()

with open("data_structure.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(input_1)
    writer.writerow(input_2)
    file.close()




import json 

print("Hi! Enter your email")
input_3 = input()

with open("file.json", "w") as file:
    json.dump(input_3, file)
    file.close()
















    





    


    
























