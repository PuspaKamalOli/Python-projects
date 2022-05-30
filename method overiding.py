# method overriding:if parents class and child class have same method and is called through child class method of child class is exexuted as it is most closest to the child class
class Car:
    def engine(self):
        print('their engine requires oil to run')

    def features(self):
        print('modern cars are fast and reliable')


class Tesla(Car):
    def engine(self):
        print('they run on electricity')

    def features(self):
        print('they have autopilot system')


tesla = Tesla()
tesla.engine()
tesla.features()
