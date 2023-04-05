original = [1, 2, [3, 4]]
copy = original.copy()

# change the nested list in the copied object
copy[2][0] = 5

# the change also affects the original object
print(original) # prints [1, 2, [5, 4]]
print(copy) # prints [1, 2, [5, 4]]
