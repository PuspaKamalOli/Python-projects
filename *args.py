# *args:allows to use as many argument as we want in a function


def integer(*args):
    ls = []

    for i in args:
        ls.append(i)
    ls = ls + [23]

    print(ls)


integer(29, 14, 89, 'apple', 'mango')
