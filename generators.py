
#In Python, a generator is a special type of iterable, which allows you to iterate over a sequence of values without actually creating the entire sequence in memory at once. Instead, a generator generates each value on-the-fly as you iterate over it.

#Generators are defined using the yield keyword, which is similar to return but instead of stopping the function and returning a value, it suspends the function and returns a generator object that can be used to iterate over the values produced by the generator.#

def number_sequence(n):
    for i in range(n):
        yield i

# Usage:
for number in number_sequence(5):
    print(number)