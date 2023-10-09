# task 1 
def help(a):
    stack = []
    for i in a:
        stack.append(i)
    a = ''

    while stack:
        a += stack.pop()
    return a 

if __name__ == "__main__":
    string = 'Python is not a snake'
    reverse = help(string)
    print('Your reverse string: ', reverse)

# task 2
def brackets_balance(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False 
            if current_char == '[':
                if char != "]":
                    return False 

if __name__ == "__main__":
    expr = "{()}[]"

    if brackets_balance(expr):
        print("This is bakanced")
    else:
        print("This is not balanced")
    
# task 3
# part 1
class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()
    
    def get_from_stack(self, items):
        for item in self._items:
            if item == items:
                return True 
            return False 
    


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)
    print(s.pop())
    print(s)

    items = 'e'
    if s.get_from_stack(items):
        print("Element is found")
    else:
        print("Element is not found")

# part 2
class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()
    
    def get_from_stack(self, element):
        for item in self._items:
            if item == element:
                return True
            return False 


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    queue_item = 'e'
    if q.get_from_stack(queue_item):
        print("Queue element is found")
    else:
        print("Queue element is not found")

# завдання з практичного заняття 
import collections

# Реалізація стеку: Напишіть клас, який реалізує структуру даних "стек" з методами для додавання (push) та видалення (pop) елементів.
class MyStack:
    def __init__(self):
        self.list_items = []
    
    def push(self, item):
        self.list_items.append(item)
    
    def pop(self):
        return self.list_items.pop()
    
    def is_list_empty(self):
        return (self.list_items == 0)
    
    def show(self):
        print("Stack items: ", self.list_items)

s = MyStack()
s.push(10)
s.push(20)
s.push(40)
s.push(60)
s.show()
popped = s.pop()
print("Popped: ", popped)
s.show()
empty = s.is_list_empty()
print("Empty list:", empty)

#  Реалізація черги: Напишіть клас, який реалізує структуру даних "черга" з методами для додавання (enqueue) та видалення (dequeue) елементів.
class MyQueue:
    def __init__(self):
        self.queue_list = []
    
    def enqueue(self, item):
        self.queue_list.append(item)
    
    def dequeue(self):
        return self.queue_list.pop()
    
    def display(self):
        print("Queue items:", self.queue_list)

q = MyQueue()
q.enqueue(300)
q.enqueue(120)
q.enqueue(30)
q.display()
deq = q.dequeue()
print("Pop items in queue: ", deq)

# Створіть чергу для обробки завдань. Кожне завдання має поля, такі як ім'я користувача та опис завдання. 
# Реалізуйте функції для додавання завдань в чергу та їх обробки у порядку черги.
queue = []
queue.append("Name: Sasha, "  "Task: Work meeting at 10pm")
queue.append("Name: Michael, "  "Task: Interview")
queue.append("Name: Kate, "  "Task: Check email")

print(queue.pop(0))
print(queue.pop(0))
print("Remaining tasks after completion: ", queue)
        
# Створіть дек та виконайте на ньому наступну послідовність операцій: додайте елементи 1, 2, 3 зліва;
# потім видаліть кожен з цих елементів зліва і додайте його знову праворуч. 
# Виведіть стан деку після кожної операції.
deq = collections.deque([11, 14, 77, 19, 33, 56])
print("Your", deq)

deq.appendleft(1)
deq.appendleft(2)
deq.appendleft(3)
print("After adding left", deq)

deq.popleft()
deq.popleft()
deq.popleft()
print("After removing left", deq)

deq.append(1)
deq.append(2)
deq.append(3)
print("After adding right", deq)
