# task 1
#show several different solutions
# 1
import unittest 

class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname 
        self.age = age 

    def talk(self):
        print(f"Hi, my name is {self.name} {self.surname},  I'm {self.age} years old.")


p = Person('Karl', 'Johnson', '26')
p.talk()

class TestPerson(unittest.TestCase):
    def test_talk(self):
        p = Person("Karl", "Johnson", "26")
        output = "Hi, my name is Karl Johnson, I'm 26 years old."
        self.assertEqual(p.talk(), output)

if __name__ == "__main__":
    unittest.main()

# 2
from function_test import div_numbers

class TestDivideNumbers(unittest.TestCase):
    def test_division(self):
        result = div_numbers(1345, 60)
        self.assertEqual(result, 22,4)
    
    def test_not_num_arguments(self):
        with self.assertRaises(TypeError):
            div_numbers("a", 20)

if __name__ == "__main__":
    unittest.main()


# task 2 
import unittest
from function_test import my_list

class TestString(unittest.TestCase):
    def test(self):
        dict1 = [{
    'name': 'Karolina',
    'surname': 'Belluchi',
    'number': '49000 3444',
    'city': 'Chicago',
    'id': '446'
}]
        dict2 = [{
    'name': 'Karolina',
    'surname': 'Belluchi',
    'number': '49000 3444',
    'city': 'Chicago',
    'id': '446'
}]
        self.assertEqual(dict1, dict2)

if __name__ == "__main__":
    unittest.main()
