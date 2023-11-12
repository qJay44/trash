import mouse
import keyboard as kb


def do():
    print('waiting...')
    kb.wait('space')
    mouse.drag(0, 0, -1000, 0, absolute=True)
    do()


do()

