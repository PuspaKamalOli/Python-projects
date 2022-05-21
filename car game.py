started = False
stopped = False
print('Welcome To Car Game Buddy!!...')
while True:
    command = input('>')
    if command == 'quit':
        break
    elif command == 'stop':
        if stopped:
            print('car has already stopped')
        else:
            stopped = True
            print('car has stopped')
    elif command == 'start':
        if started:
            print('car has already started')
        else:
            started = True
            print('car has started')
    elif command == 'help':
        print("start:to start the car\nstop:to stop the car\nquit:to quit the game")
    else:
        print("sorry i don't understand")
