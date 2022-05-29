# multilevel inheritance:child class inherits all the methods from its parents and grandparents class

class Vertebrate():
    def backbone(self):
        print('they have backbones')

    def level(self):
        print('they are highly developed animals')


class Aquatic_animals(Vertebrate):
    def live(self):
        print('they live under water')


class Fishes(Aquatic_animals):
    def respire(self):
        print('they breathe through their gills')


Fishes().live()
Fishes().backbone()
Fishes().level()
Fishes().respire()
