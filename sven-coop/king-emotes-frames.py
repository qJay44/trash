LAST_FRAME = 255

def generate(emotes: int, frameStep: int):
    cmds = ""
    width = len(str(LAST_FRAME))
    currentLastFrame = LAST_FRAME - (LAST_FRAME % frameStep)
    steps = int(LAST_FRAME / frameStep)
    for e in range(emotes):
        cmds += f'\nalias e{e}frames "alias _e_frame_prev _e{e}_frame{currentLastFrame}; alias _e_frame_next _e{e}_frame0"\n'
        for i in range(frameStep + 1):
            currValue = i * steps
            currName = f'{currValue:<{width}}'
            nextValue = ((i + 1) % (frameStep + 1)) * steps
            prevValue = ((i + frameStep) % (frameStep + 1)) * steps
            coreCmd = f'.e {e} freeze {currValue:<{width}} {currValue:<{width}}'

            cmds += f'alias _e{e}_frame{currName} "{coreCmd}; alias _e_frame_prev _e{e}_frame{prevValue:<{width}}; alias _e_frame_next _e{e}_frame{nextValue}\n'

    with open('king-emotes-frames.cfg', 'w') as f:
        f.write(cmds)

if __name__ == '__main__':
    generate(250, 10)
