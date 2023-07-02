#task1
#1 варіант
def my_favourite_movie(movie):
    print("my favourite movie is a " + movie)

my_favourite_movie('ticket to paradise')

#2варіант
def favourite_movie():
    print('my favourite movie is a ticket to paradise ')
    favourite_movie()


#task2
def make_country(name, capital):
    country = {'name': name,
               'capital': capital}
    return country

my_country = make_country("Sweden", "Stockholm")
print(my_country)

    
#task3
def make_operation(operation, *numbers):
    numbers = list(numbers)
    return_value = numbers[0]
    if operation == '+':
     for num in numbers:
        return_value = sum(numbers)
    elif operation == '-':
       for num in numbers:
          return_value -= num
    else:
       return_value = 1
       for num in numbers:
          return_value *= num
    return return_value 

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))

