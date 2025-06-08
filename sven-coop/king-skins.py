def generate(linesNum: int):
    cmds = "alias _skin _skin1\n"
    for line in range(1, linesNum + 1):
        cmds += f'alias _skin{line} ".skin -{line}; alias _skin _skin{1 if line == linesNum else line + 1}"\n'


    with open('king-skins.cfg', 'w') as f:
        f.write(cmds)


if __name__ == '__main__':
    generate(100)

