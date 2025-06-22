def decorator(func):
    def wrapper():  # nested function that is function inside function
        print("content to be printed before calling the function")
        func()
        print("content after calling the function")
    return wrapper
@decorator #without changing actual code to modify extend behaviour of function

def greet():  #decorator takes this as argument
    print("hello world!!")

greet()

#decorator with arguments(multiple arguments) here function takes multiple arguments
def decorator(func):
    def wrapper(*args, **kwargs):
        print("content to be printed before")
        func(*args, **kwargs)
        print("content to be printed after")
    return wrapper
@decorator
def value(*args, **kwargs):
    print(args, kwargs)

value(10, 20 ,30, x = 10, y = 20, z = 30)


def decorator(func):
    def wrapper(*args, **kwargs):
        print("content to be printed before")
        return func(*args, **kwargs)
    return wrapper
@decorator
def add(a, b):
    return a + b
print(add(5, 6))


#decorating a function with multiple decorator 
def decorator(func):
    def wrapper():
        a = func()
        return a * a
    return wrapper
def decorator1(func):
    def wrapper():
        a = func()
        return a * 10
    return wrapper
@decorator
@decorator1  #decorators are applied from bottom to top
def value():
    return 10

@decorator1
@decorator
def value2():
    return 20

print(value())
print(value2())

#one decorator on multiple function
def decorator(func):
    def wrapper():
        print("running for", func.__name__)
        result = func()
        return result * 2
    return wrapper
@decorator
def one():
    return 5

@decorator
def two():
    return 25

print(one())
print(two())


def decorator(func):
    def wrapper_square():
        print(f"Using square logic for {func.__name__}")
        return func() ** 2

    def wrapper_multiplyby10():
        print(f"Using multiply by 10 logic for {func.__name__}")
        return func() * 10

   
    if func.__name__ == "one":   # this requiers choose which wrapper to return
        return wrapper_square
    else:
        return wrapper_multiplyby10
    
@decorator
def one():
    return 3

@decorator
def two():
    return 4

print(one()) 
print(two())


#passing arguments to the decorator itself instead of function
def decorator(mode):  #decorator factory
    def main_decorator(func):  #used to wrap
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if mode == "square":
                return result **2
            elif mode == "multiply":
                return result * 10
            else:
                return result
        return wrapper
    return main_decorator    
@decorator("square")
def value1():
    return 3

@decorator("square")
def value2():
    return 4

print(value1())
print(value2())
