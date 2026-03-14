from decorator import my_decorator
from decorator import uppercase_decorator
from decorator import split_string

# Exemplo 1
@my_decorator
def my_function():
    print("This is my function.")

my_function()

# Exemplo 2
@uppercase_decorator
def another_function():
    return "This is another function."

print(another_function())

# Exemplo 3
@split_string
@uppercase_decorator
def yet_another_function():
    return "This is yet another function."
print(yet_another_function())
