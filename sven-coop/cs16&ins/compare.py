import json

ANSI_GREEN_HIGH = '\033[0;92m'
ANSI_RED_HIGH = '\033[0;91m'
ANSI_YELLOW_HIGH = '\033[0;93m'
ANSI_RESET = '\033[0m'

TIE = (ANSI_YELLOW_HIGH, ANSI_YELLOW_HIGH)
WL = (ANSI_GREEN_HIGH, ANSI_RED_HIGH)
LW = (ANSI_RED_HIGH, ANSI_GREEN_HIGH)

def compare(weaponsJson: str, name1: str, name2: str) -> None:
    with open(weaponsJson, 'r') as f:
        weapons = json.load(f)

    w1 = weapons[name1]
    w2 = weapons[name2]

    for infoKey in w1.keys():
        print(f'{infoKey}: {{')
        for item1, item2 in zip(w1[infoKey].items(), w2[infoKey].items()):
            key1 = item1[0]
            key2 = item2[0]

            if key1 != key2:
                continue

            val1 = item1[1]
            val2 = item2[1]

            if isinstance(val1, str):
                continue

            if 'PRICE' in key1:
                fmtWL = LW
                fmtLW = WL
            else:
                fmtWL = WL
                fmtLW = LW

            printFmt = f'\t{key1}: %s{val1} {ANSI_RESET}| %s{val2}{ANSI_RESET}'
            if val1 == val2:
                print(printFmt % TIE)
            elif val1 > val2:
                print(printFmt % fmtWL)
            else:
                print(printFmt % fmtLW)

        print('}')


if __name__ == '__main__':
    compare('ins.json', 'dragunov', 'm21')

