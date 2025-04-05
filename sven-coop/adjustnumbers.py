with open('numbers.txt', 'r', encoding='utf-8') as f:
    numbersAdjusted = ""
    for line in f.readlines():
        numberName, number = line.split(' king/')
        numbersAdjusted += f'{number[:4]}\t{numberName}\n'

    with open('numbers2.txt', 'w', encoding='utf-8') as f2:
        f2.write(numbersAdjusted)

