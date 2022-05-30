# multiple inheritance:a child class having multiple parents can inherit their all methods
class Aquatic:
    def swim(self):
        print('they can swim in water')

    def respire(self):
        print('they can breathe in water')


class Terrestrial:
    def live(self):
        print('they live in land and can run faster')

    def breathe(self):
        print('they can breathe on land')


class Amphibians(Aquatic, Terrestrial):
    pass


amphibians = Amphibians()
amphibians.swim()
amphibians.respire()
amphibians.live()
amphibians.breathe()
