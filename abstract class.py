# abstract classes:i f there's a abstract method is made in a parent class,child class must have the same method to run further programs
from abc import ABC, abstractmethod


class Vechiles(ABC):
    @abstractmethod
    def transport(self):
        pass

    # the abstract method class cannot be called or printed it just makes methods compulsory to use
    def engine(self):
        print('Their engine requires energy such as petrol,disel to run')


class Car(Vechiles):
    # this class must have transport method which is the abstract method of its parent class
    def transport(self):
        print('Cars allows you to move from one place to another')

    def tyres(self):
        print('Car must have four tyres to run')


car = Car()
car.engine()
car.transport()
car.tyres()
