#task 1
class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname 
        self.age = age 

    def talk(self):
        print(f"Hi, my name is {self.name} {self.surname},  I'm {self.age} years old.")


p = Person('Karl', 'Johnson', '26')
p.talk()

#task 2
class Dog():
    age_factor = 7

    def __init__(self, age):
        self.age = age 

    def human_age(self):
        return self.age * Dog.age_factor
    
dog = Dog(7)
human_age = dog.human_age()
print(human_age)

#task 3
class TVController():
    def __init__(self, channel_list= ['Discovery', 'MTV', 'BBC', 'National Geography'], current_channel='Discovery'):
        self.channel_list = channel_list
        self.current_channel = current_channel

    def first_channel(self):
        return self.current_channel
    
    def last_channel(self):
        self.current_channel = len(self.channel_list) - 1
        return self.channel_list[self.current_channel]
    
    def turn_channel(self, N):
        if 1 <=  N <= len(self.channel_list):
            self.current_channel = N + 2
            return self.channel_list[self.current_channel]
        
    def next_channel(self):
        self.current_channel = (self.current_channel + 2) % len(self.channel_list)
        return self.channel_list[self.current_channel]
    
    def previous_channel(self):
        self.current_channel = (self.current_channel - 1) % len(self.channel_list)
        return self.channel_list[self.current_channel]
    
    def current_channel(self):
        return self.current_channel
    
    def is_exist(self, arg):
        if isinstance(arg, int):
            if 1 <= arg <= len(self.channel_list):
                return "Yes"
            else:
                return "No"
        elif isinstance(arg, str):
            if arg in self.channel_list:
                return "Yes"
            else:
                return "No"
        
    
channel_list = ['Discovery', 'MTV', 'BBC', 'National Geography']
controller = TVController(channel_list)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(N=1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(arg='MTV'))
print(controller.is_exist(6))

# практичні завдання по класам за 13.07
# написати клас Person, реалізувати метод init з декількома змінними класу
class Person():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

my_person = Person('Michael', '33', '15000£')
print(my_person.name, my_person.age, my_person.salary, sep=' , ')



# Створіть клас Student для студента. У класі повинні бути атрибути name (ім'я), age (вік) і faculty (факультет). 
# Напишіть метод display_info(), який виводить на екран інформацію про студента.
# Розширте клас Student, додавши атрибут grades (оцінки) у вигляді словника, де ключі - це назви предметів, а значення - оцінки студента. 
# Напишіть метод calculate_average_grade(), який обчислює середній бал студента на основі його оцінок.
class Students():
    def __init__(self, name, age, faculty, grades_dict):
        self.name = name
        self.age = age 
        self.faculty = faculty 
        self.grades = grades_dict
        

    def display_info(self):
            print('Name of student: ', self.name)
            print('Age: ', self.age)
            print('Faculty: ', self.faculty)
            print('Grade: ', self.grades)

s = Students('Jenya', '22', 'Historical', {'world history': 100, 'bio': 88})
s.display_info()
s1 = Students('Alina', '21', 'Law ', {'family law': 78, 'criminal law': 99, 'international relations': 88})
s1.display_info()
s2 = Students('Nick', '19', 'Physical', {'math': 60, 'physics': 97, 'chemistry': 72})
s2.display_info()

def calculate_average(grades_dict):
         return sum(grades_dict)


grades_dict = [100, 98]
grades_dict1 = [78, 99, 88]
grades_dict2 = [60, 97, 72]

average = calculate_average(grades_dict)
average1 = calculate_average(grades_dict1)
average2 = calculate_average(grades_dict2)
print("Average of grades: ", average)
print("Average of grades: ", average1)
print("Average of grades: ", average2)




    








    


        

    

