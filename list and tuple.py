# list[]:collection of similar object that can be mutated and is ordered
# list
list_1 = [1, False, 5, 'apple', 'tesla']

# list methods
# add item at last index
list_1.append('iphone')

# add item at given index
list_1.insert(3, 'car')

# remove item
list_1.remove(5)

# remove last item
list_1.pop()

# sort items in  list
# list_1.sort(key=function,reversed=True/False)

# reverse the order of members in a list
list_1.reverse()

# list.clear():remove all members of list

print(list_1)

# tuple():unumutable,group of similar items
tuple_1 = (True, 56, 'john cena')
# tuple methods
print(tuple_1.index(1))
print(tuple_1.count(True))
