# task 1
class Person():
    def __init__(self, name, faculty):
        self.name = name 
        self.faculty = faculty 

class Student(Person):
    def __init__(self, name, faculty, grades, subjects):
        super().__init__(name, faculty)
        self.grades = grades
        self.subjects = subjects 

class Teacher(Person):
    def __init__(self, name, faculty, work_days, salary):
        super().__init__(name, faculty)
        self.work_days = work_days
        self.salary = salary

s = Student('Student name: Ronald', 'Faculty of law', 'Grades: 98 points', 'Subjects: math, chemistry, basics of programming')
print(s.name, s.faculty, s.grades, s.subjects, sep=' , ')
t = Teacher('Teacher name: Marry', 'Faculty of Chemistry', 'Work days: Monday, Wednesday and Friday', 'Salary: 1000£')
print(t.name, t.faculty, t.work_days, t.salary, sep=' , ')


#task 2
class Mathematician():
    pass

numbers = [1, 22, 50, 77, 32]
def square(numbers):
 res = [num ** 2 for num in numbers]
 print(res)

square(numbers)

numbers1 = [26, -11, -8, 13, -90]
def remove_positives(numbers):
 res = [num for num in numbers1 if num <= 0]
 print(res)

remove_positives(numbers1)

year = [2001, 1884, 1995, 2003, 2020]
def filter_leaps(year):
  for i in year:
    if i % 4 == 0 or i % 100 != 0 and i % 400 == 0:
      print(i)

filter_leaps(year)

# task 3
# я конкретно затупла на цьому дз, буду вдячна якщо вкажеш на помилки і як це виправити
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name 
        self.price = price 

    def display_info(self):
        print(f"Product type: {self.type}; Name: {self.name}; Price: {self.price}")

class ProductStore:
    def __init__(self):
        self.products = []

    def add_product(self, amount):
        amount = 3000
        if amount <= 0:
            raise ValueError("Amount must be a positive number")
        for product in self.products:
            if product in self.products:
                self.products[product] = [product, amount]
                self.products.append(product)

    
    def set_discount(self, identifier, percent, identifier_type = 'name'):
        percent = 10
        if percent > 10:
         raise ValueError("The number must be within 10")
        for product in self.products:
            if identifier_type == 'name' and product == identifier:
                product_price = product_price * (1 - percent / 100)
                return product

    
    def sell_product(self, product_name, amount):
        self.income = 0
        if product_name in self.products: 
            amount = self.products[product_name]
            if amount > amount:
                self.products[product_name] -= amount
                self.income += self.price * amount
        
    def get_income(self):
        return self.income 
    
    def get_all_products(self):
        return self.products 
    
    def get_product_info(self, product_name):
        if product_name in self.products:
            product_info = self.products[product_name]
            return product_info
        else:
            raise ValueError("Product not enough in the store")
    
p = Product(type='Milk', name='Yogurt', price='20$')
product_store = ProductStore()
product_store.add_product(p)
print(p.type, p.name, p.price, sep='; ')
discount_product = ("Milk", 10)
product_store.set_discount(discount_product, percent=10)
product_store.sell_product("Milk", "Yogurt" "20$")
product_store.sell_product("Milk", 4)
print("Income of the store: ", product_store.get_income())
print("Info about products in the store: ", product_store.get_all_products())

#task 4
# насправді не впевнена що виконала правильно завдання, але як зрозуміла
# 1 варіант
class CustomException(Exception):
    file = open("logs.txt", "w+")
    def __init__(self, message, error_code):
            self.message = message
            self.error_code = error_code

try:
    raise CustomException("The text in the file is written incorrectly", 404)
except CustomException as file:
    print(f"Error: ", file.message)
    print(f"Error: ", file.error_code)


# 2 варіант  
class CustomException(Exception):
     def __init__(self, message, error_code):
            self.message = message
            self.error_code = error_code

try: 
     print("The text in the file is written incorrectly")
except Exception as Argument:
     file = open("logs.txt", "w+")
     file.write(str(Argument))
     file.close()


