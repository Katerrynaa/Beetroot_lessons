# task 1
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()
    
    def append(self, item):
        current = self._head
        found = False
        temp = Node(item)
        while not found:
            if self._head == None:
                found = True
                self.head = temp
            elif (self._head != None) & (current.get_next() == None):
                found = True
                current.set_next(temp)
            else:
                current = current.get_next()
    
    def insert(self, item, pos):
        ind = 0
        temp = Node(item)
        previous = None
        current = self._head
        if pos == 0:
            temp.set_next(self.head)
            self.head = temp
        else:
            while ind < pos:
                ind += 1
                previous = current
                current = current.get_next()
            temp.set_next(current)
            previous.set_next(temp)

    def index(self, item):
        ind = 0
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
                return ind
            else:
                current = current.get_next()
                ind += 1

    def pop(self):
        current = self._head
        previous = None
        if current.get_next() == None:
            self.head = None
        else:
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
        return current.get_data()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))


    my_list.append(190)
    my_list.append(111)
    print(my_list)
    
    print ("Index items in the list:", my_list.index(0), my_list.index(2))
    print("Remove the last item: ", my_list.pop())
    print("list after removing the last item: ", my_list)

    print("Before insertion: ",my_list)
    print("After insertion: ", my_list.insert(2, 2))
    
# практичні завдання 
# Створити клас Node для вузла Linked list. У Node повинно бути поле data (дані) і поле next_node.
class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert(self, data):
        new_node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print_ll(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert(2)
ll.insert(10)
ll.insert(100)
ll.print_ll()


# Створити клас LinkedList для реалізації linked list з методами додавання Node, видалення Node та виведення списку.
# Реалізувати функцію для зворотнього перегляду (виведення списку в зворотньому порядку).
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None 
        self.last_node = None 
    
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next 
    
    def delete(self, key):
        if self.head is None:
            print('The list is empty')
            return 
        
        if self.head.data == key:
            self.head = self.head.next
            return 
        
        current = self.head 
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

        if current is None:
            print("Key not found")
        else:
            previous.next = current.next 

    def reverse(self):
        previous = None 
        current = self.head 
        while(current is not None):
            next = current.next
            current.next = previous
            previous = current 
            current = next
        self.head = previous

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end='')
            temp = temp.next


    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end='=>')
            current = current.next
        print()

if __name__ == "__main__":
    l = LinkedList()
    l.append(100)
    l.append(33)
    l.append(1102)
    l.append(200)
    l.append(300)
    l.display()
    l.delete(200)
    l.delete(300)
    l.display()
    print("Ordinary linked list")
    l.display()
    l.reverse()
    print("Reversed linked list")
    l.display()
