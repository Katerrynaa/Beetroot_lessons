#task 1
def function(func):
    def inner(*args):
        print(f"Call function {func.__name__} with arguments")
        print(f"Positional arguments: {args}")
        return function
    return inner 

@function
def add_numbers(a, b):
    return a / b

add_numbers(10005, 998)

@function
def square_numbers(*args):
    return [arg ** 2 for arg in args]

square_numbers(666, 99)
    


#task 2
def stop_words(stop_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                for word in stop_words:
                    result = result.replace(word, "*")
            return result
        return wrapper
    return decorator

@stop_words(["orange juice", "summer"])
def my_text(text):
    return text

result = my_text("Margo drinks orange juice every summer.")
print(result) 


    


                


    

    



        



    
