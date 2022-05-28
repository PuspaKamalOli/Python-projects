# zip():aggregate elements from two or more iterables**
fruits = ['apple', 'banana', 'papaya', 'grapes', 'mango']
price = [100, 120, 160, 175, 80]
fruits_price = list(zip(fruits, price))
price_fruits = dict(zip(price, fruits))
print(fruits_price)
print(price_fruits)
for key, value in price_fruits.items():
    print(value)
