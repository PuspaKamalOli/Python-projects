# printing odd and even number according to users desire

ask_user = input('even number(e) or odd number(0): ')
starting_number = int(input('starting number: '))
stopping_number = int(input('stopping number: '))
if ask_user == 'e':
    print('required even numbers are: ', end='')
    for i in range(starting_number, stopping_number + 1):
        if i % 2 == 0:
            print(i, end=' ')
else:
    print('required odd numbers are: ', end='')
    for i in range(starting_number, stopping_number + 1):
        if i % 2 != 0:
            print(i, end=' ')
