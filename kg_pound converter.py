# weight converter
while True:
    asking_user = input('convert to kg(k) or pounds(p): ')
    weight = int(input('enter your weight: '))
    if asking_user == 'p'.lower():
        print('your weight in pound is: ' + str(weight / 0.45))
    else:
        print('your weight in kg is: ' + str(weight * 0.45))
    ask_again = input('Do want to do convert more? yes(y) or no(n)')
    if ask_again == 'n':
        break
