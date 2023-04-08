class OuterClass:
    def __init__(self):
        self.outer_var = "Outer variable"

    def outer_method(self):
        print("This is an outer method")

    class NestedClass:
        def __init__(self):
            self.nested_var = "Nested variable"

        def nested_method(self):
            print("This is a nested method")

# Create an object of the outer class
outer_obj = OuterClass()

# Access the outer class member variables and methods
print(outer_obj.outer_var)
outer_obj.outer_method()

# Create an object of the nested class
nested_obj = outer_obj.NestedClass()

# Access the nested class member variables and methods
print(nested_obj.nested_var)
nested_obj.nested_method()
