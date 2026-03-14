def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def split_string(func):
    def wrapper():
        result = func()
        return result.split()
    return wrapper