# практичні по класам разом із наслідуванням за 15.07 
# Exercise 1: Online Store Inventory Management
# Create a class hierarchy to represent an online store's inventory management system. 
# Start with a base class called Product and include attributes such as name, price, and quantity. 
# Create subclasses for specific types of products, such as Electronics, Clothing, and Books. 
# Each subclass should have additional attributes and methods specific to the type of product. 
# Implement methods for adding new products, updating quantities, and calculating total inventory value.
class Product():
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
        self.products = []

    def add_products(self, *args):
        self.products.append(args)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        return new_quantity
    
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product['quantity']*product['price']
        print(f"Total is: ", {total})

class Electronics(Product):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.color = color 

class Clothes(Product):
    def __init__(self, name, price, quantity, size, country):
        super().__init__(name, price, quantity)
        self.size = size
        self.country = country

class Books(Product):
    def __init__(self, name, price, quantity, language, type):
        super().__init__(name, price, quantity)
        self.language = language
        self.type = type 
        

a = Electronics('laptop MNK', '10£', '88 pieces', 'black')
print(a.name, a.price, a.quantity, a.color, sep=' , ')
print("\n")
a.update_quantity('55 pieces')
print(a.quantity)
a.add_products('Mobile charging', '20£', 'pink')
print(a.products)
a.calculate_total()
print("\n")

b = Clothes('Hoodie', '100£', '7 pieces', 'M', 'Sweden')
print(b.name, b.price, b.quantity, b.size, b.country, sep=' , ')
print("\n")
b.update_quantity('19 pieces')
print(b.quantity)
b.add_products('Trousers', 'L size', '990£')
print(b.products)
b.calculate_total()
print("\n")

c = Books('Guilty stars', '56£', '2 pieces', 'English and Ukrainian', 'paper')
print(c.name, c.price, c.quantity, c.language, c.type, sep=' , ')
print("\n")
c.update_quantity('200 pieces')
print(c.quantity)
c.add_products('The old man and the sea', '30£', 'italian language')
print(c.products)
c.calculate_total()


# Exercise 5: Flight Booking System
# Create a class hierarchy to represent a flight booking system for an airline. 
# Start with a base class called Flight and include attributes such as flight_number, departure, and arrival.
#  Create subclasses for different types of flights, such as DomesticFlight and InternationalFlight. 
# Each subclass should have additional attributes and methods specific to the type of flight. 
# Implement methods for booking seats, checking flight availability, and generating passenger manifests.

class Flight():
    def __init__(self, flight_number, departure, arrival):
        self.flight_number = flight_number
        self.departure = departure 
        self.arrival = arrival 
        self.passengers = {}

    def add_passenger(self, pas_name, seat_number):
            if pas_name and seat_number:
                 self.passengers[pas_name] = seat_number
                 return self.add_passenger
                 
    def check(self, num_seats):
         return num_seats < (150 - len(self.passengers))
         
    def info_passengers(self):
          info = f"Flight manifest for Flight {self.flight_number} from {self.departure} to {self.arrival}: "
          return info

class DomesticFlight(Flight):
    def __init__(self, flight_number, departure, arrival, airline):
        super().__init__(flight_number, departure, arrival)
        self.airline = airline

class InternationalFlight(Flight):
    def __init__(self, flight_number, departure, arrival, airport, time):
        super().__init__(flight_number, departure, arrival)
        self.airport = airport
        self.time = time 


d = DomesticFlight('Number of domestic flight: WE224', 'Departure: Mexiko', 'Arrival: Tbilisi', 'Airline: Qantas airlines')
print(d.flight_number, d.departure, d.arrival, d.airline, sep='; ')
i = InternationalFlight('Number of international flight: YTTR11', 'Departure: Amsterdam', 'Arrival: Sydney', 
                        'Airport: Amsterdam International Airport', 'Time: 10p.m' )
print(i.flight_number, i.departure, i.arrival, i.airport, i.time, sep='; ')

d.add_passenger('Nick Bill', '34A')
print("Info about your reservation ticket by Domestic Flight:" )
print(d.passengers)
i.add_passenger('Mary Voi', '11C')
print("Info about your reservation ticket by International Flight:")
print(i.passengers)

print(d.info_passengers())
print(i.info_passengers())

d.check(num_seats=100)
print(d.check(num_seats=100))
i.check(num_seats=230)
print(i.check(num_seats=230))
      
     






    
   
            
        
    
        

    


        
