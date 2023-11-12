import mouse
import keyboard as kb
from time import sleep

run = False


def setState():
    global run
    run = True if not run else False


def do():
    while True:
        if run:
            mouse.move(863, 550, absolute=True, duration=0.025)
            mouse.click('left')
            sleep(1)
        else:
            print('off')
            kb.wait('ctrl+u')
            print('on')


kb.add_hotkey('ctrl+u', setState)
do()

