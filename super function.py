# super():used to give access to method of parents class
class Animal:
    def __init__(self, abdomen, mouth):
        self.abdomen = abdomen
        self.mouth = mouth

    def structure(self):
        print(f'all the animals have{self.mouth} and {self.abdomen}')


class Mouse(Animal):
    def __init__(self, abdomen, mouth, legs):
        super().__init__(abdomen, mouth)
        self.legs = legs

    def stomech(self):
        print('mices have ' + self.abdomen + 'abdomen')

    def features(self):
        print(f"they have {self.legs} legs and {self.mouth} mouth")


Animal('abdomen', 'mouth').structure()
mouse = Mouse('small', 'one and onely', '4')
mouse.stomech()
mouse.features()
