# hanges made to the copied object will not affect the original object,
# since they reference different memory locations.


import copy

original = [1, 2, [3, 4]]
copy = copy.deepcopy(original)

# change the nested list in the copied object
copy[2][0] = 5

# the change does not affect the original object
print(original)  # prints [1, 2, [3, 4]]
print(copy)  # prints [1, 2, [5, 4]]
