def add_message(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("The function has been executed successfully!")
        return result
    return wrapper


@add_message
def my_function(x, y):
    return x + y


# prints "The function has been executed successfully!"
result = my_function(2, 3)
print(result)  # prints 5
 