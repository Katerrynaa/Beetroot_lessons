# task 1
class EmailPost:
    def __init__(self, email):
        if self.validate(email):
         self.email = email 
        else:
           return ValueError("This format is not supported")

    @classmethod
    def validate(cls, email):
       return email 
    
    def display(self):
       print("Your email is:", self.email)

e1 = EmailPost('abc_def@mail.com')
e1.display()
    
# task 2
class Boss:
    def __init__(self, name, id_, company):
        self.name = name
        self.id = id_
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)
    
    def get_worker(self):
        return self.workers
    
class Worker:
    def __init__(self, name, id_, company, boss: Boss):
        self.name = name
        self.id = id_
        self.company = company
        self.boss = boss

    def set_boss(self, boss):
        if isinstance(boss, Boss):
         self._boss = boss
         boss.add_worker(self)
        
    def get_boss(self):
        return self._boss
    
b1 = Boss(name="Name: Sasha", id_='', company='Company: Environmental protection')
w1 = Worker(name="Name: Alina", id_='', company='Company: Environmental protection', boss=Boss)

w1.set_boss(b1)
b1.add_worker(w1)
print(w1.get_boss().name)
print(b1.get_worker())

# task 3
class TypeDecorators:
    def to_int(func):
        def inner(*args):
            result = func(*args)
            return int(result)
        return inner 
    
    def to_str(func):
        def inner(*args):
            result = func(*args)
            return str(result)
        return inner 
    
    def to_bool(func):
        def inner(*args):
            result = func(*args)
            return bool(result)
        return inner 
    
    def to_float(func):
        def inner(*args):
            result = func(*args)
            return float(result)
        return inner 

@TypeDecorators.to_int
def multi(a, b):
    return a + b 

@TypeDecorators.to_str
def concat_str(a1, a2):
    return a1 + a2

@TypeDecorators.to_bool
def equality_of_numbers(a1, a2):
    return a1 == a2 

@TypeDecorators.to_float
def div(a, b):
    return a / b 

print(multi(123, 16))
print(concat_str("Hello",', ' "Universe"))
print(equality_of_numbers(12, 13))
print(div(50, 20))



