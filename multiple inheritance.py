# multiple inheritance:a child class having multiple parents can inherit all the methods from its parents

class Terrestrial:
    def live(self):
        print("they can live on land")

    def run(self):
        print('they can run faster in ground')


class Aquatic:
    def respire(self):
        print('they can breathe in water')

    def swim(self):
        print('they can swim in water')


class Frog(Terrestrial, Aquatic):
    pass


frog = Frog()
frog.live()
frog.swim()
frog.respire()
