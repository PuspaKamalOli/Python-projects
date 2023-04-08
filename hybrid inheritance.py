class A:
    def w(self):
        print("this is w from  class A")
class B(A):
    def x(self):
        print("this is x from  class B")
class C(A):
    def y(self):
        print("this is y from  class C")
class D(B,C):
    def z(self):
        print("this is Z from class D")
obj=D()
obj.w()
obj.x()
obj.y()
obj.z()