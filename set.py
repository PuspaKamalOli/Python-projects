# set{}:unordered,collection of object,faster than list
set_1 = {True, 12, 'apple', 22.5}
set_2 = {False, 'apple'}
set_3 = {'jaya samvo'}

# remove item
set_1.remove(22.5)

# add item
set_1.add(23.5)

# remove all items
set_3.clear()

# add another items which is not present in present set
set_1.update(set_2)

# give union of two sets
set_1.union(set_2)

# print common elements in 2 or more sets
set_1.intersection(set_2, set_3)

# print elements which present only in originnal set
set_2.difference(set_1)
print(set_1)
print(set_2)
print(set_3)
