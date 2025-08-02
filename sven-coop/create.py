from random import choice, randint
from config import COLORNAMES, TRAIL_PALETTES, TRAIL_SPRITES, VC_VOICES, HATS, KING_CFG_PATH, MY_CFG_PATH
import history
import json
import requests


def create() -> tuple[str, str]:
    # Server config
    scfg = \
        'exec clear.cfg\n' + \
        roll(f'say trail {choice(COLORNAMES)} {choice(TRAIL_SPRITES)}\n') + \
        roll(f'.trail {choice(TRAIL_PALETTES)}\n') + \
        f'.vc voice {choice(VC_VOICES)}\n' + \
        f'.vc pitch {randint(50, 150)}\n' + \
        f'.hat {roll(choice(HATS), 'off', 25)}\n'  + \
        f'.skin {roll(-2, 0)}\n' + \
        f'.color {roll(choice(['r', 'g', 'b', 'y']), 'off')}\n' + \
        f'.brapcolor {randint(0, 255)} {randint(0, 255)} {randint(0, 255)}'

    # Client config
    ccfg = \
        f'model {history.choose('models')}\n' + \
        f'name {_chooseName()}\n' + \
        f'topcolor {randint(0, 255)}\n' + \
        f'bottomcolor {randint(0, 255)}\n' + \
        f'alias nightvision ".nightvision {choice(COLORNAMES)}"'

    return (scfg, ccfg)


def roll(winVal, loseVal: str | int ='', winTres=10):
    return winVal if randint(1, 100) < winTres else loseVal


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
        endIdx = randint(startIdx, startIdx + 2);
        name = " ".join(words[startIdx:endIdx + 1])
        name = name.replace('"', '')[:32]

        return f'\"{name}\"'


def _chooseName():
    if randint(1, 100) > 80:
        return history.choose('names')
    else:
        return _fromWikipedia()


def apply(scfg: str, ccfg: str, addToHistory: bool = True) -> None:
    with open(KING_CFG_PATH, 'w', encoding='utf-8') as f:
        f.write(scfg)

    with open(MY_CFG_PATH, 'w', encoding='utf-8') as f:
        f.write(ccfg)

    if (addToHistory):
        history.write(scfg, ccfg)


if __name__ == '__main__':
    fromHistory = randint(1, 100) == 1
    scfg, ccfg = _pick() if fromHistory else create()
    apply(scfg, ccfg, not fromHistory)

    print(f'{scfg}\n\n{ccfg}\n')
    print(f'models left: {history.length['models']}')
    print(f'names left: {history.length['names']}')

