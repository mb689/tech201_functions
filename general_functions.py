# Functions

# D R Y
# Don't Repeat Yourself

# Creating a function

# def print_something(print_String):
#     print(print_String)
#
# print_something("Hello World")
#
#
# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(1,2))

# def addition(int1=1, int2=2):
#     return int1 + int2
#
# print(addition())


# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for args in multiargs:
#         print(args)
#
# multi_args(1,2,3,4,5)

# Type Hints

def greeting(name: str):
    print("Hello, my name is " + name)

greeting("Mohamed")


def division(int1: int = 5, int2: int = 2) -> float:
    return int1 / int2

print(division())

# Functions best practices

## name your functions clearly using lower case and underscores
## All arguments should be clear in their need and where possible include in their expected type
## remember the return statement or your functions will return none
## keep functions small to preserve readability abd simplicity
## use comments in your functions to give instructions on how to use them
## consider using type hints to avoid type errors when you run your code