# object:instance of an class
# class:blueprint

#python is OOP so it mainly emphasizes on using function that everything like list,tuple,dict etc is treated like an object i
# declaring class
class Measurement:
    # constructor
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    # methods inside of a class
    def area(self):
        print(f'The area is {self.length * self.breadth}  squared centimeter.')

    def volume(self):
        print(f'The volume is {self.length * self.height * self.breadth} cubed centimeter.')


# object
rectangle = Measurement(6, 7, 0)
# object
cuboid = Measurement(9, 22, 17)
rectangle.area()
cuboid.volume()
