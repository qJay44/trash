with open('decimal-ascii.txt', 'r') as f:
    output = ""
    for line in f.readlines():
        output += chr(int(line.strip()))

    print(output)

