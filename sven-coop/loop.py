from random import randint
from time import sleep
from dop import Dop
import keyboard as kb


if __name__ == '__main__':
    print('Starting in ', 3, sep='', end='\r', flush=True)
    sleep(1)
    print('Starting in ', 2, sep='', end='\r', flush=True)
    sleep(1)
    print('Starting in ', 1, sep='', end='\r', flush=True)
    sleep(1)
    print(''*15)

    dop = Dop()
    iter = 1

    while (True):
        kb.send('insert')
        dop.apply(dop.choose())

        print('Iter: ', iter, sep='', end='\r', flush=True)
        iter += 1
        sleep(randint(1, 10000) / 10000)

