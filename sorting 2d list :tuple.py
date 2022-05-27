# list.sort(key,reverse=True/False) to sort list
# sorted(iterables,key) to sort tuples
list_1 = [('cat', 80, False),
          ('apple', 70, True),
          ('ball', 100, False)]
tuple_1 = (('cat', 80, False),
           ('apple', 70, True),
           ('ball', 100, False))
func1 = lambda x: x[1]
func2 = lambda x: x[0]
list_1.sort(key=func1),
tuple_2 = sorted(tuple_1, key=func2)

print(list_1, tuple_2)
