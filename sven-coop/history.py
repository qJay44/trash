import json
import re
import pickle
from random import choice

from config import MODELS

length = {'models': 0, 'names': 0}


# Creates pickle files of not used models and names based on history.json
def init() -> None:
    with open('history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)['cfgs']

    models = [m.name for m in MODELS]
    names = (lambda: (f:=open('cs.pkl', 'rb'), pickle.load(f), f.close())[1])()
    names += (lambda: (f:=open('hypixel-players.pkl', 'rb'), pickle.load(f), f.close())[1])()

    print(f'models: {len(models)}')
    print(f'names: {len(names)}')

    for dop in history:
        cfg = dop['ccfg']
        models.remove(re.search(r'(?<=model )(.+)', cfg).group())
        names.remove(re.search(r'(?<=name )(.+)', cfg).group())

    with open('models.pkl', 'wb') as f:
        pickle.dump(models, f)

    with open('names.pkl', 'wb') as f:
        pickle.dump(names, f)


# @param: what Should be 'models' or 'names'
def choose(what: str) -> str:
    with open(f'{what}.pkl', 'rb+') as f:
        wlist = pickle.load(f)
        c = choice(wlist)
        wlist.remove(c)
        f.seek(0)
        pickle.dump(wlist, f)
        length[what] = len(wlist)

        return c


# Saves cfgs to history.json
def write(scfg: str, ccfg:str) -> None:
    with open('history.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data['cfgs'].append({'scfg': scfg, 'ccfg': ccfg})
        f.seek(0)
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    init()

