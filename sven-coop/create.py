from random import choice, randint
from config import COLORNAMES, TRAIL_PALETTES, TRAIL_SPRITES, VC_NAMES, HATS, KING_CFG_PATH, MY_CFG_PATH
import history
import json
import requests


def create() -> tuple[str, str]:
    def roll(winVal, loseVal: str | int ='', winTres=10): return winVal if randint(1, 100) < winTres else loseVal

    # Server config
    scfg = \
        'exec clear.cfg\n' + \
        roll(f'say trail {choice(COLORNAMES)} {choice(TRAIL_SPRITES)}\n') + \
        roll(f'.trail {choice(TRAIL_PALETTES)}\n') + \
        f'.vc voice {roll(choice(VC_NAMES).name[:-7], 'scientist')}\n' + \
        f'.vc pitch {roll(randint(1, 255), 100)}\n' + \
        f'.hat {roll(choice(HATS), 'off', 25)}\n'  + \
        f'.skin {roll(-2, 0)}\n' + \
        f'.color {roll(choice(['r', 'g', 'b', 'y']), 'off')}\n' + \
        f'.brapcolor {randint(0, 255)} {randint(0, 255)} {randint(0, 255)}'

    # Client config
    ccfg = \
        f'model {history.choose('models')}\n' + \
        f'name {roll(_fromWikipedia(), history.choose('names'), 33)}\n' + \
        f'topcolor {randint(0, 255)}\n' + \
        f'bottomcolor {randint(0, 255)}'

    return (scfg, ccfg)


def _pick():
    with open('history.json', 'r', encoding='utf-8') as f:
        cfg = choice(json.load(f)['cfgs'])
    return cfg['scfg'], cfg['ccfg']


def _fromWikipedia():
    response = requests.get(r'https://en.wikipedia.org/api/rest_v1/page/random/summary')
    if response.status_code != 200:
        print('Wiki bad response')
        exit(1)
    else:
        words = response.json()['extract'].split(' ');
        startIdx = randint(0, len(words) - 1);
        endIdx = randint(startIdx, startIdx + 5);
        name = " ".join(words[startIdx:endIdx + 1])
        name.replace('"', '')

        return f'\"{name}\"'


def apply(scfg: str, ccfg: str) -> None:
    with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
        f.write(scfg)

    with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
        f.write(ccfg)

    history.write(scfg, ccfg)


if __name__ == '__main__':
    scfg, ccfg = _pick() if randint(1, 100) == 1 else create()
    apply(scfg, ccfg)

    print(f'{scfg}\n\n{ccfg}\n')
    print(f'models left: {history.length['models']}')
    print(f'names left: {history.length['names']}')

