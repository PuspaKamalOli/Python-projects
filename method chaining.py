# method chaining:it is the process of calling many methods of a class in a sinlge line of code
# we need to return self in each method for method chaining

class Computer:
    def digital_computer(self):
        print('digital computers work on digital signal')
        return self

    def analog_computer(self):
        print('analog computers work on analog signal')
        return self

    def hybrid_computers(self):
        print('hybrid computers work on both signal')
        return self


computer = Computer()
computer.digital_computer().analog_computer().hybrid_computers()
