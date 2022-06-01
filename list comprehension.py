# list comprehension:a way to create list with short code
square_number = [i * i for i in range(1, 11)]
odd_numbers = [i for i in range(1, 11) if i % 2 != 0]
odd_even_numbers = [f'{i} is even' if i % 2 == 0 else f'{i} is odd' for i in range(1, 11)]
print(square_number)
print(odd_numbers)
for i in odd_even_numbers:
    print(i)
