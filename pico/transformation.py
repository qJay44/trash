def origFunc(flag):
    return ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

print(origFunc('pico'))

with open('enc', encoding='utf-8') as f:
    encoded = f.read()
    flag = ''

    for c in encoded:
        binary = '{0:016b}'.format(ord(c))
        first_half, second_half = binary[:8], binary[8:]
        flag += chr(int(first_half, 2))
        flag += chr(int(second_half, 2))

    print(flag)

