import json
import re
import pickle
from random import choice

from config import getModels

length = {'models': 0, 'names': 0}


# Creates pickle files of not used models and names based on history.json
def init() -> None:
    with open('history.json', 'r', encoding='utf-8') as f:
        history = json.load(f)['cfgs']

    models = [m.name for m in getModels()]
    names = (lambda: (f:=open('cs.pkl', 'rb'), pickle.load(f), f.close())[1])()
    names += (lambda: (f:=open('hypixel-players.pkl', 'rb'), pickle.load(f), f.close())[1])()

    print(f'models: {len(models)}')
    print(f'names: {len(names)}')

    for dop in history:
        cfg = dop['ccfg']

        match = re.search(r'(?<=model )(.+)', cfg)
        if (match):
            models.remove(match.group())
        else:
            print(f'Cant find model [{cfg}]')
            exit(1)

        match = re.search(r'(?<=name )(.+)', cfg)
        if (match):
            names.remove(match.group())
        else:
            print(f'Cant find name [{cfg}]')
            exit(1)

    with open('models.pkl', 'wb') as f:
        pickle.dump(models, f)

    with open('names.pkl', 'wb') as f:
        pickle.dump(names, f)


# @param: what Should be either 'models' or 'names'
def choose(what: str) -> str:
    with open(f'{what}.pkl', 'rb+') as f:
        wlist = pickle.load(f)
        c = choice(wlist)
        wlist.remove(c)
        f.seek(0)
        pickle.dump(wlist, f)
        length[what] = len(wlist)

        return c


# @param: toWhat Should be either 'models' or 'names'
# @param: names A list of names
def append(toWhat: str, names: list[str]) -> None:
    with open(f'{toWhat}.pkl', 'rb+') as f:
        wlist = pickle.load(f)
        for name in names:
            wlist.append(name)

        f.seek(0)
        pickle.dump(wlist, f)
        length[toWhat] = len(wlist)


# Saves cfgs to history.json
def write(scfg: str, ccfg:str) -> None:
    with open('history.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data['cfgs'].append({'scfg': scfg, 'ccfg': ccfg})
        f.seek(0)
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    ...
    # init()

