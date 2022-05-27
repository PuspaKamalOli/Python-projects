# filter(function,iterables):creates a collection of elements from an iterables for which function which returns true
list_1 = [34, 65, 77, 33, 17, 100, 120, 5]
even_number = list(filter(lambda x: x % 2 == 0, list_1))
large_numbers = list(filter(lambda x: x >= 77, list_1))
print(even_number, large_numbers)
