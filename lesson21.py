# task 1 
# 1
class MyCar:
    def __enter__(self):
        self.car_name = 'Volvo'
        return self
    def __exit__(self, exc_type, exc_val, exc_tab):
        self.car_color = 'Red color'
        print(f'I got a new car: {self.car_name} {self.car_color} ')

with MyCar() as car:
 print("Today I was one meet")
 print("My working company made a present for me")

# 2
class MyContextManager:
    def __enter__(self):
        print("Inside context manager")
        return "Your context manager here"
    def __exit__(self, exc_type, exc_value, exc_tab):
        print("Outside")

with MyContextManager() as here:
    print(here)

# цей самий код але на основі функції 
from contextlib import contextmanager
@contextmanager
def context():
   print("Inside context manager")
   yield "Your context manager here"
   print("Outside")

with context() as c:
   print(c)

# 3
from contextlib import contextmanager
@contextmanager
def opened_file(name):
   file = open(name, "w+")
   try:
      yield file 
   finally:
      file.close()

with opened_file("new_file") as file:
   file.write('you did it!')

# task 2
import unittest
from test_sample import MyContextManager

class TestingManager(unittest.TestCase):
    def test_exit(self):
        result = "Outside"
        self.assertEqual(result, "Outside")

if __name__ == "__main__":
    unittest.main()

from test_sample import MyCar
class TestCar(unittest.TestCase):
    def test_enter(self):
        result = "Volvo"
        self.assertEqual(result, "Red Color")

if __name__ == "__main__":
    unittest.main()

from test_sample import contextmanager
class TestString(unittest.TestCase):
    def test_write_file(self):
        content = "you did it"
        self.assertEqual(content, "you did it")
    def test_type(self):
        with self.assertRaises(TypeError):
            contextmanager(int)

if __name__ == "__main__":
    unittest.main()
      
# task 3
import code_pytest
import pytest

@pytest.fixture
def test_lines():
    text = "To be or not to be: that is the question\n Water, water, everywhere, not any drop to drink\n"
    with open("file_with_lines.txt", "w+") as file:
        file.write(text)
    return file.name

def test_content_file(file_with_lines):
    with open(file_with_lines, "r+") as file:
        result = code_pytest(file)
    assert result == 2


   
   


