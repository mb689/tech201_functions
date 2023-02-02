# tech201_functions

## Functions

### How to create a function
- Use the `def` keyword to define the function.
- Name the function based on its functionality.
- Include all the logic within the function
- Examples:
```
def print_something(print_String):
print(print_String)
```

### How to use the created function
- You will need to invoke the function using the function name followed by brackets.
- Example:
`print_something()`

### The return statement
- For some functions we would like it to do some sort of logic and then return something back to us like an int.
- To use this we use the keyword `return`.
- Example:
```
def addition(int1=1, int2=2):
return int1 + int2
```
- The above code will return the addition of the two numbers.


### Specify argument types
- We can specify the types of each argument used in a function
- Example:
```
def greeting(name: str):
print("Hello, my name is " + name)
```