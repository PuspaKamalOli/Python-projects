class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def display(self):
        print("param1:", self.param1)
        print("param2:", self.param2)
        
        
obj=MyClass(100,200)
obj.display()
