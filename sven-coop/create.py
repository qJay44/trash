from random import choice, randint
from config import COLORNAMES, TRAIL_PALETTES, TRAIL_SPRITES, VC_NAMES, HATS, KING_CFG_PATH, MY_CFG_PATH
import history
import json
import requests
import re


def create() -> tuple[str, str]:
    # Server config
    scfg = \
        'exec clear.cfg\n' + \
        roll(f'say trail {choice(COLORNAMES)} {choice(TRAIL_SPRITES)}\n') + \
        roll(f'.trail {choice(TRAIL_PALETTES)}\n') + \
        f'.vc voice {roll(choice(VC_NAMES).name[:-7], 'scientist')}\n' + \
        f'.vc pitch {roll(randint(1, 255), 100, 50)}\n' + \
        f'.hat {roll(choice(HATS), 'off', 25)}\n'  + \
        f'.skin {roll(-2, 0)}\n' + \
        f'.color {roll(choice(['r', 'g', 'b', 'y']), 'off')}\n' + \
        f'.brapcolor {randint(0, 255)} {randint(0, 255)} {randint(0, 255)}'

    # Client config
    ccfg = \
        f'model {history.choose('models')}\n' + \
        f'name {_chooseName()}\n' + \
        f'topcolor {randint(0, 255)}\n' + \
        f'bottomcolor {randint(0, 255)}'

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
        
 
def _fromBabelLib(hexagon_name_length=3200):
    # https://github.com/victor-cortez/Library-of-Babel-Python-API/blob/master/pybel.py
    
    hexagon = "".join([choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(hexagon_name_length)])
    wall = str(randint(1, 4))
    shelf = str(randint(1, 5))
    volume = str(randint(1, 32))
    
    form = {"hex": hexagon,"wall": wall, "shelf": shelf, "volume": volume, "page": "1", "title": "startofthetext"}
    url = "https://libraryofbabel.info/download.cgi"
    text = requests.post(url, data=form)
    content = text.text[len("startofthetext") + 2::].rsplit('\n', 4)[0]
    
    if "<HTML>" in content:
        name = history.choose('names')
    else:
        name = choice(re.findall(r'\w+', content, re.MULTILINE))
    
    return name


def _chooseName():
    if randint(1, 100) > 80:
        return history.choose('names')
    else:
        return roll(_fromWikipedia(), _fromBabelLib(), 77)


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
