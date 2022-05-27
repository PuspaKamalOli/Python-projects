# map():applies a function to each iterables in an iterable
list_1 = [('cap', 25),
          ('pant', 100),
          ('shirt', 90)]
list_3 = [('apple', 25, 90),
          ('pineapple', 100, 30),
          ('mango', 90, 40)]
func_1 = lambda x: (x[0], x[1] * 1.25)
func_2 = lambda x: (x[0], x[2] * 5)
list_2 = list(map(func_1, list_1))
list_4 = list(map(func_1, list_3))
print(list_2)
print(list_4)
