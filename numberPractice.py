from random import randint
from time import time
import sys

print('\nType the numbers as quickly as you can. Ctrl-C to quit.\n')
streak = 0

def log(status):
    print(status.title() + ' ({0:.2f} s)\n'.format(round(end - start, 2)))

while True:
    expected = randint(0,99999)
    start = time()
    try:
        actual = int(input(str(expected) + ' -> '))
    except KeyboardInterrupt:
        print('Quit')
        exit()
    except:
        actual = None
    end = time()
    if actual != expected:
        log('wrong')
        streak = 0
    else:
        log('right')
        streak += 1
        if streak >= 5: print('Streak! (' + str(streak) + ')')
        print('')
