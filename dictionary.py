# dictionary:mutable ,unordered collection  of key:value,faster than list as it uses hashing to access a value

cost = {'macbook air m1': 1000,
        'iphone 13': 1200,
        'ipad': 800,
        'airpods': 249}
# dict_methods:

# prints value of given keys
print(cost['ipad'])
print(cost.get('iphone 13'))

# print key, value of dict
print(cost.items())

# all the keys
print(cost.keys())

# all the values
print(cost.values())

# remove key,value
cost.pop('airpods')
print(cost)

# add key,value or edit one
cost.update({'apple watch': 399})
print(cost)

# remove all the members
cost.clear()
print(cost)
