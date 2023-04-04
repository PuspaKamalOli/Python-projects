class MyClass:
    def my_method(self):
        return "Original method"

obj = MyClass()
print(obj.my_method())  # Output: Original method

def new_method(self):
    return "New method"

MyClass.my_method = new_method
print(obj.my_method())  # Output: New method
