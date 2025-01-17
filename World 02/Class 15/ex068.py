'''
    Create a even vs odd game. The game will stops if the player loses.
    In the end, show how many times the player wins.
'''
from random import randint

divisor = '=-' * 20
print(f'{divisor}\n{"Even or Odd Game":^40}\n{divisor}')
count = 0

while True:
    computer = randint(1, 5)
    number = int(input('Choose a number: '))
    option = input('Even or odd: [E/O] ').strip().lower()
    sum = computer + number

    if sum % 2 == 0:
        type = 'even'
    else:
        type = 'odd'

    print(f'You play \033[34m{number}\033[m and the computer plays \033[34m{computer}\033[m. The sum is \033[34m{sum}\033[m ({type})')

    if option == 'e' and type == 'even':
        print('\033[32mYou won\033[m, good game.')
        count += 1
    elif option == 'o' and type == 'odd':
        print('\033[32mYou won\033[m, good game.')
        count += 1
    else:
        print(f'\033[31mYou lost\033[m, try again.')
        break

print(f'You won {count} times.')
