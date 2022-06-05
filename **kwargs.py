# **kwargs:allows to pass as many key,value as in argument as we want
# works as a dictionary
def cost(**kwargs):
    keys = []
    values = []

    for key, value in kwargs.items():
        keys.append(key)
        values.append(value)
    new_dict = {key: value * 0.8 for key, value in kwargs.items()}
    print(keys)
    print(values)
    print(new_dict)


cost(pant=89, shirt=50, shoes=90, underwear=20)
