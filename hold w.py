import keyboard as kb

while True:
    kb.wait('pgup')
    kb.press('w')
    kb.wait('pgup')
    kb.release('w')
