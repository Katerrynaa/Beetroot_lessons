# task 1
class Animal():
    def __init__(self, name):
        self.name = name 

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("Woof!")

animals = [Cat("Garfield"), Dog("Michael")]
for animal in animals:
    animal.talk()

# task 2
class Library:
    def __init__(self, name, books=[], authors=[]):
        self.name = name 
        self.books = books
        self.authors = authors

    def __repr__(self):
        return (self.name + '; ' + self.books + '; ' + self.authors)
    
    def __str__(self):
         return (self.name + '; ' + self.books + '; ' + self.authors)
    
class Book:
    list_of_book = []
    def __init__(self, name, year, author):
        self.name = name 
        self.year = year
        self.author = author 
        Book.list_of_books = ['Book: Robinson Cruose', 'Year: 1719', 'Author: Daniel Defoe',
                              'Book: Clarissa', 'Year: 1748', 'Author: Samuel Richardson',
                              'Book: Tom Jones', 'Year: 1748', 'Author: Frankenstein']

    def __repr__(self):
        return (self.name + '; ' + str(self.year) + '; ' + self.author)
    
    def __str__(self):
        return (self.name + '; ' + str(self.year) + '; ' + self.author)
    
    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.list_of_books.append(book)
        return book
    
    def group_by_year(self, year):
        self.year = year
        grouped_year = [year for year in self.year if year == year]
        return grouped_year

class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name 
        self.country = country 
        self.birthday = birthday
        self.books = books 

    def __repr__(self):
        return (self.name + '; ' + self.country + '; ' + self.birthday + '; ' + self.books)
    
    def __str__(self):
        return (self.name + '; ' + self.country + '; ' + self.birthday + '; ' + self.books)
    
    def group_by_author(self, author):
        grooped_books = [book for book in self.books if author == author]
        return grooped_books
        
l = Library('Explorer Library', 'Books: Robinson Cruose, Clarissa, Tom Jones, Frankenstein',
            'Authors: Daniel Defoe, Samuel Richardson, Henry Fielding, Mary Shelley')
print(repr(l))
print(str(l))

b = Book('Book: Robinson Cruose,', 'Year: 1917',  'Author: Daniel Defoe') 
print(repr(b))
print(str(b))
b.new_book(name='Harry Potter', year='Year: 2000', author=' Author: J.K.Rowling')
print(b.list_of_books)
book1 = 'Robinson Cruose'
book2 = 'Clarissa'
book3 = 'Tom Jones'
b.group_by_year = b.list_of_books
print("Books in 1748 :", book2, 'and', book3)
for books in b.group_by_year:
    print(books)

a = Author('Name of author: Louisa May Alcott', 'Country: Germantown, Pennsylvania U.S', 'Birthday: November 29, 1832',
            'Books: Little Women, Good Wives, Eight Cousins')
print(repr(a))
print(str(a))

author1 = 'Louisa May Alcott'
a.group_by_author = a.books
print("Books by", author1,":")
for books in a.group_by_author:
    print(books)

#task 3
class Fraction():
    def __init__(self, value):
        self.value = value
    
    def Add(self, other):
        if not isinstance(other, type(self)):
            raise ValueError("The wrong type for operand")
        return Fraction(self.value + other.value)
    
    def Sub(self, other):
        if not isinstance(other, type(self)):
            raise ValueError("The wrong type for operand")
        return Fraction(self.value - other.value)
    
    def Div(self, other):
        if not isinstance(other, type(self)):
            raise ZeroDivisionError("Numbers are not divisible by zero")
        return Fraction(self.value / other.value )
    
    def Mul(self, other):
        if not isinstance(other, type(self)):
            raise ValueError("The wrong type for operand")
        return Fraction(self.value * other.value)

    def __str__(self):
        return f"<Fraction: {self.value}>"
    
if __name__ == "__main__":
    f1 = Fraction(56)
    f2 = Fraction(23)
    f3 = Fraction.Add(f1, f2)
    f4 = Fraction.Sub(f1, f2)
    f5 = Fraction.Mul(f1, f2)
    f6 = Fraction.Div(f1, f2)

    print(Fraction.__str__(f3), Fraction.__str__(f4), Fraction.__str__(f5), Fraction.__str__(f6))


