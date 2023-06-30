#task1
books = {'name': ['The Old Man and The Sea','Street cat names Bob'],
         'author': ['Ernest Hemingway', 'James Bowen'], 
         'year': ['1952', '2010'], 
         'country': 'USA', 
         'genre': ['novel', 'biography']}

for key, value in books.items():
    print(key, ':', value)



#task2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total = 0
for i in prices:
    total = total + prices[i] * stock[i]
print(total)



#task3
s = ['j**i' for i in range(1, 10)]
print(s)

#я знайшла ось цей варіант, але не впевнена що правильно зрозуміла завдання 