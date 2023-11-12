import keyboard as kb
from time import sleep


def do():
    print('waiting...\n')
    kb.wait('ctrl')
    kb.send('F11')
    sleep(0.1)
    kb.send('right arrow')
    kb.send('Enter')
    for _ in range(12):
        kb.send('down arrow')
    kb.send('Enter')
    print('done\n')
    do()


do()