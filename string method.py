# string methods:ways of editing string
apple = 'apple a day keeps the doctor away'

# finds length of character
print(len(apple))

# finds index of character or word
print(apple.find('apple'))

# replace character or word with another
print(apple.replace('apple', 'banana'))

# finds index of word or char in string
print(apple.find('day'))

# count its repeatition
print(apple.count('a'))

# check if it's in upper case
print(apple.upper())

# capitalize first letter of string
print(apple.capitalize())

# make all letters lower
print(apple.lower())

# check data_type
print(apple[0].isalpha(), apple.isdigit())
