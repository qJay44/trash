import keyboard as kb
from time import sleep


def do():
    print('waiting...')
    kb.wait('space')
    sleep(0.1)
    kb.send('alt+tab')
    sleep(0.3)
    kb.send('space')
    do()


do()
