def chain(start, end):
    cmd = 'alias chain1 ".e chain 1 loop'
    for i in range(end - start + 1):
        cmd += f" {i + start}"
    cmd += '"'
    print(cmd)


def generate(num: int):
    cmds = f"alias _e_prev _e{num}; alias _e_next _e1\n\n"
    width = len(str(num))
    for line in range(num + 1):
        currName = f'{line:<{width}}'
        currValue = f'{currName}'
        prevValue = f'{(num + line) % (num + 1):<{width}}'
        nextValue = f'{(line + 1) % (num + 1)}'
        coreCommand = f'.e {currValue} loop 1'

        cmds += f'alias _e{currName} "{coreCommand}; alias _e_prev _e{prevValue}; alias _e_next _e{nextValue}"\n'

    with open('king-emotes.cfg', 'w') as f:
        f.write(cmds)

if __name__ == '__main__':
    # generate(250)
    chain(242, 255)
