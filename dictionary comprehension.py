# dict_comprehension:creates dectionary using an expression/ replace for loops and certain lambda function
price_in_dollar = {"jacket": 25,
                   'pant': 15,
                   't-shirt': 10,
                   'shoe': 30,
                   'belt': 13

                   }
price_in_rupees = {key: (value * 122) for (key, value) in price_in_dollar.items()}
result = {key: 'expensive' if value > 15 else 'cheap' for key, value in price_in_dollar.items()}
print(price_in_rupees)
print(result)
