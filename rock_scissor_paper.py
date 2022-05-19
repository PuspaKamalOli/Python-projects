#  a game with random module
import random

while True:
    choices = ['rock', 'paper', 'scissor']
    computer = random.choice(choices)

    your_choice = ''
    while your_choice not in choices:
        your_choice = input('rock, paper, or scissor: ').lower()
    if your_choice == computer:
        print('computer choice: ' + computer)
        print('your choice: ' + your_choice)
        print('result: ' + "It's a tie!!")
    elif (computer == 'rock' and your_choice == 'scissor') or (computer == 'paper' and your_choice == 'rock') or (
            computer == 'scissor' and your_choice == 'paper'):
        print('computer choice: ' + computer)
        print('your choice: ' + your_choice)
        print('result: ' + 'computer won')
    else:
        print('computer choice: ' + computer)
        print('your choice: ' + your_choice)
        print('result: ' + ' hurray!! you won..')
    play_again = input('do want to play again? yes/no: ').lower()
    if play_again != 'yes':
        break
