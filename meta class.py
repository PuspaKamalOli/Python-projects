class MyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # Add "custom_" prefix to all attribute names
        custom_attrs = {}
        for attr_name, attr_value in attrs.items():
            custom_attrs["custom_" + attr_name] = attr_value
        return super().__new__(cls, name, bases, custom_attrs)

class MyClass(metaclass=MyMetaClass):
    var1 = "Value 1"
    var2 = "Value 2"

# Create an object of the class
obj = MyClass()

# Access the custom attributes added by the metaclass
print(obj.custom_var1)  # Output: Value 1
print(obj.custom_var2)  # Output: Value 2
