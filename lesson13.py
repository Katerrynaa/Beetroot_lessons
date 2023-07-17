#task 1
#1
def func():
    pass

def fun2():
    c = 146
    str = 'Programming tomorrow'

print(fun2.__code__.co_nlocals)


#2
def function():
    a = 'lecture'
    c, d, v = 12, 44, 78

print(function.__code__.co_nlocals)



#task 2
#1
def function(text):
    text = text
    
    def inner():
       print(text)
    
    inner()
    
if __name__ == '__main__':
        function("How are you?")


#2
def func1():
    print("something know")
    def func2():
        print("nothing, okay?")
    func2()
func1()


#task 3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]















    
