import sys
from os import system
import threading

Underscore = '-' * 27

def main():
    main_menu()


# system('cls')
def delete_input():
    t1 = threading.Thread(target=main_menu)
    t1.start()
    t1.join() # commands que up reguardless of time it takes to execute command in front of it.

# Menu format.
def main_menu():
    print(f'{Underscore}\n   __  __                  \n  |  \/  |                 \n  | \  / | ___ _ __  _   _ \n  | |\/| |/ _ \ `_ \| | | | \n  | |  | |  __/ | | | |_| | \n  |_|  |_|\___|_| |_|\__,_| \n {Underscore}')
    print('')
    print('[1] Guess the number')
    print('[2] Calculate time')
    print('[3] Print something')
    print('[4] Change a print option')
    print('')
main()

# List picker.
def pick_action():
    print(f'{Underscore}')
    choice = int(input('pick from menu: '))
    print(f'{Underscore}')
    
    # Guess the number.
    if choice == int(1):
        delete_input()
        print('Guess the number')
        print(f'{Underscore}')
        number = int(543)
        guess = int(input('Number: '))
        
        if guess == number:
            print('Correct number!')
        elif guess > number:
            print('number is too high!')
        elif guess < number:
            print('number is too low')
        else:
            print('error!')
        return(pick_action())
    
    # Calculate time.
    elif choice == int(2):
        delete_input()
        print('Calculate time')
        print(f'{Underscore}')
        
        
        return(pick_action())
        
    # Print something.
    elif choice == int(3):
        delete_input()
        print('Print something')
        print(f'{Underscore}')
        return(pick_action())
    
    # Delete_input.
    elif choice == int(4):
        delete_input()
        print('change a print option')
        print(f'{Underscore}')
        return(pick_action())
    else:
        print('Invalid input, try again:')
        print(f'{Underscore}')
        delete_input()
        return(pick_action())
        
    
pick_action()
