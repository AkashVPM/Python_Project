def something():
    print('nothing')

def mydecorator(functionPointer):
    def inner_function(*args, **kwargs):  # Proper function definition
        print("Before function call")  # Do something before calling the function
        result = functionPointer(*args, **kwargs)  # Call the function
        print("After function call")  # Do something after calling the function
        return result
    return inner_function

@mydecorator
def nothing():
    print(something())  # Call the function, not print its reference

nothing()  # Call the decorated function
