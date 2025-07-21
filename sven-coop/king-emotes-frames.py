from os import makedirs

LAST_FRAME = 255

def generate(emotes: int, frameSteps: int):
    dirName = f'eframes{frameSteps}'
    makedirs(dirName, exist_ok=True)
    cmdsEmotesFramesMain = ""
    width = len(str(LAST_FRAME))
    currentLastFrame = LAST_FRAME - (LAST_FRAME % frameSteps)
    steps = int(LAST_FRAME / frameSteps)
    for e in range(emotes + 1):
        eFramesFileName = f'{dirName}/e{e}frames.cfg'
        cmdsEmotesFramesMain += f'alias e{e}frames{frameSteps} "exec {eFramesFileName}"\n'
        cmdsEmotesFrames = f'alias _e_frame_prev _e_frame{currentLastFrame}; alias _e_frame_next _e_frame0\n'
        for i in range(frameSteps + 1):
            currValue = i * steps
            currName = f'{currValue:<{width}}'
            nextValue = ((i + 1) % (frameSteps + 1)) * steps
            prevValue = ((i + frameSteps) % (frameSteps + 1)) * steps
            coreCmd = f'.e {e} freeze 0 {currValue:<{width}} {currValue:<{width}}'

            cmdsEmotesFrames += f'alias _e_frame{currName} "{coreCmd}; alias _e_frame_prev _e_frame{prevValue:<{width}}; alias _e_frame_next _e_frame{nextValue}"\n'

        with open(eFramesFileName, 'w') as f:
            f.write(cmdsEmotesFrames)

    with open(f'king-emotes-frames.cfg', 'w') as f:
        f.write(cmdsEmotesFramesMain)

if __name__ == '__main__':
    generate(255, 255)

