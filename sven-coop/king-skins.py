def generate(linesNum: int):
    cmds = f"alias _skin_prev _skin{linesNum}; alias _skin_next _skin1\n\n"
    width = len(str(linesNum))
    for line in range(linesNum + 1):
        currName = f'{line:<{width}}'
        currValue = f'-{currName}'
        prevValue = f'{(linesNum + line) % (linesNum + 1):<{width}}'
        nextValue = f'{(line + 1) % (linesNum + 1)}'

        cmds += f'alias _skin{currName} ".skin {currValue}; alias _skin_prev _skin{prevValue}; alias _skin_next _skin{nextValue}\n'

    with open('king-skins.cfg', 'w') as f:
        f.write(cmds)


if __name__ == '__main__':
    generate(100)