# практичні завдання за 18.07
# Вправа 1: Побудова системи банківських рахунків
# Реалізуйте клас BankAccount, який представляє банківський рахунок. 
#  Він повинен мати приватні змінні, такі як номер рахунку та баланс, 
# і загальнодоступні методи для внесення, зняття та отримання балансу рахунку.
class BankAccount():
    def __init__(self, deposit, withdraw, get_balance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.get_balance = get_balance
        self.__number = '№100'
        self.__balance = '500 000£'

    def show(self):
        print("deposit: ", self.deposit, "Withdraw: ", self.withdraw, "Balance: ", self.get_balance)

bank = BankAccount('100 000 000£', '50 000£', '400 000 00£')
print("Your amount has been added to the account: ", bank.deposit, "withdraw: ", bank.withdraw, "Your balance is: ", bank.get_balance)

# Вправа 2: Створення студентського класу
# Реалізація класу Student, який представляє студента. 
# Він повинен мати загальнодоступні змінні, такі як ім’я та оцінка, і приватну змінну для зберігання ідентифікатора студента. 
# Використовуйте захищені змінні для зберігання списку курсів, які вивчає студент.
class Student():
    def __init__(self, name, grade, courses):
        self.name = name 
        self.grade = grade
        self.__id = 911
        self._courses = courses

    def show(self):
        print(f"Student's name: ", self.name,"\n" "Student's grade: ", self.grade,"\n" "Objects: ", self._courses)
    
s = Student('Nick', '100 points', 'math, chemistry, basics programming')
s.show()

# Вправа 4: Управління працівниками
# Реалізація класу Employee, який представляє працівника в компанії. 
# У кожного співробітника повинні бути такі змінні, як ім’я, відділ, керівник, навички, рівень англійської та зарплата. 
# Поле рівня англійської мови має бути захищеним, а поле зарплати має бути закритим. 
# Створіть клас Department, який містить співробітників і методи додавання та видалення співробітників, 
# а також обчислення середньої зарплати для відділу.  
class Employee():
    def __init__(self, name, department, manager, skills, english_level, salary):
        self.name = name
        self.department = department
        self.manager = manager 
        self.skills = skills 
        self._english_level = english_level
        self.__salary = salary

class Department():
    def __init__(self, name):
        self.name = name
        self.employee = []
    
    def add_empl(self, *args):
        self.employee.append(args)

    def remove_empl(self, employee):
        if employee in self.employee:
            self.employee.remove[employee]

    def calculate_average_salary(self, total):
        self.total = total
        average_salary = total / len(self.employee)
        return average_salary

e = Employee('Name: Alton', 'Legal Department', 'Manager: Albert', 'Skills: Organization and Analysis', 'English level: C1', salary='3300$')
e1 = Employee('Name: Adam', 'Accounting', 'Manager: Albert', 'Skills: Knowledge of General Business Practices', 'English level: B1', salary='5000$')
e2 = Employee('Name: Stacey', 'Service and customer service', 'Manager: Albert', 'Skills: Empathy and Time management', 'English level: C2', salary='"2100$$')
e3 = Employee('Name: Vicky', 'HR', 'Manager: Albert', 'Skills: Communication and Administrative expertise', 'English level: C2', salary='1900$')
Accounting_department = Department("Accounting")
Accounting_department.add_empl(e1)
Accounting_department.remove_empl(e)
print(Accounting_department.calculate_average_salary())

# 2 варіант виконання завдання
class Employee:
    def __init__(self, name, department, manager, skills, english_level, salary):
        self.name = name
        self.department = department
        self.manager = manager 
        self.skills = skills 
        self._english_level = english_level
        self.__salary = salary

class Department:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        return self.employees
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove[employee]

    def calculate_average_salary(self, total):
        self.total = total
        average_salary = total / len(self.employees)
        return average_salary

our_employee1 = Employee(name='Vicky', department='HR', manager='Adam', skills='Communication and Administrative expertise', 
                        english_level='B1', salary='2000$')
our_employee2 = Employee(name='Stacey', department='Legal', manager='Nick', skills='Organiztion and Analysis', english_level='C2', 
                         salary='2400$')
our_employee3 = Employee(name='Martin', department='Accounting', manager='Elizabet', skills='Knowledge of General Business Practices', 
                        english_level='B2', salary='3400$')

department = Department()
department.add_employee(our_employee1)
department.remove_employee(our_employee3)
print(department.calculate_average_salary())


  

    
    

    





        
   
        
