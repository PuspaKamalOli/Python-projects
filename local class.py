def create_person(name, age):
    # Define a local class within the function
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)

    # Create an object (instance) of the local class
    person = Person(name, age)
    
    # Call methods of the local class
    person.display()

# Call the function to create and use the local class
create_person("Alice", 25)
