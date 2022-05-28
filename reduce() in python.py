# reduce(function,iterables):converts iterables to a single value
import functools

prime_numbers = [3, 7, 5, 17, 33, 23, 29, 11]
fruit = ['b', 'a', 'n', 'a', 'n', 'a']
multiply = lambda x, y: x * y
print('resultant multiplication is: ' + str(functools.reduce(multiply, prime_numbers)))
print(functools.reduce(lambda x, y: x + y, fruit))
