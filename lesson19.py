# task 1
def with_index(iterable, start=0):
    index = start 
    for item in iterable:
        yield index, item

list_of_clothes = ['hoodie', 'jacket', 'sweater']
for index, item in enumerate(list_of_clothes, start=1):
    print(f"{index}. {list_of_clothes}")

# task 2
def in_range(start, end, step=2):
    for i in range(start, end + 2, step):
        yield i ** 4

a = in_range(2, 20, 4)
for i in a:
    print(i)

# task 3
num_in_the_cube = (i ** 3 for i in range(10))
print(num_in_the_cube)
num_in_the_cube_1 = [i ** 3 for i in range(10)]
print(num_in_the_cube_1)

