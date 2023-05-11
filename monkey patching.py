class A:

    def old_method(self):
        print("this is old method")

    def hi(self):
        pass


def modified_method(self):
    print("this is modified method")


def new_method(self):
    print("this is new method")


obj = A()
#before  modification

obj.old_method()


#after modification
A.old_method = modified_method
obj.old_method()


#adding new method in class
A.new_method = new_method
obj.new_method()


del A.hi
